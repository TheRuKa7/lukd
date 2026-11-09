# Documentation audit and corrections

Updated **8 November 2026 IST**. This report records the repository correction pass requested by the user. The38 original design documents and their technical/art/data dependencies were reviewed against [DECISIONS](DECISIONS.md). The6November refinement directory retains its named historical baseline; it is not a competing current canon. Subsequent world, art, manga, architecture and source artifacts extend that original review. [PROJECT_STATUS](PROJECT_STATUS.md) is the current implementation ledger.

## Resolved design conflicts

|Area|Correction and authoritative record|
|---|---|
|Jam scope|One10–15minute Meridian Prologue; NIL/Vesper, two single-Hound teaching encounters, one free charm, Varro, mercy/roof/results. Hyakki/extra heroes/markets/gauges remain gated. [JAM_SLICE](JAM_SLICE.md), [GDD](GDD.md), [PRODUCTION_PLAN](PRODUCTION_PLAN.md)|
|Number domains|Separate resonance, Civic Omen, Balance and normalized Audit Omen. Audit defeat does not automatically kill or set Civic00. NIL’s chosen0 remains valid; positive ending Civic10 is distinct from resonance0. [SYSTEMS](SYSTEMS.md), [WORLD_BIBLE](WORLD_BIBLE.md)|
|Combat correctness|One settlement, exact seven-pattern priority/multipliers, current-Balance Reaper snapshot, atomic simultaneous-loss precedence, zero defence overlap, actual/scored digit separation and legal party/wheel domains. [SYSTEMS](SYSTEMS.md), [TECH_DESIGN](TECH_DESIGN.md)|
|Recovery and boss|Visible third-to-first Favour/Black Cat repair; pure legal Pattern Sight; explicit Varro token capture/substitution/expiry/restoration and delayed phase warning. [SYSTEMS](SYSTEMS.md), [BESTIARY](BESTIARY.md)|
|Economy and future systems|Jam has no fen/shop; future63 charm candidates,3/5 set thresholds, campaign carryover/complete rollback, bounded effect recursion and individual implementation gates. [ECONOMY_PROGRESSION](ECONOMY_PROGRESSION.md), [SYSTEMS](SYSTEMS.md)|
|Narrative continuity|Thale inherited the older Basilica; Hina remains99 through campaign; Bai Si has four lanterns; Maeve’s recent family loss differs from ancient Rounding; required recruit/catch-up/ending gates are explicit. [STORY](STORY.md), [ACT_DESIGN](ACT_DESIGN.md), [BOND_ARCS](BOND_ARCS.md), [CHARACTER_BIBLE](CHARACTER_BIBLE.md)|
|World operation|Conserved transfers, power instruments/costs/counters, government/dissent, faction construction, jobs, stores, infrastructure and dated history now have explicit daily consequences. [WORLD_OPERATIONS](WORLD_OPERATIONS.md), [WORLD_ENCYCLOPEDIA](WORLD_ENCYCLOPEDIA.md)|
|Art specificity|Painted world/inked manga; detail hierarchy and dramatic/comedy registers; fixed anatomical turnarounds, distinct faction dress, true source/camera provenance and candid blockout status. Rahu/Ketu hostile designs are invented eclipse machines. [ART_DIRECTION](ART_DIRECTION.md), [ART_SPEC](ART_SPEC.md), [catalog](../art/catalog/characters.json)|
|Art-spec contradictions|Comparative scale differs from labelled insets; rim follows motivated light; Composite Knight insignia is an explicit Synod exception; Wards residents have work/income variation; House formal interiors differ from dusty travel wear. [ART_SPEC](ART_SPEC.md)|
|AI-only and provenance|No mandatory human finishing, runtime AI dependency or inferred paid entitlement. Source generation/process records and actual cost/rights evidence remain required. [ARTBOOK_PRODUCTION](ARTBOOK_PRODUCTION.md), [AI_DISCLOSURE](AI_DISCLOSURE.md), [LEGAL_IP_AI](LEGAL_IP_AI.md)|
|Manga/game reuse|Stable panel/dialogue IDs, separate clean/lettered pages and exact type, original craft references, declared fixed print route, read-only collectible and gated live-choice adapter. [MANGA_DIRECTION](MANGA_DIRECTION.md), [MANGA_CHAPTER_01](MANGA_CHAPTER_01.md)|
|Architecture and truthfulness|Six ADRs map92 stable technical requirements to source, decision and named proof. Every Unity requirement remains specified/not started. Browser/Python checks, generated artifacts and runtime/player acceptance are separate. [architecture](architecture/architecture.md), [traceability](architecture/traceability.md)|
|Regional authority|ACT_DESIGN owns regional narrative/traversal briefs, BESTIARY owns specified encounter counters, and typed numeric Land Law data remains disabled behind the explicit F-LAND backlog gate. No folklore brief silently becomes a runtime modifier. [ACT_DESIGN](ACT_DESIGN.md)|

