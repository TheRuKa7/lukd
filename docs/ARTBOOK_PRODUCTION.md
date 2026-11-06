# ZERO-SUM: OMEN — Art Book Production Guide

How to reach the level of *The Official Digital Artbook of Cyberpunk 2077*, and how to build our own art book in that manner. Read with [`ART_DIRECTION.md`](ART_DIRECTION.md).

---

## 1. Why that art book works (studied spread by spread)

| What you see | Where | Why it works | What we copy (method, not look) |
|---|---|---|---|
| **District line-ups**: 5–7 locals standing shoulder to shoulder, full body, slightly low camera, over a painted environment, with a rough colour block behind them and graffiti tags on top | Northside, Arasaka Waterfront, North Oak, Kabuki spreads | One image explains a whole society: class, jobs, ages, body types, gangs, corporate guards. Every outfit is evidence of the district's economy. | A line-up for **every district of every land** |
| **Costume logic**: the four style eras (Kitsch, Entropism, Neomilitarism, Neokitsch) shown on the same character slots side by side | Styles comparison spread | Design reads as a *system*, so new outfits stay consistent | Meridian's four eras of luck (Art Direction §8.2) and a comparison spread |
| **Grounded materials**: worn denim, scuffed boots, cheap plastic, real metal, tired skin | Every character | Believability comes from wear, not detail density | Every design brief names fabrics, wear and repairs |
| **Environment paintings on a 3D base**: precise architecture, real perspective, atmospheric haze, overcast diffuse light, 1–2 accent colours (red signage) | Watson, Arasaka Waterfront, City Center | 3D gives scale and correctness; painting gives mood | 3D blockout → paint pass → human overpaint |
| **Keyframe illustrations**: extreme foreshortening, saturated complementary palette, graffiti integrated into the image | The Kitsch keyframe (the shooter with the yellow tag) | One frame sells the fantasy and the energy | One keyframe per land and per hero |
| **History in the design**: every district's look comes from an event (a war, a crash, a nuclear blast, a failed resort) | District texts | Players feel a past without reading lore | Each of our districts has a "what happened here" line (Locations Guide) |
| **Graphic presentation**: one loud base colour, black type, label tabs, spray tags, marker crosses, stickers, white space for text | Every page | The book itself feels like the street | Our identity: ledger cream, ink, Nixie orange, stamps, tally marks, red-ink corrections |
| **Diversity of people** | Every line-up | A real city has every age, size and origin | Line-ups must vary age, build, height and origin |

## 2. Gap analysis: our pass-1 art vs that bar

| Bar | Pass 1 | Fix |
|---|---|---|
| Design logic (every item means something) | Generic fantasy-anime costumes | Design briefs per character tied to era, land and job (§5) |
| Material realism and wear | Clean, glossy, plastic | Name fabrics, wear, dirt, repairs in every brief; paint-over pass |
| Composition | Centred single figures on dark backgrounds | Line-ups, keyframes, environment plates with scale cues |
| Light | Generic rim-lit night | One motivated light per image; overcast day, dawn, lantern night |
| Consistency across images | None (each image a new face) | 3D base models (Meshy) + Higgsfield Elements + turnarounds |
| Presentation | Images on blank pages | Art-book spreads with text, tabs and graphic overlays (§6) |

## 3. Two registers (decision)
Professional games keep two looks, and so will we:

| Register | Used for | Look |
|---|---|---|
| **A · Concept and art book** | Art book, key art, store page, marketing, design reviews | **Painterly semi-realistic concept art**: digital painting over 3D and photobash, realistic materials and light, anime-informed faces and proportions (the Edgerunners and Ghibli influence lives in shapes, colour and faces) |
| **B · In game** | Gameplay, cutscenes, UI | **Painted world, inked people** (Art Direction §2): Ghibli-inspired painted backgrounds, Edgerunners-inspired cel characters |

Register A defines the designs; Register B is how the game renders them. The Cyberpunk 2077 art book is register A; the game itself is register B for them (real-time 3D).

## 4. The pipeline (how a concept artist at that level works, mapped to our tools)

| Step | What happens | Tools |
|---|---|---|
| 1. Research | Reference boards per land and faction: real clothing, architecture, props, festivals | Web research; cultural consultants |
| 2. Thumbnails | 20–50 tiny silhouette sketches per character or place; pick the strongest 3 | Paper or Krita; FLUX/Higgsfield at low resolution for variety |
| 3. Design callouts | Costume breakdown: materials, wear, insignia, props, colour | Character Bible + design brief template (§5) |
| 4. 3D base | Characters: rough model posed in 3D. Environments: blockout with real perspective | **Meshy** (text/image → 3D, auto-rig, GLB export to Blender); **Higgsfield 3D Jutsu** (Blender scenes, camera, lights) |
| 5. Paint pass | AI-assisted painting over the 3D render with the register-A prompt grammar | **Higgsfield** `generate_angles` (render → painting); **FLUX.1 Krea** (Hugging Face); Higgsfield **Elements** for consistent faces |
| 6. Fix and vary | Correct details, change angles, make turnarounds | **FLUX Kontext** (text edits, e.g. fix "NaN"), **Qwen Image Edit Angles** (turnarounds), **SAM3** (segment into layers), background removal (for line-ups) |
| 7. Human overpaint | Unify edges and values, fix hands and faces, add design truth, final grade | Krita / Photoshop / Procreate, **mandatory** |
| 8. Presentation | Lay out into art-book spreads with text, tabs and overlays | `tools/build_artbook.py` |
| 9. Motion | Keyframes to short clips for trailers and cutscenes | Higgsfield Seedance / Kling; Wan 2.2 (Hugging Face) |

