# ZERO-SUM: OMEN — End-to-end refinement plan

**6 November 2026, IST · source commit `3d88239` · proposed decisions, not changes to existing canon.**

## 1. Direction

Build a premium, authored **2.5D party RPG about reclaiming agency over luck**, with short build-crafting encounters inside a persistent story. Keep the strongest existing ideas: NIL's missing number, the lucky-number choice, visible Omens, the Audit, Hap, the Ledger, and companions whose numerical relationships become team mechanics. Keep the art direction's **painted world, inked people**.

Use AAA craft as a quality target for responsiveness, staging, audiovisual coherence, character consistency and reliability. A broad AAA production scale is not established by the current repository or by access to AI generators. Prove a few excellent minutes, measure accepted-content throughput, and expand only when that process repeats. AI-only production remains an unproven constraint until a complete scene passes the same gates as ordinary production.

**User decisions:** jam first; existing/free tools first. AI writes code, scripts Blender/Unity, creates and processes assets, drafts and checks story, and runs technical validation. The user directs and selects results. External player feedback is evidence about play, rather than outsourced development. If no people play a build, label its fun, clarity and emotional impact unvalidated.

## 2. What actually exists

The source snapshot has **146 tracked files**, including **38 design Markdown documents**, one HTML/JavaScript combat sandbox, tuning CSV, PDF/art-generation tools, two PDFs, 22 raster images, 68 SVG graphics and two short videos. The inventory records every path and hash.

| Area | Observed state | Consequence |
|---|---|---|
| World and campaign | Detailed outlines, regional rules, cast, bond arcs, endings | Refine continuity and implementation flags before writing more lore |
| Combat | Endless-wave browser sandbox; prototype and simulator differ from intended rules | Establish one rules specification before the Unity port |
| Unity game | No Unity project, C# gameplay, scenes, prefabs or automated Unity tests in this checkout | First deliverable is a working Web build and one fight |
| Art | Identity kit, blockouts, concepts and short generated clips | Concepts are not complete layered, rigged, validated runtime assets |
| Production | Extensive plans and checklists; some stale team/tool/status assumptions | Replace assumed completion with build evidence |
| Local tools | Unity 6000.4.11f1 with Web module structurally verified; Blender 5.2.1 LTS executable verified | Test existing installations before installing more tools |

GitHub repository access is verified through the connector, and this workspace has the repository's `origin` remote. The local review branch does not imply changes have been pushed.

## 3. Decisions that should precede implementation

| ID | Current evidence | Proposed resolution | Verify with |
|---|---|---|---|
| D01 | GDD scoring and prototype damage application diverge | Resolve one round once; reserve base-strike visuals from actual damage until settlement, or apply only the remaining difference | Exact fixture totals for every pattern |
| D02 | Prototype digit buffs contradict the design's equal lucky-number promise | Remove unsupported digit-specific starting buffs; simulate all ten choices with legal wheels | Same-policy outcomes, then player testing |
| D03 | Pattern simulator can aim at absent faces and omits hero-specific runtime behavior | Make legal face data and resolution fixtures shared; separate probability sampling from timing-skill models | Fixture parity and replay checks |
| D04 | FTUE promises a tap within 20s, but jam script starts with ~37–45s of film; historical Higgsfield shot prompts total 95s | Start interactively in Rain Alley; reveal world myth after a demonstrated action | Cold-start stopwatch and onboarding study |
| D05 | Existing minimum slice still spans Meridian and Hyakki | Make the reliable target a complete Meridian Prologue; gate Hyakki behind a completed release candidate | Jam gate below |
| D06 | Human overpaint and manual asset processing appear in production/policy docs | Replace with AI-directed edits, scripted geometry/rendering/compositing, and rejection/regeneration | One finished actor in a real scene |
| D07 | Eight/eleven companions and nine/twelve total heroes appear in different documents | Name separate counts: eight core companions, three secret companions, NIL; specify unlock timing | Canon registry and content validator |
| D08 | An optional recruit can block the true ending; Hina age and Thale timeline conflict | Use the narrative report's explicit reconciliation proposals; expose recoverable prerequisites | Flag graph, all-ending traversal |
| D09 | Player digit 0 can be confused with Settled Omen 00 in the ending | Separate resonance digit, displayed Omen, Balance and identity in model and writing | Lucky-0 campaign path |
| D10 | GDD's act lengths, STORY's scene lengths and 6–8h campaign target differ | Budget the critical path in minutes and words; estimate optional content separately | Timed integrated act |

Do not resolve these independently in scripts, tuning sheets, PDF builders and source Markdown. Give each accepted rule a stable ID, one definition and fixtures. A contributor or agent should know which version a build implements.

## 4. Jam scope: a complete short game

