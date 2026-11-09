#!/usr/bin/env python3
"""Build a portable, read-only chapter asset ZIP. No PDF or Unity import.

All native PNGs remain untouched. JPEG page/panel derivatives, portable data,
dialogue, vector lettering, open fonts and their licences are packaged together.
Run only after the manga exporter has finished; --check is read-only.
"""
from __future__ import annotations

import argparse
from copy import deepcopy
import hashlib
import json
from pathlib import Path
import re
import sys
import zipfile

from PIL import Image, ImageColor, ImageFont

ROOT=Path(__file__).resolve().parents[1]
CHAPTER=ROOT/'art/manga/chapter_01'


def read(path):
    return json.loads(path.read_text(encoding='utf-8-sig'))


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def json_text(value):
    return json.dumps(value,ensure_ascii=False,indent=2)+'\n'


def relative(path):
    return path.relative_to(ROOT).as_posix()


def font_inventory():
    folder=ROOT/'art/fonts'
    fonts=sorted(p for p in folder.rglob('*') if p.is_file() and p.suffix.lower() in {'.ttf','.otf','.woff','.woff2'}) if folder.exists() else []
    licences=sorted(p for p in folder.rglob('*') if p.is_file() and ('ofl' in p.name.lower() or 'license' in p.name.lower() or 'licence' in p.name.lower())) if folder.exists() else []
    return folder,fonts,licences


def validate():
    errors=[]
    path=CHAPTER/'game_manifest.json'
    if not path.exists():
        return ['Missing game_manifest.json'],None
    game=read(path)
    if game.get('reader_policy')!='read-only; bookmark state separate from campaign':errors.append('Reader policy changed; review before packaging')
    pages=game.get('pages',[])
    if len(pages)!=20:errors.append('Expected20 complete pages')
    panels=[panel for page in pages for panel in page.get('panels',[])]
    if len(panels)!=80:errors.append('Expected80 panels/160 crop files')
    for item in pages+panels:
        for kind in ('clean','lettered'):
            rel=item.get(kind)
            if not rel or not (CHAPTER/rel).is_file():errors.append(f"Missing {kind} {item.get('id')}")
    for page in pages:
        if not (ROOT/f"build/manga/{page['id']}.lettering.svg").is_file():errors.append('Missing SVG '+page['id'])
    folder,fonts,licences=font_inventory()
    if not fonts:errors.append('Bundled open fonts are not ready')
    if not licences:errors.append('Bundled font licences are not ready')
    provenance=folder/'sources.json'
    if not provenance.is_file():errors.append('Open-font source/hash manifest is missing')
    else:
        approved=read(provenance).get('files',[])
        for font in fonts:
            record=next((r for r in approved if r.get('file')==font.relative_to(folder).as_posix()),None)
            if not record or record.get('sha256')!=digest(font) or 'open font' not in record.get('license','').lower():errors.append('Unverified open-font licence/hash '+font.name)
    for required in ('dialogue.json','pages.json','export_report.json'):
        if not (CHAPTER/required).is_file():errors.append('Missing source '+required)
    if (CHAPTER/'export_report.json').is_file():
        report=read(CHAPTER/'export_report.json')
        for key in ('missing_images','lettering_overflows','failed_requests','blocked_remote_requests'):
            if report.get(key):errors.append('Exporter has unresolved '+key)
        # Prevent packaging half of a new export beside half of an earlier one.
        for record in report.get('outputs',[]):
            p=CHAPTER/'lettered'/f"{record['page_id']}.png"
            if not p.is_file() or digest(p)!=record['sha256']:errors.append('Export hash mismatch '+record['page_id'])
    return errors,game


class Package:
    def __init__(self,output,args):
        self.output=output
        self.args=args
        self.files={}
        self.derivatives=[]
        output.mkdir(parents=True,exist_ok=True)

    def add_bytes(self,path,data):
        dest=self.output/path;dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes(data)
        self.files[path]=dict(path=path,bytes=len(data),sha256=hashlib.sha256(data).hexdigest())
        return path

    def add_text(self,path,text):
        return self.add_bytes(path,text.encode('utf-8'))

    def copy(self,source,path):
        return self.add_bytes(path,source.read_bytes())

    def image(self,source,path,max_side):
        dest=self.output/path;dest.parent.mkdir(parents=True,exist_ok=True)
        with Image.open(source) as original:
            original_size=list(original.size)
            original.thumbnail((max_side,max_side),Image.Resampling.LANCZOS)
            if original.mode in ('RGBA','LA') or 'transparency' in original.info:
                rgba=original.convert('RGBA');picture=Image.new('RGB',rgba.size,ImageColor.getrgb('#F2E8D5'));picture.paste(rgba,mask=rgba.getchannel('A'))
            else:picture=original.convert('RGB')
            picture.save(dest,'JPEG',quality=self.args.quality,optimize=True,progressive=True)
            pixels=list(picture.size)
        record=dict(path=path,bytes=dest.stat().st_size,sha256=digest(dest),pixels=pixels,
                    original_path=relative(source),original_sha256=digest(source),original_pixels=original_size,
                    derivative='JPEG resample; originalPNG preserved',quality=self.args.quality)
        self.files[path]={k:record[k] for k in ('path','bytes','sha256')}
        self.derivatives.append(record)
        return record


