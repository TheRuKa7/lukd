# Engineering, gameplay and delivery audit

> **HISTORICAL SNAPSHOT - 6 November 2026, baseline `3d88239`.** Findings/proposals describe that snapshot, not the current corrected repository. See [adopted decisions](../DECISIONS.md), [current status](../PROJECT_STATUS.md) and [audit resolutions](../DOC_AUDIT.md).
Date: 6 November 2026 (India). Source snapshot: `3d88239dff58db1d313b8d979d6ae98a8f1ceed0` of `TheRuKa7/lukd`. This report adds proposals; it does not amend the existing canon, scope or rules. “Observed” means present in the reviewed source or reproduced with the checks below. “Proposed” means a decision still to adopt. No Unity build or human playtest was performed for this audit.

## 1. What is actually implemented

The repository is a design and art preproduction repository with one browser combat sandbox. It is not yet a Unity game project. There are no tracked C# files, Unity scenes, assemblies, `ProjectSettings`, `Packages/manifest.json`, test assemblies or CI workflows. There is no evidence here of a shipped Web build, a tuning importer, working campaign save or playable recruitment progression.

| Area | Observed implementation | Practical consequence |
|---|---|---|
| Combat | One self-contained `prototype/index.html`: digit choice, three hero picks, scrolling weighted wheels, seven base pattern classifications, attack effects, synthetic audio, enemy defence, charm offers | Useful to evaluate presentation and the stop verb; unsuitable as an authoritative rules reference until drift below is fixed |
| Structure | Four enemy templates followed by exponentially growing Basilica waves; NIL, Vesper and a Maeve-labelled third hero start together (`prototype/index.html:261`, `:286`, `:737`) | Prologue, Varro, Hina, Hyakki, act maps and story onboarding exist in documents, not this executable |
| Persistence | Browser local storage for mute and best wave | No campaign checkpoint, party roster, unlocks or versioned save |
| Accessibility | OS reduced-motion preference suppresses several effects; keyboard combat actions exist | Hold-to-stop, explicit settings, text scaling, pause, assists and a full keyboard menu path remain unimplemented |
| Tuning | 51 CSV rows and a Python odds simulator | Neither prototype nor a Unity game consumes this CSV |
| Books and artwork | Python generators for bible/artbook HTML, shared canon helpers and SVG figures/graphics; Chromium PDF renderer | Useful authoring infrastructure, separate from runtime |
| Build tools | No dependency lockfiles or project build automation | Reproducing tool output depends on packages/tools installed outside this checkout |

The `.gitignore` contains only `build/` and `__pycache__/`. Before adding Unity, add the standard Unity exclusions while preserving `Assets` and all `.meta` files, package manifests/locks and project settings. `TECH_DESIGN.md` promises LFS, but no `.gitattributes` is tracked. Configure LFS for future source assets deliberately; do not rewrite existing history during the jam.

### Local tools observed

Read-only CLI discovery found Unity CLI at `C:\Users\rushi\AppData\Local\Unity\bin\unity.exe`. `unity editors --installed --format json` reports Unity `6000.4.11f1` with its Web module and `2022.3.62f3`. `unity editors verify 6000.4.11f1 --format json` passed structural checks including Web. These checks do not establish an active licence or successful project build. `unity status` found no connected Editor with the Pipeline package. Blender was found at `C:\Program Files\Blender Foundation\Blender 5.2\blender.exe`; it was not launched. Python and Node are on PATH. Start the next implementation pass with the installed Unity 6000.4.11f1 and its Web module; verify an empty build before considering an Editor installation or change.

## 2. Confirmed defects and design conflicts

### P0: one damage equation must govern the whole round

`GDD.md` §1.2 defines total round damage as sum of strikes × Mult. The prototype subtracts every strike immediately (`prototype/index.html:584`), then adds another full `roundDamage × mult` for Jackpot/Overwrite (`:498`–`:504`). Cascade and Zero-Sum apply no multiplier damage (`:512`–`:522`). Reaper applies no ×4 pattern damage (`:506`–`:511`). Pair correctly adds one extra base total for an effective ×2 (`:523`–`:525`).

A Node harness extracted the existing `evaluate` and `resolveReel` functions with animation/audio/DOM stubs. It accounted for the base strikes already applied; these were the outputs with NIL digit 7, no charms and level-one illustrative strike bases:

