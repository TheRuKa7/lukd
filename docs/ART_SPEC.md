# ZERO-SUM: OMEN — Fixed Art Spec

The numbers and rules every artist, modeller and animator works to. [`ART_DIRECTION.md`](ART_DIRECTION.md) says *what it should feel like*; this says *exactly how big, how thick, which colour, which camera*. Updated 7 November 2026. Adopted decisions in [DECISIONS.md](DECISIONS.md) govern conflicts. The 3D blockouts in `art/cast/` and `art/envs/` establish first-draft spatial references, not final inked designs or verified runtime assets. Fresh concepts and manga follow ART_DIRECTION section0; the catalog distinguishes established facts, proposed visual dimensions and draft readiness.

---

## 1. Production treatments and dramatic registers
| Register | For | Look |
|---|---|---|
| **A · Concept / art book** | Key art, store page, art book | Detailed original inked concept art, matte painted spaces, selective crosshatching/screentone and cel colour; AI-authored corrections; no manual finishing dependency |
| **B · In game** | Gameplay, cutscenes, UI | **Painted world, inked manga**: matte backgrounds; readable cel characters; serious/comedy line-density registers; exact separate lettering |

## 2. Characters

### 2.1 Scale and proportion
- **World scale:** 1 unit = 1 m. Characters stand on z = 0 and face −Y (toward camera) in every model file.
- **Model-sheet scale:** 1 m = 260 px (the turnaround renders). Comparative body plates share this scale; never rescale one character to "fit" beside another. A labelled mechanism inset or a wide-creature detail plate may use a different stated scale; it is not a comparative height plate.
- **Heads tall:** adults **7.5 heads** (head height = 0.132 × height); children 5–6; elders 6.5 (slight hunch); bosses 8–9 (Thale, Archon, Bai Si stretched); Hap 6 with a vast robe.

| Class | Height range | Shoulder width (× height) | Notes |
|---|---|---|---|
| Heroes | 1.35 (Hina) – 1.95 (Bai Si) | 0.20–0.27 | Only explicitly stated heights are canon; other catalog dimensions are proposed spatial specifications |
| Children | 1.20–1.35 | 0.22–0.24 | Tobi, Niko, Penny, Little Lantern |
| Elders | 1.45–1.70 | 0.24–0.25 | Ofuku, Liu Shun, Vidya Rao |
| Heavies | 1.88–2.15 | 0.29–0.37 | Collectors, Varro, Ox-Head and Horse-Face |
| Bosses | 1.8–2.5 | by design | Rahu & Ketu and Jin Chan use special bodies |

