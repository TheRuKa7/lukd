#!/usr/bin/env python3
"""Prepare local contact references and requests; never upload or generate media.

Run after tools/render_encounters.py --update-catalog. Outputs 84 unique cast
references and seven three-camera environments from actual files, with source
fingerprints. Shared keeper compounds remain shared in the generation queue.
"""
from __future__ import annotations

import argparse
from collections import OrderedDict
import hashlib
import json
from pathlib import Path
import re

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
VIEWS = ("front", "left", "right", "back")
PAPER = "#F2E8D5"
INK = "#141018"
REGIONS = (
    ("meridian", "Meridian Undercity", "Rainy dawn/dusk; slate blue, moss, warm windows, Nixie orange. Stacked drainage cliffs under a plateau capital; repaired tenements, narrow catwalks and practical brass pipes. Remainder survival craft, plastic-gold Charmpunk and rigid Ledgerist administration coexist."),
    ("hyakki", "Hyakki", "Moonlit festival islands; indigo, paper, vermilion and restrained lantern gold. Volcanic coast, cedar, terraced fishing town, water and repaired paper/lacquer construction. Humans and object spirits share ordinary work; no generic neon city."),
    ("river", "The River Empire", "Golden harbour and jade river bounce; ochre, lacquer red, gold edging and shaded rice-paper storefronts. River-delta trade, abacus instruments, timber dragon-boat repair, warehouses, flood steps and lanterns; quiet misty Courts in the distance. Credit and the physical movement of goods are visible."),
    ("sunyapura", "Śūnyapura", "Monsoon break over wet sandstone, peacock tones, saffron cloth and calibrated brass. A colossal functional stone observatory, deep geometric stepwell, manuscript-drying frames and chai workstations. Invented eclipse machinery uses bolted discs and graduated rails, never sacred celestial head/body silhouettes."),
    ("kroton", "Kroton Nova", "Hard Aegean noon, chalk white, sea blue, bronze and sharp shadows. Island city built as a stone sieve: terraces, perforated architectural screens, olive workyards and ladders connecting an inhabited undercity. Honest structural loads and distinct civic/ordinary spaces."),
    ("crossroads", "The Crossroads Territory", "Desert plateau at sunset toward neon night; rust, sage, dusk violet and orange. Highway, repaired motel, diner, casino boomtown and ghost railway. Ordinary plumbing and road wear contrast with meticulously maintained formal House interiors; no indiscriminate dust on casino uniforms."),
    ("basilica", "The Basilica", "Still monumental interior; brass, steel, enamel white and restrained Nixie amber, no sun in the nave. Cathedral geometry becomes numerical bureaucracy: legible service walkways, audit workstations, archive handling and structural ribs. Gradually revealed warm sunrise belongs beyond the finale doors, not to an arbitrary open roof."),
)

CHARACTER_GRAMMAR = """Create an original, highly finished production CHARACTER TURNAROUND for ZERO-SUM: OMEN, one coherent design repeated as four actual orthographic elevations, in one clean landscape 3:2 art board. Output layout left to right: FRONT, SUBJECT'S LEFT SIDE, SUBJECT'S RIGHT SIDE, BACK. Do not print those words. All four views must use the same body scale, same foot baseline, neutral relaxed construction pose, entire head/feet/props visible with safe margins. Turn the model physically; NEVER flip a view or paste the front as the back. Handedness is anatomical. Preserve asymmetrical accessories and their actual attachment points through every view.

Original visual direction: painted world, inked people. This character board uses precise variable-weight ink contours, grounded expressive anatomy and believable hands, selective crosshatching and small screentone contact shadows, spotted blacks placed to lead toward face, hands and working prop, matte local cel colour with one deliberate hard shadow, restrained hard rim and flat metal highlights. Quiet cream paper background. Fine detail at hero props and consequential repairs, large intentional rest areas in cloth; no uniform noisy hatching. Finished faces must be individual and memorable. Beautiful material construction, seams, layered garment thickness, functional closures and believable straps/weight; no glossy generic portrait or toy/capsule body. Do not copy the primitive simplification of the reference. Use it to understand volume, views and broad placement; the written canon overrides old blockout mistakes. Do not invent additional arms, heads, fingers, ornaments, tails or props. A group model stays the same group with the same member count in every direction.

No lettering, captions, labels, numerals, symbols that function as text, logos, watermarks, UI, height bars or palette swatches: these are authored separately. Leave actual displays/identity plates blank. No speech balloons. No artist/studio references or existing copyrighted characters. No action pose, attack effect or decorative background that obscures construction. Cultural forms are fictional contextual design proposals, not claims of authenticity. Do not introduce sacred imagery that is absent from the brief. The four orthographic views are the sole focus."""

