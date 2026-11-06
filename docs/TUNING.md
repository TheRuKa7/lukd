# ZERO-SUM: OMEN — Tuning (Gate A2)

Every number in the jam slice lives in [`../tuning/jam_tuning.csv`](../tuning/jam_tuning.csv); Unity imports it, so there are **no magic numbers in code**. This page explains the targets and shows the simulation that backs them. Re-run with `python3 tools/sim_patterns.py` and `python3 tools/sim_patterns.py --favour`.

---

## 1. Targets (what "fun" means in numbers)

| Measure | Target | Why |
|---|---|---|
| Small Audit length | 3–4 rounds, 60–90 s | Long enough for a pattern, short enough to stay snappy |
| Big Audit | 5–6 rounds | Room for a Cascade or an ultimate |
| Boss | 9–12 rounds, 3–4 min | Two phases and at least one big moment |
| Pair or better | ~65% of rounds (average player) | Something good happens most rounds |
| Jackpot or Overwrite | 1 in 12 rounds (average player with own-digit Twins), about once per fight | The dream moment is common enough to chase |
| Three Busts in a row | **0%** | Bad luck never feels like a wall (Hap's Hand) |
| Damage growth | "No synergy" build stalls by Tamamo; "good synergy" build finishes Tamamo in ≤ 10 rounds | Balatro's rule: the build must matter |
| Losing | Party Settles ≈ 1 in 5 boss attempts for an average first-timer | Tension without frustration |

## 2. Pattern odds (simulated, 60,000 rounds per cell)

Party: NIL (digit 7) + Vesper (7) + Maeve (3). "Skill" = chance a tap lands the face the player aims at. The **average player** is modelled at 25%.

| Setup | Overwrite | Jackpot | Cascade | Zero-Sum | Pair | **Bust** |
|---|---|---|---|---|---|---|
| 10-face wheels, aim at own digit (original GDD) | 1.0% | 0.4% | 1.4% | 9.8% | 30.1% | **57.3%** |
| 10 faces + **Pattern Sight** (3rd striker aims to complete) | 4.7% | 1.3% | 3.3% | 14.5% | 31.6% | **44.5%** |
| **8-face starter wheels** + Pattern Sight | 5.8% | 1.8% | 2.6% | 13.5% | 35.3% | **41.1%** |
| 8 faces + Pattern Sight + **Hap's Favour** (8-round fights) | — | — | — | — | — | **34.5%** |

Findings that changed the design:
1. **Aiming at your own digit in a mixed party makes Busts more likely** (mixed party, 50% skill: 72% Busts). The fix is *reading the reel*: Pattern Sight shows the third striker which faces complete a pattern (GDD §1.1).
2. **10-face wheels are too wide for a starter.** Starters have 8 faces; removing faces is the core of wheel crafting later.
3. **Bad-luck streaks** happened in 25% of an average player's fights before Hap's Favour, and in 0% after (SYSTEMS §2.4).
4. **Overwrite must not depend on the digit** (×3·digit gave digit 0 a ×0 and digit 9 a ×27). It is now a flat **×21** for every digit.

Expected Mult per round (from the table, 8 faces + Pattern Sight): **≈ 1.6 for a random tapper, ≈ 2.8 for an average player**, most of the gap coming from Overwrites. That gap is the skill expression we want.

## 3. Damage and Balance curve (jam slice)

Strike = tens (10 × level) + digit. Round damage = Σ strikes × Mult.

| Point in the slice | Party level | Typical round (avg player, no charms) | With a good build | Enemy Balance | Rounds to win |
|---|---|---|---|---|---|
| Fight 1 (NIL alone) | 1 | (10+5)×3 × 2.8 ≈ 125 | — | Debt Hound 300 | 3 |
| Fight 2 (NIL + Vesper) | 1 | ≈ 125 | — | 3 × 300 (one at a time) | 3 each |
| Collectors (Big) | 2 | (20+5)×3 × 2.8 × 0.75 (armour) ≈ 160 | ≈ 220 | 500 | 3–4 |
| **Varro** | 2 | ≈ 210 (jars cost ~1 tube in 3 rounds) | ≈ 300 | 1,200 | 6–9 |
| Act I Small | 3 | (30+5)×3 × 2.8 ≈ 295 | ≈ 450 | 1,500 | 4–5 |
| Act I Big | 3 | ≈ 295 | ≈ 500 | 2,500 | 5–8 |
| **Tamamo** | 4 | (40+5)×3 × 2.8 ≈ 380 | ≈ 700 (Hina + charms + Link Art) | 6,000 | 9–16 |

The plain build needs ~16 rounds against Tamamo (and will likely Settle), the good build ~9: the build matters, as intended. If playtests show the plain build winning easily, raise Tamamo to 7,500 before touching anything else.

## 4. Enemy damage
Enemy strike = enemy tens + stopped digit; the player stops enemy wheels too, so parries (0) and Fortune (your digit) depend on skill. Starter enemy wheels have 10 faces (no omissions) so parry odds are 10–12%.

| Enemy | Tens | Avg hit | Hits to Settle a 300-Balance party |
|---|---|---|---|
| Debt Hound | 20 | ~24 | 12 |
| Collector | 30 | ~34 | 9 |
| Varro P1 / P2 | 40 / 80 | ~44 / ~88 | 7 / 3–4 |
| Tamamo | 60 | ~64 (+curses) | 7 at Balance 420 |

## 5. Economy (jam)
Fen: Small 8 · Big 15 · Elite 25 · Boss 40; interest 1 per 5 held (cap 5). Prices: common charm 6, rare 12, reroll 3 (+1 each time), face removal 5, enhancement 8. Expected fen at Ofuku's shrine ≈ 45: enough for one rare charm *or* two enhancements, never both (a real choice).

## 6. How to tune during the jam
1. Change the CSV, never the code.
2. Re-run the simulation if you touch wheels, faces or patterns.
3. Change one number per playtest round, and write down why in the CSV note column.
4. Priority when a fight feels wrong: enemy Balance → enemy tens → wheel speed → pattern mults (last; they're the game's language).

**Done when:** Unity loads every value above from the CSV, the simulation matches §2, and two playtest rounds have confirmed or corrected §3.
