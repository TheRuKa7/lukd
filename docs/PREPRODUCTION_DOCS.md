# ZERO-SUM: OMEN — Pre-Production Document List

What has to be written **before** we build, so that what we build is fun, polished and loved, and what we can leave until later. Read with [`PRODUCTION_PLAN.md`](PRODUCTION_PLAN.md) and [`GDD.md`](GDD.md).

---

## 0. The honest rule first

Documents don't make a game fun. **Playtests make a game fun.** Balatro, Hades and Into the Breach were found by playing builds every day, not by writing. So pre-production docs have one job: **make sure every hour of building goes into the right thing, with a clear bar for "good enough"**, and leave room to discover the fun in the prototype.

That means:
1. **Lean.** Each doc is the shortest thing that answers its questions. A table beats a page; a GIF beats a paragraph.
2. **Testable.** Every doc ends with a "done when" check someone can verify.
3. **Gated.** Only the **Gate A** docs block the jam build. Everything in Gate B can wait until after the jam, when we know what players loved.
4. **Living.** The Markdown files in `docs/` stay the source of truth; the bible and art book rebuild from them.

The jam deadline is **Sat 14 Nov 2026, 12:00 UTC**. Gate A has to be finished by the end of **Sat 7 Nov** (Day 2) at the latest, or it costs build time we don't have.

---

## 1. What we already have

