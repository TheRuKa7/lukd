# ZERO-SUM: OMEN — Systems contracts

Updated 7 November 2026 IST. [DECISIONS.md](DECISIONS.md) is authority; [PROJECT_STATUS.md](PROJECT_STATUS.md) distinguishes specified/implemented/verified. Jam contracts below are required design. `prototype/rules.js` implements a bounded reference subset; this is not a Unity build. Future catalogue entries remain disabled until their named gates pass.

## 1. Resolution contract

### 1.1 Identity and state

Store resonance digit, Civic Omen, Balance and Audit Omen independently (DECISIONS D 03). A positive max Balance and bounded nonnegative integer Balance are required. Audit Omen is ceil (99×Balance/max), clamped 01–99, or 00 at zero. Combat effects read Audit Omen unless explicitly civic. NaN is NIL's identity, never a damage value. An Audit settlement exhausts a stake; story decides any civic transfer or death.

### 1.2 Round ledger and effect ordering

A round stores `actualDigits[3]`, `scoringDigits[3]`, eligible striker IDs, fixed bases, face IDs, effect provenance and pre-round Balance snapshots. Three actual stops always complete before settlement; no provisional hit drains Balance.

Order: accepted faces → actual landing events → authored/debt/Ink scoring replacements → one visible Bust repair → wild assignment/pattern → strike flat bonuses → round flat bonuses → additive Mult → ordered ×Mult → armour/target modifiers → floor once → ordinary and snapshotted percentage damage → atomic commit → terminal check → nonterminal rewards/charge/next-turn events. Landing passives/charge read actual digits; pattern rules read resolved scoring digits. A replacement never fakes an actual stop. Jam has no Ink, wilds, armour, additive Mult, ×Mult charms or charge gauges.

Jam uses integer pattern Mult. Full-game modifier values use fixed-point thousandths, stable source-ID order, integer floor of the final rational result; no intermediate rounding unless an effect explicitly declares it. Core must check intermediate arithmetic before commit. Reference amounts are capped at 10^12; future numbers above that require a separate validated numeric domain, not silent saturation or unbounded doubles. Invalid/negative/overflowing data fails validation before a fight.

### 1.3 Base patterns and priorities

| Priority | Pattern | Predicate | Mult | Nonterminal secondary |
|---:|---|---|---:|---|
|1 |Overwrite |All three equal NIL's chosen resonance |21 |Gold feedback; no jam gauge |
|2 |Reaper |4-4-4 |4 |Percentage event below |
|3 |Jackpot |Other triple |max (2,digit) |Feedback |
|4 |Cascade |Ordered increments+1 or−1; no wrap |3 |Next player round, enemy waits |
|5 |Zero-Sum |Digit sum 10 or 20 |2 |Cancel next scheduled enemy action |
|6 |Pair |Any equality after higher priorities |2 |Feedback |
|7 |Bust |No match |1 |Increment Bust streak |

Examples: lucky 4 +444 is Overwrite; lucky 7 +444 is Reaper;334 is Zero-Sum before Pair;890 is Bust;987 is Cascade;000 for nonzero choice is Jackpot×2. Each round scores one highest-priority base pattern, never additive matches. No hidden digit bonuses.

### 1.4 Reaper and terminal rules

Before any round damage, snapshot both current Balances and normalized Audit Omens. If a snapshot Omen contains 4, that side loses floor (44×snapshot current Balance/100) once. Ordinary ×4 pattern damage hits the enemy as well. Commit both sides atomically. Party zero is LOSS even when enemy zero; otherwise enemy zero is WIN. Stop secondary events immediately on terminal state. A settled state cannot accept another round/defence. Effects cannot read a new Omen halfway through this operation.

### 1.5 Defence and zero overlap

Enemy action reveals strike base and legal faces before input. Actual 0: Parry/no damage. Nonzero chosen digit: Fortune/no damage and reflect base+digit. Chosen 0 on actual 0: combined Parry/Fortune, reflect base once, emit one defended-action event. Any other stop damages party by base+digit. Ofuda consumes the first enemy action as an automatic Parry with no accepted face and no reflection; emit one defended action. No duplicate proc for a combined result. If reflection settles the enemy, stop before jar/rewards that would belong to later combat events.