ENVIRONMENT_GRAMMAR = """Create an original, highly finished, matte painted ENVIRONMENT DESIGN BOARD for ZERO-SUM: OMEN, landscape 3:2. Show the SAME coherent place in three matched views in this exact layout: top left a true orthographic TOP-DOWN PLAN; top right a 2.5D orthographic EXPLORATION view (about 57 degrees down and -38 degrees yaw); full-width lower half a readable FRONT BATTLE STAGE view. No words naming the views. Preserve the same landmark, wall and door positions across all views; do not paint three unrelated postcard scenes. The attached primitive renders establish geography only, not surface finish.

Original painted-world/inked-manga art direction. Tactile matte gouache-like opaque planes, soft painted atmospheric depth, deliberate local colour, selective crisp ink architecture and functional detail in the foreground, cohesive lighting, two or three ordinary-life traces that imply actual jobs. Finely designed load-bearing construction, repairs following material seams, drains, service access, honest support and human scale. The scene is specific to its region rather than generic fantasy ornament. In front view preserve a completely clear walkable 24m-wide, 6m-deep battle strip, calm party-safe left and enemy-safe right floor, clear feet contacts and quiet upper-centre reel area. Give foreground, near, mid and far readable value separation; no baked UI or effects. Typical doors 2.2m; storeys 3–3.5m; do not enlarge props arbitrarily.

No actors, crowds, lettering, readable numbers, logos, watermarks, captions, border labels or UI. Shop sign surfaces and mechanical reel display faces remain blank for exact code-authored graphics. No polished CG/plastic sheen, oily bloom, generic airbrush wash, overly busy combat floor, medieval-European castle substitution, or sacred figures presented as enemies. No copying of another work or named artist's treatment."""


def read(rel):
    return (ROOT / rel).read_text(encoding="utf-8-sig")


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def flat(value):
    if value is None:
        return "Not specified; do not invent a narrative fact."
    if isinstance(value, dict):
        return "; ".join(f"{k.replace('_',' ')}: {flat(v)}" for k, v in value.items())
    if isinstance(value, list):
        return "; ".join(flat(v) for v in value)
    return str(value)


def sections(text):
    return [(p.splitlines()[0], "\n".join(p.splitlines()[1:]).strip()) for p in re.split(r"(?m)^## ", text)[1:]]


def region_text(name):
    for title, body in sections(read("docs/LOCATIONS.md")):
        if name in title or (name == "The Basilica" and "Basilica" in title):
            return re.sub(r"\*\*|`", "", body)
    return ""


def faction_rules(faction):
    lines = read("docs/ART_SPEC.md").splitlines()
    candidates = []
    aliases = {"The House": "house", "Luck Exchange": "exchange", "Yokai Courts": "yokai", "Remainder Wards": "remainder", "Synod": "synod", "Observatory": "observatory", "Ten Courts": "courts", "Collectors": "collector", "Basilica": "basilica", "Charm Bazaar": "bazaar", "Open Hand": "open hand"}
    for line in lines:
        if not line.startswith("|"):
            continue
        fields = [v.strip() for v in line.strip("|").split("|")]
        if fields and fields[0] in aliases and aliases[fields[0]] in faction.lower():
            candidates.append(f"{fields[0]}: base {fields[1]}; materials {fields[2]}; required construction {fields[3]}; avoid {fields[4]}.")
    return " ".join(candidates) or "Individual workwear and source construction govern; do not infer membership or magical ability from regional colour."


