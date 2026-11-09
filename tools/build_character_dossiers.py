"""Compile authored character trajectories and audit every ledger cast label."""
import copy,csv,hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'docs/novel'
FIELDS=['want','fear','mistaken_belief','competence','harm_or_cost','decisive_chapters','independent_relationship','voice','private_life','end_state']
GROUPS={'House staff':'Casino employees with independent wage/property claims','Synod guards':'Institutional staff; obedience is not a universal personal motive','all eight core companions':'Vesper,Maeve,Hina,Jinling,Bai Si,Shunya,Prima,Fibi','children':'Age-appropriate residents; no mandatory fighting role','companions':'Current travel roster, not a three-member combat limit','courier':'Paid carrier on the established dispatch route','depositors':'Reserve claimants distinct from the Exchange owner','dock witnesses':'Cooperative residents retaining their own testimony','guards':'Assigned security personnel with actual orders and physical limits','regional councils':'Distinct provisional local bodies, not one global mind','regional delegates':'Specific limited representatives whose mandates are recorded','surveyors':'Basilica operators with permits and machinery, not celestial figures','witness':'Custodian of a particular statement, not omniscient narration','workers':'Skilled residents with varied wages, obligations and political positions'}
ALIASES={'Ivo by record':'Ivo','Livia by letter':'Livia','Nought by letter':'Nought'}
CORE=['Nil','Vesper','Maeve','Hina','Jinling','Bai Si','Shunya','Prima','Fibi']

def validate(profiles,ledger,groups=GROUPS):
    errors=[];names=[x['name'] for x in profiles];lookup=set(names)
    if len(lookup)!=len(names):errors.append('Duplicate character profile')
    if not set(CORE)<=lookup:errors.append('Missing principal profile')
    for p in profiles:
        for key in FIELDS:
            if not p.get(key):errors.append(p['name']+': empty '+key)
        if any(not 1<=n<=49 for n in p['chapter_ids']):errors.append(p['name']+': invalid scheduled chapter')
        if p['name']!='Nil' and p['name'] in CORE and p['independent_relationship'].startswith('Nil '):errors.append(p['name']+': only Nil relationship')
    for r in ledger['chapters']:
        for token in r['cast']:
            canonical=ALIASES.get(token,token)
            if canonical not in lookup and token not in groups:errors.append(f'Chapter{r["chapter"]}: uncovered cast label '+token)
    return errors

def main():
    src=OUT/'CHARACTER_TRAJECTORIES.tsv'
    with src.open(encoding='utf-8-sig',newline='') as f:profiles=list(csv.DictReader(f,delimiter='|'))
    for p in profiles:
        p['chapter_ids']=[int(x) for x in p['decisive_chapters'].split(',')]
        p['actor_type']='machine' if p['name']=='Debt Hound' else 'remembered_deceased' if p['name']=='Wen' else 'person_or_supernatural_person'
    ledger=json.loads((OUT/'scene_ledger.json').read_text(encoding='utf-8'))
    errors=validate(profiles,ledger)
    if errors:raise ValueError(errors)
    mapping=[]
    for r in ledger['chapters']:
        for token in r['cast']:
            mapping.append(dict(chapter=r['chapter'],label=token,canonical=ALIASES.get(token,token),kind='group' if token in GROUPS else 'indirect_record' if token in ALIASES else 'profile'))
    data=dict(schema_version=1,evidence_scope='Authored development dossiers and cast coverage, not completed prose or approved new artwork',source_sha256=hashlib.sha256(src.read_bytes()).hexdigest(),scene_ledger_sha256=hashlib.sha256((OUT/'scene_ledger.json').read_bytes()).hexdigest(),profiles=profiles,groups=GROUPS,aliases=ALIASES,cast_coverage=mapping)
    (OUT/'character_trajectories.json').write_text(json.dumps(data,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    md=['# Character development dossiers','', 'Authored Phase3 trajectories for the current49-chapter edition. Read with [societies and relationships](SOCIETIES_AND_RELATIONSHIPS.md) and [the scene ledger](SCENE_LEDGER.md). These contain future knowledge for authors, not a command to reveal it in an early chapter. Scheduled anchors are selected decisive moments, not the complete appearance list. Names label existing identities; group and indirect-reference coverage is recorded separately.','']
    for p in profiles:
        md += ['## '+p['name'],'',f'Actor type: {p["actor_type"]}. Decisive chapters: {p["decisive_chapters"]}.','']
        for field in FIELDS:
            if field!='decisive_chapters':md += ['**'+field.replace('_',' ').capitalize()+':** '+p[field]+'.','']
    (OUT/'CHARACTER_DOSSIERS.md').write_text('\n'.join(md),encoding='utf-8')
    bad=copy.deepcopy(profiles);bad.pop(next(i for i,p in enumerate(bad) if p['name']=='Livia'))
    assert validate(bad,ledger)
    bad=copy.deepcopy(profiles);bad[0]['chapter_ids']=[50]
    assert validate(bad,ledger)
    bad=copy.deepcopy(profiles);bad[1]['voice']=''
    assert validate(bad,ledger)
    bad=copy.deepcopy(profiles);bad.append(copy.deepcopy(bad[0]))
    assert validate(bad,ledger)
    print(json.dumps(dict(status='PASS',profiles=len(profiles),groups=len(GROUPS),cast_mentions=len(mapping),uncovered_labels=0,negative_cases_rejected=4,limits='Field coverage and identity checks do not establish literary execution, cultural approval or scene quality.'),indent=2))
if __name__=='__main__':main()