### 2.2 Turnaround standard (every character, every outfit)
- **Views:** FRONT · LEFT · RIGHT · BACK, orthographic, in that order, left to right, feet on one baseline. LEFT shows the character's left side (their left hand nearest the camera).
- **Pose:** relaxed A-pose: arms 10 degrees from the body, feet hip-width, weight even, props in their canon hand (Vesper's revolver in the right hand, NIL's decoder on the RIGHT wrist, Hina's umbrella in the right hand, shields on the left arm).
- **Sheet:** 4 views on cream `#EFE6D2`, plus height bar in metres, palette chips with hex, canon locks, and 64 px silhouette test.
- **Extras per hero:** expression sheet (neutral, joy, anger, fear, determined, their "number habit" face), props sheet (front + side of each prop at 1:1 with the body), outfit sheet (every story outfit as a full turnaround).

### 2.3 Line, shading and colour (register B)
| Element | Rule |
|---|---|
| Outer contour | 4 px at 1080p for a 600 px-tall character (scale linearly); tapered at ends |
| Interior lines | 1.5–2 px; folds only where the cloth turns |
| Line colour | Coloured: local colour × 0.45 value, use coloured interior lines; serious-register silhouette and spotted blacks may use ink `#141018` |
| Shading | **2 tones + 1 rim.** Shadow = local colour multiplied by the land's shadow tint (Meridian `#5E4F7A`, Hyakki `#2E3A6B`, River `#3E5A4A`, Śūnyapura `#6B4A5A`, Kroton `#4A5E7A`, Crossroads `#6A3E5A`, Basilica `#4A4A5A`) at 35%; one hard-edged shadow shape per form |
| Rim light | One rim from the background's key light colour, 2–4 px, on the silhouette edge facing that motivated light; camera orientation alone does not determine the lit edge |
| Highlights | Hair and metal only; flat shapes, no gradients |
| Saturation | The **signature colour** is the most saturated thing on the character (Character Bible §0) |
| Palette | Max 4 main colours + 1 accent per character; NPCs 3 + 1 |
| Skin | Real, varied tones; never grey-shifted; flushed cheeks only for children and comedy |
| Eyes | Heroes: large, coloured iris, one hard catch-light; NPCs: smaller; keepers: calm, half-lidded |

### 2.4 Silhouette and shape language
Every character must read as a black silhouette at 64 px (the art book's readability page). Shape language per character is fixed in the Character Bible §0 (NIL tall rectangle + broken circle; Vesper triangles; Maeve circles; Hina dome; Ba fan; Bai Si vertical; Shunya ring; Prima shield; Fibi spiral; Varro block; Tamamo fan of tails; Jin Chan sphere; Rahu/Ketu invented eclipse engines: bolted disc + segmented rail; Archon column; the House ring; Thale cathedral arch; Hap star robe + orbit).

### 2.5 Faction costume keys (for every NPC)
| Faction | Base colours | Materials | Must have | Never |
|---|---|---|---|---|
| Basilica | Steel white, brass, olive | Enamel, brass, wool | Steel numerals; gear motifs | Glowing numbers |
| Collectors | Rust, gunmetal | Riveted leather, glass jars | Debt jars; peaked caps; masks for captains | Clean surfaces |
| Charm Bazaar | Magenta, sign yellow, cyan | Plastic, nylon, stickers | ≥ 3 cultures' charms worn at once | Matching outfits |
| Remainder Wards | Ash, old brass, moss | Repaired cloth, scrap, occasional new working garments | Evidence of a practical repair or retained tool; cracked tubes are one recurring option | Uniform poverty costume imposed on every resident |
| Yokai Courts | Violet, vermilion, foxfire cyan | Silk, paper, lacquer | Spirit-specific silhouettes and paper/lacquer motifs; humans are not automatically given fox traits | Neon |
| Luck Exchange | Jade, gold, lacquer red | Silk, gold leaf | Gold numerals; abacus motifs | Rust |
| Ten Courts | Ink black, rice paper, seal red | Lacquer, lamellar | Brushes, seals | Bright colour |
| Observatory | Indigo, saffron, brass | Cotton, mirror-work | Astrolabe pins | Steel |
| Synod | Bronze, chalk, Aegean | Bronze, linen | Sieve shields and prime glyphs for prime offices; Composite Knights deliberately bear 4·6·8·9 on composite shields | Composite insignia on an office explicitly sworn to primes |
| The House | Casino red, ivory, gold | Satin, felt | Cards, waistcoats; formal casino interiors meticulously maintained | Unexplained dust on formal interior uniforms; road dust is correct on Crossroads travel wear |
| Open Hand | Road dust, gold mark | Homespun | Open-hand cord; a die | Badges |

Regional costume keys describe institutional dress, not every resident. A migrant, tradesperson, dissenter or off-duty official may combine regional construction with their own income, work and history. Preserve the named individual’s locks; do not use faction colour as ethnicity or assign magical powers from clothing.

## 3. Environments

### 3.1 Scale, grid and stage
- **Grid:** 1 m. Doors 2.2 m; storeys 3–3.5 m; street widths: Wards 8–18 m, Bāfā lanes 6 m, Śūnyapura plazas 40 m+.
- **Battle stage (side-on):** walkable strip **24 m wide × 6 m deep**, flat, clear of props; party stands at x = −8…−3, enemies at +3…+9; the land's **reel object** at top centre in screen space.
- **Exploration (2.5D) area:** 60–120 m per district; every interactive object ≥ 1 m and lit.

### 3.2 Cameras (fixed)
| Camera | Projection | Angle | Use |
|---|---|---|---|
| **Battle (front view)** | Perspective, 30 mm (≈ 40° vertical FOV) | Eye at 1.7–3.2 m, 17 m from the stage line, pitch 0–5° | All fights; side-on |
| **Exploration (2.5D)** | Orthographic | Pitch 57° down, yaw −38° | Map, towns, overworld |
| **Plan (top-down)** | Orthographic | Straight down | Level design, minimap, art book plans |
| **Cinematic** | Perspective, 18–85 mm | Free | Cutscenes; respect the 180° rule toward the reel |

### 3.3 Painted layers (register B)
Sky · far (≥ 200 m) · mid (40–200 m) · near (10–40 m) · stage floor · foreground (≤ 3 m, sparse). Parallax factors 0.05 / 0.2 / 0.5 / 0.8 / 1.0 / 1.2. Characters are composited between "stage floor" and "foreground".

### 3.4 Light and time of day per land
| Land | Time | Key light | Fill / ambient | Atmosphere |
|---|---|---|---|---|
| Meridian Undercity | Rainy dawn / dusk | Window amber + Nixie signage | Wet slate blue | Rain, haze, wet ground |
| Hyakki | Summer night, full moon | Lantern gold | Indigo moonlight | Mist over water, fireflies |
| River Empire | Golden afternoon (harbor) / misty dark (Courts) | Low sun | Jade bounce | Incense, lantern smoke |
| Śūnyapura | Monsoon break | Sun through cloud | Wet sandstone bounce | Rain sheets, puddle mirrors |
| Kroton Nova | Hard noon | White sun | Aegean sky blue | Heat haze, sharp shadows |
| Crossroads | Sunset → neon night | Sunset orange / neon | Dusk violet | Dust, card storms |
| Basilica | Interior, no sun | Nixie amber | Brass bounce | Still air, motes |

## 4. The 3D pipeline (where this blockout fits)
1. **Blockout** (existing draft): parametric bodies and environments in Blender at true scale, flat object colours; `art/cast/zso_cast_blockout.blend`, `art/envs/zso_envs_blockout.blend`.
2. **Base model:** AI-scripted Blender or optional Meshy base per hero from the turnaround; T-pose; ≤ 20k tris; rigged for posing only (register A paint-overs).
3. **Colour key:** flat colours per the palette (this book's environment renders are colour keys).
4. **Paint pass:** AI-assisted (Higgsfield / FLUX) over the base render with the Art Direction §6 prompt grammar; logged in `AI_DISCLOSURE.md`.
5. **AI correction and rejection gate:** fix anatomy, construction, count and handedness through image edits, source geometry and scripted exports. Reject or simplify failed assets. No human overpaint stage is required.
6. **Register B production:** validated pose sprites or layered rigs from approved designs; preserve unseen surfaces, pivots, contact and asymmetric details. A blockout alone does not establish this acceptance.

**File naming:** `chr_<key>_<outfit>_<view>_v##.png`, `env_<land>_<view>_v##.png`; keys as in `tools/cast.py`.

## 5. Book graphic identity
Ledger cream `#F2E8D5`, ink `#141018`, Nixie orange `#FF7A2C`, red ink `#B3261E`. Preferred font roles are condensed display, readable body, monospaced data and expressive SFX. Use only installed/bundled fonts with recorded licence; the offline fallback is Segoe UI/Arial plus Consolas/monospace. Do not claim an unavailable font was embedded. Skewed black tabs, red stamps, tally-mark overlays.

## 6. QC (before anything is called final)
- [ ] Matches its turnaround's proportions and its canon locks
- [ ] Reads as a silhouette at64px; identity has shape/prop cues in addition to colour
- [ ] Line, shading and palette per §2.3; no airbrush, no stray gradients
- [ ] Environment matches its plan view's layout and its land's time and light (§3.4)
- [ ] Battle stage clear and 24 × 6 m
- [ ] Cultural details source-checked and unresolved issues labelled; do not claim external approval without a log; keepers/Hap remain distinct from invented hostile constructs

## 7. Current detailed design and manga export contract

A character has three detail scales: silhouette at64px, material/gesture at gameplay size, mechanism/repair/costume construction in close-up. Preserve purposeful detail rather than reducing everyone to a plain mannequin. The serious register uses finished linework and selective hatching; the gag register simplifies rendering after a dramatic beat without changing identity. Fresh concept studies are versioned separately from historical candidates.

Each cast record lists front, left, right and back plus source model and readiness. Side/back views must come from actual rotated geometry or separately authored consistent drawings, never a mirrored front. Wide creatures may use a separate detail plate; retain a metric scale and identify any presentation rescaling. Missing views fail coverage rather than becoming blank final pages. Old Rahu/Ketu sacred-head/body blockouts are deprecated; current hostile assets are explicitly invented mechanical eclipse engines.

Environment records retain top-down,2.5D and front cameras, a scale grid, playable floor and faction/material logic. Concept paintings may be aspirational; do not claim they are the actual model's camera render unless they are.

Manga deliverables: clean page artwork, exact lettered page, normalized panel/balloon data, dialogue IDs, page/scene commit and skip policies, and a complete PDF edition. The printed reference route uses a declared resonance/build; game cutscenes never force the player's number, reward or combat result. All text remains separately localizable. No artist name is used as a generation-style shortcut.
