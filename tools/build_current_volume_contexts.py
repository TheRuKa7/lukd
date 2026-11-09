"""Build current author-reference dossiers without importing superseded story excerpts."""
from pathlib import Path
import hashlib,json,re

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'docs/manga/volumes'

def clean(text):
    return re.sub(r'\[([^]]+)\]\((?!https?://)[^)]+\)',r'\1',text)

def main():
    ledger=json.loads((ROOT/'docs/novel/scene_ledger.json').read_text(encoding='utf-8'))
    people=json.loads((ROOT/'docs/novel/character_trajectories.json').read_text(encoding='utf-8'))
    common=['docs/novel/RESOLVED_SERIES_BIBLE.md','docs/novel/PHASE_02_CONTINUITY.md','docs/novel/SOCIETIES_AND_RELATIONSHIPS.md','docs/novel/scene_ledger.json','docs/novel/character_trajectories.json']
    volumes=[]
    for volume in range(1,8):
        rows=[r for r in ledger['chapters'] if r['volume']==volume]
        parts=[f'# Current author context — Volume{volume}','',
            'STATUS: INCOMPLETE AUTHOR REFERENCE. Not an accepted6000-line context, not a native upload and not generation approval.','',
            'The following includes current whole-story author knowledge. Do not feed the full dossier into early story extraction. Use separate bounded story packets. Historical22-chapter excerpts are archived, not imported.','']
        sources=list(common)
        for rel in common[:3]:
            parts += ['## Authority: '+rel,'',clean((ROOT/rel).read_text(encoding='utf-8-sig')),'']
        names={people['aliases'].get(n,n) for r in rows for n in r['cast']}
        parts += ['## Scheduled people — author knowledge only','']
        for person in people['profiles']:
            if person['name'] not in names:continue
            parts += ['### '+person['name'],'']
            for key in ['want','fear','mistaken_belief','competence','harm_or_cost','independent_relationship','voice','private_life','end_state']:
                parts += [key.replace('_',' ').capitalize()+': '+person[key],'']
        parts += ['## Current chapter decisions and drafted prose','']
        for row in rows:
            n=row['chapter'];parts += [f'### Chapter{n}: {row["title"]}','',
                'Relative day: '+row['relative_day'], 'Location: '+row['location'],
                'Focal identities: '+', '.join(row['cast']), 'Decision: '+row['decision'],'']
            for scene in row['scenes']:parts += [scene['id']+': '+scene['action'],'']
            parts += ['Causal exit: '+row['exit_consequence'],'']
            drafts=list((ROOT/f'docs/novel/volume_{volume:02d}').glob(f'chapter_{n:02d}_*.md'))
            if len(drafts)==1:
                rel=drafts[0].relative_to(ROOT).as_posix();sources.append(rel)
                parts += ['#### Draft prose source: '+rel,'',clean(drafts[0].read_text(encoding='utf-8')),'']
            else:parts += ['PROSE NOT WRITTEN. The scene plan above is not a completed chapter.','']
        if volume==1:
            direction='docs/manga/scripts/volume_01/DIRECTION.md';sources.append(direction)
            parts += ['## Volume1 adaptation direction','',clean((ROOT/direction).read_text(encoding='utf-8')),'']
            for ch in range(1,8):
                rel=f'docs/manga/scripts/volume_01/chapter_{ch:02d}_script.md';sources.append(rel)
                parts += ['## Provisional authored page packet','',clean((ROOT/rel).read_text(encoding='utf-8')),'']
        text='\n'.join(parts).rstrip()+'\n'
        path=OUT/f'volume_{volume:02d}_context_working.md';path.write_text(text,encoding='utf-8')
        volumes.append(dict(volume=volume,path=path.relative_to(ROOT).as_posix(),lines=len(text.splitlines()),
            nonempty_lines=sum(bool(s.strip()) for s in text.splitlines()),meets_raw_line_minimum=len(text.splitlines())>=6000,
            substantive_editorial_accepted=False,status='incomplete_current_author_reference',sha256=hashlib.sha256(path.read_bytes()).hexdigest(),
            sources=[dict(path=rel,sha256=hashlib.sha256((ROOT/rel).read_bytes()).hexdigest()) for rel in sources]))
    manifest=dict(target_lines_per_volume=6000,completion=False,evidence_scope='Current author sources and actual line counts; no meaningful-content acceptance or upload claim',volumes=volumes)
    (OUT/'manifest.json').write_text(json.dumps(manifest,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    print(json.dumps([dict(volume=v['volume'],lines=v['lines'],nonempty_lines=v['nonempty_lines'],accepted=False) for v in volumes],indent=2))

if __name__=='__main__':main()
