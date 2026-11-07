# ZERO-SUM: OMEN — Technical Design

Updated 7 November 2026 IST. Architecture is **specified**. No Unity project or hosted Unity game exists yet; see [PROJECT_STATUS.md](PROJECT_STATUS.md). The first viability target is installed **Unity 6000.4.11 f 1 + Web module**. Do not substitute an unverified LTS directory or install packages before an empty Web build proves the toolchain.

## 1. Boundaries and ownership

| Layer | Owns | Must not own |
|---|---|---|
|Core |Validated wheel/face state, accepted commands, patterns, effect pipeline, Balance, jar, terminal state, named gameplay RNG |Unity clock, rendering, network, asset lookup |
|Content |Stable typed IDs, definitions, explicit faces, scalar tuning, tutorial events, dialogue |Runtime arbitrary expression evaluation |
|Flow |One encounter/round state machine; command eligibility, pause, skip, retries |Independent damage formula |
|Presentation |Sprite rigs, in-engine cut-ins, camera, UI, VFX, audio from immutable results |Random gameplay outcomes or extra damage |
|Meta |Versioned save/settings, checkpoint/journal reconciliation |Reward grants without idempotency keys |

One sequencing owner drives timing. Prefer plain state transitions first; add Timeline/tween packages only for demonstrated presentation needs. No ECS/backend/runtime LLM/service dependency is required for the jam. Use installed/local/free tools first. Assets generated externally are offline inputs with recorded provenance, never required runtime network calls.

## 2. Core types and numeric domain

Definitions: resonance 0–9; Civic Omen 00–99; integer Balance/max; normalized Audit Omen; Face Id/digit/positive finite width/enhancement Id; actual and scoring digits; ordered accepted commands; effect provenance; complete immutable Round Result. SYSTEMS §1 defines resolution order.

Jam/reference amounts are bounded at 10^12 and validated before a fight. Core rejects negative, non-integer, invalid max and overflow-prone data. Unity uses checked integer arithmetic and rational/fixed-point thousandths for future modifiers, floor once at the defined stage. Intermediate products need checked bounds as well as final results. No unbounded double promise. Terminal settlement is atomic; party zero wins loss precedence; later events are discarded. Presentation shows provisional strike values without draining Balance.

## 3. Content import and repository contract

`tuning/jam_tuning.csv` stores unique (section,key), numeric value, unit and note. Expressions/ranges/multiple target bodies are separate typed fields, not strings such as max (2;digit),2 x 1800 or 3-4. Rules contain pattern predicates; content contains parameters. The Python model reads CSV; the browser reference currently has explicit defaults validated by tests, **not a CSV importer**. A Unity editor importer is production work.

Importer gate: exact schema/version; required keys; finite numeric validation; integer/range/unit checks; duplicate/unknown-ID diagnostics; reference validation; generated asset hash; fail build on invalid content. Runtime reads validated assets only. Face lists and encounter graphs are structured records, not loose numeric CSV formulas.

When creating Unity project: track Assets and every.meta, Project Settings, Packages manifests/lock, editor version, build script and tests. Ignore Library/Temp/Logs/Obj/generated player builds. Keep source art outside runtime imports until accepted. Configure LFS deliberately for large source assets; never infer it exists from this document or rewrite jam history. Current branch is not assumed to be main; use actual configured remote/default.

## 4. Input, motion and replay

Use an authoritative monotonic gameplay clock; pause it on pause/focus loss. Latch the face actually displayed under the stop line at accepted input, then animate deceleration without changing the outcome. Record accepted face ID, actor/slot, displayed phase/tick, settings changes, tutorial overrides and command order. Input debounce does not change the selected face.

Replay header: rules/content version, build hash, encounter seed, PRNG name/version and named stream seeds. Gameplay wheel, proc and reward streams are separate; particles/audio consume visual RNG. The reference uses Mulberry 32-v 1 for initial wheel phase; Python uses its own seeded distribution model and does not claim identical RNG streams. Unity must pin its PRNG and exact accepted-command fixtures. A seed plus wall timestamps alone is insufficient.

Replay gate: re-run accepted commands across editor/Web, compare full Core state hashes and effect ledger. Validate focus loss, altered frame rates, assists, pause, retry and scripted tutorial exceptions. Export a local replay attachment through explicit user action; no jam telemetry upload.