| Reel | Declared base Mult | Effective prototype Mult | Notes |
|---|---:|---:|---|
| 7-7-7 | 21 | 22 | 51 base damage plus 1,071 additional damage |
| 3-3-3 | 3 | 4 | 39 plus 117 |
| 1-2-3 | 3 | 1 | Extra round occurs; ×3 payout does not |
| 3-3-4 | 2 | 1 | Enemy action cancelled and party healed; ×2 payout does not |
| 7-1-7 | 2 | 2 | Correct for ordinary Pair |
| 4-4-4 | 4 | 1 | Test Omens contained no 4, so no percentage loss applied |
| 2-9-5 | 1 | 1 | Correct |

**Proposed resolution:** Core produces a single immutable round result with strike values, pattern, modifier trace, final damage and secondary events. Presentation may show provisional strike numbers, but damage settlement follows one explicit policy. If strikes truly drain Balance immediately, apply only the remaining bonus at resolution; otherwise settle the whole amount once. Specify whether death can end a round before all three digits resolve. Currently the prototype breaks early at `:616`, so low-health enemies can prevent the very reel payoff the game is selling.

### P0: the simulator is not yet a runtime specification

The published base odds reproduce at 60,000 rounds per cell, but reproduction validates this model, not the intended game.

* **Per-hero face lists are ignored.** `tools/sim_patterns.py:62`–`:72` supplies the same face set to every hero. Its eight-face setup at `:90` omits 4 and 9 for everyone, whereas `SYSTEMS.md` §2.1 gives different omissions to NIL, Maeve and Hina.
* **Impossible aimed stops occur.** `stop()` returns the aimed digit without checking a positive weight (`:39`–`:42`). Reproduced: weights with no 9, aim 9, skill 1 returns 9. `run()` falls back to the hero digit, which can itself be absent (`:70`–`:71`); the mixed Hina scenario is affected. `fight_streaks()` does not check aim membership at all.
* **Descending Cascade aim is wrong.** `closer_aim([8,7],7)` returns 9, producing 8-7-9, a Bust; 6 would complete 8-7-6. The absolute-difference branch at `:57`–`:58` generally assumes ascending order.
* **The skill model is an assumption.** A 25% independent aim success and warm-state +10 percentage points are not measured player timing data. Widths imply time exposure only under a specified motion/tap model; a skilled timing game is not an ordinary random draw.
* **Hap's Hand changes only the classification.** `:115`–`:116` relabels a Bust as Pair without producing the altered reel digits. That is adequate for a rough frequency estimate, inadequate for a damage, passive, charge or replay reference.
* **The reference sim omits the game that must be balanced:** damage, defence, party sizes one/two, hero order, charms, Land Laws, bosses, deaths, progression and unlock cadence.

**Proposed resolution:** make content data and rule cases authoritative. Exhaustively enumerate the small base pattern domain, compare exact Python/C# outcomes on identical fixture inputs, and use a full fight simulator for balance. Statistical rates can be a secondary check with named seeds, uncertainty and model assumptions. A 0.5 percentage-point Monte Carlo tolerance must not substitute for exact outcome parity.

### P0: prototype and documents describe different games

| Evidence | Conflict | Proposed disposition |
|---|---|---|
| `prototype/index.html:571` | All heroes still have ten faces | Port explicit per-hero eight-face content; settle NIL omission rule first |
| `SYSTEMS.md` §2.1 | “Two digits farthest” from NIL 7 gives example 2 and 1, with no distance/tie metric | Store explicit validated lists for all ten choices; specify linear/circular distance if procedural |
| Prototype has no Pattern Sight or Favour state | Both are Must in `JAM_SLICE.md` §2 and drive tuning claims | Implement before using the published balance targets |
| `prototype/index.html:451`, `:524`, `:571`, `:634`, `:712`, `:750` | Chosen digit gives extra buffs: 6 unordered runs, 2 stronger Pairs, 1 slower wheels, 5 wider parry, 8 extra shop offer, 9 healing | Remove unless deliberately specified and tested. Equal ×21 Overwrite alone does not imply equal starter difficulty |
| `prototype/index.html:509`, `:511` | Reaper removes 44% of maximum Balance; prose says 44% of Balance | Specify current/max basis and snapshot timing for both targets before implementing |
| `prototype/index.html:749`–`:755` | Enemy death is checked before party death; Reaper party death can be followed by an enemy turn | Define simultaneous defeat and stop resolution immediately after terminal events |
| Prototype `CHARMS` and hero stats | Eight sandbox charms and hardcoded base values differ from jam lists/CSV | Mark sandbox content as experimental; runtime uses validated definitions |
| `TUNING.md` introduction | Claims Unity imports every value and no magic numbers | Importer/runtime do not exist; change status language when canonical docs are next edited |

