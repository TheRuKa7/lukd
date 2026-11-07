# ZERO-SUM: OMEN — Game Design Document

Updated 7 November 2026 IST. **Specified design, not proof of a Unity implementation.** [DECISIONS.md](DECISIONS.md) resolves conflicts; [PROJECT_STATUS.md](PROJECT_STATUS.md) records evidence; [JAM_SLICE.md](JAM_SLICE.md) owns current deliverable scope.

> Every number is spinning. You choose when to stop.

An anime 2.5 D party RPG about luck, debt and sharing possibility. The player follows NIL across the Tally, stopping digits, combining patterns and recruiting companions. The jam proves this fantasy in Meridian; the full campaign remains gated expansion.

## 0. Pillars, in priority order

1. Responsive, readable decisions: accepted input and its actual digit precede spectacle.
2. One central action: stop a number. Party order, wheels and build choices change its consequences.
3. Spectacle rewards a readable result; repeats and cinematics respect skip/speed/settings.
4. Narrative and mathematics reinforce each other without treating a culture as one mechanic or stereotype.
5. Complexity is earned through play. Introduce one rule, test it, then combine it.

## 1. Core combat: the Audit

### 1.1 Three strikes

Each player round has exactly three strikes before scoring. Solo NIL acts three times; a two-person party uses both heroes with either acting twice; a three-person party uses each once. NIL is mandatory. Choose the next eligible hero, stop their wheel, see a provisional strike value, then deposit its actual digit in the reel. Provisional values do not drain enemy Balance. Resolve all three, settle the total once, then check terminal state.

The third wheel offers Pattern Sight: legal faces show the pattern they would complete, with a word/shape as well as colour. Debt substitutions and automatic repair must be included in previews. Actual stopped digits and resolved scoring digits are stored separately.

### 1.2 Damage

`strike = fixed base + actual stopped digit + declared strike bonuses`

`round damage = floor((sum of strikes + round flat bonuses) × fixed-point Mult)`

For the jam, Mult is the integer base pattern Mult and Vesper adds +7 to **each of the three strikes per actual 7** when she is in the active party. This applies retroactively in the round result; provisional displays reconcile visibly. No undocumented digit-specific buffs. No base damage is paid twice. Exact order, bounds and future modifier stages are in [SYSTEMS.md](SYSTEMS.md) §1.

### 1.3 Seven base patterns

| Pattern | Match | Base Mult | Secondary consequence |
|---|---|---:|---|
| Overwrite | Three chosen resonance digits | 21 for every digit | In-engine gold payoff; no jam ultimate gauge |
| Reaper | 4-4-4 unless chosen digit is 4 | 4 | Current-Balance percentage loss on qualifying Audit Omens |
| Jackpot | Other three of a kind | max (2, digit) | Strong payoff |
| Cascade | Ordered +1 or −1 steps; no wrap | 3 | Another player round; no enemy action |
| Zero-Sum | Sum exactly 10 or 20 | 2 | Cancels the next scheduled enemy action |
| Pair | Exactly two equal, after higher priorities | 2 | Flourish |
| Bust | Otherwise | 1 | Warms Favour |

Priority is the table order. Reaper reads both pre-round Audit Omens and current Balances, then removes floor (44% × current Balance) from each qualifying side in addition to ordinary damage. Commit both results atomically. Party zero means loss, including simultaneous zero; no rewards, enemy action or later effect follows terminal state.

### 1.4 Defence

Enemy wheels reveal all legal faces and the strike base. Actual 0 is Parry, chosen nonzero digit is Fortune (reflect base+digit), other digits damage the party. Chosen 0 on actual 0 combines Parry/Fortune: one reflection, one defensive proc. Ofuda automatically parries the first enemy action, with no accepted stop and no reflection. This counts as one defended action. Equal Overwrite strength does not assert equal win rates across digits.

### 1.5 Wheels, Favour and agency