## 5. Web targets and measurement

| Planning budget | Target | Evidence required |
|---|---|---|
|Compressed total |≤50 decimal MB |Hosted release response sizes/build report |
|Initial package |≤25 decimal MB |Cold network waterfall |
|Peak memory |≤512 Mi B |Named reference laptop/browser/resolution and measurement method |
|Desktop frame rate |60 fps target |Frame-time distribution, long frames and test route |
|Start→first action |≤20 s |After title Start, excludes cold download |
|Start→lucky choice |≤60 s |Authored opening route timestamp |

These are starting budgets, not achieved measurements. Name reference hardware before acceptance. Cold download/startup is measured separately with bandwidth/cache recorded; a 25 MB download cannot be promised instant. Mobile is best effort until independently measured; desktop Web GL 2 is jam priority. Reduce scope/assets before increasing budgets.

Use one selected release compression format with correct host Content-Encoding/MIME. If host headers cannot be controlled, test that format's Java Script decompression fallback. There is no automatic Brotli→Gzip alternate build. Unity documents the distinction in [Web deployment](https://docs.unity.com/en-us/engine/6000.5/manual/platform-specific/webgl/building-distribution/deploying).

Test the actual itch iframe. Safari iframe Indexed DB limitations require graceful save unavailability; a desktop standalone tab test is insufficient. [Unity browser compatibility](https://docs.unity.com/en-us/engine/6000.3/manual/platform-specific/webgl/intro/browsercompatibility).

Texture import choice depends on target GPU, alpha/quality and measured memory; do not prescribe Crunch indiscriminately. A 2048² RGBA texture is 16 Mi B before mipmaps. Use atlases, pooled effects, bounded particles, deliberate transparency and a small shader set. Profile Web allocations and load peaks; no “zero allocations” achievement is inferred from a spec.

## 6. Cinematic/audio contract

Required gameplay feedback is in engine and skippable/speedable. Video is optional: bundled on itch, URL-backed VideoPlayer, subtitles/speaker labels and an immediate still fallback on error/timeout. No critical event depends on a particular video frame; Web video is not frame-accurate and embedded VideoClips are unsupported. [Unity Web video](https://docs.unity.com/en-us/engine/6000.6/manual/platform-specific/webgl/develop/video).

Title gesture unlocks audio. Test mute, missing/blocked audio and background resume. Select Web-supported import/load settings through a measured clip/mixer pass, rather than promising desktop Vorbis streaming. Unity animation/audio presentation cannot decide combat results.

## 7. Saves and retries

Jam persistent schema: save Version/content Version, chosen resonance, encounter checkpoint 0/1/2, chosen Charm Id|null, settings, journal event IDs. No mid-fight save. A retry restores full checkpoint Balance, actor availability, named seed, zero Favour/jar and per-fight flags; selected reward remains one item. Encounter 2 restart never grants another reward. Write atomically with a recoverable last-good checkpoint; validate/repair or offer New Game when storage is malformed/unavailable. Settings can fall back to memory. Continue appears only for a validated compatible checkpoint.

Browser reference currently retries from volatile in-memory state and persists only mute; it does not claim this Unity save implementation. Full-game act snapshots, retained journals and idempotent rewards are ECONOMY_PROGRESSION §4.

## 8. Build, tests and release gates

1. Empty project→local Web→actual hosted iframe with logged Editor/module/licence result.
2. Core fixture suite and typed importer, then one greybox Audit.
3. Three-encounter required path plus actual story/settings/credits.
4. Fixed-input smoke, all ten digits, retries/storage failure, accessibility and browser checks.
5. Record build number/hash, source commit, content hash, size/performance evidence, unresolved issues.

Local build script first; CI is optional until licences/secrets and clean local build are verified. No paid CI or service is required. Private hosted builds need actual account access; no deployment has occurred in this documentation pass. After submission, preserve the exact artifact/tag/hash and obey jam judging update restrictions; root production/legal docs own release procedure.

## 9. Implementation gate status

Pure browser reference functions and corrected Python model have automated checks; Unity Core/importer/save/replay/presentation/build remain production work. Gate every future F-KIT/F-REEL/F-ECON family in SYSTEMS. Disable incomplete content in data/menus. “Done” requires reproducible artifact plus the appropriate tests and player/performance evidence, not this architecture document.