READER_CSS='''
*{box-sizing:border-box}body{margin:0;background:#18151b;color:#f2e8d5;font:17px/1.5 sans-serif}header{padding:18px 24px;background:#28222b;border-bottom:2px solid #ff7a2c}h1{font-size:24px;margin:0}header p{font-size:14px;margin:7px 0 0;color:#ddcfba}nav{display:flex;gap:10px;flex-wrap:wrap;align-items:center;margin-top:15px}button,select,a.control{font:inherit;padding:8px 12px;color:#18151b;background:#f2e8d5;border:2px solid transparent;border-radius:4px}button:focus-visible,select:focus-visible,a:focus-visible{outline:3px solid #ff7a2c;outline-offset:3px}button:disabled{opacity:.45}main{max-width:1200px;margin:auto;padding:16px}figure{margin:0;text-align:center}figure img{max-width:100%;height:auto;background:#f2e8d5}figure.page img{width:min(100%,800px)}figure.panel img{max-height:85vh;width:auto}figcaption{font-size:14px;padding:8px;color:#d9cdbb}#transcript{max-width:840px;margin:20px auto;background:#f2e8d5;color:#18151b;padding:24px;border-radius:5px}#transcript h2{margin:0 0 15px}#transcript p{margin:0 0 13px}.speaker{font-weight:bold}#notice{margin:12px 0;color:#ffe1a6}footer{font-size:13px;max-width:1000px;padding:20px;margin:auto;color:#bcae9e}a{color:#ffab70}[hidden]{display:none!important}@media(prefers-reduced-motion:reduce){*{scroll-behavior:auto!important}}
'''

READER_JS=r'''
(()=>{'use strict';const data=window.MANGA_DATA,pages=data.pages;let index=0,panelIndex=0;
const $=id=>document.getElementById(id),state={variant:'lettered',panels:false};
const key='zso-read-only-bookmark-'+data.chapter_id;
try{const saved=Number(localStorage.getItem(key));if(Number.isInteger(saved)&&saved>=0&&saved<pages.length)index=saved;}catch{}
pages.forEach((p,i)=>{const option=document.createElement('option');option.value=i;option.textContent=String(i+1).padStart(2,'0')+' · '+p.title;$('page-select').append(option);});
function textFor(p){const ids=new Set(p.panels.flatMap(x=>x.dialogue_ids));return data.dialogue.filter(e=>ids.has(e.id));}
function render(){const p=pages[index];const item=state.panels?p.panels[panelIndex]:p;const img=$('art');img.src=item[state.variant];img.alt=(state.panels?'Panel '+(panelIndex+1)+' of '+p.panels.length+', ':'')+'Page '+(index+1)+': '+p.title+'. Transcript follows.';
$('figure').className=state.panels?'panel':'page';$('page-select').value=index;$('caption').textContent='Page '+(index+1)+' / '+pages.length+(state.panels?' · panel '+(panelIndex+1)+' / '+p.panels.length:'')+' · '+state.variant+' image';
$('previous').disabled=index===0&&(!state.panels||panelIndex===0);$('next').disabled=index===pages.length-1&&(!state.panels||panelIndex===p.panels.length-1);
$('panels').textContent=state.panels?'Show full page':'Read panels';$('variant').textContent=state.variant==='lettered'?'Show clean art':'Show lettered art';
const block=$('transcript');block.replaceChildren();const h=document.createElement('h2');h.textContent='Page '+(index+1)+' transcript';block.append(h);
for(const e of textFor(p)){if(state.panels&&!item.dialogue_ids.includes(e.id))continue;const para=document.createElement('p');const speaker=document.createElement('span');speaker.className='speaker';speaker.textContent=e.speaker+': ';para.append(speaker,document.createTextNode(e.text.replace(/\{\{resonance\}\}/g,String(data.print_route.resonance))));block.append(para);}
try{localStorage.setItem(key,String(index));}catch{}
document.title='Page '+(index+1)+' · ZERO-SUM: OMEN';$('position').textContent=(index+1)+' / '+pages.length;
}
function step(delta){if(state.panels){panelIndex+=delta;if(panelIndex<0&&index>0){index--;panelIndex=pages[index].panels.length-1;}else if(panelIndex>=pages[index].panels.length&&index<pages.length-1){index++;panelIndex=0;}panelIndex=Math.max(0,Math.min(panelIndex,pages[index].panels.length-1));}else{index=Math.max(0,Math.min(index+delta,pages.length-1));panelIndex=0;}render();}
$('previous').onclick=()=>step(-1);$('next').onclick=()=>step(1);$('page-select').onchange=e=>{index=Number(e.target.value);panelIndex=0;render();};
$('variant').onclick=()=>{state.variant=state.variant==='lettered'?'clean':'lettered';render();};$('panels').onclick=()=>{state.panels=!state.panels;panelIndex=0;render();};
$('toggle-transcript').onclick=()=>{$('transcript').hidden=!$('transcript').hidden;$('toggle-transcript').setAttribute('aria-expanded',String(!$('transcript').hidden));};
document.addEventListener('keydown',e=>{if(/INPUT|SELECT|TEXTAREA/.test(e.target.tagName))return;if(e.key==='ArrowRight'){e.preventDefault();step(1);}if(e.key==='ArrowLeft'){e.preventDefault();step(-1);}});
$('art').onerror=()=>{$('notice').textContent='An image is unavailable. Extract the complete ZIP before opening index.html; the transcript remains available.';};
window.mangaReader={show:i=>{index=Math.max(0,Math.min(Number(i),pages.length-1));panelIndex=0;render();},state:()=>({page:index,panel:panelIndex,variant:state.variant,panels:state.panels,readOnly:true})};render();
})();
'''