### 1.6 Party eligibility

NIL is required. Three strikes: solo=NIL three times; two heroes=both participate with either twice; three heroes=each once. While selecting, remaining slots must remain sufficient for every unused required actor. Party passives apply only from the active party. Jam Vesper: each actual 7 adds+7 to every one of the round's three strike values, including earlier provisional hits. The final ledger reconciles this explicitly. Jam NIL: chosen face×2; fixed base and one digit, no advanced verb/gauge.

### 1.7 Varro Debt Jar: exact jam boss contract

`boss_varro` starts Balance 1200, enemy strike base 40, full ten-face enemy wheel including 0. Intro telegraphs the capture before round 1. Once per fight, after the first complete nonterminal player round, snapshot resolved scoring slot 3 into one visible token. The captured round is not retroactively changed.

State machine: `idle → holding → restoring → spent`. While holding, replace scoring slot 3 with 0 after its actual stop and before repair/pattern. Actual digit still drives landing effects. Count each affected completed player round, including Cascade/Zero-Sum rounds. Open after three successful defended enemy actions (actual Parry/Fortune or Ofuda; one credit each), OR at the end of the third affected player round. The next player round restores the token's saved digit into scoring slot 3 visibly after its actual stop, before normal repair/evaluation, then clears the token to spent. No stacking, recapture or reward per replacement. Expiry works even if enemy actions are skipped. Retries reset the jar.

Phase 2 is entered at≤50% current/max enemy Balance after settlement. Show “next action 40, then 80” before it occurs: the first subsequent enemy action remains base 40, all later ones use 80. If that action is cancelled, the warning remains until an enemy action actually occurs. Neither phase removes 0 or requires an optional character. Tests cover ten chosen digits, expiry under repeated extra turns, one restore only, and Ofuda counting once. See BESTIARY for authored presentation.

## 2. Wheels, Pattern Sight and Favour

### 2.1 Explicit starter faces

NIL omissions are (chosen+4)mod 10 and (chosen+5)mod 10; replace an omitted 0 with (chosen+6)mod 10. This preserves zero and the chosen digit. Lists are authoritative:

| NIL resonance | Legal faces |
|---:|---|
|0 |0,1,2,3,6,7,8,9 |
|1 |0,1,2,3,4,7,8,9 |
|2 |0,1,2,3,4,5,8,9 |
|3 |0,1,2,3,4,5,6,9 |
|4 |0,1,2,3,4,5,6,7 |
|5 |0,2,3,4,5,6,7,8 |
|6 |0,3,4,5,6,7,8,9 |
|7 |0,3,4,5,6,7,8,9 |
|8 |0,1,4,5,6,7,8,9 |
|9 |0,1,2,5,6,7,8,9 |

Vesper:0,1,2,3,5,6,7,8. Own resonance face width×2. Jam base speeds at 720 p logical stage: NIL 470 px/s, Vesper 620 px/s; scaling the stage must not change logical timing. Reference cell unit 128 px; authored first spin×0.6 is explicitly a sandbox teaching assist. Assist mode×0.7 is a settings contract, not a claim of implementation.

Future wheel candidates (gate F-WHEEL): Maeve omits 4/8, Hina 4/0, Ba 4/1, Bai Si 9/0, Shunya 4/9, Fibi 4/6, Varro 4/9, Kyūsuke 4/9, Liu Shun 4/7; Prima deliberately 0/2/3/5/7. Candidate movement, widths and enhancements require typed per-face data and timing tests before that recruit is enabled. Hina's reversal RNG must be seeded and telegraphed; no hidden reversal after accepted input.

### 2.2 Timing/exposure

Faces have positive finite widths. Absent faces cannot be targeted or sampled; aim requests to them are errors. Random phase plus constant motion is only an exposure model. Aiming skill is a separately stated model assumption. At input latch the face actually displayed under the stop line; deceleration cannot change it. Record accepted face ID, displayed phase/tick and settings. Gameplay phase/RNG is separate from particles/audio noise. Focus loss pauses accepted gameplay time in the Unity contract; no out-of-focus progress.

### 2.3 Pattern Sight

