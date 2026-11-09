// Render offline lettered pages and panel crops. Intentionally does not create PDFs.
// Usage: node tools/render_manga.js input.html output_dir [--width 2336]
const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');
const crypto = require('crypto');
const { pathToFileURL } = require('url');

(async () => {
  const [input, output, ...rest] = process.argv.slice(2);
  if (!input || !output) throw new Error('Usage: node render_manga.js input.html output_dir [--width 2336]');
  const warg = rest.indexOf('--width');
  const width = warg >= 0 ? Number(rest[warg + 1]) : 2336;
  if (!Number.isInteger(width) || width < 1024 || width > 3600) throw new Error('Width must be1024..3600');
  const height = Math.round(width * 1.5);
  const launch = {};
  if (process.env.PLAYWRIGHT_CHROMIUM_EXECUTABLE_PATH) launch.executablePath = process.env.PLAYWRIGHT_CHROMIUM_EXECUTABLE_PATH;
  const browser = await chromium.launch(launch);
  try {
    const page = await browser.newPage({ viewport:{width,height}, deviceScaleFactor:1 });
    const blocked=[],failed=[];
    await page.route('**/*', async route => {
      if (/^https?:/i.test(route.request().url())) { blocked.push(route.request().url()); await route.abort(); }
      else await route.continue();
    });
    page.on('requestfailed', req => failed.push(req.url()));
    await page.goto(pathToFileURL(path.resolve(input)).href,{waitUntil:'load',timeout:60000});
    await page.evaluate(()=>document.fonts.ready);
    const loadedFonts=await page.evaluate(async()=>{
      const checks=[['ZSO Dialogue','700 50px "ZSO Dialogue"'],['ZSO Display','400 104px "ZSO Display"']];
      return await Promise.all(checks.map(async([family,spec])=>({family,loaded:(await document.fonts.load(spec,'NaN 0123456789')).length>0})));
    });
    if (loadedFonts.some(f=>!f.loaded)) throw new Error('Bundled lettering font failed to load: '+JSON.stringify(loadedFonts));
    const data=await page.evaluate(()=>JSON.parse(document.getElementById('manga-data').textContent));
    await page.evaluate(({width,height})=>{
      document.body.classList.add('capture');
      document.querySelectorAll('.manga-page').forEach(e=>{e.style.width=width+'px';e.style.height=height+'px';});
    },{width,height});
    for (const folder of ['clean','lettered','panels/clean','panels/lettered']) fs.mkdirSync(path.join(output,folder),{recursive:true});
    const report={chapter_id:data.manifest.chapter_id,page_count:0,panel_count:0,missing_images:[],lettering_overflows:[],loaded_fonts:loadedFonts,blocked_remote_requests:blocked,failed_requests:failed,outputs:[],source_sha256:data.source_sha256,note:'Technical export evidence only; final page sequence still requires visual review.'};
    for (let i=0;i<data.manifest.pages.length;i++) {
      const item=data.manifest.pages[i];
      await page.evaluate(i=>window.mangaReader.show(i),i);
      const element=page.locator('#'+item.id);
      const sourceClean=await element.getAttribute('data-clean-path');
      const stagedClean=path.resolve(output,'clean',item.id+'.png');
      if (path.resolve(sourceClean)!==stagedClean) fs.copyFileSync(sourceClean,stagedClean);
      const check=await element.evaluate(e=>({
        badImages:[...e.querySelectorAll('img')].filter(i=>!i.complete||!i.naturalWidth).map(i=>i.src),
        overflows:[...e.querySelectorAll('text[data-letter-id]')].flatMap(t=>{
          const b=t.getBBox(),r=JSON.parse(t.dataset.bounds),epsilon=5;
          return b.x<r[0]-epsilon||b.y<r[1]-epsilon||b.x+b.width>r[0]+r[2]+epsilon||b.y+b.height>r[1]+r[3]+epsilon ? [{id:t.dataset.letterId,actual:[b.x,b.y,b.width,b.height],box:r}]:[];
        })
      }));
      report.missing_images.push(...check.badImages);report.lettering_overflows.push(...check.overflows);
      const dest=path.join(output,'lettered',item.id+'.png');
      await element.screenshot({path:dest,animations:'disabled'});
      const box=await element.boundingBox();
      for (const panel of item.panels) {
        const [x,y,w,h]=panel.rect;
        const clip={x:box.x+x*width,y:box.y+y*height,width:w*width,height:h*height};
        await page.screenshot({path:path.join(output,'panels/lettered',panel.id+'.png'),clip,animations:'disabled'});
      }
      await page.evaluate(()=>document.body.classList.add('clean'));
      for (const panel of item.panels) {
        const [x,y,w,h]=panel.rect;
        await page.screenshot({path:path.join(output,'panels/clean',panel.id+'.png'),clip:{x:box.x+x*width,y:box.y+y*height,width:w*width,height:h*height},animations:'disabled'});
      }
      await page.evaluate(()=>document.body.classList.remove('clean'));
      report.outputs.push({page_id:item.id,path:path.resolve(dest),pixels:[width,height],sha256:crypto.createHash('sha256').update(fs.readFileSync(dest)).digest('hex')});
      report.page_count++;report.panel_count+=item.panels.length;
    }
    // Self-contained runtime data references exact PNGs; it never executes story events.
    const game={schema_version:1,chapter_id:data.manifest.chapter_id,reading_direction:'ltr',print_route:data.manifest.print_route,reader_policy:'read-only; bookmark state separate from campaign',page_size_px:[width,height],clean_image_policy:'Original source pixels preserved; lettered export and panel crops use declared page size.',future_adapter_only:data.manifest.adaptation_boundaries,pages:data.manifest.pages.map(p=>({id:p.id,title:p.title,clean:'clean/'+p.id+'.png',lettered:'lettered/'+p.id+'.png',game_usage:p.game_usage,event_postconditions_only:p.story_events,panels:p.panels.map(x=>({id:x.id,rect:x.rect,clean:'panels/clean/'+x.id+'.png',lettered:'panels/lettered/'+x.id+'.png',dialogue_ids:x.dialogue_ids}))})),dialogue:data.dialogue.entries};
    fs.writeFileSync(path.join(output,'game_manifest.json'),JSON.stringify(game,null,2)+'\n');
    fs.writeFileSync(path.join(output,'export_report.json'),JSON.stringify(report,null,2)+'\n');
    if (report.missing_images.length||report.lettering_overflows.length||blocked.length||failed.length) throw new Error('Export checks failed; see export_report.json');
    console.log(JSON.stringify({pages:report.page_count,panels:report.panel_count,letteringOverflows:report.lettering_overflows.length,output:path.resolve(output)}));
  } finally {await browser.close();}
})().catch(err=>{console.error(err);process.exitCode=1;});