READER_HTML='''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>ZERO-SUM: OMEN · The Remainder</title><link rel="stylesheet" href="reader.css"></head><body><header><h1>ZERO-SUM: OMEN · The Remainder</h1><p>A complete20-page companion chapter. Fixed authored resonance7 / Horseshoe reference edition. This reader never changes campaign state or resolves live choices/combat.</p><nav aria-label="Comic reader controls"><button id="previous">← Previous</button><label>Page <select id="page-select" aria-label="Choose page"></select></label><button id="next">Next →</button><button id="variant">Show clean art</button><button id="panels">Read panels</button><button id="toggle-transcript" aria-expanded="true" aria-controls="transcript">Toggle transcript</button><a class="control" href="transcript.txt">Full text</a><span id="position" role="status" aria-live="polite"></span></nav></header><main><p id="notice" role="status">Read left to right, then top to bottom. Arrow keys turn pages. Bookmark storage belongs only to this reader.</p><figure id="figure" class="page"><img id="art" alt=""><figcaption id="caption"></figcaption></figure><section id="transcript" aria-label="Current page transcript"></section></main><footer>Portable review and asset package. No Unity import or playable game is included. The future adapter must stop at the live gates in game_manifest.json. Clean pages/crops, lettered derivatives, exact dialogue and editable SVG lettering remain separate. <a href="README.txt">Package notes and licences</a></footer><script src="reader-data.js"></script><script src="reader.js"></script></body></html>'''


