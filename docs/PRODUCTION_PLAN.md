# ZERO-SUM: OMEN - Production Plan

> **8 November editorial revision:** [Resolved series bible](novel/RESOLVED_SERIES_BIBLE.md) supersedes conflicting older naming, origin wording, character backstories, political outcomes and story-length targets below. Gameplay formulas retain their existing domain authority. This source is being adapted to the49-chapter edition; its historical schedules and game scene numbering are not manga chapter numbering.

Updated7November2026 (IST). AI-only development, existing/free tools first, jam first then expansion. [DECISIONS.md](DECISIONS.md) resolves design conflicts, [JAM_SLICE.md](JAM_SLICE.md) owns scope, and [PROJECT_STATUS.md](PROJECT_STATUS.md) owns evidence. Production targets below are not achievements.

## 1. Production goal

Finish a coherent10-15minute Meridian Prologue. Prove responsive stopping, a legible pattern, a companion, one build choice and Varro's local story. The full campaign has NIL, eight core companions and three secrets (12 authored playable characters across campaign/postgame), a capital plus five lands and a return finale. Its release date must follow measured throughput; the previous12-15month forecast and dated2027/2028 promises are withdrawn.

AAA is a craft aspiration for selected scenes, not a certification or guaranteed production scale. Measure accepted content rather than generation counts. A finished scene includes correct rules, art in motion, sound, accessibility, persistence, performance and a player-observed learning path.

## 2. Jam schedule (IST)

| Date | Required exit artifact | Response if missed |
|---|---|---|
| 7Nov | Empty Unity Web build in intended itch embed; correct Core fixtures; one greybox Audit | Stop secondary systems; fix engine/rules before art scale-up |
| 8Nov | Baseline Prologue playable start-to-results in greybox; one approved game-frame style | Cut extra rigs/film/regions |
| 9Nov | NIL/Vesper/Varro/Debt Hound and Meridian in motion; boss and choice integrated | Keep all extensions out |
| 10Nov | Feature freeze: complete baseline systems, settings, skip, save fallback | Remove unintegrated optional work |
| 11Nov | Content lock, final required audio/art/text, full critical path | Only fixes afterward |
| 12Nov | Release candidate passes technical matrix and fresh-browser completion | Fix blockers; no content additions |
| 13Nov | Upload and submit; independently complete exact uploaded build | Reserve deadline buffer |
| 14Nov before17:30 | Buffer for submission/packaging failure | No feature work |

This replaces the previous Day1/Day2 labels and mixed UTC schedules. No private itch page, hosted build, signature or test result is assumed to exist. Community rating begins after submissions close; the three-game rating queue is not a13November task. Keep the submitted artifact immutable through judging; future work uses a separate development build. [Official jam overview](https://itch.io/jam/official-unity-game-jam-2026)

## 3. Responsibility and handoffs

| Role | Artifact owned | Acceptance handoff |
|---|---|---|
| Integration agent | Versioned project, content IDs, scene and build | One reproducible build command and logs; resolves cross-owner changes |
| Rules agent | Core, tuning import, fixtures, replay | Exact state/event fixtures; legal face and party validation |
| Narrative agent | Beat IDs, lines, prerequisites, skip/commit policies | Required information survives skip; flags/rewards idempotent |
| Art/animation agent | Reproducible sources, runtime exports, metadata | Canon locks, silhouette and motion captured in engine |
| Audio/UI agent | Exact cues, mix, accessible state labels | Muted/reduced-intensity path still communicates outcomes |
| Review agent | Diff inspection, automated checks, captured evidence | Finds defects against contracts; does not invent player approval |
| User | Direction, preference and spending decisions | Chooses results; no manual production finishing is required |

Every task names allowed files, decision IDs, inputs/outputs, validation and rollback. Independent agents may work concurrently; one integrator owns shared schemas/scenes. [TEAM_HANDBOOK.md](TEAM_HANDBOOK.md) defines the detailed contract.

## 4. Asset and technical pipeline

Use the installed Unity6000.4.11f1+Web module for the first viability test. Pin exact Editor/packages after the empty build works. No new Editor, paid package or generation service is a dependency. The reference HTML sandbox is not a portable campaign; port validated rules/fixtures, not its incidental UI or unsupported mechanics.

Free-first asset path: brief/canon references -> scripted Blender/SVG composition -> candidate image or procedural render -> AI-directed correction -> reproducible animation/export -> Unity composition -> validation/provenance. Use limited pose animation if rigs are unstable. Character text/digits and all gameplay timing remain in engine. Higgsfield/Meshy authenticated read access was checked7Nov; account access does not guarantee a request is free or its output licensed for a specific release. Never retry an uncertain paid submission blindly.

[ASSET_LIST.md](ASSET_LIST.md) owns exact rows/status; [ART_DIRECTION.md](ART_DIRECTION.md) owns style; [ARTBOOK_PRODUCTION.md](ARTBOOK_PRODUCTION.md) owns source/export flow; [AUDIO.md](AUDIO.md) owns cues; [TECH_DESIGN.md](TECH_DESIGN.md) owns the single budget/architecture table. A binary file's presence means candidate/reference, not accepted runtime content.

## 5. Expansion gates

| Gate | Scope unlocked | Required evidence |
|---|---|---|
| G0 | Single Unity Audit | Correct fixtures, responsive accepted face and Web boot |
| G1 | Meridian jam | Uploaded end-to-end completion, coherent presentation, release checks |
| G2 | Hyakki/Hina/Tamamo | Repeatable character/stage pipeline; party3, bonds, curse and illusion counters |
| G3 | River Empire | Economy/crafting/Ink and save migrations; legal build/fight simulation |
| G4 | Later acts | Canon/ending graph fixed; two accepted acts establish content cost |
| G5 | Finale/content complete | All required recruits and four endings reachable, including lucky0 |
| G6 | Commercial release | Platform/accessibility/localization/performance/rights evidence and truthful store captures |

Full-story hypothesis is315minutes critical path plus45-105minutes optional material (6-7hours). Postgame, custom mercenaries, mobile/consoles, leaderboards, Daily Omen and Far Lands are separately gated research/expansion work, not launch promises. Plan festival/launch dates only after checking actual eligibility/deadlines and build readiness.

## 6. Risk and correction policy

| Risk | Trigger | Action |
|---|---|---|
| Engine viability | Empty Web build fails | Resolve install/licence/module/host issue before content production |
| AI identity drift | Wrong prop count, handedness or rendering treatment | Edit from locked reference or simplify; reject failed output |
| Timing/correctness | Accepted face or score differs from trace | Fix rules/input contract; do not compensate with balance values |
| Cinematic waiting | Repeated effect delays meaningful input | Shorten/reuse/skippable presentation; preserve committed outcome |
| Content overload | Baseline gate missed | Cut optional region/hero/film; never move every gate toward deadline |
| Invalid cultural claim | Disputed attribution or no evidence | Source/qualify/simplify; do not claim native approval |
| Misleading completion | Checkbox lacks evidence | Revert to specified and attach actual verification task |

No production gate is passed by this document. The [audit report](DOC_AUDIT.md) records checks performed and remaining implementation work.