## Reproducible checks

|Command|What it establishes|What remains separate|
|---|---|---|
|`python tools/check_docs.py --self-test`|Adversarial link-parser/anchor checks, including balanced parentheses, reference links, literal examples, Unicode/duplicate headings and missing anchors|Full Markdown grammar, external site liveness and document semantics|
|`python tools/check_docs.py`|Every repository-area Markdown local link/anchor; unique source/ADR/catalog IDs; upstream cast coverage; view/source paths; backlog DAG; typed scalar CSV; available source/render hashes|Visual identity, model quality, native engine import, rights/cultural review and player evidence|
|`node tests/reference_rules.test.js`|Exact reference rule regressions including single settlement, Reaper, zero defence, repair and Varro|Unity port, complete DOM/story/input/save path and player timing|
|`python -m unittest discover -s tests -p 'test_*.py'`|Python model boundary/scalar/fixture checks and manga layout/lettering contract tests|Simulation realism, all final panels’ visual quality and working Unity reader|
|Book/manga builder check modes|Required input/export structure and source-linked derivative generation|Final PDF/layout/image acceptance until actual output is rendered and inspected|

Executed on8November: the documentation validator and its seven adversarial self-tests passed. The run checked63 Markdown files/553 local destinations and anchors,92 technical requirements,56 source cast IDs,37 bestiary table opponents,35 backlog nodes,51 tuning scalars,67 jam-script IDs,20 manga pages/80 panels/81 dialogue IDs and122 recorded source/render hashes. There were no errors or pending path warnings at that run. Node reference regressions and all14 Python tests also passed. These numbers identify the checked snapshot; rerun the commands after integration changes.

The catalog's91 indexed records point to84 unique four-view sets, including seven explicitly shared group/uniform records and two contextual non-anatomical studies. Index coverage is not91 independently modelled bodies. The validator reports these categories separately. Missing material must remain null/gated or fail an existing-file claim. Nonexistent future implementation paths are not presented as completed artifacts. Historical FILE_INVENTORY/ASSET_METADATA CSV hashes intentionally describe source snapshot3d88239; they are not compared as current-source checksums. Generated build/cache directories are excluded from the canonical Markdown scan.

## Current evidence limits and remaining work

Architecture verdict is **CONCERNS**: engine viability and production remain unproven. There is no verified Unity game project/build, C# Core/importer/save/replay, hosted submission, runtime rig/audio acceptance, measured Web performance, external cultural approval or fresh-player sign-off. The next production action is the empty hosted Unity Web build, followed by one correct greybox Audit. Artbook and manga work must not imply these gates passed.

Final regenerated PDF page counts, every image-generation completion and representative/all-page visual inspection results are **pending integration evidence** in this report. The integrating agent records the actual output manifest and verification; no guessed total is substituted. Source turnarounds and procedural drafts can establish spatial coverage while remaining visibly first drafts. AI-generated illustrated pages still need continuity, action/reading-order and anatomy/prop-count review beyond export checks.

Run the commands above after changes. A passing documentation check is a local integrity result, not a claim that every sentence is semantically perfect or every planned feature exists. New contradictions should update DECISIONS and the owning domain document together, then extend the stable registry or fixture that prevents recurrence.
