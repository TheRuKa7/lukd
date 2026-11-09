"""Compile authored scene rows and verify temporal prerequisites, not prose quality."""
import csv,hashlib,json,re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'docs/novel'
PROOFS={'enma_page':(11,14,'Hina'),'true_accounts':(20,21,'Jinling'),'dead_count':(18,19,'Bai Si'),'remainder_equation':(23,28,'Shunya with Nil consent'),'lachesis_thread':(32,35,'Prima'),'first_gear_horseshoe':(33,35,'Maeve'),'marked_deck':(16,41,'Vesper'),'black_book_page':(39,41,'Fibi')}
SEALS={7:1,14:9,21:8,27:0,35:2,41:7}
DECISIONS=['Interrupt the seizure at the cost of anonymity','Return six existing units rather than flee','Accept shelter and hear the risks without surrendering choice','Choose Nil as a name and7 as a separate resonance','Coordinate with Vesper despite an unresolved fee','Help the forge and choose Horseshoe','Spare Varro and accept the slower route','Work the ferry crossing rather than demand passage','Follow Hina to a household instead of the court','Restore Hina\'s patch and listen to her objection','Accept a witnessed absence without calling it soullessness','Hear Tamamo\'s actual terms before answering','Refuse permanence purchased with another person','Reopen care channels and carry the independent record','Negotiate shelter with a right to leave','Present a tentative comparison as certain, causing harm','Withdraw the claim publicly and restore access','Preserve contradictory testimony instead of rounding it away','Make a bounded correction with counter-evidence','Protect the archive and admit withheld culpability','Fund specific relief and accept divided oversight','Limit the investigation before granting access','Retrieve the private record without claiming resurrection','Renew consent when the question changes','Ask for the plain conclusion once evidence converges','Refuse further testing and choose the engine mission','Disable machinery while preserving uncertainty and independent sky','Warn stewards and follow the dated school threat','Question an exclusion rule while still under escort','Disclose past complicity before demanding trust','Defy orders and accept residents\' direction','Sacrifice a permitted ribbon rather than protected evidence','Preserve the dated gear and name the personal risk','Contest the doctrine through remaining lawful options','Save the teacher without restoring his office','Enter the House jurisdiction after disclosed terms','Fibi invites investigation and states her own future','Use corroborated prior records without killing Fibi again','Fibi chooses cancellation and limits Vesper\'s involvement','Accept Mara\'s refusal, restitution and a fair loss','Relinquish the control claim and confirm cancellation separately','Livia consents to care; Varro offers restitution as a guest','Authorize a bounded transition with dissent and a withdrawal condition','Use distinct credentials and Ivo\'s earned defection','Refuse to treat freed chance as automatically just','Reject coercion after hearing its genuine benefits and costs','Protect essential coverage while opposing Fixed Fate','Yield executive control and renew each contributor\'s permission','Implement limited reform and choose ordinary repair work']

def validate(data):
    errors=[];rows=data['chapters']
    if [r['chapter'] for r in rows]!=list(range(1,50)):errors.append('Expected ordered49 chapters')
    for r in rows:
        n=r['chapter']
        if r['volume']!=(n-1)//7+1:errors.append(f'Chapter{n}: wrong volume')
        if len(r['scenes'])!=3 or any(not x['action'].strip() for x in r['scenes']):errors.append(f'Chapter{n}: missing authored scenes')
        if r['requires_previous_chapter']!=(n-1 if n>1 else None):errors.append(f'Chapter{n}: broken causal chain')
        if not r['decision'] or not r['exit_consequence']:errors.append(f'Chapter{n}: absent decision/consequence')
    gates=data['gates']
    if gates['origin_confirmed']!=26 or gates['origin_evidence_converges']!=25 or gates['physical_cage_revealed']!=45:errors.append('Reveal gate moved')
    for p in data['proofs']:
        if not 1<=p['introduced']<=p['secured']<gates['proof_review']<gates['positive_sum']:errors.append('Invalid proof acquisition/use: '+p['id'])
    if len({p['id'] for p in data['proofs']})!=8:errors.append('Missing/duplicate protected proof')
    seals=data['seals']
    if [s['digit'] for s in seals]!=[1,9,8,0,2,7] or len(seals)!=6 or any(s['secured']>=gates['ritual_gate'] for s in seals):errors.append('Seal gate prerequisites invalid')
    if gates['mandates_ratified']>=gates['positive_sum'] or gates['small_test']>=gates['mandates_ratified'] or gates['failed_test']>=gates['small_test']:errors.append('Ending mechanism/mandate unseeded')
    stages=data['core_arcs']
    if len(stages)!=8 or any(len(v)!=4 or v!=sorted(v) or v[-1]>gates['proof_review'] for v in stages.values()):errors.append('Core relationship schedule incomplete or late')
    return errors

