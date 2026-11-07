# ZERO-SUM: OMEN — Asset List and Contracts

Updated 7 November 2026. Required: **The Remainder, Meridian Prologue**(JAM_SLICE, D01). All rows are **specified** unless supported by actual source/check evidence. Concepts are candidates. Owner agents are responsibilities, not a staffed human team.

## 1. Export/runtime contracts

| Type | Source | Initial runtime / acceptance |
|---|---|---|
| Hero/boss | Scripted vector/Blender or generated reference+correction; pose/layer source | 1024–2048px atlas/poses, explicit facing/pivots; neutral/attack/hurt/victory in engine; canon/contacts checked; PSB not required |
| Debt Hound | Reproducible poses | 512–1024px; idle/attack/hurt and clear tell |
| Stage | Camera/floor/masks/depth source | 1920×1080,  2–3 useful planes for 1280×720; empty floor, no baked actors/UI/digits; parallax seams checked |
| Reel | Frame/glass/glow apart from labels | ≤1200×500 source; exact Unity digits/anchors |
| UI/icons | SVG/code source; actual font provenance | ≤2048² atlas,128–256px icons as needed; shape/text/focus/720p tests |
| VFX | Procedural source or flipbook | 512–1024 atlas, pooled/lifetime caps; reduced effects variant |
| Story | Layers/edit decision list | 1280×720 or1920×1080; exact subtitles separate; skip/replay-safe logic |
| Optional video | Still/request/edit provenance | 1280×72016:9 candidate; local bundled URL, subtitles/skip/still fallback; browser test |
| Audio | Note/synthesis/edit scripts; any sample licence | WAV master; Web import settings measured; loop/mix checks(AUDIO) |

4K is an optional master size. Six 4K RGBA planes cost about 190 MiB before mips, unsuitable as an automatic default. Planning budgets(not achievements): ≤50 MB compressed total, ≤25 MB initial, ≤512 MiB measured peak on a named laptop, desktop 60 fps(TECH_DESIGN). Verify compression/alpha/lines on target build.

Naming: `{type}_{id}_{state}_{version}.{ext}`. Target folders: `game/Assets/Art/{Characters,Enemies,Bosses,Stages,Reels,VFX,UI,Story,Video}` and `game/Assets/Audio`; specified until Unity project exists.

## 2. Required jam assets

| ID | Deliverable | Owner agent | Target IST | Evidence/current state |
|---|---|---|---|---|
| chr_nil | Pose set, decoder/halo overlays, Overwrite | Character/motion | 8 Nov | Candidate key art; runtime pack unverified |
| chr_vesper | Pose set, prop, entrance/reaction panel | Character/motion | 9 Nov | Candidate key art; runtime pack unverified |
| boss_varro | Two phases/tells/defeat, separate jars | Character/motion | 9 Nov | Candidate key art; runtime pack unverified |
| enm_debthound | Three poses/attack tell | Character/motion | 8 Nov | Specified |
| stg_rainalley | One stage; dawn/audit/drain/rooftop variants | Environment | 9 Nov | Base/colour-key PNGs exist; source scene/layered runtime plate missing |
| reel_meridian | Brass three tubes/glass/glow/digit anchors | Environment/UI | 8 Nov | Candidate SVG; runtime acceptance missing |
| jar_varro | Slot3 token, defence/round progress, restore cue | UI/VFX | 9 Nov | Specified; SYSTEMS/BESTIARY controls logic |
| ico_charm_horseshoe | Open-end-up silhouette+label | UI | 9 Nov | Candidate `art/graphics/charm_horseshoe.svg` |
| ico_charm_black_cat | Cat shape+label | UI | 9 Nov | Candidate `art/graphics/charm_black_cat.svg` |
| ico_charm_ofuda | Abstract paper ward, no sacred writing | UI | 9 Nov | Generator candidate specified; runtime icon unaccepted |
| vfx_audit | Stop/hit/Parry/Fortune/Favour/jar | VFX | 9 Nov | Specified; consequences stay engine logic |
| vfx_patterns | Seven labels/payoffs, shared grammar | VFX/UI | 10 Nov | Specified; concise repeated mode |
| ui_jam | Title/audio/settings/Naming/fight/charm/results/retry/credits | UI | 10 Nov | Specified; no shop/fen/crafting |
| cin_jam | Ama/Naming, Vesper, mercy, rooftop/map panels | Narrative/motion | 10 Nov | Specified; no mandatory intro film |
| npc_jam | Ama/Tobi/Nought/Gus where script needs them | Narrative/character | 10 Nov | Panels/silhouettes acceptable; no separate rig quota |
| aud_jam | Meridian loop, stop/hit/defence/pattern/UI/ambience | Audio | 10 Nov | Specified; no accepted tracked audio sources |

Varro: one visible slot 3 token, substitutes 0 for at most 3 player rounds; opens after 3 qualifying defences or expiry; next slot 3 visibly restores stored digit. Exact ordering/overlap in SYSTEMS. Art never determines damage or implies luck creation.

## 3. Three charm IDs/effect labels

Free pick **one of three**. No fen/purchase/crafting/sets in required jam.

| Gameplay ID | Label | Presentation contract |
|---|---|---|
| charm_horseshoe | Horseshoe | Chosen resonance faces on allied wheels, **where present**, ×1.5 width; never add an absent face |
| charm_black_cat | Black Cat | First would-be Bust/fight: visibly third→first digit, then re-evaluate priority; single conversion with Favour |
| charm_ofuda | Ofuda ward | First enemy strike autoParry, no accepted stop/reflection; counts once toward Varro defence |

## 4. Evidence and scope

Per asset: ID/version, source/reference/output hashes, canon IDs, tool/model/request(ifknown), script/scene, actual processing, licence evidence, dimensions/pivots/layers, import settings, capture/build ID. No credentials/signed URLs. Historical generation claims/missing sources stay explicit in AI_DISCLOSURE.

Implemented means source/export exists. Verified means named checks/build evidence recorded. A checkbox/date never establishes that. All required files must be in the same packaged itch build; no mutable remote content.

Maeve/Hina/Tamamo, Hyakki stages/reel/audio, other cultures' assets, full bonds/Link Arts, expanded rigs and long videos are **not in required jam**. Their future briefs require JAM_SLICE's extension gate/post-jam planning, not silent Must promotion.