### P1: progression and synergy need executable definitions

1. **Mandatory NIL makes some examples illegal.** `GDD.md` §2 says NIL plus two companions, but the Prime Party example is Prima + Maeve + Vesper, and Powers of Two is Prima + Bai Si + Ba. Define legal examples such as NIL 7 + Prima 2 + Maeve 3, or NIL 2 + Bai Si 4 + Ba 8. Decide whether off-party characters can ever contribute; do not silently implement four combatants.
2. **Zero's Complement is undefined.** `GDD.md` §2.3 says sum to 10, but §2.4's partner claim includes 0↔Shunya. 0+0 is not 10. Proposed: explicitly give zero a separate bond, or adopt sum ≡ 0 mod 10 and explain it. Do not change the mathematical rule only in the implementation.
3. **Shunya bond-wild behaviour is granted twice.** GDD §2.3 grants zero wild for every bond immediately; `SYSTEMS.md` §5 gives that as an Awakening. Choose base pattern-wild first, bond-wild later if progression is desired.
4. **Several progression rewards repeat baseline functionality.** Favour already warms after one Bust (`SYSTEMS.md` §2.4), yet Cat's Eye level two (§3) and NIL's Open Hand Awakening (§5) promise warming after one Bust. Specify an actual upgrade such as starting a fight warm, not an inert reward.
5. **Four/five-tube patterns lack complete semantics.** `SYSTEMS.md` §2.2 lists a few payouts, but no priority relative to Overwrite/Reaper/Prime Trio, no wildcard tie-break, and no handling for every non-matching extended reel. Keep these out of the first build until fixtures cover them.
6. **Character effects need a shared timing vocabulary.** Vesper's “each 7 adds +7 to every strike,” Maeve doubling the third strike and Hina's +9 Mult must state when earlier strikes are recalculated, how often they trigger, and what counts as a landed digit. Hina's condition Omen ≤99 is always true for a living combatant; her +9 per 9 can dominate the tuning assumptions. Treat this as a simulation priority, not proof of a measured imbalance.
7. **Unlock counts disagree.** GDD still says eight companions and ~90 charms; Systems lists eight core companions plus three secret (11 total) and 63 charms. Some combination counts still use eight. Maintain a generated content manifest of IDs, availability, scope and status.
8. **Act carryover conflicts.** `ECONOMY_PROGRESSION.md` §1 labels charms/faces/gems “per act,” while §4 keeps enhancements and three charms; gems' fate is unstated. Define exactly what is kept, stashed, lost and restored on defeat. Prefer a persistent inventory with three equipped ferry keeps if avoiding perceived loss is the goal, subject to balance.
9. **Economy example is arithmetically false.** `TUNING.md` §5 says 45 fen affords one rare charm OR two enhancements, never both; the same paragraph prices them at 12 and 8. Both cost 28, below 45. Fix the intended budget or prices after an explicit node economy simulation.
10. **Campaign duration does not add up.** `GDD.md:193` says acts are 25–35 minutes and campaign is 6–8 hours. Seven segments of that size are about 2.9–4.1 hours before optional scenes. Specify a measured critical path and separately count bonds, quests and exploration. `ECONOMY_PROGRESSION.md` §6's “something new every ~15 minutes” also needs an encounter-by-encounter teaching plan.
11. **Loop and retrigger guarantees need bounded rules.** Unlimited Cascade turns, Powers of Two chaining, Favour rerolls and charm-trigger loops need per-event/per-round limits. Four minimum faces does not guarantee fair timing or prevent deterministic optimal play; validate actual accessible wheel configurations.
12. **Display hacks can break world rules.** Deals capping only Omen display at 77 and Link Art forcing 01 must say whether Balance/max Balance changes or this is an illusion. Omen-reading effects otherwise receive contradictory inputs.

## 3. Recommended first Unity implementation

This is a proposal designed for the user's existing-tools-first, Unity-jam-first preference. Retain the broad campaign as the future target; obtain proof with a small Prologue.

### Scope to prove first

