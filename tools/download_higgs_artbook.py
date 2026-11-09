"""Fetch completed illustrated-board originals and record their exact provenance."""
import argparse
from concurrent.futures import ThreadPoolExecutor
import hashlib
import json
from pathlib import Path
import urllib.request
from PIL import Image, ImageOps, ImageDraw

ROOT=Path(__file__).resolve().parents[1]
CATALOG=ROOT/'art/catalog/higgsfield_artbook_requests.json'
OUTPUTS=ROOT/'art/catalog/higgsfield_artbook_outputs.json'

def main():
    ap=argparse.ArgumentParser();ap.add_argument('jobs');args=ap.parse_args()
    manifest=json.loads(CATALOG.read_text(encoding='utf-8-sig'))
    requests={r['index']:r for r in manifest['requests']}
    jobs=json.loads((ROOT/args.jobs).read_text(encoding='utf-8-sig'))
    def download(job):
        if job['status']!='completed':raise ValueError('Not completed: '+str(job['index']))
        r=requests[job['index']];p=ROOT/r['output_target'];p.parent.mkdir(parents=True,exist_ok=True)
        with urllib.request.urlopen(job['result_url'],timeout=120) as response:content=response.read()
        p.write_bytes(content)
        with Image.open(p) as im:im.verify()
        with Image.open(p) as im:size=list(im.size)
        return dict(index=r['index'],request_id=r['request_id'],catalog_ids=r.get('catalog_ids',[]),
                    name=r['name'],kind=r['kind'],path=r['output_target'],sha256=hashlib.sha256(content).hexdigest(),pixels=size,
                    provider='Higgsfield',model='gpt_image_2_6',quality='high',requested_resolution='4k',
                    job_id=job['job_id'],reference_path=r['reference_path'],reference_sha256=r['reference_sha256'],
                    status='Illustrated design proposal; distinct from actual Blender camera renders; visual QA pending')
    records=list(ThreadPoolExecutor(max_workers=4).map(download,jobs))
    merged={r['index']:r for r in json.loads(OUTPUTS.read_text(encoding='utf-8'))['outputs']} if OUTPUTS.exists() else{}
    merged.update({r['index']:r for r in records});all_records=sorted(merged.values(),key=lambda r:r['index'])
    OUTPUTS.write_text(json.dumps(dict(date='2026-11-08',requests_sha256=hashlib.sha256(CATALOG.read_bytes()).hexdigest(),outputs=all_records),indent=2)+'\n',encoding='utf-8')
    first=min(r['index'] for r in records)
    sheet=Image.new('RGB',(1600,1450),'#eee6d6');draw=ImageDraw.Draw(sheet)
    for i,r in enumerate(sorted(records,key=lambda r:r['index'])):
        with Image.open(ROOT/r['path']) as im:
            thumb=ImageOps.contain(im.convert('RGB'),(390,255));x=(i%4)*400+(400-thumb.width)//2;y=(i//4)*290+25
            sheet.paste(thumb,(x,y));draw.text(((i%4)*400+7,(i//4)*290+5),f"{r['index']:02d} {r['name']}",fill='black')
    sheet.save(ROOT/f'build/higgs_art_contact_{first:02d}.jpg',quality=95)
    print(json.dumps(dict(downloaded=len(records),total=len(all_records),actual_sizes=sorted({tuple(r['pixels']) for r in records}))))

if __name__=='__main__':main()