**Why the 3D base matters:** it is the single biggest jump in quality. It fixes perspective, proportion and lighting before any painting starts, and it makes every angle of a character match.

### Meshy specifics (when connected)
- **Characters:** image-to-3D from an approved front design → auto-rig → pose (idle, attack key poses) → render front, side and back for turnarounds and as paint-pass bases.
- **Props:** text-to-3D for charms, weapons, the decoder, Nixie tubes, the Basilica clock; consistent props across every image.
- **Environments:** kitbash modular pieces (tenements, torii, stalls) for blockouts.
- Export GLB → Blender (local) for camera and light, then paint pass.

## 5. Design brief template (one per character, faction or district)
```
NAME / FACTION / LAND / ERA (Charmpunk · Remainder · Ledgerism · Gilded Fortune · or land tradition)
JOB & DAY: what they do all day; what their hands touch
BODY: age, height, build, posture
SILHOUETTE: dominant shape (Character Bible)
OUTFIT LAYERS: base / mid / outer, each with MATERIAL + WEAR (patched, faded, oil-stained…)
OMEN DISPLAY: how their number shows (holo-halo, enamel pin, tattoo, hidden)
CHARMS: which culture's charms they wear and why
PROPS: tools, weapons, personal object
COLOUR: signature + secondary + accent (hex)
STORY DETAIL: one item that hints at their past
DON'T: things that would break the design
```

## 6. Our art book: spread list
Landscape spreads, like the reference. Template: `tools/build_artbook.py` (draft PDF in `docs/`).

| # | Spread | Contents |
|---|---|---|
| 1 | Cover | Key art: the party at the Naming terminal |
| 2 | Foreword | Director's note |
| 3 | Styles opener | Full-bleed Meridian keyframe |
| 4–5 | The four eras of luck | Each era: text + keyframe |
| 6 | Comparison | Person · charm · Omen display × 4 eras |
| 7 | The Tally | World map with stamps and tally-mark overlays |
| 8–13 | Meridian districts | Per district: map tab + environment + line-up |
| 14–19 | Hyakki | Map, Moon Pier, Night Parade, Shrine of the Seven Lucky Gods, Tamamo's palace, yokai line-up |
| 20–25 | River Empire | Bāfā Harbor, the Exchange, the Ten Courts, line-ups |
| 26–31 | Śūnyapura | Observatory, stepwell, Chitragupta's Hall, line-ups |
| 32–37 | Kroton Nova | The Sieve, the undercity, the Moirai's cave, line-ups |
| 38–43 | Crossroads | The crossroads, Lucky Strike, the Ghost Train, line-ups |
| 44–55 | Characters | Per hero: keyframe + design sheet (callouts, palette, props, expressions) |
| 56–61 | Auditors and Keepers | Boss keyframes and designs |
| 62–64 | Bestiary | Enemies by land |
| 65–66 | Charms of the World | Catalog with culture notes |
| 67 | The Basilica | Finale keyframe |
| 68 | Credits | |

## 7. First 12 images (priority for the jam)
1. Meridian Undercity environment painting (register A).
2. Remainder Wards line-up (6 locals).
3. Four-eras comparison (4 figures).
4. NIL keyframe (action, graffiti overlay).
5. NIL design sheet (front/side/back + callouts).
6. Vesper design sheet.
7. Maeve design sheet.
8. Hina design sheet.
9. Hyakki Moon Pier environment painting.
10. Hyakki yokai line-up (Night Parade).
11. Varro keyframe.
12. Tamamo keyframe.

## 8. Quality bar checklist (compare every image against the reference)
- [ ] Could a stranger guess this person's job and income from the outfit?
- [ ] Are materials readable (cloth vs leather vs metal vs plastic) and worn?
- [ ] One motivated light source; believable shadows; atmospheric depth
- [ ] Correct perspective and proportion (3D base used?)
- [ ] Silhouette and signature colour readable at thumbnail size
- [ ] At least one story detail
- [ ] Hands, faces and props correct after overpaint
- [ ] Consistent with the Character Bible's canon locks

## 9. Tool status (end of Nov 6)
| Tool | Status |
|---|---|
| Higgsfield 3D Jutsu (renders) | Working (free). Clay bases and colour keys done for the Remainder Wards and the Moon Pier, plus a six-figure line-up base (`art/base3d/`) |
| Higgsfield image/video generation | **Blocked**: 6 paint passes stuck in "submission unknown"; check credits and reconcile with Higgsfield |
| Hugging Face Spaces (FLUX Krea, Kontext, Qwen Angles, SAM3) | Available but invoke is disabled in this session's connector headers (`gradio=none`) |
| Vector kit (`tools/graphics.py`, `tools/figures.py`) | Working: faction emblems, Omen displays, charm icons, reel objects, and flat model-sheet figures for all 16 characters and the four eras. These fill the art book's design pages until paintings land |
| Meshy | Not connected in this session; connect via claude.ai connector settings or use the Meshy web app |
