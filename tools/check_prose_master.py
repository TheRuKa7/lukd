"""Fail the full-manuscript file gate without inventing literary acceptance."""
from pathlib import Path
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[1]

def inspect(root=ROOT):
    plan = (root/'docs/manga/SEVEN_VOLUME_NOVEL_PLAN.md').read_text(encoding='utf-8-sig')
    expected = [(int(n), title) for n,title in re.findall(r'(?m)^(\d+)\. \*\*(.*?)\*\* — ',plan)]
    errors = []
    if [n for n,_ in expected] != list(range(1,50)):
        errors.append('Plan must provide ordered chapters1–49')
    chapters = []
    for number,title in expected:
        volume=(number-1)//7+1
        paths=list((root/f'docs/novel/volume_{volume:02d}').glob(f'chapter_{number:02d}_*.md'))
        item=dict(chapter=number,volume=volume,title=title,status='missing',body_words=0)
        if len(paths)>1:
            errors.append(f'Chapter{number}: duplicate prose sources')
        if len(paths)==1:
            path=paths[0]
            raw=path.read_bytes()
            text=raw.decode('utf-8-sig')
            heading=f'## Chapter {number}: {title}'
            body=text.split(heading,1)[1].strip() if text.count(heading)==1 else ''
            words=len(re.findall(r"\b[\w’'-]+\b",body))
            valid=bool(body) and words>=500 and not re.search(r'(?im)^\s*(TODO|TBD|PLACEHOLDER|SUMMARY ONLY)\b',body)
            item.update(status='draft' if valid else 'invalid_source',body_words=words,
                        source=path.relative_to(root).as_posix(),sha256=hashlib.sha256(raw).hexdigest())
            if not valid:errors.append(f'Chapter{number}: wrong heading, very short source or explicit placeholder')
        chapters.append(item)
    missing=[c['chapter'] for c in chapters if c['status']=='missing']
    total=sum(c['body_words'] for c in chapters)
    warnings=[]
    if not 110000<=total<=140000:
        warnings.append('Current word total is outside the110,000–140,000 full-novel planning range')
    return dict(schema_version=1,status='NOT_READY' if missing or errors else 'FILE_GATE_PASS',
                evidence_scope='Chapter identity, substantive-length floor, explicit placeholder screening and hashes; not scene execution, originality or literary acceptance',
                expected_chapters=49,draft_chapters=sum(c['status']=='draft' for c in chapters),
                missing_chapters=missing,body_words=total,errors=errors,warnings=warnings,
                full_novel_revision_ready=not missing and not errors,
                editorial_accepted=False,chapters=chapters)

def main():
    report=inspect()
    out=ROOT/'output/novel/prose_master_gate.json'
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(report,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    print(json.dumps({key:report[key] for key in ['status','draft_chapters','missing_chapters','body_words','errors','warnings','full_novel_revision_ready']},indent=2))
    raise SystemExit(0 if report['full_novel_revision_ready'] else 1)

if __name__=='__main__':
    main()