Preview every **legal** third face through current scoring replacements, repair availability and pattern rules. Show word/shape plus colour. Do not highlight absent digits or a pattern the boss substitution prevents. Preview is pure: it consumes no RNG, charm charge, Favour or jar state. On two-person parties it works regardless of which eligible hero acts last.

### 2.4 Favour and Black Cat

A real Bust increments `bustStreak`. At≥1, next round speed×0.8 and each face whose digit already appears on that reel gets×1.5 width **once**, not once per duplicate. At≥2, a would-be Bust changes scoring slot 3 to slot 1 with a visible `haps_hand` event. Re-evaluate normal priorities: the repair can become Zero-Sum, not only Pair. Actual stopped digits remain unchanged for landing passives.

Black Cat applies the same repair to the first would-be Bust each fight, emits `black_cat` and consumes its charge. If both are available, Black Cat wins and there is no second conversion. Any resulting pattern cools streak to 0. Generated repair cannot recursively trigger its source. Rerolls do not reset per-fight charges. Fight retry/checkpoint initializes all transient charges/streaks once.

### 2.5 Wild assignments and extended reels: expansion gates

Shunya's base 0-wild affects pattern matching only; bond-wild is her later Awakening. Actual 0 remains 0 for charge, land effects and face procs. Enumerate allowed substitutions and maximize: pattern priority, then base multiplier, then lexicographically smallest resolved vector. Record the assignment in the result. No random tie-break.

Gate F-REEL must pass before any 4/5-tube ability, extra slot Deal or permanent tree slot is enabled. Domain: exactly 4/5 scoring digits, all actual strike slots retained, added slots carry an accepted free-wheel digit and zero strike value. Entire-reel priority: Overwrite (all chosen,×21^(n−2):441 at 4 slots/9261 at 5 slots; balance hypothesis) → Reaper (all 4,×4 and one percentage event) → Four/Five of a Kind (max (2,digit²/digit³)) → Full House (5 slots,counts 3+2,×6) → Long Cascade (ordered±1 across all slots,×5) → Two Pair (4 slots,counts 2+2,×3) → whole-reel sum 10/20(×2,cancel) → Pair (anyduplicate,×2) → Bust×1. Never select a favourable subset of 3. A four/five-slot fullkind is not an ordinary three-slot Jackpot. Repair changes the final scoring slot to the first and re-evaluates once. Wild resolution uses the same tie-break. Favour counters describe the **final** outcome. Required fixtures cover every length/category, overlap, wildcard assignment, slot restoration and simultaneous defeat.

## 3. Three jam charms

One free choice, one equipped for the remaining Prologue; no fen, shop, reroll or set bonus in jam.

| ID | Name | Exact effect | Reset |
|---|---|---|---|
|`charm_horseshoe` |Horseshoe |Chosen resonance face width×1.5 on any allied wheel **where present**, multiplied after own resonance×2 and Favour width; never adds a face |Persistent chosen reward; widths recomputed per spin |
|`charm_black_cat` |Black Cat |First would-be Bust repair from §2.4; changes scoring third→first, normal priority evaluation |Once per fight, reset on encounter retry |
|`charm_ofuda` |Ofuda |Skip accepted stop on first enemy action; automatic Parry, no reflect; one defended event |Once per fight, reset on encounter retry |

Offers are mutually exclusive: first accepted choice closes all three buttons atomically. Retry restores the selected charm, not a new offer or a second charm. No effect secretly changes NIL's chosen digit.

## 4. Future ability gates and roster

**Gate F-KIT** for each new ability requires: stable ability ID; owner/unlock; legal actor/target; named event; actual-versus-resolved digit domain; numeric/rational amount; duration; per-event/fight caps; replacement priority; save/reset rule; animation skip behaviour; readable counter; exact success/overlap/terminal fixtures; and an end-to-end playable encounter. Disabled candidates may appear in the bible but cannot be selected or advertised as implemented. This gate is separate for every ability, not a blanket unlock of the catalogue.