Explicit starter lists, widths, repair order and Pattern Sight are in SYSTEMS §2. Width means exposure under the motion model, not measured human probability. Warm Favour slows next round ×0.8 and widens already-matching faces ×1.5. After two consecutive Busts, a would-be Bust changes scoring slot three to slot one visibly and is evaluated again. Black Cat uses the same conversion once per fight and takes precedence; only one conversion occurs. Pattern results cool the streak. Authored teaching results are declared tutorial events, never presented as sampled outcomes.

### 1.6 Four different numbers

Resonance is identity/build affinity; Civic Omen is social luck outside combat; Balance is the luck staked; Audit Omen is its normalized display. Positive Balance displays ceil (99×Balance/Max Balance), clamped 01–99; zero displays 00. Combat Omen rules read Audit Omen. NIL's NaN identity remains visible beside the party Audit frame. Settling a stake ends an Audit, not automatically a life. See DECISIONS D 03 and WORLD_BIBLE.

## 2. Party and recruitment

Full game: NIL + up to two of **eight core and three secret companions** (12 authored playable characters total). Jam: NIL and Vesper only. Varro becomes a full recruit after the ending/NG+, not an early complement. Required companions have guaranteed catch-up recruitment; secret companions do not silently gate central resolution. Narrative bonds and mathematical bonds are separate state.

### 2.1 Implemented reference contract versus future kits

NIL's chosen resonance has a double-width face. Vesper's 7 is double-width and her Lucky Seven passive follows §1.2. The reference sandbox implements these two heroes, not their advanced verbs, charged ultimates or awakenings. Full roster/ability pitches and explicit production gates are in SYSTEMS §4–§6; CHARACTER_BIBLE owns appearance, voice and narrative availability.

### 2.2 Resonance bonds, expansion only

| Bond | Eligibility | Intended payoff | Legal example |
|---|---|---|---|
| Complement | Nonzero digits sum to 10 | Zero-Sum ×4; authored Link Art | NIL 7 + Maeve 3 + Hina 9 |
| Neighbours | Difference 1, no wrap | Eligible adjacent-digit pattern rule | NIL 7 + Ba 8 + Hina 9 |
| Twins | Equal digits, including 0 | That Jackpot ×2; shared charge after gauge gate | NIL 7 + Vesper 7 |
| Prime Party | All active resonances prime | Prime Trio ×5 | NIL 7 + Prima 2 + Maeve 3 |
| Powers of Two | Three distinct digits from 1,2,4,8 | Bounded next-round Mult bonus | NIL 2 + Bai Si 4 + Ba 8 |
| Śūnya | Shunya's later bond-wild Awakening | Zero may satisfy one bond slot | NIL 6 + Shunya 0 + Bai Si 4 |
| Old/New Ledger | Declared regional tags | Cross-set contribution | NIL + Hina + Vesper |

Zero has no ordinary Complement. Partner access varies by chosen digit and story stage. Bonds never activate from inactive roster members unless a future effect explicitly declares that scope. Requirements and acceptance fixtures are in SYSTEMS; no bond/Link Art is required in the jam.

## 3. Build systems and content gates

Jam contains **one free choice among Horseshoe, Black Cat and Ofuda**; one equipped choice, no purchase, fen or crafting. IDs/effects are fixed in SYSTEMS §3.

Full game specifies 63 party charms (nine per seven sets), slots 3→6, wheel crafting, oracle sticks, Ink, Karma, Navaratna gems, the Ledger Tree, awakenings and Deals. These are expansion families, each blocked by its SYSTEMS gate and exact content data. Personal gear is separate from party slots/sets. No runtime generation or paid service is a gameplay dependency.

## 4. Structure and difficulty

### 4.1 Full campaign pacing hypothesis

Critical-path segment minutes: Prologue 35, Hyakki 45, River 50, Śūnyapura 50, Kroton 45, Crossroads 50, Finale 40 =315. Optional bonds/quests/navigation add 45–105 minutes: total 6–7 hours. These are authored budgets, not measured duration. Distinguish them from the shorter 10–15-minute jam Prologue. Scene-level budget is owned by STORY.

