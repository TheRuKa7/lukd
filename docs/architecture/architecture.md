# Architecture and implementation boundary

Updated **8 November 2026 IST**. Verdict: **CONCERNS**. The architecture now maps the adopted contracts, but engine viability, an integrated Unity Audit and production acceptance remain open. No Unity project, C# Core, package lock, hosted Unity build or performance result is established by these documents. [PROJECT_STATUS](../PROJECT_STATUS.md) owns current artifact evidence.

## System ownership

|Boundary|Authoritative responsibility|Communication contract|
|---|---|---|
|Core|Validated wheel/state, accepted commands, pure preview, pattern/effect ledger, atomic settlement and terminal state|Synchronous immutable results; no Unity objects, clock, rendering or asset/network lookup|
|Content|Stable typed IDs, versioned definitions, explicit face lists, encounter graph, dialogue and scalar tuning|Validated generated assets and content hash; invalid input fails import/build|
|Flow|One encounter/round sequencer; eligibility, accepted input, pause, skip and checkpoints|Commands enter Core once; completed results drive presentation; no second damage formula|
|Presentation|Inked actors, painted stage, UI, motion, camera, VFX and audio|Consumes committed results; visuals cannot reroll faces, grant rewards or change damage|
|Meta|Versioned settings/checkpoints, last-good recovery and future idempotent journal|Validated snapshots and unique event/reward IDs; reader bookmarks isolated|
|Offline tooling|Source art, models/cameras, manga, derivative books, provenance and checks|Versioned files with source hashes and candid readiness; no runtime generator service|

The accepted-command boundary is important: capture the face actually displayed, record its tick/ID, then animate it. A preview uses the same evaluator without consuming state. The entire round settles once after three stops; presentation may show provisional values. Rules read separate actual and resolved scoring digits. The four number domains—resonance, Civic Omen, Balance and Audit Omen—remain separate in storage and UI.

## Decisions and traceability

|Decision|Owns|
|---|---|
|[ADR-0001](adr-0001-engine.md)|Installed Unity6000.4.11f1 viability, project boundaries, Web deployment and measured budgets|
|[ADR-0002](adr-0002-rules.md)|Deterministic rules, checked numerics, patterns, defence, Favour, Varro and future effect domains|
|[ADR-0003](adr-0003-content.md)|Typed import, encounter graph, structured expansion records and localization gates|
|[ADR-0004](adr-0004-persistence.md)|Jam checkpoint/reset, failure recovery, future campaign snapshots/journals and manga state isolation|
|[ADR-0005](adr-0005-presentation.md)|Input clock, accessible UI/feedback, optional video/audio, art and manga export contracts|
|[ADR-0006](adr-0006-tooling.md)|AI-only free-first reproducibility, provenance, exact tests, truthful evidence and release gates|

[Traceability](traceability.md) contains **92 registered technical requirements**:46 jam,31 campaign,14 production and1 post-jam. All are written specifications with an owning ADR. This is document mapping, not implementation coverage. The machine-readable [TR registry](tr-registry.json) links each requirement to source heading, ADR, present test paths where applicable, and required future proof. IDs are append-only within a system; remove intent only through an explicit deprecated record rather than reusing its number.

## Next proof

1. Create and clean-import the smallest project with the installed Editor/Web module; retain licence/module/build logs. No renderer/package API is assumed compatible from a newer manual page.
2. Load the empty build in the actual intended itch iframe with correct compression headers or tested JS fallback. Name browser/device and separate cold load from after-Start timing.
3. Port the pure rules fixtures into checked C# and a typed content importer. Prove one greybox Audit, accepted-face replay and atomic results before scaling art.
4. Integrate the required three-encounter Prologue, then retry/storage/settings/skip/accessibility/audio and measured Web budgets. Preserve the exact artifact/source/content hashes.

The browser reference and Python exposure model provide useful independent regression evidence. Neither proves Unity, DOM input, a complete story, player stopping behaviour or fun. Use [QA_TEST_PLAN](../QA_TEST_PLAN.md) and [QUALITY_BAR](../QUALITY_BAR.md) for release evidence.

## Open decisions and future gates

The renderer pipeline, UI framework, actual input package/API, save serializer/storage adapter, pinned PRNG, replay encoding and video/audio import details require a working Unity project before their versions can be chosen and verified. A named layer boundary does not select an untested package.

Every future F-KIT ability, F-CHARM item, awakening, bond/Link bundle and localization locale still needs its own complete typed record and acceptance evidence. Four/five-slot multipliers and later-act Balance remain balance hypotheses. Campaign economy, tree, Deals, custom recruits and House loops stay disabled until their explicit contracts pass. Screen reader/strategy modes and telemetry services are separate gates. Do not expose empty controls or advertise candidate mechanics as present.

Known conflict-prone areas now have explicit owners: identity versus stake; actual versus scoring digits; provisional versus committed damage; preview versus mutable effects; visual skip versus story transactions; snapshot rollback versus retained unlock rewards; source art versus accepted runtime rig. No independent ADR overrides [DECISIONS](../DECISIONS.md) or its domain sources. Correct both sides of any newly found conflict.

## Documentation validation

Run `python tools/check_docs.py --self-test`, then `python tools/check_docs.py`. The standard-library validator checks all tracked-area Markdown local destinations/heading anchors, stable IDs/source links, catalog source coverage and actual paths, historical backlog DAG, scalar tuning types, and available provenance hashes. It checks current files rather than classifying old historical prose as new design. Historical links still must resolve. Future proof is an explicitly named gate rather than a link to a nonexistent implementation file.

The verdict remains CONCERNS until actual engine/runtime evidence closes the open gates. No AAA quality, legal, safety, accessibility or player sign-off is inferred from a successful document check.
