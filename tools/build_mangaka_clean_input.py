"""Prepare a clean story-only upload; no cover, tables or production appendix."""
import argparse
import hashlib
import json
from pathlib import Path
import markdown
import canon

ROOT=Path(__file__).resolve().parents[1]

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--source',default='docs/manga/MANGAKA_CH01_CLEAN_INPUT.md');args=ap.parse_args()
    source=(ROOT/args.source).resolve()
    if ROOT not in source.parents or not source.is_file():raise ValueError('Source must be a real repository manuscript')
    folder=ROOT/'build/mangaka-clean'/source.stem;folder.mkdir(parents=True,exist_ok=True)
    text=source.read_text(encoding='utf-8-sig')
    content=markdown.markdown(text,extensions=['sane_lists'])
    css='''@page{size:A4}body{margin:0;color:#17151b;font:10.5pt/1.4 var(--body)}h1,h2{font-family:var(--display);line-height:1.1;break-after:avoid}h1{font-size:28pt}p{margin:0 0 3mm;break-inside:avoid;orphans:3;widows:3}ol{padding-left:6mm}li{margin:0 0 3mm;break-inside:avoid}'''+canon.open_font_css(folder)
    digest=hashlib.sha256(source.read_bytes()).hexdigest()
    (folder/'input.html').write_text('<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="source-sha256" content="'+digest+'"><title>OMEN story-only input</title><style>'+css+'</style></head><body>'+content+'</body></html>',encoding='utf-8')
    (folder/'source-manifest.json').write_text(json.dumps(dict(source=args.source,sha256=digest,words=len(text.split()),characters=len(text),note='Story-only provider input. No chapter production implied.'),indent=2)+'\n',encoding='utf-8')
    print(folder/'input.html')

if __name__=='__main__':main()
