# ZERO-SUM: OMEN — Art and strictly AI production pipeline

> **HISTORICAL SNAPSHOT - 6 November 2026, baseline `3d88239`.** Findings/proposals describe that snapshot, not the current corrected repository. See [adopted decisions](../DECISIONS.md), [current status](../PROJECT_STATUS.md) and [audit resolutions](../DOC_AUDIT.md).
Audit date: 6 November 2026 (Asia/Calcutta). Source: repository commit `3d88239dff58db1d313b8d979d6ae98a8f1ceed0`.

Status: evidence and proposed refinements, not implemented production changes. Original art, policy documents and builds were not changed. User direction for this plan: **Unity jam first; free and already available tools first; AI performs development and asset production**. Human direction and player feedback can guide the work; the plan does not depend on a manual artist, animator, editor, composer or programmer completing AI drafts.

## 1. Verdict

The art direction already has a coherent idea: **painted world, inked people**, with the Basilica's graphic machinery intruding on softer lived-in regions. Keep that. The production gap is the ability to make the same character act, react and remain recognizable in an actual game frame. More isolated key art or a longer art book will not close that gap.

The practical target is a small, visually authored game with unusually good presentation. A full AAA campaign's content volume, facial performance, cinematics and QA cannot be promised from this repository or an AI tool list. Build one final-quality fight, measure its production time and browser cost, then expand only the proven process. The jam can demonstrate the game's identity without producing the entire world.

Use local scripted Blender, AI-authored vector art, procedural materials and deterministic Unity animation as the primary production route. Higgsfield and Meshy are optional accelerators when existing access and quotas are verified. They are not dependencies for finishing the jam and no paid jobs were submitted in this audit.

## 2. What actually exists

The complete machine inventory is [ASSET_METADATA.csv](ASSET_METADATA.csv). It contains every tracked raster, vector, motion and PDF artifact with byte size, SHA-256, dimensions/viewBox, applicable page count/codecs/duration, provenance evidence and a visual-sampling flag.

| Group | Observed | Production meaning |
|---|---:|---|
| Character/environment concept JPEGs | 13 | Flattened concept images; no alpha or rigs |
| Layout/base PNGs | 9 | Composition guides and colour keys; source scenes are absent |
| SVGs | 68 | Strongest reproducible asset family: generators exist in `tools/graphics.py` and `tools/figures.py` |
| MP4s | 2 | Cinematic experiments, not an assembled intro |
| World/art bible PDF | 147 pages, A4 portrait | Derived presentation of Markdown and art; not an additional implementation |
| Art book PDF | 39 pages, A4 landscape | Derived draft; builder labels pass-1 placeholders |

The 94 inventoried files total 42,133,881 bytes. No exact byte duplicates were found by SHA-256. This does not exclude visually similar assets or repeated subject matter. PDF metadata reports Skia/PDF m153; their builders use HTML/CSS and `tools/render_pdf.js`. They are outputs from the existing sources, not separate canonical design specifications. Neither PDF was rendered or visually audited in this task.

`git ls-files` finds no `.blend`, `.glb`, `.fbx`, `.psb`, `.psd`, `.wav`, `.ogg` or `.mp3` production sources. A base render is not a reusable 3D scene. Rebuilding the same camera or editing a character consistently requires preserving the scene/script, rather than retaining only its image.

### Representative visual observations

Visual sampling was limited to NIL key art, Meridian battle alley, Hyakki bridge and the Moon Pier colour key; the NIL SVG source was inspected as text. Other images were inventoried but not visually approved. No motion clip was watched; video statements below are metadata findings.

- `art/concepts/nil_keyart.jpg`: the expected white hair/orange streak and decoder identity read clearly. Clothing and hair use extensive soft rendering and the art has baked glowing digits. It is a useful reference, but does not yet satisfy the v2 two-tone character rule. Generated digits should not become gameplay numbers.
- `art/concepts/env_meridian_battle_alley.jpg`: stage composition and three-tube motif are useful. Materials and wet reflections read as a rendered cinematic plate rather than the matte gouache specification. The glowing tubes are baked into the plate, limiting reel animation and lighting control.
- `art/concepts/env_hyakki_battle_bridge.jpg`: strong indigo/vermilion identity, but a foreground character is baked into the right side. This fails the empty battle-plate contract and can overlap the enemy. The large moon and lanterns also compete for the eye with a top-centre reel.
- `art/base3d/hyakki_pier_colorkey_v1.png`: usable camera, floor and reel blockout. It is an early layout, not final painterly art.