def font(size, bold=False):
    candidates = ("C:/Windows/Fonts/arialbd.ttf",) if bold else ("C:/Windows/Fonts/arial.ttf",)
    for path in candidates:
        if Path(path).exists():
            return ImageFont.truetype(path, size)
    return ImageFont.load_default(size=size)


def paste(canvas, source, rect, scale=None):
    """Compose actual pixels; no repaint, mirroring or fabricated unseen surface."""
    with Image.open(source) as im:
        im = im.convert("RGBA")
        x, y, w, h = rect
        factor = scale if scale is not None else min(w / im.width, h / im.height)
        target = im.resize((max(1, round(im.width*factor)), max(1, round(im.height*factor))), Image.Resampling.LANCZOS)
        canvas.paste(target, (round(x+(w-target.width)/2), round(y+h-target.height)), target)


def cast_board(entries, path):
    paths = [ROOT / entries[0]["view_paths"][v] for v in VIEWS]
    sizes = []
    for p in paths:
        with Image.open(p) as im:
            sizes.append(im.size)
    # One pixel-to-board factor for all elevations; no per-view body resizing.
    factor = min([550/w for w,h in sizes] + [1300/h for w,h in sizes])
    canvas = Image.new("RGB", (2400,1600), PAPER)
    d = ImageDraw.Draw(canvas)
    title = " / ".join(e["name"] for e in entries)
    if len(title)>120:
        title=entries[0]["name"]+" — shared compound model"
    d.text((48,35),title,font=font(36,True),fill=INK)
    d.text((48,88),"ACTUAL SPATIAL DRAFT REFERENCE · written canon overrides primitive construction",font=font(21),fill=INK)
    for i,(view,p) in enumerate(zip(VIEWS,paths)):
        paste(canvas,p,(i*600+25,150,550,1300),factor)
        d.text((i*600+40,1490),["FRONT","SUBJECT LEFT","SUBJECT RIGHT","BACK"][i],font=font(26,True),fill=INK)
    canvas.save(path,optimize=True)


def environment_board(key, name, path):
    canvas=Image.new("RGB",(2400,1600),PAPER);d=ImageDraw.Draw(canvas)
    d.text((45,25),name+" — same place / three cameras",font=font(35,True),fill=INK)
    for view,rect,label in [("top",(25,105,1150,570),"TOP-DOWN PLAN"),("iso",(1225,105,1150,570),"2.5D EXPLORATION"),("front",(25,790,2350,730),"FRONT BATTLE STAGE")]:
        paste(canvas,ROOT/f"art/envs/{key}_{view}.png",rect)
        d.text((rect[0]+20,rect[1]+rect[3]+8),label,font=font(24,True),fill=INK)
    canvas.save(path,optimize=True)