### 4.2 Balance growth hypothesis

| Segment | Small / Big / Boss Balance | Expected level |
|---|---|---|
| Prologue |300 /500 /1200 |1–2 |
| Hyakki |1500 /2500 /6000 |3–4 |
| River |8000 /14000 /35000 |6–8 |
| Śūnyapura |50000 /90000 /200000 |10–12 |
| Kroton |300000 /600000 /1500000 |14–17 |
| Crossroads |2500000 /5000000 /12000000 |19–22 |
| Finale |Phase pool totals 99,999,999, subject to encounter validation |24–26 |

These numbers require a legal-party fight model and player validation. They do not prove synergy necessity or acceptable boss length. Defeat restores the complete act-start gameplay snapshot in full campaign; the jam retries its encounter checkpoint.

### 4.3 Bosses

Varro's one-token Debt Jar and two-phase contract are SYSTEMS §1.7/BESTIARY. Future Tamamo, Jin Chan, Eclipse Constructs, Archon, House and Thale contracts are gated by BESTIARY plus SYSTEMS effect schemas; they must preserve a reachable counter for every required party. Rahu/Ketu are revered figures; invented Basilica constructs take their names. Do not turn human defeat into death when later scenes require survival.

## 5. Teaching ladder

Jam: interactive rescue → chosen resonance → NIL solo three-stop round → parry → Vesper and order → free charm choice → Varro's clearly telegraphed debt → mercy/map payoff. One Debt Hound per tutorial encounter, not hidden packs. No forced Bust to demonstrate Favour. [FIRST_10_MINUTES.md](FIRST_10_MINUTES.md) owns scripted-demo timing.

Expansion: Hyakki introduces three-person party and curated charms; River teaches crafting/Ink; Śūnyapura adds Karma/gems; Kroton awakenings; Crossroads Deals/loops. Each new rule requires learn/test/combine encounters and production gates, not merely arriving in a land.

## 6. NIL's future growth

Splice, Carry, Rewrite, Place Value, Factor, Deal and Divide by Zero are future ability contracts in SYSTEMS §4. They cannot enter a runtime merely because their name appears here. The jam uses one fixed base and one stopped digit; optional later Splice must pass an onboarding comparison before replacing this baseline.

## 7. Persistent progression

Shared levels add 10 fixed strike base per level, cap 30 full game; jam uses level 1 then level 2 at Varro. Bonds have four authored stages; Awakening is a separate kit choice; personal gear does not count toward party-charm sets. Act transitions keep wheel modifications/gems/permanent unlocks, equip three selected party charms and stash the rest, halve fen with floor, and retain floor (0.75×Karma). See ECONOMY_PROGRESSION for rollback/idempotence.

## 8. UX and production quality

Diegetic objects retain readable semantic layers. Menus must support mouse/touch/keyboard and settings without timing pressure. Captions, reduced motion, flash checks, accepted-face visibility, pause, skip and save recovery are required implementation work; specs alone do not verify them. See UX_SPEC, GAME_FEEL and QUALITY_BAR.

## 9. Jam scope

The Remainder:10–15-minute Meridian Prologue, three encounters (one solo Hound, one two-hero Hound, Varro), NIL/Vesper, one-of-three free charm, interactive story opening, ending/results/checkpoint/settings/credits/disclosure. No charged ultimates, bonds, extended reels, Hyakki or economy required. Extension gate 9 Nov IST, feature freeze 10 Nov, content lock 11 Nov, verification 12 Nov, submit 13 Nov; hard deadline 14 Nov 17:30 IST. JAM_SLICE owns details.

## 10. Technical target and evidence

Installed Unity 6000.4.11 f 1 + Web module is the first viability target. Pure Core, typed content, one sequencing owner, in-engine presentation and versioned saves. No Unity project/build is present yet. The browser reference is a finite three-encounter rules sandbox, not the story submission. Current checks and limitations are in TUNING/PROJECT_STATUS; no playtest success is inferred.