**10–15-minute Prologue:** Naming, NIL solo teaching, Vesper recruitment, one meaningful charm decision, Varro with a clear Debt Jar counter, Seal/world-map payoff, results and replay. Two playable heroes; one or two reusable Meridian stages. All seven base classifiers can exist in Core even if rare patterns are not forced into the tutorial. Splice is retained only if it improves first-minute clarity within the stop verb; otherwise explicitly propose an onboarding simplification before changing canon.

The existing `JAM_SLICE.md` calls two regions and ~18 minutes its “minimum lovable” version. The smaller Prologue here is a **new scope proposal**, not an assertion that it is already approved canon. Hyakki, Hina, party-of-three bonds and Tamamo are an extension gate: add them only after the complete Prologue runs from start to results in the hosted Web build, tests pass, art is coherent and observed first-time players understand the loop. Do not spend the first days generating five future regions.

### Architecture

Retain the useful separation in `TECH_DESIGN.md`; make it smaller and testable:

* **Core:** plain C# definitions, wheel state, digit/pattern evaluation, effect ordering, round result, party Balance, boss state and seeded random streams. No Unity clock, renderer or asset lookup.
* **Content:** stable IDs and validated typed definitions. CSV for numeric scalars only; explicit face lists and effect definitions in structured content. Import at edit time, fail with row/ID diagnostics. Expressions such as `max(2;digit)`, `2x1800` and `3-4` are currently mixed into CSV values; do not invent an unbounded runtime expression evaluator.
* **Flow:** small encounter/round state machine, owns transitions, terminal-state policy, pause and skip. Integrate a single sequencing approach first; UniTask, Timeline and tweens should not each independently own combat timing.
* **Presentation:** reads emitted events, never rolls a gameplay die or computes damage. UI, sprite rigs, VFX, camera and audio can be replaced without changing outcomes.
* **Persistence:** versioned save DTO containing content/rules version, lucky digit, unlocked/active party, node checkpoint, inventory and settings. Validate and recover cleanly from malformed or unavailable storage. Keep an act-start snapshot if defeat rewinds progress.

Avoid record syntax/library assumptions until a project compiles under the selected Unity runtime. Pin the exact Editor patch and package lock once the smoke build works. The initial project needs no networking, runtime LLMs, content service, multiplayer, ECS or bespoke graph editor.

### Stop timing and determinism contract

A seed plus wall-clock timestamps is insufficient unless the phase integration, input sampling and random draws are also fixed. The current wheel integrates clamped frame deltas and samples a frame-cached position (`prototype/index.html:393`–`:408`), so stalls affect the relationship between tap time and shown face.

Proposed contract:

1. Store explicit face IDs, digit, width and enhancement; require positive finite widths and at least one accessible face.
2. Use a defined monotonic game clock and analytical phase or fixed ticks. At input, latch the same face highlighted under the stop line. Deceleration is presentation; it must not change the latched answer.
3. Record command order, encounter seed, selected actor, phase/tick and accepted face ID. Pauses, focus loss and accessibility speed changes must be recorded events. Replays can validate face selection and always reproduce resolved results.
4. Hina reversals, proc chances, reward offers and visual effects use separate named RNG streams. Changing particle count must not change a future charm or wheel.
5. Version the PRNG and rules. Exact fixtures compare events and state hashes across editor and Web builds.
6. Specify effect order: face conversion → digit changes → pattern/wild resolution → strike flat bonuses → additive Mult → multiplicative Mult → armour/target modifiers → rounding → damage and secondary events → terminal-state check. This ordering is proposed, and must be reconciled with existing hero language before it becomes canon.
7. Define numeric bounds. `long` prevents ordinary `int` overflow but not unbounded stacking; `double` plus unspecified rounding weakens exact replay guarantees. Use bounded integer/fixed-point or rational modifiers with explicit rounding and checked intermediate arithmetic. Test maxima and fail safely before overflow.

### Web build choices

