# ZERO-SUM: OMEN - Jam tuning and model evidence

Updated 8 November 2026. [DECISIONS](DECISIONS.md), [SYSTEMS](SYSTEMS.md) and [JAM_SLICE](JAM_SLICE.md) define the rules. [`jam_tuning.csv`](../tuning/jam_tuning.csv) contains 51 finite numeric inputs and planning targets. The JavaScript reference implements the core rules; **a Unity CSV importer and a Unity game have not been implemented or verified**. The CSV is not evidence that every runtime value is already data driven.

## 1. Current values and scope

| Item | Current specification |
|---|---|
| Encounters | One solo Debt Hound, one two-hero Debt Hound, then Varro; no three-Hound gauntlet or Collector fight |
| Party | Start level 1 / Balance 300; Varro checkpoint level 2 / Balance 340; jam level cap 2 |
| Enemy stakes | Each Hound 300; Varro 1,200 |
| Enemy base | Hound 20; Varro 40, then 80 at half Balance with one further base-40 warning action |
| Pattern multipliers | Overwrite 21; Reaper 4; Jackpot max(2, triple digit); Cascade 3; Zero-Sum 2; Pair 2; Bust 1 |
| Round settlement | Once, after three accepted stops and any explicit scoring repair; no provisional damage double-payment |
| Reaper | Additional floor(0.44 x current Balance) on each qualifying side, snapshotted before normal damage and committed atomically |
| Chosen zero | Accepted defensive zero combines Parry and Fortune once; automatic Ofuda has no accepted face and no reflection |
| Reward | Free choice of Horseshoe, Black Cat or Ofuda; no fen shop or crafting in the jam |

Actual stopped digits and resolved scoring digits are distinct. Vesper's per-seven landing bonus uses actual digits. Varro's stored digit, replacement, expiry and restoration follow SYSTEMS; do not approximate a jar as a flat damage penalty. Exact fixtures live in [`reference_rules.test.js`](../tests/reference_rules.test.js).

## 2. Timing and difficulty hypotheses

| Measure | Target | Evidence needed |
|---|---|---|
| Hound | 3-4 rounds / 60-90 seconds | Full encounter simulation plus fresh-player observations |
| Varro | 9-12 rounds / 180-240 seconds | Includes defence, jar, phase transition and retries |
| Full Prologue | 10-15 minutes | Interactive story, Naming, three fights, reward and ending |
| First action / Naming | Within 20 / 60 seconds after Start | Measure separately from cold download |
| Three consecutive scored Busts | Prevented by visible Hap's Hand repair | Exact event/state test, including reset boundaries |

These are acceptance hypotheses, not measured averages. No evidence currently supports a 20% first-time boss loss rate, a universal 65% success rate, or equal difficulty across the ten chosen digits. Do not silently engineer every player into the printed manga's reference route.

## 3. Reproducible pattern-exposure model

Run from repository root:

```sh
python tools/sim_patterns.py 60000 --favour --json
```

Evidence generated on 8 November with model `jam-pattern-v2`, seed 7, **60,000 rounds for each of 60 cells**: ten chosen digits x solo/two-hero x three hypothetical aim probabilities. Each cell resets Favour every eight rounds. NIL uses D05's legal eight-face list; Vesper uses `[0,1,2,3,5,6,7,8]`. The solo order is NIL/NIL/NIL. The two-hero order is one legal fixed order, NIL/Vesper/NIL, not every player-selected order. Own-resonance width is 2; warm matching width is 1.5. Third-stop Pattern Sight targets the highest-priority available completion, breaking ties by multiplier and smaller digit. Failed aims draw by face width. Favour repairs scoring slot three to slot one before classification.

The `aim` value is an **independent Bernoulli assumption**, not a measured beginner/average/expert label. Wheel speed has no fitted conversion to aim accuracy. This model omits defence, damage, charms, Varro's jar, phase changes, player adaptation and economy; it cannot predict fight length, win rate or fun.

Selected cells below report percentages after Favour. Rounding can change totals by 0.01 points.

| Party / chosen digit / aim | Overwrite | Reaper | Jackpot | Cascade | Zero-Sum | Pair | Bust |
|---|---|---|---|---|---|---|---|
| Solo / 0 / 0.00 | 1.42 | 0.00 | 1.33 | 1.21 | 9.66 | 40.52 | 45.86 |
| Solo / 0 / 0.25 | 7.86 | 0.00 | 2.02 | 2.73 | 20.69 | 34.69 | 32.01 |
| Solo / 7 / 0.25 | 7.76 | 0.29 | 1.73 | 5.92 | 21.83 | 31.08 | 31.40 |
| Solo / 7 / 0.50 | 23.28 | 0.21 | 1.12 | 8.63 | 26.76 | 23.39 | 16.62 |
| NIL/Vesper/NIL / 0 / 0.25 | 1.75 | 0.00 | 2.64 | 4.68 | 22.39 | 31.18 | 37.36 |
| NIL/Vesper/NIL / 7 / 0.25 | 7.94 | 0.00 | 1.42 | 5.47 | 20.26 | 31.27 | 33.63 |

Vesper lacks face 4, so the fixed two-hero order cannot make 444. This is a legal-wheel consequence, not a broken classifier. Overwrite on chosen 4 still wins priority over Reaper. Chosen-zero defensive overlap is absent from this exposure table, so its balance cannot be inferred from the zero row. The ten-digit distribution must inform a real encounter model and playtests before any fairness claim.

Hap's Hand prevents a third consecutive **scored** Bust by visibly converting a would-be Bust into at least a Pair. It does not eliminate all Busts, guarantee a Jackpot, or prove a player cannot lose. Warm Favour alone has no such guarantee. Black Cat and Hap's Hand share one repair pipeline and do not double-convert the same event.

## 4. Damage and economy boundaries

An unmodified strike is `10 x level + actual stopped digit`; specified landing/passive modifiers apply in the documented order. Sum the three strike bases, apply the one winning pattern and settle once. Future extended reels, armour, charge, Link Arts and Tamamo builds are excluded from this jam model. Do not multiply a guessed mean by enemy Balance and present the result as an observed fight duration.

Full-campaign fen/interest/prices and act transitions are specified in [ECONOMY_PROGRESSION](ECONOMY_PROGRESSION.md). They do not enter the jam reward flow. That document's illustrative affordability example uses a 20-fen budget: a 12-fen charm plus two 8-fen enhancements costs 28. A 45-fen budget could afford all three and cannot support a scarcity claim.

## 5. Change and acceptance process

Change one factor per measured playtest round and record the reason, source revision, digit, party order, charm, Assist setting and result. For enemy difficulty, investigate stake/base damage and the jar's readable counterplay before changing the pattern language. Face or pattern changes require exact fixtures and a fresh versioned exposure report. Timing/width changes require input and accessibility checks; a statistics-only rerun is insufficient.

Before accepting a Unity tuning pass: implement a strict CSV importer (duplicate/unknown/nonfinite/range checks), demonstrate that runtime settings use the imported values, pass exact rule fixtures on the target engine, verify the complete hosted encounter sequence, then collect two fresh-player rounds. These production gates remain open.
