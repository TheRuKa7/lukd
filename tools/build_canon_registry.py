"""Build the single canon registry (pre-production phase 1).

Sources, in order of authority:
  1. docs/novel/RESOLVED_SERIES_BIBLE.md + docs/novel/scene_ledger.json (the story spine)
  2. docs/novel/character_trajectories.json (48 novel profiles)
  3. art/catalog/characters.json (91 design records with appearance, palette and locks)
Output: canon/characters.json, canon/items.json, canon/places.json and canon/REGISTRY.md.
Every name in the scene ledger must resolve to exactly one registry record (or a declared group).
Run: python tools/build_canon_registry.py [--check]
"""
import glob
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
OUT = ROOT / 'canon'

# novel profile name -> catalog id (None: no design record yet)
NOVEL_TO_ID = {
    'Nil': 'nil', 'Vesper': 'vesper', 'Maeve': 'maeve', 'Hina': 'hina', 'Jinling': 'ba', 'Bai Si': 'bai_si',
    'Shunya': 'shunya', 'Prima': 'prima', 'Fibi': 'fibi', 'Varro': 'varro', 'Livia': 'livia', 'Thale': 'thale',
    'Hap': 'hap', 'Ama': 'ama', 'Tobi': 'tobi', 'Baker': 'baker', 'Collector': 'collector', 'Debt Hound': 'debt_hound',
    'cart resident': 'cart_resident', 'Nought': 'brother_nought', 'Gus': 'gus', 'Ivo': 'ivo_marr', 'Tetsu': 'tetsu',
    'Ofuku': 'ofuku', 'Enma': 'enma', 'Ao': 'ao', 'Aka': 'aka', 'Tamamo': 'tamamo', 'Little Lantern': 'little_lantern',
    'Jin Chan': 'jin_chan', 'Ox-Head': 'ox_head', 'Horse-Face': 'horse_face', 'Judge Cui': 'judge_cui', 'Wen': 'wen',
    'Vidya Rao': 'vidya_rao', 'Meera': 'meera', 'Chitragupta': 'chitragupta', 'Kallisto': 'kallisto', 'Niko': 'niko',
    'Clotho': 'clotho', 'Lachesis': 'lachesis', 'Atropos': 'atropos', 'Archon': 'archon', 'Stranger': 'stranger',
    'Penny': 'penny', 'Vance': 'sheriff_vance', 'House': 'house', 'Mara': 'mara',
}

# records the novel needs that have no design record yet
NEW_RECORDS = {
    'baker': dict(name='Baker', group='Story characters', region='Meridian Wards', role='Breakfast stall keeper; first person to give Nil work'),
    'mara': dict(name='Mara Vale', group='Story characters', region='The Crossroads', role='Survivor of Vesper\'s rigged hand; mutual-aid worker at sixteen'),
    'wen': dict(name='Wen', group='Records of the dead', region='River Empire', role='Ferry-rope maker, deceased; known through testimony and a work knot'),
    'cart_resident': dict(name='Cart resident', group='Background', region='Meridian Wards', role='Laundry-court resident who helps block the Hound'),
}

