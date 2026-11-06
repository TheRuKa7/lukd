# ZERO-SUM: OMEN — Economy and Progression (Gate B3)

The full-game model behind [`TUNING.md`](TUNING.md) (jam). Build power must grow faster than linear stats so that synergy, not grinding, wins (GDD §4.2).

---

## 1. Progression layers

| Layer | Grows by | Resets? | Where |
|---|---|---|---|
| Party level | XP from fights (cap 30) | No | Tens +10 per level |
| NIL's verbs | Story (one per act) | No | GDD §6 |
| Companions | Story + secret quests | No | 8 core + 3 secret |
| Bonds | Teahouse scenes (4 per hero) | No | Second passive, Link Art upgrade, true-ending flag |
| Awakenings | Act IV choice per hero | No (respec at Act IV shrines) | SYSTEMS §5 |
| Ledger Tree | Memory digits from Seals and side quests | No | 7 branches |
| Charms, faces, gems | Fen, rewards, shrines | **Per act** (see §4) | The build |
| Fen | Fights, interest, gold faces | Per act (half carries) | Markets |
| Karma | Parries, Zero-Sums | Decays 25% per act | Śūnyapura+ |

## 2. Enemy Balance curve (GDD §4.2, exponential)

| Act | Small | Big | Boss | Party level (expected) | Expected Mult needed |
|---|---|---|---|---|---|
| Prologue | 300 | 500 | 1,200 | 1–2 | ~2.5 |
| I | 1,500 | 2,500 | 6,000 | 3–4 | ~4 |
| II | 8,000 | 14,000 | 35,000 | 6–8 | ~10 |
| III | 50k | 90k | 200k | 10–12 | ~35 |
| IV | 300k | 600k | 1.5M | 14–17 | ~150 |
| V | 2.5M | 5M | 12M | 19–22 | ~700 |
| Finale | — | — | 99,999,999 | 24–26 | ~3,000 (over Phase 3 with Link Arts) |

Linear tens alone give ~5× damage from Prologue to finale; Balances grow ~80,000×. The rest must come from Mult: patterns × gems × charms × bonds × Link Arts. That is the Balatro curve and the reason builds matter.

## 3. Fen economy (per act)

| Source | Fen |
|---|---|
| Small / Big / Elite / Boss | 8 / 15 / 25 / 40 (+50% per act) |
| Interest | 1 per 5 held, cap 5 (Jinling's Bank of Bells removes the cap) |
| Gold faces | +3 per stop |
| Whispers, side quests | 5–30 |

| Sink | Price (Act I → V) |
|---|---|
| Common / rare / legendary charm | 6 / 12 / 25 → ×1.5 per act |
| Re-roll a Market | 3, +1 each re-roll in the same Market |
| Face removal / duplicate / enhancement | 5 / 8 / 8 |
| Oracle stick | 4 |
| Gem | 10 |
| Wager | any |

**Rule of thumb:** each Market should offer one thing the player wants and can't quite afford. Expected fen at each Market ≈ 1.2× the price of one rare item.

## 4. What resets between acts (the roguelite spine)
Within the **story campaign**, each act is a mini-run: your **charms and face enhancements carry over**, but you choose which **3 charms** to keep at each act's end ("pack light: the ferry only takes three"); fen halves; Karma decays 25%. This keeps each act's build fresh and each new land's charm set relevant, without throwing away the player's work. In the **Endless Ledger**, everything resets per run.

## 5. Difficulty and losing
- **Losing a fight** returns you to the act's start **with the build you had there** plus any memory digits earned (never a total loss).
- **Assist mode** (any time): wheels −30%, enemy Balance −25%.
- **Omen Levels 1–8** (post-game): +25% enemy Balance per level, faster enemy wheels, harsher Land Laws, fewer Shops, no Hap's Hand at level 8.

## 6. Unlock cadence (something new every ~15 minutes)
Prologue: patterns, parry, charms · Act I: party of 3, bonds, Link Arts, curses · Act II: fen economy, wheel crafting, sticks, Ink · Act III: Karma, gems, Ledger Tree · Act IV: Awakenings, number properties · Act V: Deals, Wagers, loops · Finale: everything, then taken away · Post-game: Endless Ledger, Omen Levels, Daily Omen, Hap's Gallery, New Game+.

## 7. Validation
Extend `tools/sim_patterns.py` into a run simulator (party + charms + gems) and check that a "no synergy" build fails the Act III boss while a "synergy" build passes it with ~10 rounds. Tune boss Balances, not pattern mults, first.
