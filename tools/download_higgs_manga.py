"""Fetch the exact completed Higgsfield page artifacts without changing their pixels."""
from concurrent.futures import ThreadPoolExecutor
import argparse
import hashlib
import json
from pathlib import Path
import urllib.request
from PIL import Image, ImageOps, ImageDraw

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / 'art/manga/chapter_01'

def download(job):
    if job['status'] != 'completed':
        raise RuntimeError(f"Page {job['index']} is not complete")
    target = BASE / 'clean' / f"p{job['index']:03d}.png"
    with urllib.request.urlopen(job['result_url'], timeout=120) as response:
        content = response.read()
    target.write_bytes(content)
    with Image.open(target) as im:
        im.verify()
    with Image.open(target) as im:
        size = list(im.size)
    return dict(page=job['index'], job_id=job['job_id'], provider='Higgsfield',
                model='gpt_image_2_6', requested_quality='high', requested_resolution='4k',
                path=target.relative_to(ROOT).as_posix(), pixels=size,
                sha256=hashlib.sha256(content).hexdigest(), status='generated; visual QA pending')

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--jobs',default='build/higgs_manga_downloads.json');args=ap.parse_args()
    jobs=json.loads((ROOT/args.jobs).read_text(encoding='utf-8-sig'))
    records=sorted(ThreadPoolExecutor(max_workers=4).map(download,jobs),key=lambda x:x['page'])
    previous=BASE/'higgsfield_outputs.json'
    if previous.exists():
        merged={r['page']:r for r in json.loads(previous.read_text(encoding='utf-8'))['outputs']}
        merged.update({r['page']:r for r in records});records=sorted(merged.values(),key=lambda r:r['page'])
    (BASE/'higgsfield_outputs.json').write_text(json.dumps(dict(date='2026-11-08',outputs=records),indent=2)+'\n',encoding='utf-8')
    for start in range(0,len(records),10):
        sheet=Image.new('RGB',(1500,1100),'#ece7dd');draw=ImageDraw.Draw(sheet)
        for i,r in enumerate(records[start:start+10]):
            with Image.open(ROOT/r['path']) as im:
                thumb=ImageOps.contain(im.convert('RGB'),(290,500))
                x=(i%5)*300+(300-thumb.width)//2;y=(i//5)*550+30
                sheet.paste(thumb,(x,y));draw.text(((i%5)*300+10,(i//5)*550+7),f"Page {r['page']:02d}",fill='black')
        sheet.save(ROOT/f"build/higgs_contact_{start+1:02d}.jpg",quality=93)
    print(json.dumps(dict(pages=len(records),sizes=sorted({tuple(r['pixels']) for r in records}))))

if __name__=='__main__': main()
