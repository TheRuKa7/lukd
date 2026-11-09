"""Compile authored page plans; never count them as generated or accepted manga."""
from pathlib import Path
import argparse,csv,hashlib,json,re

ROOT=Path(__file__).resolve().parents[1]
SRC=ROOT/'docs/manga/scripts/volume_01'

def digest(data):
    return hashlib.sha256(data).hexdigest()

def parse_rows(rows):
    pages=[]
    for row in rows:
        ch,p=int(row['chapter']),int(row['page'])
        if not 1<=ch<=7 or not 1<=p<=22:raise ValueError('Chapter/page outside Volume1')
        if not row['turn'].strip() or not row['layout'].strip():raise ValueError('Missing page purpose/layout')
        panels=[]
        for i,part in enumerate(row['panels'].split(' ~~ '),1):
            split=part.split(' >> ',1)
            visual=split[0].strip()
            if not re.match(r'^\[(W|M|C|EC|S|L)\] ',visual):raise ValueError('Missing shot/visual: '+visual)
            if len(visual.split())<5:raise ValueError('Visual too vague')
            lines=[]
            for line in split[1].split(' // ') if len(split)>1 else []:
                if ':' not in line:raise ValueError('Unowned lettering: '+line)
                owner,text=line.split(':',1)
                if not owner or not text.strip():raise ValueError('Empty speaker or text')
                lines.append(dict(owner=owner.strip(),text=text.strip()))
            panels.append(dict(id=f'V01C{ch:02d}P{p:02d}F{i:02d}',visual=visual,lettering=lines))
        if not 2<=len(panels)<=5:raise ValueError('Panel count outside authored2–5 contract')
        words=sum(len(re.findall(r"\b[\w’'-]+\b",x['text'])) for panel in panels for x in panel['lettering'])
        if words>90:raise ValueError(f'Lettering too dense: chapter{ch} page{p}: {words}')
        pages.append(dict(chapter=ch,page=p,global_page=(ch-1)*22+p,layout=row['layout'],turn=row['turn'],panels=panels,lettering_words=words))
    if [(p['chapter'],p['page']) for p in pages]!=[(c,p) for c in range(1,8) for p in range(1,23)]:
        raise ValueError('Expected ordered, unique7x22 authored pages')
    return pages

def chapter_text(ch,pages,title):
    out=[f'# Chapter {ch}: {title}','', 'Provisional page script; English LTR; B&W story pages. Not approved for generation.','']
    for page in pages:
        out += [f'## Page {page["page"]:02d} — volume page {page["global_page"]:03d}', '',
                'Layout: '+page['layout']+'.', 'Turn: '+page['turn'], '']
        for panel in page['panels']:
            out += [f'### {panel["id"]}', '', panel['visual'], '']
            for line in panel['lettering']:out += [line['owner']+': '+line['text'],'']
    return '\n'.join(out).rstrip()+'\n'

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--check',action='store_true');args=ap.parse_args()
    raw=(SRC/'pages.tsv').read_bytes()
    with (SRC/'pages.tsv').open(encoding='utf-8',newline='') as f:pages=parse_rows(list(csv.DictReader(f,delimiter='|')))
    ledger=json.loads((ROOT/'docs/novel/scene_ledger.json').read_text(encoding='utf-8'))
    inputs=json.loads((SRC/'story_inputs.json').read_text(encoding='utf-8'))
    cast=json.loads((SRC/'CAST_AND_PROPS.json').read_text(encoding='utf-8'))
    ids=[x['id'] for x in cast['cast']]+[x['id'] for x in cast['machine_instances']]+[x['id'] for x in cast['props']]
    if len(ids)!=len(set(ids)):raise ValueError('Duplicate local identity/prop IDs')
    references={x['request_id'] for x in json.loads((ROOT/'art/catalog/higgsfield_artbook_outputs.json').read_text(encoding='utf-8'))['outputs']}
    for entry in cast['cast']+cast['machine_instances']:
        ref=entry.get('candidate_reference',entry.get('base_reference'))
        if ref and ref not in references:raise ValueError('Unknown candidate reference: '+ref)
    if set(inputs)!={str(n) for n in range(1,8)}:raise ValueError('Need exactly seven authored lean story inputs')
    outputs=[];chapters=[];compiled=['# The Remainder — Volume1 provisional page script','']
    for ch in range(1,8):
        title=ledger['chapters'][ch-1]['title']
        sources=list((ROOT/'docs/novel/volume_01').glob(f'chapter_{ch:02d}_*.md'))
        if len(sources)!=1:raise ValueError('Missing unique prose source')
        subset=[p for p in pages if p['chapter']==ch]
        script=chapter_text(ch,subset,title)
        path=SRC/f'chapter_{ch:02d}_script.md'
        story=f'# Chapter {ch}: {title}\n\n'+inputs[str(ch)].strip()+'\n'
        if len(story)>3500:raise ValueError('Lean story exceeds local3500-character packet budget')
        outputs += [(path,script.encode()),(ROOT/f'output/manga/native_inputs/volume_01_chapter_{ch:02d}_story.md',story.encode())]
        chapters.append(dict(chapter=ch,title=title,prose_source=sources[0].relative_to(ROOT).as_posix(),
            prose_sha256=digest(sources[0].read_bytes()),script_path=path.relative_to(ROOT).as_posix(),
            script_sha256=digest(script.encode()),authored_pages=len(subset),native_story_characters=len(story),
            native_story_sha256=digest(story.encode()),approved_for_generation=False))
        compiled += [script]
    data=dict(schema_version=1,edition='seven_volume_49_chapter',volume=1,status='provisional_script',reading_direction='ltr',story_art='black_and_white',
              source_sha256=digest(raw),direction_sha256=digest((SRC/'DIRECTION.md').read_bytes()),
              story_inputs_sha256=digest((SRC/'story_inputs.json').read_bytes()),cast_and_props_sha256=digest((SRC/'CAST_AND_PROPS.json').read_bytes()),authored_pages=len(pages),
              panels=sum(len(p['panels']) for p in pages),accepted_native_pages=0,approved_for_generation=False,chapters=chapters,pages=pages)
    manifest={k:v for k,v in data.items() if k!='pages'}
    outputs += [(ROOT/'output/manga/volume_01_script.json',(json.dumps(data,indent=2,ensure_ascii=False)+'\n').encode()),
                (ROOT/'output/manga/volume_01_script_manifest.json',(json.dumps(manifest,indent=2,ensure_ascii=False)+'\n').encode()),
                (ROOT/'output/manga/volume_01_page_script.md',('\n'.join(compiled).rstrip()+'\n').encode())]
    for path,value in outputs:
        if args.check:
            if not path.is_file() or path.read_bytes()!=value:raise ValueError('Missing/stale output: '+str(path))
        else:
            path.parent.mkdir(parents=True,exist_ok=True);path.write_bytes(value)
    print(json.dumps(dict(status='PASS',authored_pages=len(pages),panels=data['panels'],chapters=len(chapters),
                         native_packet_characters=[c['native_story_characters'] for c in chapters],accepted_native_pages=0,approved_for_generation=False),indent=2))

if __name__=='__main__':main()
