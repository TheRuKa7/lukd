# ZERO-SUM: OMEN - Jam Slice and Cut List

Updated 7 November 2026 (IST). Adopted scope under [DECISIONS.md](DECISIONS.md). **The Remainder: a 10-15 minute Meridian Prologue.** This replaces the older two-region jam scope. Nothing below is a claim of implemented content; see [PROJECT_STATUS.md](PROJECT_STATUS.md).

## 1. Required player journey

| Beat ID | Content | Target window from Start | Required evidence |
|---|---|---|---|
| JAM-01 | Title, audio unlock, settings; Rain Alley opens immediately | 0:00-0:10 | Keyboard/pointer Start, muted path and settings work |
| JAM-02 | Ama's Civic Omen01; stop reroutes six visible units from a confiscation jar to her07 | First action by0:20 | Transfer is visible; NIL does not create luck or erase the Collector's Omen |
| JAM-03 | Naming shrine: choose resonance0-9; REMAINDER DETECTED | Choice by1:00; reveal before3:00 | Zero is valid; choice is not presented as a difficulty selector |
| JAM-04 | One Debt Hound; NIL acts three times; safe scripted pattern teaching and one defence | About1:00-3:00 | Tutorial exceptions explicit; legal normal wheels resume afterward |
| JAM-05 | Vesper rescue and recruit | About3:00-4:00 | Recruited flag commits once; entrance remains understandable muted/skipped |
| JAM-06 | One Debt Hound; two heroes, one acts twice; Pattern Sight | About4:00-6:00 | Both heroes used; third-digit opportunities and accepted stop are clear |
| JAM-07 | Gus offers Horseshoe, Black Cat, Ofuda; choose one free | About6:00-7:00 | One grant only; descriptions match exact effect; no shop/fen prerequisite |
| JAM-08 | Varro, Debt Jar, telegraphed phase change | About7:00-11:00 | Boss counter works for all ten digits and every charm choice |
| JAM-09 | Mercy, Livia thread, Seal1, quiet rooftop/map reveal | About11:00-13:00 | Varro survives defeat; local arc resolves; future lands are a teaser |
| JAM-10 | Results, credits/disclosure, replay/new number | Total10-15min target | Biggest score, patterns and time; restart clears transient effects |

Windows are pacing hypotheses; do not speed-read story to force a stopwatch result. The detailed line/event/skip contract is [JAM_SCRIPT.md](JAM_SCRIPT.md), and teaching details are in [FIRST_10_MINUTES.md](FIRST_10_MINUTES.md). The full campaign Prologue remains a separate35-minute budget in STORY.

## 2. Required systems and content

| Type | Required for this build | Excluded from baseline |
|---|---|---|
| Heroes | NIL, Vesper | Maeve, Hina and all later recruits |
| Encounters | Debt Hound solo tutorial; Debt Hound two-hero test; Varro | Collectors, additional packs, Tamamo, keeper trials |
| Combat | Three strikes, legal hero quotas/faces, seven base patterns/priority, one settlement, Pattern Sight, visible Favour repair, defence, Balance/Audit Omen, Debt Land Law, Varro jar | Extended reels, wildcard heroes, gem/Deal/Karma systems |
| Builds | Free choice of one of three charms below | Fen, shops, rerolls, crafting, sets and progression tree |
| Presentation | Exact runtime digits, stop/hit/settlement effects, reusable Overwrite payoff, limited pose animation | Required generated film, ultimate gauge, Link Arts, full narrative-bond menu |
| Story | Rescue, Naming, Vesper, Varro mercy, rooftop | Mandatory mythology montage, Hap Dream, Hyakki gameplay |
| Assets | NIL/Vesper/Varro/Debt Hound poses, one empty Meridian plate plus variants, Nixie reel, three charm icons, UI/VFX/audio | A mandatory PSB rig, six-layer stage or new 3D service |
| Reliability | Assist, reduced motion, text/subtitles, audio settings, pause/skip/retry, node checkpoint and storage fallback, credits | Network telemetry, live content or online services |

### The three charm contracts

- `charm_horseshoe`: chosen resonance faces on allied wheels are1.5 times their normal width, when the face exists; it cannot add an absent face.
- `charm_black_cat`: first would-be Bust per fight visibly replaces scoring slot3 with slot1 and re-evaluates normal priority once. It shares the nonrecursive conversion pipeline with Favour.
- `charm_ofuda`: first enemy strike is automatically Parried, no accepted stop and no reflected damage; it counts once toward Varro's defence counter.

[SYSTEMS.md](SYSTEMS.md) defines effect order and actual-versus-resolved digits. [BESTIARY.md](BESTIARY.md) defines the jar and phase telegraphs. A Vesper finishing shot may reference Seven-Chamber Requiem visually; it must not teach or require an absent ultimate system.

## 3. Expansion gate and cut rules

The baseline is already the minimum complete game: tutorial, recruit, meaningful choice, boss, resolution and replay. Simplify animation, stage variants and optional dialogue if needed; do not cut the mechanic explanation or boss recovery.

Maeve or Hyakki may enter only if the entire baseline is already hosted, has final required presentation, passes technical checks, and fresh players understand it by end of9November IST. Otherwise they remain future content. An extension must also have a complete script, asset/data contracts, tests, save/skip behavior and time for regression; a single attractive frame is not enough. No additions after feature freeze10November. Content lock end11November; verify12November; submit13November.

## 4. Release acceptance

Every lucky digit and every jam charm choice can finish Varro; no optional character is required. Skip/pause/retry do not duplicate rewards or omit recruit/Seal flags. Audio is not required to read a cue. The uploaded itch build is completed from a fresh browser and its exact hash/version is recorded. Technical targets and browser matrix live only in [TECH_DESIGN.md](TECH_DESIGN.md); passing a desktop prototype check does not certify Unity/Web.

Hard deadline:14November2026 at17:30IST (12:00UTC). Unity is required and WebGL is required for prize eligibility; AI use must be described. The project targets WebGL. [Official jam overview](https://itch.io/jam/official-unity-game-jam-2026)