**Proposed target: 10–15 minutes, Meridian Prologue.** This is narrower than the current `JAM_SLICE.md`; it is the recommended scope change for a repository with no Unity implementation yet.

| Keep in the first shipping target | Scope |
|---|---|
| Opening | Rain Alley interactive stop, Naming choice, REMAINDER DETECTED |
| Party | NIL and Vesper; three strikes with legal repeat/order selection for a two-person party |
| Encounters | One safe teaching fight, one build/defence test, Varro's Debt Jar boss |
| Choices | One charm choice with three clearly different effects; lucky number; striker order |
| Rules | Seven base patterns and priority, honest wheel faces, Pattern Sight, Favour, defence, Balance/Omen, one boss rule |
| Spectacle | One excellent Overwrite payoff, Vesper's entrance, Varro defeat, rooftop/map cliffhanger |
| Presentation | One coherent Meridian stage with lighting variants; limited pose animation; reusable motion graphics |
| Reliability | Settings, audio unlock, skip, replay/restart, safe save fallback, credits/disclosure |

Maeve, Hina/Hyakki, Tamamo, face crafting, Link Arts, multi-stem music and additional staged films are expansion candidates. **Do not add Hyakki unless the Prologue already runs on the uploaded Web build, has no critical-path blocker, passes readability/input checks, and has its final required art/audio by the end of 9 November IST.** If not, use a brief Hyakki image in the ending as a future promise. The default plan remains the Prologue.

The boss counter must remain possible after any scope cut. Varro's jar needs visible progress and a deterministic recovery path, including for lucky 0. Never depend on an optional hero, charm or undisclosed rule to finish a required encounter.

### Jam dates (all IST)

