"""Build a provenance-backed collection of existing Higgsfield boards."""
from pathlib import Path
import hashlib,json,io
from PIL import Image
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import HexColor

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'output/pdf/ZERO-SUM_OMEN_Concept_Collection.pdf'
def main():
    data=json.loads((ROOT/'art/catalog/higgsfield_artbook_outputs.json').read_text(encoding='utf-8-sig'))['outputs']
    catalog={e['id']:e for e in json.loads((ROOT/'art/catalog/characters.json').read_text(encoding='utf-8-sig'))['entries']}
    pdfmetrics.registerFont(TTFont('Body',str(ROOT/'art/fonts/BarlowSemiCondensed-Regular.ttf')))
    pdfmetrics.registerFont(TTFont('Title',str(ROOT/'art/fonts/BebasNeue-Regular.ttf')))
    OUT.parent.mkdir(parents=True,exist_ok=True)
    c=canvas.Canvas(str(OUT),pagesize=(960,680)); manifest=[]
    def base(title,sub):
        c.setFillColor(HexColor('#efe6d2'));c.rect(0,0,960,680,fill=1,stroke=0)
        c.setFillColor(HexColor('#19151e'));c.setFont('Title',28);c.drawString(30,641,title)
        c.setFont('Body',11);c.drawString(30,621,sub)
        c.setFont('Body',9);c.drawString(30,17,'ZERO-SUM: OMEN / THE REMAINDER / CONCEPT COLLECTION / 8 NOVEMBER 2026')
        c.drawRightString(930,17,str(c.getPageNumber()))
    def lines(rows,y=570):
        c.setFont('Body',15)
        for row in rows:
            c.drawString(45,y,row);y-=29
    base('THE REMAINDER','An illustrated concept collection for ZERO-SUM: OMEN')
    lines(['Painted world. Inked people.','84 cast / costume / encounter boards and 7 regional environment boards.','Existing Higgsfield illustrations, collected without new generation.','Original PNGs and job provenance remain preserved in the repository.','Spoilers: the complete cast and final-region design appear in this book.','The seven-volume story is under development; these are visual references.'])
    cover=Image.open(ROOT/'art/concepts/complete/env_meridian.png').convert('RGB');cover.thumbnail((1800,1200))
    coverbuf=io.BytesIO();cover.save(coverbuf,format='JPEG',quality=86)
    c.drawImage(ImageReader(coverbuf),40,60,880,330,preserveAspectRatio=True,anchor='c')
    c.showPage()
    base('HOW TO READ THE COLLECTION','Scope, identity and evidence')
    lines(['Character boards propose front, anatomical left, anatomical right and rear views.','They are illustrations, not proof of a rigged or anatomically validated 3D model.','Environment boards propose top, 2.5D and front compositions.','Actual Blender camera drafts remain separately indexed in the complete artbook.','The same person can appear in several outfits; a board is not always a new character.','Selected boards retain their original lettering gaps: exact numeric overlays require authoring.','Vetala is an upright costume study; its action pose is not established by this image.','Broad visual triage exists. Final cultural, animation and game acceptance remain separate.'])
    c.showPage()
    base('CURRENT STORY DIRECTION','Resolved series bible / 49 chapters / 1,078 story pages')
    lines(['NIL starts as a registration designation. Nil becomes a chosen personal name in chapter 4.','The decoder stays on the RIGHT wrist; the longer coat tail stays on the LEFT.','Civic allocation, chosen resonance, Audit Balance and Audit Omen remain distinct.','The protagonist is a person, not a royal heir or an ingredient owned by a god.','Hina remains 99 until the one-year-later epilogue. Bai Si has four lanterns.','Varro keeps his mature build across boss and ally appearances.','New story details need new design evidence: Mara Vale and Wen have no dedicated boards.','Baker, the shrine interior and several daily-life props also lack dedicated approved plates.','Existing concepts do not establish every future story scene or expression sheet.'])
    c.showPage()
    for item in data:
        path=ROOT/item['path'];raw=path.read_bytes();sha=hashlib.sha256(raw).hexdigest()
        if not path.is_file():raise FileNotFoundError(path)
        label=item['name'];ids=item.get('catalog_ids',[])
        if ids and ids[0] in catalog:
            entry=catalog[ids[0]];label=entry['name'];detail=entry.get('outfit') or entry.get('role','')
        else:detail='Regional composition and material reference'
        base(label, str(detail)[:155])
        im=Image.open(io.BytesIO(raw)).convert('RGB');im.thumbnail((2400,1600))
        buf=io.BytesIO();im.save(buf,format='JPEG',quality=86)
        c.drawImage(ImageReader(buf),30,70,900,540,preserveAspectRatio=True,anchor='c',mask='auto')
        c.setFont('Body',9);c.drawString(30,49,item['request_id']+' / Higgsfield / illustrated proposal')
        c.drawString(30,35,'Source SHA256 '+sha[:24]+' / '+('upright costume study' if item['index']==68 else 'source PNG preserved'))
        manifest.append(dict(page=c.getPageNumber(),request_id=item['request_id'],path=item['path'],sha256=sha,job_id=item['job_id'],kind=item['kind'],catalog_ids=ids,initial_manifest_hash_match=sha==item['sha256']))
        c.showPage()
    c.save()
    report=dict(pages=3+len(data),cast_boards=sum(x['kind']=='character_turnaround' for x in data),environment_boards=sum(x['kind']=='environment_three_view' for x in data),new_generations=0,boards=manifest,pdf_sha256=hashlib.sha256(OUT.read_bytes()).hexdigest(),bytes=OUT.stat().st_size)
    (OUT.with_suffix('.manifest.json')).write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in report.items() if k!='boards'},indent=2))
if __name__=='__main__':main()