def main():
    source=OUT/'SCENE_LEDGER_SOURCE.tsv'
    with source.open(encoding='utf-8-sig',newline='') as f:raw=list(csv.DictReader(f,delimiter='|'))
    titles={int(n):t for n,t in re.findall(r'(?m)^(\d+)\. \*\*(.*?)\*\* — ',(ROOT/'docs/manga/SEVEN_VOLUME_NOVEL_PLAN.md').read_text(encoding='utf-8-sig'))}
    rows=[]
    for row in raw:
        n=int(row['chapter'])
        roster=[name for name,start in [('Nil',1),('Vesper',5),('Maeve',6),('Hina',9),('Jinling',15),('Bai Si',17),('Shunya',22),('Prima',29),('Fibi',37),('Varro',42)] if n>=start]
        rows.append(dict(chapter=n,title=titles[n],volume=(n-1)//7+1,relative_day=row['day'],location=row['location'],cast=row['cast'].split(';'),travelling_roster=roster,roster_note='Active focal participants are listed separately; no obligation to place every traveller in every panel. Bai Si is guide until19; Prima escort until31; Jinling guest until21; Varro late guest.',viewpoint='Nil-close; chapter4 Ivo-observed cutaway only',requires_previous_chapter=n-1 if n>1 else None,decision=DECISIONS[n-1],scenes=[dict(id=f'ch{n:02d}_s{i}',action=row[f'scene_{i}']) for i in range(1,4)],exit_consequence=row['exit_consequence']))
    data=dict(schema_version=1,evidence_scope='Authored scene plan, not prose, page scripts or generated manga',source_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),chapters=rows,proofs=[dict(id='piece.'+k,introduced=v[0],secured=v[1],custodian=v[2],review=43,use=49) for k,v in PROOFS.items()],seals=[dict(digit=d,secured=c,use=44) for c,d in SEALS.items()],gates=dict(origin_evidence_converges=25,origin_confirmed=26,physical_cage_revealed=45,failed_test=23,small_test=31,mandates_ratified=43,proof_review=43,ritual_gate=44,positive_sum=49),core_arcs={'Vesper':[5,20,40,41],'Maeve':[7,10,33,35],'Hina':[9,10,12,14],'Jinling':[15,16,20,21],'Bai Si':[17,18,26,33],'Shunya':[22,24,26,28],'Prima':[29,31,32,35],'Fibi':[37,38,39,41]})
    errors=validate(data)
    if errors:raise ValueError(errors)
    (OUT/'scene_ledger.json').write_text(json.dumps(data,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    md=['# Complete49-chapter scene ledger','', 'Phase2 planning artifact:147 authored scenes,49 central decisions and49 exit consequences. This is not a finished novel or manga page script. Read with [continuity schedules](PHASE_02_CONTINUITY.md) and [resolved authority](RESOLVED_SERIES_BIBLE.md).','']
    for r in rows:
        md += [f'## {r["chapter"]:02d} — {r["title"]}', '',f'Volume{r["volume"]} · relative Day{r["relative_day"]} · {r["location"]}', '', '**Focal participants:** '+', '.join(r['cast'])+'.', '', '**Travel roster (not a mandatory panel list):** '+', '.join(r['travelling_roster'])+'.', '', '**Central decision:** '+r['decision']+'.','']
        for s in r['scenes']:md += [f'### {s["id"]}', '',s['action'],'']
        md += ['**Consequence driving the next chapter:** '+r['exit_consequence'],'']
    (OUT/'SCENE_LEDGER.md').write_text('\n'.join(md),encoding='utf-8')
    # Adversarial checks verify that the gate rejects damaged schedules.
    import copy
    cases=[]
    bad=copy.deepcopy(data);bad['chapters'].pop();cases.append(bad)
    bad=copy.deepcopy(data);bad['proofs'][0]['secured']=49;cases.append(bad)
    bad=copy.deepcopy(data);bad['seals'][-1]['secured']=45;cases.append(bad)
    bad=copy.deepcopy(data);bad['gates']['physical_cage_revealed']=20;cases.append(bad)
    bad=copy.deepcopy(data);bad['core_arcs']['Fibi'][-1]=48;cases.append(bad)
    bad=copy.deepcopy(data);bad['gates']['mandates_ratified']=49;cases.append(bad)
    assert all(validate(bad) for bad in cases)
    print(json.dumps(dict(status='PASS',chapters=len(rows),scenes=sum(len(r['scenes']) for r in rows),proofs=len(data['proofs']),seals=len(data['seals']),core_arcs=len(data['core_arcs']),negative_cases_rejected=len(cases),limits='Structural temporal checks and authored plan review, not literary acceptance or completed prose.'),indent=2))
if __name__=='__main__':main()