| Candidate | Domain contract to implement | Dependencies/gate |
|---|---|---|
|NIL Splice |Optional fixed-base bonus wheel, then ordinary ones stop; bonus choices 0/10/20, one extra accepted input; no change to actual ones |F-KIT plus onboarding comparison; out of jam |
|NIL Carry |First actual strike value>50 each round increments next scoring digit mod 10 once; actual landing unchanged; no carry loop |F-KIT, scoring replacement fixtures |
|NIL Rewrite |One chosen scoring-digit replacement 0–9 after three stops, once/fight; cannot change actual charges |F-KIT, Ink UI |
|NIL Place Value |Choose one actual digit from completed round; add 10×digit to first next-round strike base once, then clear |F-KIT, next-round snapshot |
|NIL Factor |Choose one strike remainder modulo 100 that is a product of two digits 2–9; replace its scoring slot by the ordered factor pair; choose among valid pairs, no extra base damage |F-KIT+F-REEL; unavailable with no valid pair |
|NIL Deal |One in-combat authored Deal offer/fight; explicit accept/decline and persistent price |F-KIT+F-DEAL |
|NIL Divide by Zero |Chosen resonance faces become pattern-wild for one round; actual digits remain; no division arithmetic |F-KIT+wild fixtures; finale scripted recall independent of missing faces |
|Remainder Release |One free wheel fills a fourth zero-strike slot; duration one round |F-KIT+F-REEL; no jam charge gauge |
|Seven-Chamber Requiem |Seven authored free digit draws, each base 10+digit; each actual 7 doubles **that shot only**, cap×2/shot; one enemy target |F-KIT+gauge; jam may use a non-gameplay scripted defeat shot |
|Triskele |Replace three scoring slots by 3 for one round; original landing effects unchanged |F-KIT+replacement fixtures |
|Hundred-Year Night |Next round wheels retain only party resonance digits already present, preserving at least one face; normal widths renormalize |F-KIT+F-WHEEL; no age change |
|Eight Bells |Current round ×(11/10)^8, rounded once;64 fen after win only |F-KIT+F-ECON; no repeated payout on replay |
|Four Lanterns Out |One Reaper percentage event, enemy only, plus declared base damage; does not stack a second ordinary Reaper event |F-KIT+Reaper fixtures |
|Shunya Place Value |Choose actual digit; add 10×digit to each next-round base, once then clear |F-KIT+state snapshot |
|Sieve of Light |Remove tagged composite shields/armour from declared targets; no damage to untagged bodies |F-KIT+armour data |
|Spiral Deal |Two zero-strike free-wheel slots extend one round to five |F-KIT+F-REEL |
|Debt Collector |Snapshot enemy's last accepted strike digit; next round flat bonus 6×digit once; unavailable before one accepted enemy stop |F-KIT; full Varro recruit post-ending |
|Cucumber Tide |After nonterminal round heal floor (5%max party Balance) per actual 5, capped at max; no revive |F-KIT+healing order |
|Thirteen Orphans |Separate thirteen-tile mini-round with authored tile pool; first legal tile-pair gives×13 to the next ordinary round once/fight, not recursive tile payout |F-KIT+separate minigame input/data fixtures |

Eight core companions: Vesper, Maeve, Hina, Ba Jinling, Bai Si, Shunya, Prima, Fibi. Three secret/postgame: Varro, Kyūsuke, Liu Shun. Their passive pitches require their own F-KIT records: no passive is activated merely from this list. Hina's Ninety-Nine condition cannot be Audit Omen≤99 (always true): candidate effect is immunity to 9 curse plus +1 additive Mult per actual 9, once/landing, gated for balance. Ba's Compound adds 0.8 per consecutive patterned round capped+4 and resets on Bust/fight. Bai Si marks every fourth actual strike, next round damage×1.44 once. Shunya 0-wild follows §2.5. Prima primes 2/3/5/7 pierce tagged armour and each add+1 Mult. Fibi cycles final digits of 1,1,2,3,5,8,13,21… with index saved per fight; sequence recurrence/state defined before enable. Varro's first would-be Bust/fight may replace third scoring slot by 1 before ordinary repair; not a guaranteed pattern. Kyūsuke's once/fight bow is a telegraphed next-stop 5 skip. Liu Shun's first two actual 6 s in a round grant one extra player round once; no fake Cascade classification.

## 5. Awakenings: individually gated expansion

