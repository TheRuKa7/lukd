# ZERO-SUM: OMEN — Telemetry and Balancing Plan (Gate B10)

**Opt-in only**, anonymous, post-jam. The jam build makes no network calls ([`TECH_DESIGN.md`](TECH_DESIGN.md) §8).

---

## 1. Consent and privacy
- First launch asks: "Share anonymous play data to help balance the game?" Default **off**.
- No personal data; a random install id; no IP storage; data deleted after 12 months; a "delete my data" button.
- Compliant with GDPR/CCPA; privacy policy linked from settings and the store page.

## 2. Events
| Event | Fields | Answers |
|---|---|---|
| `run_start` | lucky_digit, mode, omen_level | Which digits players choose |
| `fight_end` | fight_id, result, rounds, party, charms, damage_max, busts, patterns{...} | Fight length vs targets; pattern odds in the wild |
| `pattern` | type, digit, round | Real pattern distribution vs the simulation |
| `favour` | warm/haps_hand count per fight | How often luck turns |
| `boss_attempt` | boss_id, phase_reached, result | Difficulty spikes |
| `node_choice` | act, node_type, options, chosen | Map choice balance |
| `charm_pick` | offered[], picked | Pick rates; dead charms |
| `quit` | location, time | Where people stop |
| `setting_changed` | setting, value | Accessibility usage |

## 3. Dashboards
Fight length by node · win rate by boss and attempt · pattern frequencies vs `tools/sim_patterns.py` · charm pick and win rates · hero pick rates and pair frequencies · quit heat-map by node · lucky-digit distribution.

## 4. Balancing process
1. Weekly review of dashboards.
2. Flag: any boss with first-attempt win rate < 40% or > 85%; any charm picked < 5% or with win rate > 15 points above average; any node where > 10% quit.
3. One change per item per patch; note it in the patch notes with the reason.
4. Re-run the simulation for any wheel/pattern change.