Use the installed Editor and generate an empty hosted Web build before choosing additional packages. Keep WebGL 2 as the jam path. The manual currently lists desktop and some mobile support, but browser support is not a promise that this game meets its performance targets. Safari iframe IndexedDB limitations require an actual itch-embedded save test, plus graceful no-storage fallback. [Unity browser compatibility](https://docs.unity.com/en-us/engine/6000.3/manual/platform-specific/webgl/intro/browsercompatibility).

Keep cinematics optional to gameplay progression. Use bundled URL-backed `VideoPlayer` content with subtitles and a still fallback; Unity Web does not support embedded `VideoClip` playback or frame-accurate video. Do not tie accepted inputs or boss windows to a particular video frame. [Unity Web video](https://docs.unity.com/en-us/engine/6000.6/manual/platform-specific/webgl/develop/video).

Replace “Brotli with Gzip fallback” with a tested deployment configuration: choose one build compression format and verify actual host headers. Unity decompression fallback adds the corresponding JavaScript decoder; it is not a second gzip build automatically selected by the browser. [Unity Web deployment](https://docs.unity.com/en-us/engine/6000.5/manual/platform-specific/webgl/building-distribution/deploying).

The current 250 MB download and 1.5 GB heap values are ceilings in a spec, not measured results. Proposed Prologue starting budgets are ≤50 MB compressed total, ≤25 MB to first interaction, and ≤512 MB measured peak Web memory on the chosen reference laptop. Validate these against actual build overhead; adjust scope rather than asserting they are already achieved. Record build size, cold-load conditions, resolution, browser, GPU, frame-time percentiles and peak memory. Profile target formats rather than choosing Crunch indiscriminately; a 2048² uncompressed RGBA texture alone uses 16 MiB before mipmaps. Bundle later-act assets with the submission when they are eventually added; do not depend on mutable remote game content for the jam.

## 4. Prioritized backlog and acceptance evidence

| Order | Deliverable | Observable acceptance |
|---|---|---|
| 1 | Existing Editor viability | Empty project compiles and Web build opens on intended host; Editor/package versions recorded |
| 2 | Core rules and canonical fixtures | All seven priorities, 10 lucky digits, Omen bounds, weighted-face validation, Favour repair, damage totals and terminal states pass exact cases |
| 3 | One greybox Audit | Boot → choose digit → complete three strikes → enemy defence → settle/retry; mouse and keyboard; no art dependency |
| 4 | Honest timing and feedback | Stop accepts one input, highlights actual latched face; no lost/duplicate input; speed/pause/focus changes safe; reduced-motion readable |
| 5 | Prologue learning path | NIL solo, Vesper joins, order choice, Varro telegraph; fresh testers can explain stop, pattern and parry without help |
| 6 | Data and charm choice | Two or three thoroughly implemented charm effects, clear offers and deterministic retries; expand to 12 only after full-loop proof |
| 7 | Cohesive presentation | One approved combat frame, both heroes and Varro at gameplay scale; complete sound/animation loop; skip controls |
| 8 | Save/settings/release | Node checkpoint, storage failure handling, build number, credits/disclosure; all ten digits reach results |
| 9 | Optional Hyakki extension | Only starts after orders 1–8 are green with time for a complete regression pass; explicit cut gate |
| 10 | Campaign production | Build one new region and one recruit at a time using reusable tooling; measure actual cost before promising five more |

The future backlog adds party-of-three synergies, bond state, region rules, wheel crafting, balancing tools, quests, unlock persistence, localization, expanded cutscenes, optional custom recruits and postgame in that order of dependency. A custom recruit should use a bounded authored template with approved art/kit/voice fields and a save-safe ID. Avoid arbitrary generated mechanics or lore at runtime. Recruitment events must define first availability, requirements, recovery from missed opportunities, combat function, bond entry point and save migration.

For full-game balance, simulate each act with legal parties across all ten NIL choices, weak and strong builds, timing-skill distributions and assists. Report win rate, rounds, defence burden, runaway loops, charm offer dead ends and spending choices. Then compare against observed play. The exponential Balance curve is a hypothesis until that model exists.

## 5. AI-only development workflow

Interpret the constraint as AI producing code, design drafts, art edits and tool automation, with the user directing choices and running/assessing the result. Generated work must still pass the same evidence gates. This does not require paid tools: use the installed Unity/Blender, repository tools, local scripts and existing credits first. Do not introduce a subscription as a dependency of the first playable.

Each task should state: current source commit; allowed files; relevant canon sections; one measurable player behaviour; acceptance fixtures or visual examples; expected build artefact; and what can be cut. Assign concurrent agents independent owned files, then integrate through a single build owner. No agent marks its own feature done merely because code compiles.

The cycle is: small specification → implementation → compiler/tests → AI code review against behaviour and fixtures → Web smoke → captured evidence → user play assessment → integrate. Maintain a decision log and asset manifest. Freeze canonical IDs and character reference sheets before mass generation. Save the prompt, source/reference assets, tool/version, output ID, licence evidence and revisions for every generated asset. Code, assets, scene setup and import settings must be reproducible from the repository, not hidden in a particular agent's conversation.

Keep all runtime gameplay local and deterministic for the jam. AI can draft test scenarios, automate browser input, inspect frames and suggest fixes; it cannot supply evidence that real players find the game enjoyable, that a cultural depiction has community approval, or that photosensitivity requirements were clinically validated. Record those statuses honestly. The existing playtest and cultural-review requirements remain outstanding until evidence exists or the project owner explicitly revises them.

## 6. Tests and checks actually performed

* `python tools/sim_patterns.py 60000`: completed, 36 scenarios ×60,000 rounds (2.16 million simulated rounds). The documented jam party averages reproduce: 57.3% Bust for ten-face own-digit aims, 44.5% with smart third aim, 41.1% with common eight-face smart aim. These are the current model's outputs, subject to its defects.
* `python tools/sim_patterns.py --favour`: completed with default seeds/settings. Average skill 0.25 reports 24.5%→0% fights with a 3+ Bust streak and 39.7%→34.5% Bust rounds. Again, this models classification protection, not an implemented game guarantee.
* Python AST parsing: all six Python source tools parsed successfully. This does not test their dependencies, outputs or layouts.
* Pattern-domain check: all 10,000 combinations of three digits and chosen lucky digit returned a recognized classification without exception. Triple priority checks produced Overwrite for lucky 4 on 4-4-4 and Reaper for lucky 7 on 4-4-4. This is limited sanity coverage, not exhaustive specification validation.
* Adversarial simulator probes reproduced descending aim and absent-face defects described above.
* Node `new Function` parse of the prototype script passed. A separate extracted-function harness reproduced the damage table. The harness stubbed effects and DOM; it did not launch the browser, measure frame latency, verify sound or prove touch accessibility.
* CSV parse: 51 data rows, no duplicate `(section,key)` pairs. Typed value validation remains unimplemented.
* Unity installed-version discovery and structural verification completed as described in §1. No editor project was created, no game ran, and no Unity tests or Web build were executed.

### Tooling maintenance findings

`tools/build_bible.py:31` and `:42` reuse image/video caches based only on existence, so regenerated source artwork can leave stale book images. Artbook's image cache checks source modification time (`tools/build_artbook.py:36`), but neither cache includes rendering parameters. Use content hashes plus transform settings when this tooling is next changed. Both generators depend on remote font CSS; pin/bundle fonts for reproducible offline output.

`tools/render_pdf.js` assumes Playwright/Chromium; bible generation also needs Python Markdown, Pillow and ffmpeg. No dependency lockfile or bootstrap script exists. Do not run the generators merely to test this audit: they overwrite tracked PDFs. Add a non-mutating validation/temporary output mode in a future tooling task.

The book data is only partly sourced from Markdown: `tools/canon.py` hardcodes character locks/palettes/land facts. `tools/build_artbook.py:378` still describes “HUMAN OVERPAINT,” which conflicts with the user's new AI-only production constraint; preserve the quality-check intent while replacing the production role in a later canonical edit. Mirrored front silhouettes are labelled as back silhouettes (`tools/build_artbook.py:175`); these cannot serve as real turnaround reference or prove asymmetric canon details.

## 7. Read scope

Read in this audit: `prototype/index.html`; all nine files in `tools/` (`artbook.css`, `bible.css`, `build_artbook.py`, `build_bible.py`, `canon.py`, `figures.py`, `graphics.py`, `render_pdf.js`, `sim_patterns.py`); `tuning/jam_tuning.csv`; `.gitignore`; and docs `GDD`, `SYSTEMS`, `TUNING`, `TECH_DESIGN`, `ECONOMY_PROGRESSION`, `GAME_FEEL`, `UX_SPEC`, `ACCESSIBILITY`, `LOCALISATION`, `TELEMETRY`, `QA_TEST_PLAN`, `PLAYTEST`, `QUALITY_BAR`, `JAM_SLICE`. Narrative and asset/art review are covered by the companion refinement reports. Tracked PDFs were not rendered by this engineering pass. All citations and implementation observations refer to the reviewed snapshot, not an asserted deployed game.