The official page lists a deadline of **14 November 2026, 12:00 UTC = 5:30 p.m. IST**. It requires a Unity game; WebGL is required for prize eligibility; generative AI use must be described on the submission page. Preserve the submitted game during voting/judging, with all runtime content packaged on itch. This review uses the public overview; it is not a complete prize-eligibility assessment. [Official jam page](https://itch.io/jam/official-unity-game-jam-2026)

| Date | Evidence required at end of day | Cut if absent |
|---|---|---|
| 7 Nov | Empty Web build works in itch embed; correct seven-pattern Core; one responsive greybox fight | All secondary systems |
| 8 Nov | Prologue start-to-finish greybox; first approved game-frame composition | New regions and long video pipeline |
| 9 Nov | One finished stage, NIL/Vesper/enemy readable in motion; Varro playable | Hyakki extension and extra party members |
| 10 Nov | Feature freeze; onboarding, charm choice and boss finish with audio/settings | Any unintegrated feature or cinematic |
| 11 Nov | Content lock; technical checks, save/restart, build-size and presentation sweep | Unfinished content; fix main path |
| 12 Nov | Release candidate; clean-browser/embedded-browser tests; credits and disclosure | All content additions |
| 13 Nov | Upload and submit; independently open the submitted itch build and finish it | No last-minute feature work |
| 14 Nov before 5:30 p.m. | Deadline buffer for packaging/upload failures | — |

These are work targets, not measured duration estimates. If 7 November's build gate fails, reduce content immediately; do not move all gates toward the deadline.

## 5. The player's first ten minutes

Suggested flow: title/audio/settings → protect Ama by stopping a wheel in ≤20 seconds from Start → choose lucky digit before minute 1 → Remainder detection before minute 3 → Vesper rescue → predict one pattern using visible information → parry a clearly signalled attack → choose a charm and see the effect → defeat Varro → quiet rooftop/map ending.

Teach one decision at a time. Script the tutorial outcome explicitly and label authored tutorials in data; normal wheels must follow the odds shown. Show the actual accepted face immediately after a stop. Keep vital digit and state labels in runtime UI rather than generated imagery. Make the ten lucky digits equally valid at Naming and explain that the choice is personal, not a hidden difficulty selection.

Repeated pattern cinematics should compress automatically after familiarity and support skip/fast playback. Hold a frame for a story turning point, not every score. The user should spend most of a fight choosing and acting, rather than waiting for animation.

## 6. Full game: depth through consequences

Keep the existing Prologue → five lands → Basilica structure. Before creating additional regions, make each current land change the player's decisions, the party's relationships, and the interpretation of the Ledger.

| Region | Core question to strengthen | Gameplay evidence | Lasting consequence to author |
|---|---|---|---|
| Meridian | Who owns a person's luck? | Debt, numbers as status, jars and enforcement | People saved or harmed recognize NIL later |
| Hyakki | What does a community owe its old things? | Curses, spirit relationships, Hina | An object/ritual returns with changed meaning |
| River Empire | What is inherited: wealth, obligation or memory? | Interest, taxation, living/dead ledgers | A debt decision affects later aid or trust |
| Śūnyapura | Is NIL absence, damage, or possibility? | Zero, place value, Karma, eclipse | Midpoint truth changes a usable verb and a relationship |
| Kroton Nova | Who gets excluded by a definition of perfection? | Prime/composite restriction and protection | Prima's choice materially changes who is protected |
| Crossroads | Can one choose freely when outcomes repeat? | Persistent knowledge across loops, Deals | Vesper/Fibi resolve a choice through action |
| Basilica | Is shared uncertainty better than imposed safety? | Fixed Fate removes familiar control; bonds restore agency | Ending expresses played choices, not a final quiz |

These are refinements to the fictional regions, not claims that a real culture shares one belief. Preserve variation within regions: dissenting residents, mundane lives, class differences, and people who do not follow a custom. AI research should cite regional/linguistic sources, record disagreements, and avoid claiming expert cultural validation.

For long buildup, maintain a **reveal ledger**: question → first clue → misleading interpretation → contradictory evidence → reveal → changed action → emotional aftermath → final payoff. Give every major reveal at least two earlier clues in different media, one companion response, and a mechanical consequence. The narrative report maps this to Hap, NIL, Thale and the Seals. Mandatory information must be available on the critical path; optional lore changes interpretation rather than providing the only missing explanation.

Do not lengthen the game by multiplying regions or terminology. Earn length with relationship reversals, recurring locations/NPCs that react to events, meaningful side quests, and consequences that return two acts later. Freeze the campaign's ending prerequisites before expanding its middle.

### Recruits, customization and synergies

Preserve eight authored core companions and three secret recruits as the current full-game roster. Track each recruit as: first encounter, reason to travel, playable unlock, teaching encounter, first bond, signature utility, return opportunity, finale participation. A recruit needs a new choice, not only new numbers or an illustration.

Use a guaranteed story catch-up for any core companion required by an ending. Secret recruits can remain optional and should offer hints and return routes; they should not silently lock the central story's resolution. Bond growth should follow authored decisions and encounters, with reserve-party catch-up so players can experiment.

Interpret **custom characters** initially as authored companions with selectable visual variants, wheel/build choices, titles where story-safe, and Awakening branches. Preserve NIL's identity/pronouns and the authored companions' canonical names. If player-created recruits are later desired, add a bounded, prebuilt archetype system after the authored roster works. Do not generate unbounded characters, arbitrary combat code or live story canon in the shipping runtime. Generated candidates become normal, validated offline content packs. NIL's identity reveal must remain authored.

Mathematical bonds need the same evidence as any build system: show the relationship, preview its effect, demonstrate it safely, then offer a counterpressure. Test every lucky digit against available companions at each act, not just the complete endgame roster. Define how zero, wilds, Fibi's changing digit, four/five-tube ultimates and overlapping bonds interact before authoring unique cinematics for them.

### Progression and economy

Separate permanent story/roster/bonds from act-start checkpoints and temporary build resources. Preserve the existing three-charms carry rule only if players understand what will be lost and confirm the transition. Make the keep/discard screen explicit before ending an act. Specify rollback behavior for XP, purchases, flags and currency to prevent duplication or accidental loss.

Build three simulated routes: minimal synergy, reasonable first-time build, strong synergy. Simulate legal rewards, shop offers, costs, combat and carryover across the full act. Report failure rate, rounds, currency and recovery options. Do not approve the exponential Balance curve from pattern frequencies alone. Prefer optional challenge for extreme engines; the mandatory story should have a recoverable path when an early reward is weak.

## 7. AI-only production with existing/free tools

| Tool | Primary job | Free-first operating rule |
|---|---|---|
| Git + GitHub | Versioned source, reviewable changes, provenance and releases | Separate agent ownership; one integrator; no binary history rewrite |
| Unity (installed) | Rules, staging, animation, UI, audio, builds | AI-authored C# and editor tooling; confirm Web build before new packages |
| Blender (installed) | Consistent cameras, blockouts, props, rigs, turntable renders and reusable scenes | AI-authored Python; retain `.blend`, script and export settings |
| Existing SVG/raster assets | UI identity, concepts and composition anchors | Scripted SVG work and non-destructive derived assets; validate source art before promotion |
| Existing image-generation access | Identity-locked revisions and style frames | Short, targeted edits; no dependency on free credits being available |
| Higgsfield | Optional image-to-video hero shots | Only after stills, shot timing and plan/credit access are verified |
| Meshy | Optional prop/geometry starting points | Not a requirement for the 2.5D jam; always inspect topology, UVs, rig and export |
| Scripted audio/compositing tools | SFX, loops, renders, encodes and metadata | No critical-path dependency on a paid music/voice service |
| Web research | Primary game/tool docs, references and fact checking | Save URL/date/claim; separate fact, interpretation and proposal |

Detailed vendor capabilities and local installation evidence are in [ART_AND_AI_PIPELINE](ART_AND_AI_PIPELINE.md). Documentation availability does not establish account access, free quotas, installed connectors or commercial clearance.

Asset workflow: **asset contract → canon references → deterministic composition/blockout → generation or procedural rendering → AI-directed correction → scripted layer/rig/export → runtime integration → visual and technical rejection gate → provenance record**. A failed hand, face, prop, digit or silhouette means reject/edit, not mark done. Never rely on a generated image/video to draw a required number correctly.

Use deterministic limited animation as the jam default: approved poses, anticipation/impact/recovery, motion paths, secondary movement and camera/VFX. Prefer an in-engine cutscene or animated still over a generated film that breaks identity or cannot be corrected reliably. A low-complexity consistent result serves this art direction better than increasing detail with each generator.

### Agent work contract

Each work item must include source rule IDs, allowed files, input/output IDs, acceptance checks and rollback. Agents can independently propose narrative, assets, code and validation, but one integrator owns the shared scene/data schema and resolves conflicts. A second pass reviews actual diffs and runtime results. An AI reviewer is a useful filter; it is not evidence of player enjoyment or cultural sign-off.

Every generation job needs an ID, prompt/reference hashes, model/tool, parameters, cost if known, source license note, output location, processing script and status. Poll an existing job after an uncertain submission; do not automatically pay for duplicate work. Keep secrets out of the repo and game build. Import finalized runtime files, not entire source-generation folders.

## 8. Define quality using evidence

The numbers below are **proposed acceptance targets**, not measured achievements.

| Dimension | Gate |
|---|---|
| Combat correctness | Priority and score fixtures pass; replay identical inputs produces identical state; no impossible faces |
| Responsiveness | Target ≤50ms stop-to-visible acknowledgement on named test hardware; accepted digit is unambiguous |
| Accessibility | Keyboard/pointer parity, slower timing option, reduced motion/flash, readable text, visible sound cues |
| Onboarding | First action ≤20s, choice ≤60s; aim for four of five fresh players to explain a pattern and defence unaided |
| Fight pacing | Start with 60–90s normal fights and 3–4min boss targets; retune after observed play |
| Art identity | Locked silhouette, handedness, palette and prop count; coherent character/background treatment in motion |
| Cinematics | Skip cannot alter outcomes; subtitles/speaker IDs correct; immediate input return and replay-safe completion |
| Web performance | Measure cold download/load and frame time on named hardware; stable desktop 60fps target, no accepted critical blockers |
| Release | Finish uploaded build from a fresh browser; restart/save fallback/credits/disclosure verified |

Do not treat the existing 250MB download/1.5GB heap ceilings as proof of quality. Measure realistic transfer conditions: even 40MB takes about 32 seconds at 10Mbps before startup overhead. Separate title-load time, download time and Start-to-first-action time. Keep the jam package much smaller by cutting long video and duplicate art before chasing rendering complexity.

## 9. Expansion after the jam

| Gate | Deliverable | Expansion allowed only after |
|---|---|---|
| G0 | Correct, responsive single fight on Web | Rules fixtures and actual input/render evidence |
| G1 | Complete Meridian jam game | Uploaded end-to-end playthrough and release checks |
| G2 | Hyakki production-quality act | Art pipeline repeats; party swaps/bonds and Tamamo work; measured content cost |
| G3 | River Empire systems demo | Legal build simulation, economy/crafting, data-driven content, save migrations |
| G4 | Full campaign production | Continuity and ending flags settled; two finished acts establish throughput |
| G5 | Content complete | All critical-path acts/companions/endings playable with final assets |
| G6 | Commercial candidate | Platform QA, accessibility, localization, performance, disclosure and store-ready captures |

Do not carry forward the old calendar as a promise. Forecast from accepted content per week, not generated candidates per hour. Track retries, integration time, defect rate and cost for one hero, one enemy, one stage, one boss and one story minute. Use those measurements to choose campaign length and release date. Reserve time for integration and corrections rather than allocating every week to new content.

Marketing should show what the build currently delivers: the stop, one intelligible synergy, and the party's emotional hook. The planned six-land/late-boss trailer belongs after those scenes exist. Keep jam builds frozen as required while future development proceeds separately. Treat consoles, mobile, online leaderboards and daily seeds as later projects with their own gates.

## 10. First implementation package

Take backlog items **J01–J08** as one dependency chain: reconcile rules → correct reference data/fixtures → create Unity project → prove an embedded Web build → implement deterministic combat → stage one fight → add skip/settings/save behavior → run repeatable technical and onboarding checks. Accept one finished game frame alongside the playable fight.

The next valuable result is **one correct, readable, satisfying Unity Audit that runs in the browser**, with NIL, Vesper and a Debt Hound. That result decides the scope of everything that follows.