CLASS_BY_GROUP = {
    'Main character': ('protagonist', 'A'),
    'Companions': ('core_companion', 'A'),
    'Secret recruits': ('secret_recruit', 'B'),
    'Bosses': ('boss', 'B'),
    'Keepers': ('keeper', 'C'),
    'The god of luck': ('deity', 'B'),
    'Story characters': ('story_npc', 'C'),
    'Factions and jobs': ('faction_archetype', 'D'),
    'Encounter archetypes': ('enemy_archetype', 'D'),
    'Environmental studies': ('environmental', 'D'),
    'Postgame concept studies': ('postgame_study', 'D'),
    'Records of the dead': ('record_only', 'D'),
    'Background': ('background', 'D'),
}
OVERRIDES = {
    'thale': ('final_antagonist', 'A'),
    'varro': ('boss', 'A'),               # Prologue boss, later secret recruit; most-seen antagonist
    'collector_captain': ('recurring_hunter', 'B'),  # the field pursuer the critique asks for (S2)
    'livia': ('story_npc', 'B'), 'brother_nought': ('story_npc', 'B'), 'ivo_marr': ('story_npc', 'B'),
    'mara': ('story_npc', 'B'), 'gus': ('story_npc', 'B'),
}
GAME_ROLE = {
    'protagonist': 'playable', 'core_companion': 'recruitable', 'secret_recruit': 'optional_recruit', 'boss': 'boss',
    'final_antagonist': 'final_boss', 'keeper': 'trial_giver', 'deity': 'story_presence', 'story_npc': 'npc',
    'faction_archetype': 'npc_template', 'enemy_archetype': 'enemy', 'recurring_hunter': 'recurring_enemy',
    'record_only': 'none', 'background': 'npc_template', 'environmental': 'hazard', 'postgame_study': 'postgame',
}
CULTURAL_REVIEW = {'enma', 'judge_cui', 'chitragupta', 'rahu_ketu', 'ox_head', 'horse_face', 'oxhead_horseface', 'baital', 'vetala', 'hap', 'tamamo', 'jiangshi', 'hungry_ghost', 'hungry_ghost_swarm', 'monsoon_naga', 'yantra_guardian'}
NOT_IN_NOVEL_NOTE = {
    'kyusuke': 'Game-only optional recruit; absent from the novel. Decide in phase 6 whether to keep.',
    'liu_shun': 'Game-only optional recruit; absent from the novel. Decide in phase 6 whether to keep.',
    'rahu_ketu': 'The novel stages chapter 27 as an operator-built eclipse engine, not the deities themselves. Any game boss must follow that staging and pass cultural review.',
    'baital': 'Game/concept only; not in the novel ledger.',
}


def load(p):
    return json.loads((ROOT / p).read_text(encoding='utf-8'))


def concept_board(cid):
    hits = sorted(glob.glob(str(ROOT / 'art/concepts/complete' / f'cast_*_{cid}.png')))
    return pathlib.Path(hits[0]).relative_to(ROOT).as_posix() if hits else None


def build():
    catalog = load('art/catalog/characters.json')['entries']
    traj = load('docs/novel/character_trajectories.json')
    ledger = load('docs/novel/scene_ledger.json')
    profiles = {p['name']: p for p in traj['profiles']}
    first, chapters = {}, {}
    alias = traj.get('aliases', {})
    for ch in ledger['chapters']:
        for label in ch['cast']:
            name = alias.get(label, label)
            chapters.setdefault(name, []).append(ch['chapter'])
            first.setdefault(name, ch['chapter'])
    id_to_novel = {v: k for k, v in NOVEL_TO_ID.items()}

    records = {}
    for e in catalog:
        records[e['id']] = dict(id=e['id'], name=e['name'], group=e['group'], role=e.get('role'), region=e.get('region'),
                                outfit=e.get('outfit'), height_m=e.get('height_m'), pronouns=e.get('pronouns'),
                                resonance=e.get('resonance'), civic_omen=e.get('civic_omen'), palette=e.get('palette'),
                                canon_locks=e.get('canon_locks'), appearance=e.get('appearance'), power=e.get('power'),
                                faction=e.get('faction'), identity_kind=e.get('identity_kind'),
                                art=dict(concept_board=concept_board(e['id']), blockout_views=e.get('view_paths'),
                                         status='concept_board' if concept_board(e['id']) else 'needs_design'))
    for cid, r in NEW_RECORDS.items():
        records[cid] = dict(id=cid, **r, art=dict(concept_board=None, blockout_views=None, status='needs_design'))
    # outfits of one person share an identity
    for cid in ('nil_rags', 'nil_parade', 'nil_openhand'):
        records[cid]['variant_of'] = 'nil'
    records['varro_ally']['variant_of'] = 'varro'

    for cid, r in records.items():
        base = r.get('variant_of', cid)
        cls, tier = OVERRIDES.get(base) or CLASS_BY_GROUP.get(records[base]['group'], ('story_npc', 'C'))
        r['class'], r['tier'], r['game_role'] = cls, tier, GAME_ROLE[cls]
        novel = id_to_novel.get(base)
        r['novel_name'] = novel
        r['in_novel'] = novel is not None
        r['first_chapter'] = first.get(novel) if novel else None
        r['ledger_chapters'] = chapters.get(novel, []) if novel else []
        r['novel_profile'] = profiles.get(novel) if novel else None
        r['cultural_review'] = base in CULTURAL_REVIEW
        if base in NOT_IN_NOVEL_NOTE:
            r['note'] = NOT_IN_NOVEL_NOTE[base]

    # every ledger name must resolve
    groups = set(traj['groups'])
    unresolved = sorted({n for n in chapters if n not in groups and n not in NOVEL_TO_ID})
    missing = sorted({NOVEL_TO_ID[n] for n in chapters if n in NOVEL_TO_ID and NOVEL_TO_ID[n] not in records})
    items = dict(seals=ledger['seals'], proofs=ledger['proofs'], gates=ledger['gates'],
                 nil_verbs=[dict(id='carry', introduced=11), dict(id='rewrite', introduced=19),
                            dict(id='place_value', introduced=None), dict(id='factor', introduced=None), dict(id='deal', introduced=36)])
    places = [dict(chapter=c['chapter'], volume=c['volume'], day=c['relative_day'], location=c['location']) for c in ledger['chapters']]
    return records, items, places, unresolved, missing


