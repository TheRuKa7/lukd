# ZERO-SUM: OMEN — QA and test plan

Updated 7 November 2026 IST. Current jam: three-encounter Meridian Prologue, NIL/Vesper and one free charm. Tests below distinguish automated reference evidence from required Unity/browser/player verification. No build success is inferred from a plan.

## 1. Current automated reference checks

Run `node tests/reference_rules.test.js` and `python -m unittest discover -s tests -p 'test_*.py'`. Shared authored examples are `tests/pattern_cases.json`; they cover priority collisions, zero/triples, no-wrap and descending cases. Node additionally checks exact single-settlement damage, current-Balance Reaper snapshot, simultaneous terminal precedence, no action after settlement, zero defence/reflection, visible repair, active Vesper passive and Varro token expiry/restoration. Python rejects absent aimed faces, tests legal wheellists/closer selection, CSVscalars and reproducible model output.

These checks do not prove DOMflow, touchinput, frame latency, sound, save or Unity behaviour. A syntaxparse is not a playtest. Any corrected Monte Carlo run must name modelversion/seed/party/order/aim assumptions; statistical parity cannot replace exact fixtures.

## 2. Required Unity automation gates

|Gate |Acceptance |
|---|---|
|Q-CORE |Exactfixtures for all pattern overlaps, tenchoices, Balancebounds, passive ordering, Favour/Black Catrepair, Ofuda/zerooverlap, jar/cancellation/phase warning and terminal atomicity |
|Q-CONTENT |Typed importer detects invalid/duplicate/missingkeys and unavailable content; no disabled future ability in offers |
|Q-SMOKE |Boot→interactive opening→Naming→solo Hound→Vesper→two-hero Hound→onecharm→Varro→ending/results; fixed accepted commands |
|Q-RETRY |Everyencounter checkpoint, selected reward persists once, transient flags reset, no duplicate journal/reward |
|Q-REPLAY |Same accepted commands produce same Corestatehash in editor/Web, including settings/focus loss |
|Q-WEB |Actual hostediframe load, correct compression headers, sizes/memory/timing; no runtime external gameplay API |

Fixtures should target behaviour and past defects, not private implementation details. Add an independent expected outcome before fixing a failed rule. No exhaustive future-kit test promise until that F-KIT record is enabled.

## 3. Manual critical path matrix

All ten chosen digits × three charm choices on the required path; include chosen 0 actual 0 and chosen 4 Reaperpriority. One Hound per teaching encounter. Check both validtwo-hero orders (repeated NIL/repeated Vesper), Pattern Sight under Jar/Favour and the three-round jar expiry when enemy actions are skipped. Verify actual/scored digit distinctions and living human aftermath.

Inputs: mouseonly, keyboardonly, touchonly; hold-to-stop; pause/resume; held input during focus loss; rapid/doubleinput; selection during recovery; no phantomstop. Settings: muted, Reduced Motion, fast presentation,150%text, assist, captions/skip. Save: restart at every checkpoint, corrupted/blocked storage, iframe limits, incompatible version and correct Continue visibility.

Browsers: named current Chrome/Edge/Firefox on reference Windows machine; Safari/mac OS when available; mobilebest-effort only after separate testeddevice. Record unavailable platforms as unverified, never passed by analogy. Capture final keyframes and input/replay evidence.

## 4. Triage

S 1=crash/soft-lock/dataloss/blocked required path. S 2=wrongcombat rule, misleading counter, inaccessible essential input or majorstory/art defect. S 3=minorvisual/text/balanceissue. S 4=optional polish. Everyissue includes build/hash, platform, steps, expected/actual, replay/capture and owner. Do not label an unimplemented required feature S 4 to pass a gate.

## 5. Release candidate acceptance

Zero S 1/S 2 on requiredpath; all ten chosen digits/all three choices verified; save/retry/input/settings gates green; finalassets/provenance/disclosure accepted; no flash/accessibility claim without its actual check; cold load and Startfirst action measured separately; build artifact/source hash preserved. Player feedback is recorded with findings and fixes, not inferred from AI walkthroughs. November 12 is verification target, not completed sign-off. If future features fail gate, remove their availability and references; protect Prologue scope.