| Doc | Status | Gap that still matters |
|---|---|---|
| [GDD](GDD.md) | ✅ Strong | Needs numbers (Gate A #2) and a moment-to-moment feel spec (Gate A #1) |
| [World Bible](WORLD_BIBLE.md), [Lore Lexicon](LORE_LEXICON.md), [Locations](LOCATIONS.md) | ✅ Strong | Full act scripts are Gate B |
| [Character Bible](CHARACTER_BIBLE.md) | ✅ Strong | Bond-arc scripts are Gate B |
| [Narrative Style](NARRATIVE_STYLE.md) | ✅ Good | Jam script itself is missing (Gate A #8) |
| [Art Direction](ART_DIRECTION.md), [Art Book Production](ARTBOOK_PRODUCTION.md), art book PDF | ✅ Strong | Asset list with specs (Gate A #6); painted style frames still blocked |
| [Production Plan](PRODUCTION_PLAN.md) | ✅ Good | Needs a cut list per feature (Gate A #3) and a definition of done (Gate A #10) |
| [AI Disclosure](AI_DISCLOSURE.md) | ✅ Running log | Final summary at submission |
| [Prototype](../prototype/index.html) | ✅ Playable core verb | Must be playtested against Gate A #9 before Unity work locks the rules |

The **missing** layer is everything between "great idea" and "great to play": feel, numbers, the first ten minutes, sound, and the quality bar. That's what Gate A covers.

---

## 2. Gate A: write before jam development (11 docs, about 1 day of work in total)

Ordered by how much they decide whether people love the game.

| # | Doc (file) | Owner | Time | Why it matters for fun |
|---|---|---|---|---|
| 1 | **Game Feel Spec** (`GAME_FEEL.md`) | Lead dev + design | 2 h | The tap-to-stop is the whole game. If stopping a wheel doesn't feel incredible, nothing else saves it |
| 2 | **Tuning Sheet** (`tuning/jam_tuning.csv` + `TUNING.md`) | Design | 2 h | Fun lives in the numbers: fight length, how often patterns land, how fast Mult grows |
| 3 | **Jam Slice Spec + Cut List** (`JAM_SLICE.md`) | Producer | 1 h | A finished small game beats an unfinished big one; cuts are decided calmly now, not at 3 am on Day 6 |
| 4 | **First 10 Minutes (FTUE) Beat Sheet** (`FIRST_10_MINUTES.md`) | Design + writing | 1.5 h | Jam players decide in 60 seconds. Raters play 10–20 minutes. This is the game they actually judge |
| 5 | **UX, Diegetic UI and Accessibility Spec** (`UX_SPEC.md`) | Design + UI | 1.5 h | Minimal UI only works if every state is still readable; a timing game must be playable by everyone |
| 6 | **Asset List and Specs** (`ASSET_LIST.md`) | Art lead | 1.5 h | Art is the bottleneck. Every asset needs a size, format, layer split and owner before anyone generates or rigs |
| 7 | **Audio Direction and Sound List** (`AUDIO.md`) | Audio | 1 h | Sound is half the game feel; a reel that clicks on the beat feels twice as good |
| 8 | **Jam Script and Storyboards** (`JAM_SCRIPT.md` + `storyboards/`) | Writing + cinematics | 2 h | Cutscenes are our biggest wow and our biggest risk; boards first, generation second |
| 9 | **Playtest Plan and Fun Metrics** (`PLAYTEST.md`) | Design | 45 min | Tells us what "fun" means in numbers, and when to change course |
| 10 | **Quality Bar and Definition of Done** (`QUALITY_BAR.md`) | Whole team | 45 min | "GOTY quality" has to mean a checklist, or it means nothing |
| 11 | **Technical Design Doc** (`TECH_DESIGN.md`) | Lead dev | 1.5 h | WebGL limits, deterministic rules, data-driven content: the things that are expensive to change on Day 5 |

### A1. Game Feel Spec (`GAME_FEEL.md`)
**Must answer**
- The exact anatomy of one strike, frame by frame: wheel appears → spin → tap → stop (ease, overshoot, settle) → hit-stop → camera → number tear-off → digit slams into the reel. Timings in milliseconds.
- Input: latency target (< 50 ms tap-to-visual), input buffering, what happens on a mistimed or double tap, keyboard/mouse/touch parity.
- Payoff ladder: what Bust, Pair, Zero-Sum, Cascade, Jackpot, Overwrite and Reaper's Toll each look and sound like, scaled by importance (hit-stop length, shake strength, flash, slow-mo, music sting).
- Speed: how a round speeds up after the player has seen a pattern 3 times (shortened cinematics, hold to fast-forward), so spectacle never becomes waiting.
- "Readability first": the stopped digit must be legible within 150 ms, under every effect.
- Reference clips (GIFs) from games that nail it: Balatro (score counting), Hi-Fi Rush (beat sync), Persona 5 (all-out attack), Hades (hit-stop), Peggle (Ode to Joy finale).

**Done when** the prototype implements it and 4 of 5 playtesters say stopping a wheel "feels good" without being asked about it.

### A2. Tuning Sheet (`tuning/jam_tuning.csv` + `TUNING.md`)
**Must answer**
- Every number in the jam slice in one sheet: wheel speeds and face sizes per hero, base tens, enemy Balances and wheels, pattern mults, charm values, fen rewards, shop prices.
- Targets: an ordinary fight lasts **60–90 s**, a boss **3–4 min**; a Pair or better lands in about **50%** of rounds, a Jackpot in **5–10%**, an Overwrite about once per fight with a good build.
- The growth curve: damage per round at each node for a "no-synergy" build vs a "good synergy" build. The good build has to clearly win by the boss, as in Balatro; the plain build should struggle by Tamamo.
- A simple simulation (a script running 10,000 random rounds) that checks the pattern odds against the targets.

**Done when** the Unity build loads its values from this sheet (no magic numbers in code) and the simulation output matches the targets.

### A3. Jam Slice Spec + Cut List (`JAM_SLICE.md`)
**Must answer**
- The exact content of the slice: every node, fight, enemy, charm, hero, cutscene and line count. (Production Plan §3 has the outline; this is the locked list.)
- Every item tagged **Must / Should / Could**, with the day by which a Should or Could is cut if it isn't working.
- The **"minimum lovable slice"**: what ships if everything goes wrong (e.g. intro + Prologue + one Hyakki fight + Tamamo).

**Done when** the team signs it and nothing new enters without something else leaving.

### A4. First 10 Minutes Beat Sheet (`FIRST_10_MINUTES.md`)
**Must answer**
- Second-by-second for minute 1, then beat-by-beat to minute 10: what the player sees, does, learns and feels.
- Rules: the first tap happens within **20 s** of pressing Start; choosing the lucky number happens in **minute 1**; the first Jackpot is guaranteed in the first fight (scripted wheel); no text box over 2 lines; every new mechanic is taught by doing it once, safely.
- The "hook moment": the REMAINDER DETECTED reveal must land before minute 3.
- What the skip button skips, and what returning players never see again.

**Done when** 5 first-time players reach the first boss without asking a question, and at least 3 can explain Pair, Jackpot and Parry afterwards.

### A5. UX, Diegetic UI and Accessibility Spec (`UX_SPEC.md`)
**Must answer**
- Every screen and state (combat, choose striker, enemy turn, reel payoff, map, market, teahouse, pause, settings, game over, victory), each as the in-world object from GDD §8, with a wireframe.
- What is always visible vs shown on demand; how the player knows whose turn it is, which hero is next and what the enemy will do, without HUD panels.
- Accessibility: reduced motion (no shake or flashes), slower-wheel assist, hold-to-stop alternative, colour-independent digits (shape and number, never colour alone), subtitles and text size, photosensitivity check for flashes, one-hand play, rebinding.
- Mouse, touch and keyboard parity; safe areas for itch's embedded player.

**Done when** each screen has a wireframe and every accessibility option is in the settings menu of the jam build.

### A6. Asset List and Specs (`ASSET_LIST.md`)
**Must answer**
- One row per asset in the slice: id, type, owner, source (3D base / AI paint / hand), resolution, layer split for parallax or rigs, animation states, status, and the day it's due.
- Specs per type: character PSB layer naming for Unity 2D Animation, background parallax layer count and sizes, VFX sheet sizes, video codec and length, UI atlas.
- File naming and folders, so assets drop into Unity without renaming.

**Done when** every Must item from A3 has a row, an owner and a due day.

### A7. Audio Direction and Sound List (`AUDIO.md`)
**Must answer**
- Music: tempo per land (the reel and stops sync to the beat clock), stems that build as the reel fills, the boss themes, cutscene cues.
- The SFX vocabulary: wheel tick, stop, hit, each pattern sting, parry, Settle, UI. Each pattern needs a sound you'd recognise with your eyes closed.
- Mix rules (the stop sound always cuts through), loudness target, and sources and licences (plus AI-use disclosure for any generated audio).

**Done when** every Must interaction in A1 has a named sound in the list, and the temp music runs on the beat clock in the prototype.

### A8. Jam Script and Storyboards (`JAM_SCRIPT.md` + `storyboards/`)
**Must answer**
- Every line of dialogue in the slice, in the Narrative Style format, with speaker, emotion and trigger.
- Storyboards (thumbnails are fine) for the intro (World Bible §8), Vesper's rescue, the world-map reveal, Hina's entrance, Tamamo's defeat and the cliffhanger, each with timing and "skippable / not" marked.
- Which shots are video (Higgsfield/Seedance), which are in-engine, which are still frames with motion graphics.

**Done when** an animatic (boards with temp audio) of the intro plays end to end and the team agrees it hooks.

### A9. Playtest Plan and Fun Metrics (`PLAYTEST.md`)
**Must answer**
- When: a playtest every day from Day 2 (the prototype counts), with 3–5 new players per round, plus one cultural reviewer before release.
- What we watch: time to first tap; time to first smile or "oh!"; deaths and quits by node; "one more run?" said or done; which pattern players cheer.
- What we ask afterwards (5 questions max): what was the best moment, when were you confused, when were you bored, which hero do you want next, would you play again.
- Thresholds that change the plan, e.g. if fewer than half want one more run, stop adding content and fix the core.

**Done when** the first session has happened on the browser prototype and its findings are logged.

### A10. Quality Bar and Definition of Done (`QUALITY_BAR.md`)
**Must answer**
- One checklist per feature type (fight, cutscene, character, background, UI screen, sound), drawn from Art Direction §5, Art Book Production §8 and A1/A5. A feature is done only when it passes its checklist **and** has been playtested.
- The "trailer test": would a 3-second clip of this feature make someone click? If not, it isn't done.
- What we never ship: placeholder text, stray AI artefacts (wrong digits, broken hands), untranslated or unreviewed cultural details, flashes that fail the photosensitivity check.

**Done when** the team uses it in the Day 5 feature freeze review.

### A11. Technical Design Doc (`TECH_DESIGN.md`)
**Must answer**
- Architecture: the pure C# `Core` (rules, patterns, Balance/Omen, scoring, RNG with seeds), `Sequencing`, `Data`, `Presentation` (Production Plan §5), and the boundaries between them.
- Data: ScriptableObject schemas for heroes, wheels, faces, charms, enemies, boss rules and maps; how the tuning sheet (A2) imports.
- Determinism and testing: seeded RNG; EditMode tests for every pattern and the priority order (GDD §1.5); a replay log for bug reports.
- WebGL: memory and size budgets, video playback, audio unlock, load time (first fight within 20 s), browser test matrix (Chrome, Firefox, Safari, mobile Chrome).
- Build and release: daily build to a private itch page, versioning, save data (localStorage via PlayerPrefs) and what happens when it's cleared.

**Done when** an empty WebGL build is live on itch and the `Core` tests pass for all seven patterns.

---

## 3. Gate B: write after the jam, before full production

These matter for the full game, but they need what the jam teaches us. Writing them now would be guessing.

| # | Doc | What it answers | Start after |
|---|---|---|---|
| B1 | **Player Experience and Emotional Arc** | Target emotion per act; an intensity curve for the whole campaign (spikes, rest beats, the midpoint reveal) | Jam feedback |
| B2 | **Systems Design, one doc per system** | Charms (all ~90, with set bonuses), wheel crafting, oracle sticks, Ink, Karma, Navaratna gems, Awakenings, Deals, Wagers, Ledger Tree; an **interaction matrix** of which systems combo, and which break the game | B3 |
| B3 | **Economy and Progression Model** | Fen income and costs per act; difficulty curve vs expected build power (a simulation like A2, for 6–8 hours); run length; how losing feels fair | Jam tuning data |
| B4 | **Act and Encounter Design, one doc per land** | Node maps, encounter tables, Elites, the Keeper trial, the boss script with phases and telegraphs, set pieces | B1, B3 |
| B5 | **Enemy and Boss Sheets** | Per enemy: wheel profile, behaviour, telegraph, counter, art and animation needs | B4 |
| B6 | **Full Script, Bond Arcs and Dialogue Database** | Every scene and line; 4 bond scenes per hero; the branching and ending flags for the four endings | B1 |
| B7 | **Cultural Consultation Plan and Review Log** | Reviewers per culture (Japanese, Chinese, Indian, Greek, American), what each signs off, issues found and fixed (World Bible §10) | Before any public Act II–V material |
| B8 | **Localisation Guide** | String rules, font coverage (kanji, hanzi, Devanagari, Greek), text expansion, glossary for translators, the Japanese, Chinese and Hindi plan | B6 |
| B9 | **Accessibility Plan (full game)** | Extends A5 against the Game Accessibility Guidelines and Xbox Accessibility Guidelines; difficulty and assist modes | Jam feedback |
| B10 | **Telemetry and Balancing Plan** | Events to log (opt-in), dashboards for win rates, pick rates and quit points, the balance-patch process | B3 |
| B11 | **QA and Test Plan** | Test cases per system, regression suite, platform matrix, bug triage rules | B2 |
| B12 | **Market, Audience and Positioning** | Target players, comparable games (Balatro, Persona, Slay the Spire, Hades), the hook in one sentence, price, platforms, Steam tags | Jam ratings |
| B13 | **Marketing Beat Plan and Trailer Script** | Steam page, wishlists, festivals (Next Fest), trailer shot list built from Link Arts and Overwrites, community plan | B12 |
| B14 | **Legal, IP and AI Policy** | Originality review (inspired by Balatro and anime, never copying), asset licences, music licences, AI-generated asset policy and disclosure, trademark check on the name | Before the Steam page |
| B15 | **Team, Pipeline and Tools Handbook** | Who owns what, review cadence, the art pipeline end to end (3D base → paint → overpaint), version control rules for large assets | When the team grows |

---

## 4. Order of work for the next 36 hours

1. **Today (Fri 6 Nov), 2 h:** A3 Jam Slice + Cut List, then A1 Game Feel. Everyone needs to know what we're making and how it should feel.
2. **Today, 2 h:** A2 Tuning Sheet; wire the browser prototype to it and run the first playtest (A9) tonight.
3. **Sat 7 Nov, morning:** A4 First 10 Minutes, A5 UX, A11 Tech Design (lead dev starts Unity in parallel).
4. **Sat 7 Nov, afternoon:** A6 Asset List, A7 Audio, A8 Script + boards, A10 Quality Bar.
5. **From Sun 8 Nov:** no new docs. Update Gate A docs only when a playtest changes something.

---

## 5. One-page checklist

**Written** means the document exists and answers its questions. Each doc's **"done when"** check (a playtest, a build, a sign-off) still has to happen in production; those are tracked in the right-hand column.

**Gate A (blocks the jam build)**
| | Doc | Written | "Done when" still needs |
|---|---|---|---|
| A1 | [Game Feel Spec](GAME_FEEL.md) | ✅ | Prototype implements §2–§4; 4 of 5 testers say it feels good |
| A2 | [Tuning](TUNING.md) + [`jam_tuning.csv`](../tuning/jam_tuning.csv) + `tools/sim_patterns.py` | ✅ (simulated) | Unity loads the CSV; two playtest rounds confirm §3 |
| A3 | [Jam Slice + Cut List](JAM_SLICE.md) | ✅ | Team signatures |
| A4 | [First 10 Minutes](FIRST_10_MINUTES.md) | ✅ | 5 testers reach Varro without help |
| A5 | [UX, Menus, Diegetic UI, Accessibility](UX_SPEC.md) | ✅ | Wireframes in `art/ui/wireframes/`; settings in build |
| A6 | [Asset List and Specs](ASSET_LIST.md) | ✅ | Owners assigned; status kept daily |
| A7 | [Audio Direction + Sound List](AUDIO.md) | ✅ | Temp music on the beat clock |
| A8 | [Jam Script + Storyboards](JAM_SCRIPT.md) | ✅ script | Thumbnails in `art/storyboards/`; intro animatic |
| A9 | [Playtest Plan](PLAYTEST.md) | ✅ | First session logged |
| A10 | [Quality Bar](QUALITY_BAR.md) | ✅ | Used at the Tue 10 freeze review |
| A11 | [Technical Design](TECH_DESIGN.md) | ✅ | Empty WebGL build live; Core tests pass |

**Gate B (after the jam; written now so production starts from a full plan)**
| | Doc | Written |
|---|---|---|
| B1 | [Player Experience, Loops, Emotional Arc](PLAYER_EXPERIENCE.md) | ✅ |
| B2 | [Systems Design](SYSTEMS.md) (luck and fantasy mechanics, kits, ultimates, Awakenings, Link Arts, 63 charms, interaction matrix) | ✅ |
| B3 | [Economy and Progression](ECONOMY_PROGRESSION.md) | ✅ (run simulator still to build) |
| B4 | [Act and Encounter Design](ACT_DESIGN.md) (all lands) | ✅ |
| B5 | [Bestiary: Enemies, Elites, Keepers, Bosses](BESTIARY.md) | ✅ |
| B6 | [Full Story](STORY.md) + [Bond Arcs and Dialogue Database](BOND_ARCS.md) | ✅ (outline + key lines; full line-by-line script per act still to write) |
| B7 | [Cultural Consultation Plan](CULTURAL_CONSULTATION.md) | ✅ (reviewers to hire) |
| B8 | [Localisation Guide](LOCALISATION.md) | ✅ |
| B9 | [Accessibility Plan](ACCESSIBILITY.md) | ✅ |
| B10 | [Telemetry and Balancing](TELEMETRY.md) | ✅ |
| B11 | [QA and Test Plan](QA_TEST_PLAN.md) | ✅ |
| B12 | [Market and Positioning](MARKET_POSITIONING.md) | ✅ (update with jam data) |
| B13 | [Marketing Plan + Trailer Script](MARKETING_PLAN.md) | ✅ |
| B14 | [Legal, IP and AI Policy](LEGAL_IP_AI.md) | ✅ (lawyer review before Steam) |
| B15 | [Team Handbook](TEAM_HANDBOOK.md) | ✅ |