These samples support the repository's own pass-1 diagnosis. They do not establish that every JPEG has the same defects.

### Motion metadata

| File | Dimensions | Duration | Video/audio | Finding |
|---|---|---:|---|---|
| `intro_meridian_dawn.mp4` | 1280×720 | 8.064 s | H.264, 24 fps / AAC | Landscape test; not a complete 45-second intro |
| `nil_reveal.mp4` | 720×1280 | 5.056 s | H.264, 24 fps / AAC | Portrait orientation conflicts with the 16:9 cinematic contract |

Reframe the reveal as a deliberately bordered portrait panel or regenerate a landscape shot when an existing quota permits. Do not stretch it to 16:9. A metadata match alone does not validate animation continuity or browser playback.

## 3. Specific document conflicts and missing contracts

| Evidence | Consequence | Proposed resolution |
|---|---|---|
| `ARTBOOK_PRODUCTION.md` §4 makes human overpaint mandatory; `LEGAL_IP_AI.md` §3 says people overpaint shipped art; `TEAM_HANDBOOK.md` §4 repeats it | The written pipeline cannot satisfy strict AI production | Replace the human finishing stage with agent-driven editing, scripted cleanup, model-assisted revision and in-engine review. Reject or simplify assets that cannot pass. User direction supersedes these old workflow assumptions; it does not require another approval loop |
| `AI_DISCLOSURE.md` submission draft says final art, editing, arrangement and writing were made by the team, while log rows promise future human finishing | Copying this text could misdescribe the actual shipped work | Rewrite from the final asset manifest. Credit AI writing, code, vector generation, animation and audio wherever actually used. Never claim human edits that did not occur |
| `ARTBOOK_PRODUCTION.md` §3 has painterly concept register A and cel in-game register B | Expensive polish can go to art that the player never sees | For the jam, make register B style frames the approval reference. Register A is optional promotional output from already finished designs |
| `ART_DIRECTION.md` §6 supersedes prompt styles; `HIGGSFIELD_PROMPTS.md` still contains old glossy/painterly suffixes and several scene-bound character prompts | Copy/paste can reintroduce pass-1 gloss and inconsistent backgrounds | Store one active prompt template per asset type and version it. Character sheets use neutral backgrounds; battle plates exclude characters and UI |
| `ASSET_LIST.md` specifies layered PSB characters and six-layer stages; only flattened concepts are tracked | Segmentation, hidden parts, pivots, rig deformation and layer seams remain unsolved work | Prove one complete imported actor before scaling. Prefer exported sprite pose sheets for the jam if layered-rig generation is slower or unstable |
| `ASSET_LIST.md` §2 says ~45 s intro; `HIGGSFIELD_PROMPTS.md` §6 lists 8+4+4+4+4+4+12+15+10+8+12+10 = **95 s**, excluding engine shots | Cinematic production and onboarding time can double silently | Treat the prompt list as historical material. The locked jam storyboard must have exact shot durations totaling the approved opening, with a shorter fallback |
| `ARTBOOK_PRODUCTION.md` §9 records 3D Jutsu working, Higgsfield jobs unknown, Meshy disconnected in another session | Historical connector status may be mistaken for current access | Mark it historical. Establish account, quota and request status afresh before any generation |
| `ASSET_LIST.md` owners are human role placeholders, statuses mostly unstarted | Nobody/agent is accountable for integration and acceptance | Assign an agent role, generated artifact, validator and acceptance evidence per row; completion means imported and running, not downloaded |
| `CULTURAL_CONSULTATION.md` has paid-review plans but an empty review log | Cultural correctness is not verified | Preserve a research/uncertainty record. AI source research and consistency checks do not constitute native-speaker consultation. For the jam, simplify disputed specifics and avoid claims of expert verification |

## 4. Local tools and external capabilities

### Verified in this task