def build(args,game):
    output=Path(args.output_dir)
    if not output.is_absolute():output=ROOT/output
    pkg=Package(output,args);portable=deepcopy(game)
    portable['package_variant']='complete pages, clean art and optional-on-demand panel assets'
    portable['page_size_px']=None
    portable['page_size_policy']='Each image records its actual derivative pixels; originals remain in the source repository.'
    portable['reader_policy']='read-only; bookmark state separate from campaign'
    portable['event_execution']='none; event_postconditions_only and future_adapter_only are data, never reader callbacks'
    portable['initial_load_policy']='Only the current full page is loaded. Panel images load only after Read panels is selected. No preloading, network, telemetry or campaign storage.'
    portable['clean_image_policy']='JPEG derivatives of preserved original cleanPNG; not new drawn resolution.'
    for page in portable['pages']:
        for kind in ('clean','lettered'):
            original=CHAPTER/page[kind];path=f"pages/{kind}/{page['id']}.jpg"
            record=pkg.image(original,path,args.page_max);page[kind]=path;page[kind+'_asset']={k:record[k] for k in ('pixels','bytes','sha256')}
        for panel in page['panels']:
            for kind in ('clean','lettered'):
                original=CHAPTER/panel[kind];path=f"panels/{kind}/{panel['id']}.jpg"
                record=pkg.image(original,path,args.panel_max);panel[kind]=path;panel[kind+'_asset']={k:record[k] for k in ('pixels','bytes','sha256')}
    page_sizes={tuple(p[kind+'_asset']['pixels']) for p in portable['pages'] for kind in ('clean','lettered')}
    portable['page_size_px']=list(next(iter(page_sizes))) if len(page_sizes)==1 else None
    # Fonts are distributed only with the corresponding bundled open licences.
    folder,fonts,licences=font_inventory();font_css=[]
    for source in fonts+licences:
        path='fonts/'+source.relative_to(folder).as_posix();pkg.copy(source,path)
        if source in fonts and source.suffix.lower() in ('.ttf','.otf'):
            family,style=ImageFont.truetype(str(source),20).getname()
            font_css.append("@font-face{font-family:"+json.dumps(family)+";src:url('../../"+path+"');font-weight:"+('700' if 'bold' in style.lower() else '400')+";font-style:"+('italic' if 'italic' in style.lower() else 'normal')+";}")
    pkg.copy(folder/'sources.json','fonts/sources.json')
    font_style=''.join(font_css)
    for page in portable['pages']:
        source=ROOT/f"build/manga/{page['id']}.lettering.svg"
        svg=source.read_text(encoding='utf-8-sig')
        svg=svg.replace('url("fonts/','url("../../fonts/').replace("url('fonts/","url('../../fonts/")
        svg=re.sub(r'(<svg\b[^>]*>)',lambda m:m.group(1)+'<style>'+font_style+'</style>',svg,count=1)
        if re.search(r'(?:[A-Za-z]:[/\\]|file:///)',svg):raise ValueError('Absolute filesystem reference in SVG '+page['id'])
        pkg.add_text(f"source/lettering/{page['id']}.svg",svg)
        page['lettering_svg']=f"source/lettering/{page['id']}.svg"
    pkg.copy(CHAPTER/'dialogue.json','source/dialogue.json')
    source_pages=read(CHAPTER/'pages.json')
    for page in source_pages['pages']:
        page['clean_art']='pages/clean/'+page['id']+'.jpg'
    source_pages['portable_asset_paths_relative_to']='package root'
    pkg.add_text('source/pages.json',json_text(source_pages))
    transcript=['ZERO-SUM: OMEN — THE REMAINDER','Fixed authored resonance7 / Horseshoe reference edition. Read-only; not actual player results.','']
    for page in portable['pages']:
        transcript.extend([f"PAGE {page['id'][1:]} — {page['title']}",''])
        for panel in page['panels']:
            entries=[e for e in portable['dialogue'] if e['id'] in panel['dialogue_ids']]
            for e in entries:
                transcript.append(f"{e['speaker']}: "+e['text'].replace('{{resonance}}',str(portable['print_route']['resonance'])))
        transcript.append('')
    pkg.add_text('transcript.txt','\n'.join(transcript)+'\n')
    pkg.add_text('game_manifest.json',json_text(portable))
    pkg.add_text('reader-data.js','window.MANGA_DATA = '+json.dumps(portable,ensure_ascii=False).replace('</','<\/')+';\n')
    reader_fonts='@font-face{font-family:"ZSO Reader";src:url("fonts/BarlowSemiCondensed-Regular.ttf");font-weight:400}@font-face{font-family:"ZSO Reader";src:url("fonts/BarlowSemiCondensed-Bold.ttf");font-weight:700}body{font-family:"ZSO Reader",sans-serif}'
    pkg.add_text('index.html',READER_HTML);pkg.add_text('reader.css',READER_CSS+reader_fonts);pkg.add_text('reader.js',READER_JS)
    pkg.add_text('README.txt',f'''ZERO-SUM: OMEN — CHAPTER01 PORTABLE REVIEW / GAME ASSETS

Extract the complete ZIP and open index.html. No server, account, network request or install is required. All200 JPEGs are included:20 clean pages,20 separately lettered pages,80 clean panels and80 lettered panels. A page’s pixels/byte size/SHA-256 are recorded in game_manifest.json; original PNG hashes and derivative settings are in package_manifest.json.

This is a complete read-only companion chapter and asset handoff, NOT an implemented Unity reader, Unity import, playable game or approved production asset pipeline. Reader navigation changes only its own bookmark. It never chooses resonance/charms, wins combat, grants a Seal or writes a campaign checkpoint. Live integration must enforce every future_adapter_only gate in game_manifest.json, omit printed reference combats and resume only after actual completed gameplay. Event postconditions are documentation, never executable callbacks.

The fixed authored reference route uses resonance7 / Horseshoe. It does not promise the player’s outcome. Left-to-right reading, static pages and an exact transcript are available. The transcript follows declared panel reading order; full-size native PNGs remain in the repository. Browser zoom is available. Panel assets load only when explicitly selected.

Native artwork and lettering sources are preserved. This package uses JPEG derivatives (page maximum long side{args.page_max}px, panel maximum{args.panel_max}px, quality{args.quality}). SVGs under source/lettering contain editable lettering overlays, not complete illustrations. Bundled open fonts and their OFL/licence texts are under fonts/. Do not assume the game’s artwork or story is licensed under a font’s OFL. Font licences apply only to those fonts. Source-page coordinates remain normalized; asset paths are relative to the package root.

No audio, branching gameplay, Unity project, motion rig or save-game integration is included. This edition is an asset review candidate; illustration, cultural and runtime acceptance remain separate.
''')
    # Make the package manifest last. It hashes every delivered file except itself.
    total=sum(r['bytes'] for r in pkg.files.values())
    manifest=dict(schema_version=1,chapter_id=portable['chapter_id'],date='2026-11-08',status='Portable read-only asset package; no Unity import or playable game',page_count=len(portable['pages']),panel_count=sum(len(p['panels']) for p in portable['pages']),image_count=len(pkg.derivatives),derivatives=pkg.derivatives,files=sorted(pkg.files.values(),key=lambda r:r['path']),source_fingerprints={relative(CHAPTER/p):digest(CHAPTER/p) for p in ('game_manifest.json','dialogue.json','pages.json','export_report.json')},uncompressed_bytes_excluding_manifest=total,budget_decimal_bytes=args.budget_mb*1000000,budget_pass=None,note='Hashes cover files except this self-referential manifest. ZIP/report size is external packaging evidence.')
    # The self-size is small; evaluate actual written bytes before producing a ZIP.
    manifest['budget_pass']=total+len(json_text(manifest).encode('utf-8'))<=args.budget_mb*1000000
    pkg.add_text('package_manifest.json',json_text(manifest))
    total=sum(r['bytes'] for r in pkg.files.values())
    if total>args.budget_mb*1000000:
        raise ValueError(f'Complete package {total} bytes exceeds {args.budget_mb} decimalMB. Rebuild with a smaller --panel-max/--page-max at q85/86; do not omit pages silently.')
    zip_path=Path(args.zip)
    if not zip_path.is_absolute():zip_path=ROOT/zip_path
    zip_bytes=None
    if not args.no_zip:
        zip_path.parent.mkdir(parents=True,exist_ok=True)
        with zipfile.ZipFile(zip_path,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=6) as z:
            for path in sorted(pkg.files):
                z.write(output/path,arcname='ZERO-SUM_OMEN_Chapter_01/'+path)
        zip_bytes=zip_path.stat().st_size
        with zipfile.ZipFile(zip_path) as z:
            if z.testzip() is not None:raise ValueError('ZIP CRC verification failed')
        if zip_bytes>args.budget_mb*1000000:raise ValueError('ZIP exceeds declared budget')
    report=dict(output_dir=str(output),zip=str(zip_path) if not args.no_zip else None,uncompressed_bytes=total,zip_bytes=zip_bytes,image_count=len(pkg.derivatives),page_count=20,panel_crop_files=160,budget_pass=True)
    print(json.dumps(report,indent=2));return 0


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--output-dir',default='output/game/chapter_01')
    ap.add_argument('--zip',default='output/game/ZERO-SUM_OMEN_Chapter_01.zip')
    ap.add_argument('--page-max',type=int,default=1200)
    ap.add_argument('--panel-max',type=int,default=1024)
    ap.add_argument('--quality',type=int,choices=(85,86),default=86)
    ap.add_argument('--budget-mb',type=int,default=50)
    ap.add_argument('--check',action='store_true')
    ap.add_argument('--no-zip',action='store_true')
    args=ap.parse_args()
    if not 600<=args.page_max<=1200 or not 512<=args.panel_max<=1024:ap.error('Page/panel bounds must stay within the documented derivative budgets')
    errors,game=validate()
    if args.check:
        print(json.dumps(dict(errors=errors,note='Read-only packaging preflight; final source exporter must be READY.'),indent=2));return 1 if errors else 0
    if errors:
        print(json.dumps(dict(errors=errors),indent=2));return 1
    return build(args,game)


if __name__=='__main__':
    try:raise SystemExit(main())
    except (ValueError,OSError) as exc:
        print('Packaging failed: '+str(exc),file=sys.stderr);raise SystemExit(1)