Gate F-AWAKEN requires F-KIT for both branches, respec at Act IV shrines, permanent chosen branch saved by ID, and tests that its benefit is not already baseline. Hina remains 99 until true-ending epilogue.

| Hero | Branch A | Branch B |
|---|---|---|
|NIL |Remainder: final ability charge rate×2 |Open Hand: start each fight warm, rather than duplicating one-Bust baseline |
|Vesper |Dead Man's Hand: first actual 1 followed later by 8 in round gives×3 that round once |Blackjack: sum of actual digits 21 gives×21 base pattern override once; full override priority record required |
|Maeve |Forge-Mother: one selected charm upgrade/fight at forge, maximum authored level |Triskelion: every third round uses one visible repair if otherwise Bust |
|Hina |Hundred Years: self-acceptance, +10 fixed base, no literal age 100; loses 9 immunity |Kasa-obake: once/round choose a visible adjacent legal face after stop; accepted override recorded |
|Ba |Bank of Bells: interest 1 per 4 held, per-node payout cap 25 |Golden Fan: secondary enemies each take floor (8%ordinary round damage), once |
|Bai Si |True Count: mark lasts fight, max one stack |Mourning White: own Reaper percentage instead heals same floor amount, no revive |
|Shunya |Śūnya: zero bond-wild; one slot assignment per bond |Astrolabe: show next scheduled enemy wheel's seeded initial face, not a guaranteed stop |
|Prima |Even Prime:2 may satisfy either prime/composite predicate, one trigger/source |Aegis: first two damaging enemy actions prevented, no reflect |
|Fibi |1597: freeze sequence index one round/fight |Golden Spiral: one Cascade/fight opens fourth slot next round |
|Varro |Bailiff: Debt Collectorflatbonus×2 |Free Man: one free actual-wheel retry/fight |
|Kyūsuke |Full Dish: Cucumber Tide heals 6%per 5 |River God's Friend: firstbow 5 also clears one curse |
|Liu Shun |Heavenly Hand: tile-pair reward×15 |Mahjong Queen: first tileoffer canbe redealt once |

## 6. Bonds, Link Arts and recursion

Complement=nonzero sum 10; Twins=equal including 0; Neighbours=absolute difference 1 without wrap; Prime Party=all three active prime; Powers of Two=three distinct from 1/2/4/8. Shunya bond-wild is an Awakening, never baseline. Legal examples include NIL. Narrative bond stages do not fabricate mathematical eligibility.

Gate F-BOND requires party-screen preview from the same evaluator, eligible active actors, unlock/charge policy and exact fixtures. Prime Trio is a three-slot expansion pattern: priority after Jackpot, before Cascade, all resolved digits prime,×5, no intrinsic extra turn. Neighbour bond permits a two-digit ordered adjacent subsequence with any third digit to count as Cascade, after Prime Trio; both orientations allowed. Powers Of Two grants a pending×2 **for next round only**, not exponential accumulated Mult; duplicate grants from this source replace rather than multiply. All next-round boosts have source IDs and expiry.

Gate F-LINK requires declared eligible pair/three-actor set, one activation/fight, one nonrecursive event bundle and a skippable visual using the same resolved result. Candidate names: Lucky Strike (Vesper/Maeve), Golden Sieve (Ba/Prima), Ninety-Nine and One (Hina/Varro or Fibi 1), Six Lanterns/Four Lanterns (Bai Si/Liu Shun), Lucky Eight (Vesper/Ba), Lantern Fan (Ba/Hina), Spark and Shield (Prima/Maeve), Third Lantern (Maeve/Bai Si), Midnight Parade (Hina/Vesper), Zero Count (Bai Si/Shunya), Golden Ratio Deal (Fibi/Shunya), Prime Directive (legal active prime trio including NIL), Powers of Two (legal active trio), Twins (NIL/matchinghero). Effect data must reference F-KIT primitives. Ninety-Nine and One may apply a damage multiplier; it must not falsify normalized Audit Omen 01 without changing stake. No unlimited generated attack/charge/Link chain. Trigger depth 1 for generated effects; Hap's Laugh may repeat each eligible charm once per Overwrite, tagged to prevent re-entry. Current jam contains no Link Arts.

