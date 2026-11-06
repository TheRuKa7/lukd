# ZERO-SUM: OMEN — QA and Test Plan (Gate B11)

---

## 1. Automated
| Layer | Tests | When |
|---|---|---|
| Core (EditMode) | Every pattern; priority order; Omen readout; Favour and Hap's Hand; each Land Law; each charm; each boss rule; Balance overflow (`long`) | Every push (CI) |
| Simulation parity | C# pattern odds vs `tools/sim_patterns.py` within 0.5% | Nightly |
| PlayMode smoke | Boot → Naming → Fight 1 (fixed seed) → Results | Every build |
| Replay | Re-run saved replay logs; outputs must match | Nightly |
| WebGL | Build size, load time, memory ceiling | Every build |

## 2. Manual test passes
| Pass | Scope | When |
|---|---|---|
| Critical path | New game → Tamamo → results, with each of the 10 lucky digits | Daily from Day 4 (jam) |
| Fight matrix | Every enemy × every hero pair present in the slice | Feature freeze |
| Input | Mouse, touch, keyboard; hold-to-stop; assist | Feature freeze |
| Browsers | Chrome, Firefox, Safari, Edge; Android Chrome; iOS Safari | RC |
| Accessibility | Every option on; reduced motion; colour-blind presets; text 150% | RC |
| Save | Quit at every node type and resume; storage blocked | RC |
| Localisation (post-jam) | Text overflow, fonts, line breaks per language | Per language |
| Cultural | Reviewer sign-off per land | Before public release |

## 3. Bug triage
| Severity | Definition | Rule |
|---|---|---|
| **S1 Blocker** | Crash, soft-lock, data loss, critical path broken | Fix now; no build ships with one |
| **S2 Major** | Wrong rule, broken feature, bad cultural error | Fix before RC |
| **S3 Minor** | Visual glitch, typo, small balance issue | Fix if time |
| **S4 Polish** | Nice-to-have | Backlog |

Every bug report includes: build number, browser/device, steps, expected vs actual, and the **replay log** if it happened in a fight.

## 4. Exit criteria (jam RC, Thu 12 Nov)
Zero S1 · zero S2 on the critical path · all ten lucky digits complete the slice · load ≤ 20 s · 60 fps on the reference laptop · QUALITY_BAR "never ship" sweep passed · AI disclosure complete.
