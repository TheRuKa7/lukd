"""Inventory the current edition without inferring creative or runtime acceptance."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib,json,re

ROOT=Path(__file__).resolve().parents[1]
def read(rel):return (ROOT/rel).read_text(encoding='utf-8-sig')
def digest(rel):return hashlib.sha256((ROOT/rel).read_bytes()).hexdigest()
def main():
    errors=[]
    sources=['docs/novel/RESOLVED_SERIES_BIBLE.md','docs/manga/SEVEN_VOLUME_NOVEL_PLAN.md','docs/TEN_PHASE_PLAN.md','docs/manga/README.md','docs/novel/README.md']
    plan=read(sources[1]);chapters=[]
    authored={}
    script_manifest=ROOT/'output/manga/volume_01_script_manifest.json'
    if script_manifest.is_file():
        scripts=json.loads(script_manifest.read_text(encoding='utf-8'))
        if scripts['source_sha256']!=digest('docs/manga/scripts/volume_01/pages.tsv'):
            errors.append('Authored page source differs from compiled script manifest')
        for entry in scripts['chapters']:
            if digest(entry['script_path'])!=entry['script_sha256'] or digest(entry['prose_source'])!=entry['prose_sha256']:
                errors.append('Stale manga/prose link for chapter'+str(entry['chapter']))
            authored[entry['chapter']]=entry['authored_pages']
    prose={}
    for path in sorted((ROOT/'docs/novel').glob('volume_*/chapter_*.md')):
        match=re.fullmatch(r'chapter_(\d+)_.*\.md',path.name)
        if not match:continue
        n=int(match[1])
        if n in prose:errors.append(f'Duplicate prose chapter: {n}')
        if path.parent.name!=f'volume_{(n-1)//7+1:02d}':errors.append(f'Wrong prose volume: {path}')
        prose[n]=path.relative_to(ROOT).as_posix()
    for number,title in re.findall(r'(?m)^(\d+)\. \*\*(.*?)\*\* — ',plan):
        n=int(number);rel=prose.get(n)
        if rel and f'## Chapter {n}: {title}' not in read(rel):errors.append(f'Prose heading differs from plan: {rel}')
        body='\n'.join(line for line in read(rel).splitlines() if not line.startswith('#')) if rel else ''
        chapters.append(dict(chapter=n,volume=(n-1)//7+1,title=title,outline_present=True,prose_path=rel,prose_status='draft' if rel else 'not_written',prose_words=len(re.findall(r"\b[\w’'-]+\b",body)),prose_sha256=digest(rel) if rel else None,editorial_accepted=False,target_story_pages=22,authored_current_page_instructions=authored.get(n,0),accepted_native_story_pages=0))
    if set(prose)-set(range(1,50)):errors.append('Prose outside current49-chapter edition')
    if [x['chapter'] for x in chapters]!=list(range(1,50)):errors.append('Chapter scaffold must be ordered1–49')
    contexts=[]
    for v in range(1,8):
        rel=f'docs/manga/volumes/volume_{v:02d}_context_working.md';content=read(rel).splitlines();lines=len(content);nonempty=sum(bool(s.strip()) for s in content)
        contexts.append(dict(volume=v,path=rel,lines=lines,nonempty_lines=nonempty,required_lines=6000,meets_raw_line_minimum=lines>=6000,meets_line_minimum=nonempty>=6000,substantive_editorial_accepted=False,sha256=digest(rel)))
    boards=json.loads(read('art/catalog/higgsfield_artbook_outputs.json'))['outputs'];assets=[]
    for b in boards:
        rel=b['path'];present=(ROOT/rel).is_file();sha=digest(rel) if present else None
        if not present or sha!=b['sha256']:errors.append('Missing/changed selected asset: '+rel)
        assets.append(dict(id=b['request_id'],path=rel,kind=b['kind'],sha256=sha,present=present,source_manifest_match=sha==b['sha256']))
    pdf='output/pdf/ZERO-SUM_OMEN_Concept_Collection.pdf';qa=json.loads(read('output/pdf/ZERO-SUM_OMEN_Concept_Collection.qa.json'))
    if digest(pdf)!=qa['sha256']:errors.append('Concept PDF differs from reviewed output')
    if len(assets)!=91:errors.append('Expected91 selected boards')
    if len(re.findall(r'^## Volume ',plan,re.M))!=7:errors.append('Expected7 volumes')
    if '1,078' not in read('docs/manga/README.md'):errors.append('Current manga entry point lacks current scope')
    report=dict(schema_version=1,observed_utc=datetime.now(timezone.utc).isoformat(),evidence_scope='Files, hashes and declared draft status; not literary acceptance or tool-account live state',errors=errors,source_authority=[dict(path=x,sha256=digest(x)) for x in sources],totals=dict(volumes=7,chapters=len(chapters),target_story_pages=1078,prose_drafts=sum(x['prose_path'] is not None for x in chapters),editorially_accepted_chapters=0,authored_current_page_instructions=sum(authored.values()),accepted_native_story_pages=0,selected_boards=len(assets)),chapters=chapters,contexts=contexts,selected_assets=assets,concept_collection=dict(path=pdf,pages=qa['pages'],bytes=(ROOT/pdf).stat().st_size,sha256=digest(pdf),qa_path='output/pdf/ZERO-SUM_OMEN_Concept_Collection.qa.json'))
    (ROOT/'docs/phase_01_inventory.json').write_text(json.dumps(report,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    print(json.dumps(dict(errors=errors,totals=report['totals'],context_lines=[x['lines'] for x in contexts],concept_pages=qa['pages']),indent=2))
    raise SystemExit(bool(errors))
if __name__=='__main__':main()
