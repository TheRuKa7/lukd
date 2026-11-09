"""Vendor unmodified OFL fonts from the official Google Fonts repository."""
import hashlib
import json
from pathlib import Path
import urllib.request

ROOT=Path(__file__).resolve().parents[1]
DEST=ROOT/'art/fonts'
SOURCES={
    'BarlowSemiCondensed-Regular.ttf':'barlowsemicondensed/BarlowSemiCondensed-Regular.ttf',
    'BarlowSemiCondensed-Bold.ttf':'barlowsemicondensed/BarlowSemiCondensed-Bold.ttf',
    'BarlowSemiCondensed-OFL.txt':'barlowsemicondensed/OFL.txt',
    'BebasNeue-Regular.ttf':'bebasneue/BebasNeue-Regular.ttf',
    'BebasNeue-OFL.txt':'bebasneue/OFL.txt',
}

def main():
    DEST.mkdir(parents=True,exist_ok=True); records=[]
    for name,path in SOURCES.items():
        url='https://raw.githubusercontent.com/google/fonts/main/ofl/'+path
        with urllib.request.urlopen(url,timeout=60) as response: content=response.read()
        (DEST/name).write_bytes(content)
        records.append(dict(file=name,url=url,sha256=hashlib.sha256(content).hexdigest(),bytes=len(content),license='SIL Open Font License 1.1; bundled unmodified'))
    (DEST/'sources.json').write_text(json.dumps(dict(retrieved='2026-11-08',files=records),indent=2)+'\n',encoding='utf-8')
    print('Vendored',len(records),'font/license files with provenance')

if __name__=='__main__':main()
