# ZERO-SUM: OMEN — Art Direction v3

Updated 7 November 2026. **Specified, not accepted runtime art.** [DECISIONS.md](DECISIONS.md) resolves conflicts; JAM_SLICE limits required content; PROJECT_STATUS records evidence.

**Painted world, inked people.** Matte lived-in backgrounds carry the old plural world; graphic cel characters and numerical machinery carry the struggle over luck. These are original production choices, not a claim of verified research into another studio's process.

## 0. Current illustrated direction: painted world, inked manga

The illustrated edition and in-game motion comic add dense, deliberate ink craft to the shared foundation. The user means **Versus, the manga series**, not merely a generic VS card. For reference accuracy, its official credit is story by ONE, manga by Kyoutarou Azuma, organized by bose; One-Punch Man credits ONE and Yusuke Murata. These titles and Berserk are references for broad craft questions, not prompts to reproduce an artist's personal style, characters, compositions or signature marks. [Kodansha's Versus credit](https://kmanga.kodansha.com/title/10569/episode/34962), [VIZ's One-Punch Man credit](https://www.viz.com/one-punch-man).

**Original visual brief:** tactile brass bureaucracy and plural folklore, drawn with precise variable-weight ink, spotted blacks, selective crosshatching and screentone, grounded anatomy, cinematic depth and clear action geography. Soft matte painted spaces contrast with decisive foreground drawing. Colour is deliberate: local cel colour, region atmosphere, and restrained signature accents. No uniform muddy wash, generic glossy portrait treatment or indiscriminate mechanical ornaments.

### Two dramatic registers

| Register | Line and rendering | Staging and timing |
|---|---|---|
| Serious | Finished anatomy; confident contour; blacks lead to faces/hands; hatching concentrated in contact/material shadows | Establish geography, wind up, make contact, show consequence; foreshortening serves a readable action |
| Comedy | Same identity and costume; simplified face/line detail; quiet flat values | A still reaction after a resolved beat; precise deadpan or an observed contradiction, not a joke over grief |

NIL's humour is literal observation; Vesper's is generous bravado and selective honesty. Punchlines target the system and powerful people's contradictions. Keepers, personal grief, disability, poverty and a culture are not punchlines. A gag never conceals an attack tell or interrupts a necessary explanation.

### Detail that belongs to this world

NIL's abacus-lock clasps, interrupted decoder ring and repaired ledger lining express a life made from discarded accounting. Vesper's dealer tailoring, erased House insignia seam, worn coin and mechanical revolver express experience rather than decoration. Varro's hinged ledger plates, three-lever confiscation clamp and protected exemption token connect his silhouette to his job and sister. A Debt Hound's stamp-pad paws, receipt clip and abacus spine make it an enforcement machine. These are the fresh design refinements; game-readable silhouettes and canon handedness still govern them.

### Manga and game contracts

English pages read left-to-right, then top-to-bottom. Use 3-5 panels normally, with sparse splash pages at earned turning points. Establish actor positions before reversing an angle; preserve the 180-degree line across a blow. Leave sufficient quiet space for text. Generate clean artwork **without lettering**, then add exact vector/raster lettering from the dialogue manifest. Speech, Civic Omen, resonance, Audit values and sound-effect typography are authored layers. Do not trust generated writing.

Clean art, lettered page, panel regions, dialogue IDs, reading order, safe areas and reduced-motion behavior are separate deliverables. A printed chapter depicts one clearly identified authored route; a live cutscene must yield to actual player choices and combat outcomes. Technical determinism means state/outcomes replay; it does not promise identical video decoding or every rendered frame. Detailed rules live in MANGA_DIRECTION and TECH_DESIGN.

The old 3D cast and environment views are first spatial blockouts. Fresh inked concepts establish the current visual treatment; they do not retroactively make the old models detailed matching final turnarounds. The artbook distinguishes concept, spatial draft, model source, technical specification and accepted runtime asset.

## 1. Pass-1 assets and the target

Existing JPEGs are exploration references, not final layered/rigged assets. Retain originals and create derived files. The 6 November metadata/sample audit is historical evidence in `docs/refinement/ASSET_METADATA.csv`, not a current acceptance ledger.

| Reject | Correction |
|---|---|
| Glossy, evenly detailed skin/cloth | Flat base + one hard shadow; optional one hard rim |
| Characters merge into background | Value separation, calm actor-safe areas, coloured contour |
| Repeated mannequin poses | Character-specific anticipation, impact and recovery |
| Inconsistent face/costume/prop counts | Shared canon/reference package and pose comparison |
| Baked meaningful digits/writing | Exact runtime/code-native text; remove it from image layers |
| Busy floor or baked foreground actor | Empty stage plate and safe masks |
| Correct still but broken motion | Actual gameplay-size sequence before acceptance |

## 2. The painted world

Matte gouache/poster-colour appearance: soft brush texture, opaque planes, gentle sky gradients and about twenty mixed colours per region. One motivated light/time of day, atmospheric depth and two or three everyday details (repairs, food, laundry, moss). A scripted Blender base establishes geometry without becoming a shiny rendered finish.

Actors left, enemy right, floor/intent/UI clear; reel frame separately composited top-centre. Save camera, scale, horizon, floor anchors, depth planes and occlusion masks with the source scene/script. Segmentation does not supply unseen surfaces. Six parallax layers are not mandatory; use only useful planes.

## 3. Inked people and action

Silhouette reads as a black fill at 64 px in a separate test. Colour supports identity but is never the only gameplay cue. Stylized proportions vary by build/age; child-shaped spirits do not inherit adult proportions. Readable hands, variable-width coloured contours, simple faces, flat base+hard shadow and optional rim. No airbrush.

| Character | Shape | Signature | Secondary |
|---|---|---|---|
| NIL | Rectangle + broken circle | `#FF7A2C` orange | Ink, bone |
| Vesper | Triangles | `#E5243B` crimson | Black, brass |
| Maeve (future) | Circles/arcs | `#D9822B` copper | Clover |
| Hina (future) | Umbrella dome | `#E34234` vermilion | Indigo |
| Tamamo (future) | Fan/crescent | `#8E44AD` violet | Gold |
| Varro | Block | `#B7410E` rust | Gunmetal |
| Thale (future) | Cathedral arch | `#E8E6E1` steel white | Brass |

Canon locks live in CHARACTER_BIBLE. NIL: right-wrist decoder, one orange hair streak, amber eyes, longer left coat tail, exact `NaN`. Vesper: left-shoulder braid and seven chambers. A mirrored front is **not a back view**; never mirror asymmetric runtime art without correction.

Limited animation uses strong holds, brief smears and anticipation/impact/recovery. Flat angular effects and diagonal cut-ins support hits. Flashes/shake obey ACCESSIBILITY/GAME_FEEL and have reduced alternatives. Glitch/chromatic effects belong to Noise/Basilica moments, not permanent filters. Input response precedes spectacle.

### Detail hierarchy: specificity without noise

Fresh designs need lore-bearing detail, not uniform flat cutouts. At 64 px read silhouette; at game size read material, weight and gesture; in close-up read the decoder/prop, wear, fasteners and repairs that explain a life. Concentrate craft detail at hands, primary prop and story-bearing repair points; rest areas protect hierarchy. Use tactile brass luck machinery and worn bureaucratic folk-fantasy materials. Preserve cel shading while varying seams, construction, scuffs and mechanism. Detail must change who this person is, not merely add gacha ornament. Pair hero views with prop/macro callouts in the art book.

## 4. Regional colour scripts

| Land | Light | Base / accent |
|---|---|---|
| Meridian | Rain dawn→dusk/night | Slate, warm windows, moss / Nixie orange; yellow `#F5E400`, magenta `#FF2E88`, cyan `#00E5FF` accents |
| Hyakki (future) | Moon/festival | Indigo, paper / vermilion, gold |
| River Empire (future) | Golden harbour; misty courts | Jade, ochre, lacquer / gold |
| Śūnyapura (future) | Monsoon break | Sandstone, peacock / saffron, brass; purple for invented Basilica eclipse constructs |
| Kroton Nova (future) | Hard noon | Chalk, Aegean / bronze |
| Crossroads (future) | Sunset→neon | Rust, sage, dusk violet / sunset orange |
| Basilica (future) | Interior→sunrise | Brass, steel / Nixie orange |

Maintain shared line/shading/actor/typography grammar. Vary geography, materials, occupations and weather. Cite cultural sources and disagreements; no authenticity/community approval claim from AI checks. Rahu/Ketu constructs must be mechanically distinct from revered celestial figures.

## 5. Jam production and acceptance

Required: NIL, Vesper, Varro, Debt Hound; one Rain Alley stage with light/staging variants; Meridian reel; three charm icons; shared UI/panels/VFX/audio. Other regions/actors are future behind JAM_SLICE's gate. No mandatory myth film or art-book painting quota.

Contract→AI-authored SVG/Blender base→procedural render or optional generation→AI-directed correction→scripted pose/layer/rig/export→engine integration→review→provenance. **No human finishing stage.** Simplify, re-render or reject failures. Source scenes/scripts/pivots are deliverables. First approve one 1280×720 fight frame, then NIL/Vesper attacks and Varro response in motion. Check canon, contacts, safe areas, reduced effects and legibility. Runtime budgets live in ASSET_LIST/TECH_DESIGN; 4K masters do not imply 4K runtime.

## 6. Active prompt grammar

Use technique/original design attributes, not artist/studio-name shortcuts. Subject briefs are in `art/HIGGSFIELD_PROMPTS.md`. Select models only after current schema/access checks.

**Character:** flat base plus one hard shadow, optional hard rim in {emotion colour}, variable-width coloured contour, dominant {shape}, palette led by {signature}, locked reference costume/proportions, neutral background, no skin/cloth gradients, no text/digits/logo.

**Empty stage:** matte animation background, soft gouache-like texture, limited {palette}, one light at {time/weather}, atmospheric depth, two lived-in details, clear actor-safe floor/reel space, no actors/writing/digits/glossy sheen.

**Action:** locked cel actors over matte plate, correct handedness, readable anticipation/contact/recovery, angular {accent} effects, clear silhouettes/contacts, no text/digits.

## 7. Reference discipline

References answer narrow craft questions (composition/timing/value). Preserve URL/date and actual observation. Earlier external art-book quotes and process-study assertions are retired as production authority; no unsupported spread-by-spread/interview study is claimed. Dated primary-source game-feature research and its limits are in `docs/refinement/COMPARATIVE_RESEARCH.md`.

## 8. Meridian's four eras

Fictional styles follow LORE_LEXICON's timeline; captions must not invent dates.

| Era | Motto | Materials / people | Civic Omen frame |
|---|---|---|---|
| Charmpunk | Luck over sense | Street repairs, plastic gold, varied charm combinations | Gaudy/imitation display |
| Remainder | Survival over luck | Scrap brass, patched cloth, rope, salvaged tubes | Cracked/hidden display |
| Ledgerism | Order over chance | Brass, steel, enamel, uniforms, arches | Stamped steel numerals |
| Gilded Fortune | Fortune and order | Gold leaf, jade, silk, gardens | Restrained gold/embroidery |

Wards mix Remainder/Charmpunk; Exchange layers Gilded over Ledgerism; Ring is Ledgerism; Bazaar is mixed street craft. A person/object/frame comparison is optional after the game frame.

Graphic identity: cream `#F2E8D5`, ink `#141018`, orange `#FF7A2C`, seals/corrections/tallies. Civic Omen, resonance, `NaN` and Audit Omen use distinct frames(D03). Bundled fonts need actual file/licence/glyph evidence. Book builds use local/system fallbacks without network fonts.