def character_prompt(entries):
    e=entries[0]
    locks="; ".join(dict.fromkeys(lock for item in entries for lock in item.get("canon_locks",[])))
    text=[CHARACTER_GRAMMAR,f"PRIMARY SUBJECT: {e['name']} ({e['id']}). Role: {e.get('role')}. Outfit: {e.get('outfit')}. Region: {e.get('region')}. Identity kind: {e.get('identity_kind')}. Faction/affiliation: {e.get('faction')}.",f"Individual identity: age {e.get('age')}; pronouns {e.get('pronouns')}. Height specification {e.get('height_m')} metres when assigned; blockout dimensions are proposals, never imply a measured lore fact. Adults generally 7.5 heads tall, children 5–6, elders around 6.5, specific supernatural bodies keep their own construction.",f"SILHOUETTE: {e.get('silhouette')}. PALETTE: {flat(e.get('palette'))}.",f"FOUR-SIDE CONSTRUCTION: {flat(e.get('appearance'))}.",f"WORKING PROPS: {flat(e.get('props'))}. CANON LOCKS, overriding the draft: {locks}.",f"WHY THE DESIGN EXISTS: {e.get('design_rationale')}.",f"POWER LOGIC, used only to motivate material/prop design, no attack effects in this sheet: {flat(e.get('power'))}. Power is never assigned solely by clothing, and no free luck is created.",f"FACTION CONSTRUCTION: {faction_rules(e.get('faction',''))}"]
    if len(entries)>1 or e.get('provenance',{}).get('render_scope','').startswith('compound'):
        text.append("SHARED COMPOUND REFERENCE: This set contains the same paired/three-person keeper group in all four cameras. Preserve the actual group membership and count from the reference; named catalog sub-records do not add duplicate people. These are nonlethal trial keepers, never villain attack trophies. Catalog records linked to this exact model: "+", ".join(f"{x['name']} ({x['id']})" for x in entries)+".")
    if e['id'] in ('noise_storm','default'):
        text.append("CONTEXTUAL ENCOUNTER STUDY, NOT A CHARACTER BODY: four matched camera studies of the same environmental phenomenon. Do not invent a deity, monster anatomy or canonical physical embodiment. Default has still grey negative-space volumes and NO wheel/orbit; Noise Storm is unresolved chance fragmentation with readable scene depth. These remain conceptual scene proxies.")
    if e['id']=='rahu_ketu':
        text.append("CRITICAL REPLACEMENT DESIGN: two invented Basilica-built eclipse engines nicknamed Rahu and Ketu: a bolted occluder disc and a segmented graduated surveyor rail/cursor, with operator access and service fasteners. No severed celestial head, serpent torso, sacred deity body or devotional icon. Preserve these two mechanically different instruments in all four views.")
    if e['id'].startswith('nil'):
        text.append("NIL identity must remain consistent across every outfit: androgynous young adult, they/them, amber eyes, one orange hair streak; right-wrist decoder and longer LEFT coat tail when this costume includes the coat. Exact NaN lettering is NOT generated: leave the display blank. Abacus-lock closures and ledger lining are functional, with local repairs that preserve motion.")
        if e['id']!='nil':
            text.append("The additional detailed NIL reference is for face, body identity, right-wrist decoder and ink/material treatment only. This sheet MUST use the outfit named in this request and the first spatial reference; do not replace the alternate outfit with the default coat.")
    if e['id']=='vesper':
        text.append("Vesper is an adult of 28. Left-shoulder braid, two hat cards; tailored but repaired former dealer uniform and worn coin. Right-hand bespoke revolver has precisely SEVEN physical chambers, not a six-shot generic cylinder. Give cylinder depth and seven openings where visible, no impossible bore geometry. The wrist, grip and braid must not switch sides.")
    if e['id']=='varro':
        text.append("Varro is a human in a hinged hound-skull MASK, never a literal animal head. Three secured jars; confiscation clamp with three release levers; protected sister-exemption token. Mask straps, hinges and neck opening remain physically credible; every large apparatus is supported.")
    return "\n\n".join(text)


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--output-dir',default='build/higgs_artbook_refs')
    ap.add_argument('--manifest',default='art/catalog/higgsfield_artbook_requests.json')
    args=ap.parse_args()
    out=ROOT/args.output_dir;out.mkdir(parents=True,exist_ok=True)
    catalog=json.loads(read('art/catalog/characters.json'))['entries'];groups=OrderedDict()
    for e in catalog:
        key=tuple(e.get('view_paths',{}).get(v) for v in VIEWS)
        if not all(key) or not all((ROOT/p).is_file() for p in key):
            raise ValueError(f"Missing real four-view evidence: {e['id']}")
        groups.setdefault(key,[]).append(e)
    requests=[]
    for i,(paths,entries) in enumerate(groups.items(),1):
        key=entries[0]['id'];path=out/f'cast_{i:03d}_{key}.png'
        cast_board(entries,path)
        requests.append(dict(index=i,request_id=f'cast_{i:03d}_{key}',kind='character_turnaround',catalog_ids=[e['id'] for e in entries],name=entries[0]['name'],reference_path=str(path.relative_to(ROOT)).replace('\\','/'),reference_sha256=sha(path),source_views={v:dict(path=p,sha256=sha(ROOT/p)) for v,p in zip(VIEWS,paths)},aspect_ratio='3:2',resolution_request='highest available 3:2 image; retain entire four-view board',prompt=character_prompt(entries),output_target=f'art/concepts/complete/cast_{i:03d}_{key}.png',status='prepared_not_submitted',provenance='Local contact composition of actual camera references; no generation or upload performed by this tool.'))
    for request in requests:
        key=request['catalog_ids'][0]
        extra='art/concepts/fresh/chr_nil_v5.png' if key.startswith('nil') else {'vesper':'art/concepts/fresh/chr_vesper_v5.png','varro':'art/concepts/fresh/chr_varro_v5.png','debt_hound':'art/concepts/fresh/enm_debthound_v5.png'}.get(key)
        request['reference_paths']=[request['reference_path']]+([extra] if extra and (ROOT/extra).is_file() else [])
        request['additional_reference_scope']='Only this same character’s detailed identity/material treatment; alternate outfit construction still follows the named outfit and primary spatial board.' if extra else 'No unrelated hero face reference.'
        request['additional_reference_fingerprints']={p:sha(ROOT/p) for p in request['reference_paths'][1:]}
    for i,(key,name,description) in enumerate(REGIONS,len(requests)+1):
        path=out/f'env_{key}.png';environment_board(key,name,path)
        prompt='\n\n'.join([ENVIRONMENT_GRAMMAR,f'REGION: {name}. {description}',f'LOCATION AND ORDINARY-LIFE LOGIC: {region_text(name)}',"Do not reproduce generated text implied by the old location document: blank signs and devices only. Story chronology and everyday infrastructure guide objects, never a decorative tourist collage."])
        requests.append(dict(index=i,request_id=f'env_{key}',kind='environment_three_view',region_id=key,name=name,reference_path=str(path.relative_to(ROOT)).replace('\\','/'),reference_sha256=sha(path),source_views={v:dict(path=f'art/envs/{key}_{v}.png',sha256=sha(ROOT/f'art/envs/{key}_{v}.png')) for v in ('top','iso','front')},aspect_ratio='3:2',prompt=prompt,output_target=f'art/concepts/complete/env_{key}.png',status='prepared_not_submitted',provenance='Three actual Blender camera views composed locally; no upload or generation.'))
        requests[-1]['reference_paths']=[requests[-1]['reference_path']]
    sources=['docs/ART_DIRECTION.md','docs/ART_SPEC.md','docs/LOCATIONS.md','docs/WORLD_OPERATIONS.md','art/catalog/characters.json']
    manifest=dict(schema_version=1,updated='2026-11-08',status='Prepared references and prompts only. Provider submission/credits/acceptance tracked separately.',character_records=len(catalog),unique_cast_requests=len(groups),environment_requests=len(REGIONS),total_requests=len(requests),source_fingerprints={p:sha(ROOT/p) for p in sources},requests=requests)
    target=ROOT/args.manifest;target.parent.mkdir(parents=True,exist_ok=True);target.write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(dict(manifest=str(target),cast_boards=len(groups),environment_boards=len(REGIONS),requests=len(requests),output_dir=str(out)),indent=2))
    return 0


if __name__=='__main__':
    raise SystemExit(main())