def markdown(records):
    order = ['protagonist', 'core_companion', 'final_antagonist', 'boss', 'recurring_hunter', 'secret_recruit', 'deity', 'keeper',
             'story_npc', 'record_only', 'background', 'faction_archetype', 'enemy_archetype', 'environmental', 'postgame_study']
    lines = ['# Canon registry', '',
             'Generated by `tools/build_canon_registry.py` from the scene ledger, the novel profiles and the art catalog. **Do not edit by hand**; edit the sources or the script. This is the single list of who exists, what they are in the story and in the game, and what design work they still need. Tiers decide effort (see [PREPRODUCTION_PLAN](../docs/PREPRODUCTION_PLAN.md)).', '',
             '| Tier | Count |', '|---|---:|']
    tiers = {}
    for r in records.values():
        if 'variant_of' not in r:
            tiers[r['tier']] = tiers.get(r['tier'], 0) + 1
    lines += [f'| {t} | {tiers[t]} |' for t in sorted(tiers)] + ['']
    for cls in order:
        rows = [r for r in records.values() if r['class'] == cls]
        if not rows:
            continue
        lines += [f'## {cls.replace("_", " ").title()}', '', '| ID | Name | Tier | Game role | First chapter | Art | Notes |', '|---|---|---|---|---:|---|---|']
        for r in sorted(rows, key=lambda r: (r['first_chapter'] or 99, r['id'])):
            notes = []
            if r.get('variant_of'): notes.append(f'outfit of `{r["variant_of"]}`')
            if not r['in_novel']: notes.append('not in novel')
            if r['cultural_review']: notes.append('cultural review')
            if r.get('note'): notes.append(r['note'])
            lines.append(f"| `{r['id']}` | {r['name']} | {r['tier']} | {r['game_role']} | {r['first_chapter'] or '—'} | {r['art']['status']} | {'; '.join(notes)} |")
        lines.append('')
    return '\n'.join(lines) + '\n'


def main():
    records, items, places, unresolved, missing = build()
    if unresolved or missing:
        sys.exit(f'Unresolved ledger names: {unresolved}; missing records: {missing}')
    outputs = {
        OUT / 'characters.json': json.dumps(dict(schema_version=1, generated_by='tools/build_canon_registry.py', characters=records), indent=1, ensure_ascii=False) + '\n',
        OUT / 'items.json': json.dumps(dict(schema_version=1, **items), indent=1, ensure_ascii=False) + '\n',
        OUT / 'places.json': json.dumps(dict(schema_version=1, ledger_locations=places), indent=1, ensure_ascii=False) + '\n',
        OUT / 'REGISTRY.md': markdown(records),
    }
    for path, text in outputs.items():
        if '--check' in sys.argv:
            if not path.exists() or path.read_text(encoding='utf-8') != text:
                sys.exit(f'Stale: {path}')
        else:
            path.parent.mkdir(exist_ok=True)
            path.write_text(text, encoding='utf-8')
    stats = {}
    for r in records.values():
        stats[r['class']] = stats.get(r['class'], 0) + 1
    print(json.dumps(dict(status='PASS', records=len(records), by_class=stats,
                          needs_design=sorted(k for k, r in records.items() if r['art']['status'] == 'needs_design'))))


if __name__ == '__main__':
    main()