- Blender executable at `C:/Program Files/Blender Foundation/Blender 5.2/blender.exe` reports **5.2.1 LTS**. Its local help confirms background execution, Python scripts and exception exit codes. This is sufficient to author scripted scenes and validation without a new service. The [Blender command-line manual](https://docs.blender.org/manual/en/latest/advanced/command_line/index.html) describes batch automation; direct page fetching was unavailable, so the actual command options were additionally checked against the installed executable.
- `ffprobe` runs and read both video files successfully. Pillow read all raster dimensions/modes; standard XML parsing read all SVG viewBoxes. Poppler `pdfinfo` read both PDFs.
- `C:/Program Files/Unity/Hub/Editor/6000.4.11f1/Editor/Unity.exe` exists and its installation contains `WebGLSupport`. This audit did not launch Unity, activate a license, compile a shader, import assets or build the game. The `6000.3.17f1` directory exists but the expected editor executable was not found there during inspection. Presence of a directory is not a working LTS installation.
- No currently enabled tool found by the Unity/Blender/Meshy/Higgsfield capability-name search provides an authenticated production connector for those services. Local command-line tools and documented APIs are different access routes. No API credential, generation balance or account plan was tested.

### Higgsfield: optional images and short motion

Higgsfield currently documents a submit/poll/cancel REST flow at `api.higgsfield.ai`. Persist each returned request ID before polling; an unknown submission is a reconciliation problem, not a reason to blindly submit again. Select the actual model's schema before writing an adapter. The repository's old model names and `generate_angles` calls are not verified current API contracts. [Official API quick start](https://open.higgsfield.ai/quick-start), [documentation index](https://docs.higgsfield.ai/docs/llms.txt).

Its API terms separate API balance from consumer subscriptions, do not claim ownership of outputs or restrict their commercial use, and do not guarantee originality, non-infringement or IP protection. Partner-model conditions may differ. Record the actual model and terms for each shipped asset; this audit is not rights clearance. Download and preserve accepted outputs rather than relying on provider URLs. [Higgsfield API terms, §§1.2, 5, 7.4, 12](https://open.higgsfield.ai/terms-of-service).

Use Higgsfield for an approved style-frame variant or a short, noninteractive atmospheric shot if existing access is available. **Elements and 3D Jutsu automation were not verified here.** Do not design a pipeline that depends on their API exposure. Deterministic cameras, vector plates and Unity animation cover the jam without them.

### Meshy: optional 3D bases, never a finished character guarantee

Meshy's rigging endpoint is designed for textured humanoid bipeds with clear limbs. GLB/FBX rigged results are documented; faces must point +Z. This does not solve Tamamo's nine tails, Hina's umbrella, layered robes, facial acting, hair or correct prop grips. Give those a scripted Blender rig or use purpose-built sprites. [Meshy rigging API](https://docs.meshy.ai/en/api/rigging).

Remesh provides quad-dominant or decimated-triangle output and multiple exports. The requested face count is a target and can differ; this is not a guarantee of deformation-friendly edge loops. New integrations should use the separate conversion/resize endpoints rather than deprecated remesh parameters. Validate generated geometry and animation poses in Blender before accepting it. [Meshy remesh API](https://docs.meshy.ai/en/api/remesh).

Meshy's current ownership/help pages describe paid private ownership subject to reference rights, and free outputs as CC BY 4.0 with attribution. A general features page gives a more restrictive free-use summary; preserve the applicable account/output terms rather than assuming a license from marketing. Free web credits do not establish free API entitlement. Existing account access and terms remain unverified. [Ownership help](https://help.meshy.ai/en/articles/10137554-what-is-the-ownership-of-the-generated-models), [commercial-use help](https://help.meshy.ai/en/articles/9992001-can-i-use-meshy-assets-commercially-license-copyright-explained), [features summary](https://www.meshy.ai/features).

### Unity: final composition and all interactive timing

Use Unity to composite actors, apply regional light/grade, animate camera and reel, render exact digits, mix sound, and run skip/replay behavior. Generated video never controls a combat result or contains the only readable tutorial information. Unity's Web documentation notes URL-based video playback, no embedded VideoClip support and no frame accuracy; this supports keeping gameplay effects in-engine. The fetched documentation is for 6000.5, so validate behavior on the selected installed editor before depending on it. [Unity Web video documentation](https://docs.unity.com/en-us/engine/6000.5/manual/platform-specific/webgl/develop/video).

## 5. Production route with no manual finishing dependency

Every asset moves through **brief → reproducible base → candidate → correction → validation → engine composition → acceptance**. A rejected candidate returns to correction or is simplified. It does not become a handoff to a human artist.

1. **Art-director agent writes the contract.** Asset ID, story use, character canon, shape, palette, camera, runtime size, exclusions and reference hashes. Three final-style anchors: NIL on Rain Alley floor, Vesper firing, Varro receiving a stopped hit. Review the actual 1280×720 game composition before making another region.
2. **Layout agent authors Blender scenes or SVG geometry.** Save the `.blend` and the `bpy`/vector script. Use an orthographic or explicitly locked camera, shared scale and anchor positions. Procedural geometry is especially suitable for brass tubes, lanterns, alleys, charm silhouettes and Nixie machinery.
3. **Candidate agent produces the image.** Default to scripted cel materials, layered vector figures and stylized procedural backgrounds. An existing image-model quota may paint a base or revise a pose, but generated output remains attached to the same canon/reference package. Batch a few controlled alternatives, select one direction and stop exploring once the contract passes.
4. **Correction agent fixes the specific defect.** Use bounded image edits when available; otherwise simplify shapes, edit source vectors, re-render the same scene, change material parameters or redraw geometry through code. Never rely on asking a new independent generation to remember the old face or costume.
5. **Animation agent authors reproducible motion.** Prefer three strong attack poses, a short anticipation, hit hold and recovery over long interpolated generic motion. Character scale and foot contacts remain fixed. Use scripted coat/tail secondary motion and exact prop parenting; avoid deriving a playable rig from an opaque video.
6. **Validator checks objective contracts and captures test scenes.** Dimensions, transparency, palette coverage, missing layers, basename/ID, compression/import settings, material count, triangles and bone counts are machine checks. Silhouette, anatomy, readable action and cultural context require image/sequence critique against references. A model critic is fallible; no automated score certifies artistic quality.
7. **Integrator agent imports, composes and profiles.** Capture idle/attack/hurt/victory over both light and dark backgrounds, at game size and 64 px silhouette size. Record a full fight and reduced-motion version. Keep the runtime independent of generation APIs; all shipped assets are frozen build outputs.

### Character production

- Keep the existing canon: NIL's decoder on the **right** wrist, white hair with one orange streak, amber eyes, asymmetric coat and exact `NaN`; Vesper's seven chambers/left-shoulder braid; Hina's one-eyed umbrella; Tamamo's nine tails. Encode counts and handedness in the brief and test views. Never mirror an asymmetric actor without swapping/correcting the design.
- Render **all text and meaningful digits in Unity**. The concept art's glyphs are reference effects, not reliable text. Hina's kimono can use a generated numeric-pattern texture authored by code, so values remain ≤99 without trusting image generation.
- Start with NIL and one enemy. A full layered character requires painted hidden surfaces under every moving part; automatic segmentation alone cannot supply them. For the jam, use AI-authored transparent pose sprites and small deterministic motions if a generated rig cannot deform cleanly.
- Reuse a small expression vocabulary, consistent facing, body proportions and neutral lighting. Keep alternate outfits, elaborate facial rigs and many camera angles beyond the jam.

### Backgrounds and regional identity

Use one renderer/texture grammar across all lands; vary materials, weather, values, occupation and rhythm. Do not make every region a different rendering pipeline.

| Place | Keep from canon | Production emphasis |
|---|---|---|
| Meridian | Remainder repairs, Ledgerist brass, intrusive numbers | Rain and warm windows over matte slate planes; exact tube/reel props separately composited |
| Hyakki | Indigo, vermilion, moonlit community and paper | Calm play floor, restrained lantern bloom, paper texture; parade silhouettes in a distant independent layer |
| River Empire | Lacquer/jade port vs misty courts | Wealth and labor visible in construction; clear atmospheric separation rather than maximal ornamental density |
| Śūnyapura | Monsoon stone, instruments, living mathematics | Scale-accurate observatory/stepwell blockouts; decorative scripts authored separately after source checking |
| Kroton Nova | Noon, white stone, sieve, bronze | Hard geometric shadows and institutional repetition; distinguish inhabited spaces from monumental sets |
| Crossroads | Sunset dust, casino neon, ghost rail | Long horizons and empty space; separate frontier life from casino branding |
| Basilica | Steel/brass order, numerical enclosure | Repeated modular motifs; finale restores warmth through lighting/composition before requiring new geometry |

For each stage, save camera, floor, horizon and actor-safe masks. Paint/generate empty layers rather than cutting a complete image into arbitrary strips; newly revealed areas need actual content. Use six layers only when parallax proves useful. A two- or three-layer composition with correct depth is an acceptable jam fallback.

### Cutscenes

Default to staged stills with camera moves, character expression swaps, exact subtitle text, lighting and procedural particles. Use one visual payoff per scene. The interaction that changes Ama's Omen should happen through player input and in-engine digits, preserving the game's central verb.

Create a timed edit decision list before generation: shot ID, source image, duration, camera, subtitle IDs, audio cue, skip destination and state changes. State changes happen once in game logic; skipping or replaying never repeats rewards or loses a recruit. First-view skip and transcript/recap support should be implemented rather than waiting for perfect video.

Keep optional Higgsfield shots short and low-motion when continuity matters. Build a still fallback for loading failure. Package accepted video with the itch game and refer to its local build URL; a live remote generation or mutable remote content service is not a jam distribution plan.

### Audio

The synth-noir motif and stop-clack vocabulary are useful existing decisions. Implement the stop sound first, followed by impact, parry, pattern, UI and regional ambience. The stop sound responds immediately; only its resonance or optional musical layer aligns with the beat.

Use AI-authored deterministic synthesis/arrangement scripts as the free baseline: oscillators/noise/envelopes, a short original motif, tempo-aligned stems, rain/gear/lantern textures. Keep MIDI/note-event data, synthesis parameters, render commands and stems. Licensed existing samples can be used only with a recorded source; do not invent musician or cultural-instrument credits. This route cannot certify an authentic traditional instrumental performance.

AI voice is optional. Prefer written dialogue plus distinctive synthetic barks over inconsistent, unlicensed or expensive speech. If an existing voice provider is used, record its model/license and use an original voice design. Keep subtitles independent of audio. Check stem loop lengths, seam clicks, peak/loudness and dialogue intelligibility. Existing targets are −16 LUFS integrated and −1 dBTP; verify by measurement, not a prompt. Retain a low-intensity mix and reduced-transient versions.

## 6. Asset contract and validation budgets

These are **proposed starting budgets**, not measured game performance. Keep 4K source masters out of runtime by default. Runtime dimensions follow on-screen size, not export prestige.

| Type | Starting runtime contract | Acceptance evidence |
|---|---|---|
| Hero | 1024–2048 px pose/atlas family; shared pivots; explicit facing and handedness | Contact sheet in neutral pose, 64 px silhouette, attack/hurt/victory sequence, no foot sliding |
| Enemy | 512–1024 px; three distinct poses initially | Intent recognizable without color alone; no overlap with reel/UI |
| Stage | 1920×1080 layers initially for a 1280×720 game view; 2–3 useful planes | Empty actor masks, no baked UI/digits/foreground character, parallax edge inspection |
| UI/vector | Code-native vector master; atlas rasterizations only at needed sizes | Font/glyph coverage, legible 720p capture, consistent 9-slice and padding |
| VFX | 512–1024 atlas; pooled, bounded lifetimes | Pattern reads during action, reduced-motion capture, no full-screen strobe dependency |
| Video | 1280×720 16:9 delivery, short shots; fallback still | Actual target-browser playback, skip, subtitles, missing-media fallback |
| Optional 3D base | Apply scale; known forward axis; separated props; polygon/material/bone report | Extreme pose/deformation test and render parity; reject intersecting or fused limbs |

Six 3840×2160 RGBA layers need about **190 MiB uncompressed**, or about **253 MiB with full mip chains**, before other assets or duplicate buffers. One 2048² RGBA atlas is 16 MiB before mips. File compression is not runtime texture memory. Treat the existing six-layer 4K requirement as a master-art ceiling and profile actual imported format/size. No texture compression mode is universally correct for alpha, atlas quality and all browsers; test on the chosen Unity build target.

Do not set an unexplained AAA polygon or bone budget for characters that are delivered as sprites. For optional live 3D actors, establish budgets from a representative battle with three heroes and a boss, then enforce measured material/draw-call and GPU costs. The team's existing 60 fps laptop/30 fps phone aspirations need named hardware/browser captures before they become claims.

Store a machine-readable manifest per accepted asset with: `id`, `version`, `source_commit`, `canon_reference`, `source_files`, `sha256`, `provider`, `model`, `request_id` if any, `input_reference_hashes`, `prompt_file`, `seed` when supported, `license_snapshot`, `runtime_dimensions`, `pivot`, `layers`, `variants`, `validator_results`, `engine_capture`, `status`. Never commit secrets or signed output URLs. Some providers do not expose seeds or reproducible model versions; mark those unavailable rather than inventing them.

## 7. Jam-first priorities and expansion gate

1. **Prove a final game frame:** one actor, one enemy, one stage, one reel and immediate stop feedback. Make these consistent at actual game size. Produce the Blender/vector sources and import settings with the assets.
2. **Prove motion and readability:** attack, hurt, parry, one pattern payoff, UI intent and reduced-motion version. Remove baked text/characters from plates and check image scale/pivots.
3. **Finish the minimum story package:** exact Naming digits, Vesper rescue, Varro sequence and a resolved ending card. Extend to Hina/Hyakki/Tamamo only within the jam scope selected by the production lead. This is a fallback proposal; it does not silently replace the existing locked slice.
4. **Fill missing audio before additional paintings:** one good score loop, dependable stop/hit/parry/UI and readable mix contribute more to a finished game than twelve non-playable art-book images.
5. **Freeze art and run browser acceptance:** import/runtime size report, first-load test, full fight, cutscene skip, missing-media fallback, no generated placeholder text, provenance/disclosure reconciled to shipped assets.

After the jam, expand one new region at a time only after one recruit, one regional enemy mechanic, one boss, one bond scene and one finished stage can be produced reproducibly. Record elapsed production time, rejected generations, retries, optional credit spend and final build size per content unit. Forecast the full game from those observed units instead of treating one image as a completed character.

An asset generator should have an agreed per-asset attempt/time limit and an optional service-credit ceiling. If a tool has unknown job status or exhausted free access, use the local scripted fallback. No automatic purchase or subscription is part of this plan.

## 8. Methodology and verification limits

Read in full: `ART_DIRECTION.md`, `ARTBOOK_PRODUCTION.md`, `ASSET_LIST.md`, `AUDIO.md`, `CULTURAL_CONSULTATION.md`, `LEGAL_IP_AI.md`, `AI_DISCLOSURE.md`, `TEAM_HANDBOOK.md`, `art/HIGGSFIELD_PROMPTS.md`, `JAM_SLICE.md`, `QUALITY_BAR.md`. Read relevant canon/budget/accessibility/feel sections of `CHARACTER_BIBLE.md`, `TECH_DESIGN.md`, `ACCESSIBILITY.md`, `GAME_FEEL.md`; inspected source/provenance excerpts of `build_artbook.py` and `build_bible.py` and the NIL SVG. Other agents' audits cover the complete game/narrative files.

Read the PDF skill at `C:/Users/rushi/.codex/plugins/cache/openai-primary-runtime/pdf/26.1030.10813/skills/pdf/SKILL.md` for read-only metadata inspection. No PDF authoring, content-summary review, rendering or layout approval was performed. Source Markdown and builder excerpts establish the described derivation; PDF metadata does not prove a fresh rebuild or complete source synchronization.

Ran: raster metadata reads; XML reads of all SVGs; SHA-256 over all 94 inventory files; `ffprobe` on both videos; `pdfinfo` on both PDFs; installed Blender `--version` and relevant `--help`; executable/module existence checks; tracked source-file searches. All inventory operations completed. An expected executable was absent in the 6000.3 directory, as noted. No Unity import/build/playtest, animation viewing, audio listening, exhaustive image review, authenticated external-tool test, paid generation or cultural/legal expert review occurred. Proposed quality checks remain work to execute.
