// Offline Chromium renderer. Node + Playwright + installed Chromium required.
// Usage: node tools/render_pdf.js input.html output.pdf [landscape]
const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');
const { pathToFileURL } = require('url');

(async () => {
  const [input, output, mode] = process.argv.slice(2);
  if (!input || !output || (mode && mode !== 'landscape')) {
    throw new Error('Usage: node render_pdf.js input.html output.pdf [landscape]');
  }
  if (!fs.existsSync(input)) throw new Error('Missing HTML: ' + input);
  fs.mkdirSync(path.dirname(path.resolve(output)), { recursive: true });
  const launch = {};
  if (process.env.PLAYWRIGHT_CHROMIUM_EXECUTABLE_PATH) launch.executablePath = process.env.PLAYWRIGHT_CHROMIUM_EXECUTABLE_PATH;
  const browser = await chromium.launch(launch);
  try {
    const page = await browser.newPage({ viewport: { width: 1400, height: 1000 } });
    const blocked = [];
    const failed = [];
    await page.route('**/*', async route => {
      if (/^https?:/i.test(route.request().url())) {
        blocked.push(route.request().url());
        await route.abort();
      } else await route.continue();
    });
    page.on('requestfailed', req => failed.push(req.url()));
    await page.goto(pathToFileURL(path.resolve(input)).href, { waitUntil: 'load', timeout: 60000 });
    await page.emulateMedia({ media: 'print' });
    await page.evaluate(() => document.fonts.ready);
    const report = await page.evaluate(() => ({
      source_sha256: document.querySelector('meta[name="source-sha256"]')?.content || null,
      missingImages: [...document.images].filter(x => !x.complete || !x.naturalWidth).map(x => x.getAttribute('src')),
      designedPages: document.querySelectorAll('section.page').length,
      overflowWarnings: [...document.querySelectorAll('.col-text,.hs-right,.opener,.toc-art')]
        .filter(x => x.scrollHeight > x.clientHeight + 2 || x.scrollWidth > x.clientWidth + 2)
        .map(x => ({class: x.className, text: x.textContent.trim().slice(0, 90), scrollHeight: x.scrollHeight, clientHeight: x.clientHeight})),
      fonts: [...document.fonts].map(f => ({ family: f.family, status: f.status }))
    }));
    report.blockedRemoteRequests = blocked;
    report.failedRequests = failed;
    report.note = 'Structural render report only; visual inspection and glyph/semantic checks still required.';
    fs.writeFileSync(output + '.render-report.json', JSON.stringify(report, null, 2) + '\n');
    if (blocked.length || failed.length || report.missingImages.length) {
      throw new Error('Offline resource validation failed; see ' + output + '.render-report.json');
    }
    const options = { path: output, printBackground: true };
    if (mode === 'landscape') Object.assign(options, { preferCSSPageSize: true, margin: { top: 0, bottom: 0, left: 0, right: 0 } });
    else Object.assign(options, {
      format: 'A4', displayHeaderFooter: true, headerTemplate: '<div></div>',
      footerTemplate: '<div style="width:100%;font-family:monospace;font-size:7px;color:#6d6257;padding:0 14mm;display:flex;justify-content:space-between"><span>ZERO-SUM: OMEN · specification snapshot</span><span class="pageNumber"></span></div>',
      margin: { top: '14mm', bottom: '16mm', left: '14mm', right: '14mm' }
    });
    await page.pdf(options);
    console.log('PDF:', output);
    console.log('Structural report:', output + '.render-report.json');
    if (report.overflowWarnings.length) console.log('Layout warnings:', report.overflowWarnings.length);
  } finally { await browser.close(); }
})().catch(error => { console.error(error); process.exitCode = 1; });
