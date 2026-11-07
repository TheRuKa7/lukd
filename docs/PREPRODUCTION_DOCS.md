# ZERO-SUM: OMEN - Documentation and Production Gates

Updated7November2026 (IST). Documentation reduces uncertainty; it does not demonstrate fun or a running game. The previous written/missing/complete tables mixed obsolete information with production acceptance. This index now distinguishes **specified**, **implemented** and **verified** using [PROJECT_STATUS.md](PROJECT_STATUS.md).

## 1. Sources of truth

- Cross-domain decisions: [DECISIONS.md](DECISIONS.md).
- Jam content: [JAM_SLICE.md](JAM_SLICE.md); schedule: [PRODUCTION_PLAN.md](PRODUCTION_PLAN.md).
- Gameplay semantics: [SYSTEMS.md](SYSTEMS.md); overview: [GDD.md](GDD.md).
- World/history: [WORLD_BIBLE.md](WORLD_BIBLE.md), [LORE_LEXICON.md](LORE_LEXICON.md).
- Technical contracts/budgets: [TECH_DESIGN.md](TECH_DESIGN.md).
- Dated audit and validation: [DOC_AUDIT.md](DOC_AUDIT.md), [architecture traceability](architecture/traceability.md).

Markdown is the design source. PDFs are generated presentations; their cover/build metadata must identify their source snapshot/date. Historical refinement reports preserve findings at3d88239 and are superseded by the adopted decisions and current domain docs.

## 2. Gate A: required for the jam

Every listed spec exists. Its production acceptance remains open until evidence is attached; existence is not completion.

| ID | Specification | Production acceptance artifact |
|---|---|---|
| A1 | [GAME_FEEL.md](GAME_FEEL.md) | Input/accepted-face capture, timing measurements and first-player feedback |
| A2 | [TUNING.md](TUNING.md), [CSV](../tuning/jam_tuning.csv) | Typed data/fixture checks, Unity import and actual encounter results |
| A3 | [JAM_SLICE.md](JAM_SLICE.md) | Exact baseline beats playable in hosted Unity build |
| A4 | [FIRST_10_MINUTES.md](FIRST_10_MINUTES.md) | Timed fresh-player session, comprehension and zero-choice path |
| A5 | [UX_SPEC.md](UX_SPEC.md), [ACCESSIBILITY.md](ACCESSIBILITY.md) | Integrated screen/state captures and assist/input/storage checks |
| A6 | [ASSET_LIST.md](ASSET_LIST.md) | Required runtime assets imported, canon checked, source/provenance retained |
| A7 | [AUDIO.md](AUDIO.md) | All required cues/mix/loop checks; muted information preserved |
| A8 | [JAM_SCRIPT.md](JAM_SCRIPT.md) | Beat/line IDs, boards or in-engine staging, skip-safe outcomes |
| A9 | [PLAYTEST.md](PLAYTEST.md) | Actual dated observations; automated scenarios labelled separately |
| A10 | [QUALITY_BAR.md](QUALITY_BAR.md), [QA_TEST_PLAN.md](QA_TEST_PLAN.md) | Candidate review and critical-path regression, no blocking defect |
| A11 | [TECH_DESIGN.md](TECH_DESIGN.md) | Empty and gameplay Web builds, exact rules fixtures, measured budgets |

Write changes only to resolve a decision, observed defect or missing interface. Do not postpone development for more speculative lore. Conversely, a necessary correction is not forbidden by an obsolete no-new-documents date.

## 3. Gate B: full-game specification coverage

| Domain | Existing documents | Next production artifact |
|---|---|---|
| Campaign | [STORY.md](STORY.md), [ACT_DESIGN.md](ACT_DESIGN.md), [BESTIARY.md](BESTIARY.md) | One integrated act with prerequisites, counters and aftermaths |
| Cast/relationships | [CHARACTER_BIBLE.md](CHARACTER_BIBLE.md), [BOND_ARCS.md](BOND_ARCS.md) | Recruit/guest/catch-up and bond flag graph; complete local dialogue data |
| Lore/places/voice | [LOCATIONS.md](LOCATIONS.md), [NARRATIVE_STYLE.md](NARRATIVE_STYLE.md), world/lexicon above | Source-checked glossary and scene references, bounded spoiler tiers |
| Progression | [ECONOMY_PROGRESSION.md](ECONOMY_PROGRESSION.md), SYSTEMS above | Legal full-act economy/combat simulator and observed play |
| Experience | [PLAYER_EXPERIENCE.md](PLAYER_EXPERIENCE.md) | Pacing/quiet-beat evidence and player recall |
| Art pipeline | [ART_DIRECTION.md](ART_DIRECTION.md), [ARTBOOK_PRODUCTION.md](ARTBOOK_PRODUCTION.md), [prompts](../art/HIGGSFIELD_PROMPTS.md) | Repeated accepted actor/stage/export process |
| Representation | [CULTURAL_CONSULTATION.md](CULTURAL_CONSULTATION.md) | Source/uncertainty log; any actual external review clearly recorded |
| Language | [LOCALISATION.md](LOCALISATION.md) | String table, font/expansion testing and verified target-language review |
| Telemetry | [TELEMETRY.md](TELEMETRY.md) | Post-jam opt-in implementation only after consent/data contracts |
| Market | [MARKET_POSITIONING.md](MARKET_POSITIONING.md), [MARKETING_PLAN.md](MARKETING_PLAN.md) | Evidence-based platform/store/trailer decision |
| Rights/provenance | [LEGAL_IP_AI.md](LEGAL_IP_AI.md), [AI_DISCLOSURE.md](AI_DISCLOSURE.md) | Final shipping manifest and actual disclosure |
| Team/tooling | [TEAM_HANDBOOK.md](TEAM_HANDBOOK.md) | Reproducible import/build/export instructions and review evidence |

Future catalog entries and advanced systems have the explicit readiness/validation gates in SYSTEMS. Their named design is not a claim that full production data, line-by-line scripts, rigs, localization or tests already exist.

## 4. Acceptance vocabulary and change propagation

**Specified:** interface/behavior/owner/acceptance known. **Implemented:** source/content exists and runs in its intended context. **Verified:** named check passed on a recorded revision/device. **Not in scope:** deliberately excluded from the current build. Avoid unqualified green checks and estimates labelled as measurements.

When a rule changes: update DECISIONS and affected domain docs, CSV/content fixtures and reference tools, traceability and regression cases, then regenerate affected books and update their provenance. Record unresolved production work in the backlog; do not keep a contradicted proposal beside a current requirement without a historical label. Run the documentation validator after integration.
