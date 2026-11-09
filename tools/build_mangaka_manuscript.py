"""Build the authored Mangaka upload manuscript, not illustrated manga pages."""
import hashlib
import html
import json
from pathlib import Path
import re
import markdown
import canon

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'build/mangaka-manuscript'
SOURCES=[
    ('Production brief - rules for the adaptation','docs/manga/SERIES_PRODUCTION_BRIEF.md'),
    ('Chapters01-03 -90 authored page beats','docs/manga/OPENING_SCRIPT_01_03.md'),
    ('Chapters04-22 -570 planned pages','docs/manga/CHAPTER_TREATMENT_04_22.md'),
    ('Reveal and relationship ledger - continuity appendix','docs/manga/SERIES_REVEAL_LEDGER.md'),
]

def build():
    OUT.mkdir(parents=True,exist_ok=True)
    sections=[];inputs=[]
    for title,rel in SOURCES:
        path=ROOT/rel;text=path.read_text(encoding='utf-8-sig')
        text=re.sub(r'\[([^]]+)\]\((?!https?://)[^)]+\)',r'\1',text)
        body=markdown.markdown(text,extensions=['tables','fenced_code','sane_lists'])
        body=re.sub(r'<(/?)h([1-5])>',lambda m:f'<{m[1]}h{int(m[2])+1}>',body)
        sections.append('<section class="part"><div class="part-label">'+html.escape(title)+'</div>'+body+'</section>')
        inputs.append(dict(path=rel,sha256=hashlib.sha256(path.read_bytes()).hexdigest()))
    css='''@page{size:A4}*{box-sizing:border-box}body{margin:0;color:#17151b;font:10.5pt/1.4 var(--body)}
    h1,h2,h3,h4{font-family:var(--display);line-height:1.1;break-after:avoid}h1{font-size:44pt}h2{font-size:28pt}h3{font-size:20pt;margin-top:7mm}
    p,li{orphans:3;widows:3}p{margin:0 0 3mm}strong{font-weight:700}a{color:#653e27}code{font-size:8pt;overflow-wrap:anywhere}
    table{width:100%;border-collapse:collapse;font-size:9pt;line-height:1.28;margin:3mm 0 7mm}thead{display:table-header-group}tr{break-inside:avoid}th,td{padding:2.2mm;border-bottom:1px solid #c9bda9;vertical-align:top}th{background:#242027;color:#fff5df;text-align:left}td:first-child{font-weight:700;min-width:15mm}blockquote{border-left:3px solid #b59a67;padding-left:4mm;color:#5b5146}
    .cover{height:250mm;break-after:page;background:#eee5d4;padding:16mm;display:flex;flex-direction:column;justify-content:center}.cover h1{font-size:59pt;margin:8mm 0}.cover .scope{font-size:24pt}.cover .small{font-size:11pt;margin-top:14mm}.part{break-before:page}.part-label{font:9pt var(--body);letter-spacing:.1em;text-transform:uppercase;border-bottom:2px solid #b28c4b;padding-bottom:3mm;margin:0 0 8mm}'''+canon.open_font_css(OUT)
    source_hash=hashlib.sha256(json.dumps(inputs,sort_keys=True).encode()).hexdigest()
    cover='<section class="cover"><p>AUTHORING MANUSCRIPT /8 NOVEMBER2026</p><h1>ZERO-SUM:<br>OMEN</h1><p class="scope">22 chapters x30 story pages<br>660 B&amp;W story pages</p><p class="small">Mangaka-native production. English left-to-right. Original story and visual direction. Covers, colour inserts and lore appendices are separate.<br><br>This is a production manuscript, not completed illustrated pages. The rejected20-page colour study is excluded.</p></section>'
    page='<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="source-sha256" content="'+source_hash+'"><title>OMEN - Mangaka production manuscript</title><style>'+css+'</style></head><body>'+cover+''.join(sections)+'</body></html>'
    (OUT/'manuscript.html').write_text(page,encoding='utf-8')
    (OUT/'source-manifest.json').write_text(json.dumps(dict(inputs=inputs,source_sha256=source_hash,note='Production manuscript only; no Mangaka chapter generation/export implied'),indent=2)+'\n',encoding='utf-8')
    print(OUT/'manuscript.html')

if __name__=='__main__':build()