## 7. Full-game charm catalogue:63 candidates

Holding 3 from one set: set bonus I; 5: set bonus II. Slots grow 3 → 6. These are full-game design candidates, not implemented effects. Only the three jam rows in §3 are active scope. Gate F-CHARM below requires exact data and fixtures before each candidate is enabled.

| Set | Charms (rule in short) | Set bonus I / II |
|---|---|---|
| **Meridian** (street luck) | Four-Leaf Clover (1 in 4: duplicate a digit) · Thirteenth Floor (×13 if the round total ends in 13) · Black Cat (first Bust → visible repair (§2.4)) · Lucky 77 Jacket (+7 tens per 7) · Nixie Pendant (your digit +1 width) · Bazaar Ribbon (+1 charm slot, −10% damage) · Collector's Badge (+20% vs Collectors) · Naming Token (your digit's Pair ×3) · Gus's Receipt (Markets −15%) | +1 Mult per different culture held / charms trigger twice on Overwrite |
| **Hyakki** (shrine luck) | Beckoning Cat (+1 fen per strike ending in your digit) · Daruma (land your digit 3× → ×2 Mult for the fight) · Ofuda (first enemy action automatically parried; no reflect) · Ebisu (+fen on Pairs) · Daikokuten (+tens on 8 s) · Bishamonten (+parry window) · Benzaiten (Link Arts +20%) · Jurōjin & Fukurokuju (one combined charm; heal 3% per actual 7) · Hotei (Busts give +3 fen) | 7 s are blessed twice / five-piece set: each actual 7 adds +7 to that strike once |
| **River Empire** (prosperity) | Red Envelope (+8 fen on a Jackpot) · Door God (parries strike back) · Peach-Wood Sword (×2 vs ghosts and Noiselings) · Money Toad (interest +1) · Jade Bi Disc (Jade faces +2 Mult) · Firecracker String (first round ×2) · Lucky Knot (Pairs heal 2%) · Dragon Boat Oar (Cascades +1 extra round chance) · Joss Paper (on Settle, +88 fen) | Interest doubled / every 8 on the reel is gold (+3 fen) |
| **Śūnyapura** (auspicious) | Lemon and Seven Chillies (cancel one curse per fight; +7 tens per 7) · 108 Beads (every 108 th point counts double) · Rangoli Chalk (first Zero-Sum each fight ×3) · Peacock Feather (Favour warms 1 Bust sooner) · Brass Diya (+1 Karma per Pair) · Kolam Thread (Neighbours bonds active for any two digits) · Shankha Shell (enemies' wheels −10% speed) · Navagraha Ring (+1 gem slot) · Palm-Leaf Page (see the boss rule early) | Karma ×2 / 0 is wild for bonds |
| **Kroton Nova** (proportion) | Evil-Eye Bead (see the enemy's next digit) · Fortuna's Wheel (once per fight, re-roll the reel) · Owl Coin (+1 Mult per prime strike) · Olive Wreath (+10% Balance) · Golden Ratio (Fibonacci triples count as Cascade) · Tetractys Token (if strikes sum to 10, ×10) · Amphora (store a digit for later) · Laurel of Seven (×7 on 7-7-x) · Thread of Lachesis (one Atropos-style cut per act: remove an enemy face) | Primes pierce / perfect numbers (6, 28) on the round total pay ×6 |
| **Crossroads** (deals) | Horseshoe (chosen resonance faces ×1.5 width where present) · Rabbit's Foot (one free re-spin per fight) · Lucky Penny (+1 fen per 1) · Seven-Come-Eleven Dice (×7 if the round totals 7 or 11) · Pumpkin Lantern (×2 vs the headless) · Silver Dollar (Wager wins +50%) · Route 7 Sign (+7% speed on enemy wheels, +7 Mult) · Dead Man's Card (1-8 in a round: ×8) · Last Train Ticket (loop rounds keep the reel) | Deals' prices halved / one free Deal per act |
| **The Open Hand** (Hap; legendary, from shrines and Whispers) | Hap's Die (once per fight, set any reel digit) · Open Palm (Favour never cools below warm) · Shooting Star (once per act, re-deal a whole Market) · Coin on Its Edge (a Bust has 1 in 10 to become an Overwrite) · Rainbow at Night (+1 Mult per different digit on the reel) · Lucky Stranger (a random companion's passive each fight) · The Long Shot (Jackpots of 0 or 1 pay ×20) · Second Chance (revive once per run) · Hap's Laugh (on Overwrite, every charm triggers again) | Hap's Whispers appear twice as often / the finale's Fixed Fate is halved |


Gate F-CHARM is per charm: ID, set, rarity, event, input domain, amount, duration, caps, ordering, reset and three interaction fixtures. Set bonuses at 3/5 equipped **party** charms; personal gear never counts. Hyakki's Jurōjin/Fukurokuju is one item. Five-piece bonus replaces the impossible seven-equipped-item requirement. Catalogue prose is a candidate brief; no UI may promise an effect until its complete typed record and F-KIT primitive are present. Jam rows §3 override any shorthand for their three IDs.

## 8. Future systems and implementation gates

| Gate | Contract before enable | Acceptance evidence |
|---|---|---|
|F-WHEEL |Explicit positive-width faces; min 4 faces after removal; enhancement stacking/expiry/shatter IDs |No absent aim; known exposure; exact removal/retry/save fixtures |
|F-ECON |Fen faucets/sinks per node; one payout keyed node+run; fixed interest rounding/caps; no clock income |Full-node budget trace, no retry duplication/infinite loops |
|F-INK |One selected scoring replacement after stop; consumes one charge; no actual landing/charge retrigger |Normalpriority, debt ordering, terminal/cancel tests |
|F-STICK |24 authored offers with fortune poem, precise boon/visible price, consume once |Offer determinism, safe decline, save/retry |
|F-KARMA |Parry/Zero-Sum +1 once/event; max 9; rerollcost 1; lethalguardcost 3 once/fight; guard leaves Balance 1 |Overlap 0 one proc, no free guard loop, floor carryover |
|F-GEM |Pattern-level delta rational/cap and owned gem ID; level survives acts |Every gem materially differs from baseline and exact rounding |
|F-TREE |Seven branches with node IDs, costs, prerequisites; memory reward unique |No cycle, no duplicate grant, save migration and soft-lock-free path |
|F-DEAL |12 authored boon/price records; price changes real max Balance/slots/rules, never only display |Accept/decline, limits, rollback, no negative/inaccessible wheel |
|F-LOOP |House resets enemy Balance and local reel after every third completed player round; keeps party Balance/build; max 3 loops then explicit final phase |No reward duplication, no infinite reset, checkpoint/replay parity |
|F-CUSTOM |Bounded authored recruit template, canonical name/look/kit ID, no arbitrary runtime mechanics/lore |Assetprovenance, legal party/save/load/unlock tests; no central ending gate |

Wheel enhancements candidates: Gold+3 fen, Jade+4 additive Mult, Glass×2 strike with 25%post-stopbreak, Iron+20 fixed base when not stopped, Lanternslowsdeclaredpassage, Inkwild, Horseshoe 25%declared scoring conversion, Cursed+50 fixed base/next-strike curse. Their F-WHEEL/F-CHARM records must distinguish actual digit and scoring conversion; no hidden relabel. Min 4 faces avoids collapse but is not proof of balance. Gem candidates map Ruby/Jackpot, Pearl/Pair, Coral/Reaper, Emerald/Cascade, Yellow Sapphire/Overwrite, Diamond/Link, Blue Sapphire/Zero Sum, Hessonite/Bust, Cat's Eye/Favour. Cat's Eye upgrade starts fight warm, rather than restating baseline. Each needs typed levels/caps before offer generation.

## 9. Reset, replay and validation

Jam checkpoint stores chosen resonance, encounter index, selected charm and settings; retry resets Balance, seed, jar, Favour and per-fight charm flags together. No extra reward/choice on retry. Full campaign carryover/rollback is ECONOMY_PROGRESSION; no optional secret recruit gates central ending. Replay includes rules/content version, seed/stream names, accepted face IDs/ticks, choices and result state hashes; visuals consume a separate RNG. Exact cross-language fixtures precede statistical rates. No future family is implemented merely by this specification.
