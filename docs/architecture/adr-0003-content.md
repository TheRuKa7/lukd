# ADR-0003: Typed content and progression gates

Status: **adopted specification** · Updated8November2026 IST · Unity implementation: **not started**.

## Context

The jam is the Meridian Prologue. [Canonical decisions](../DECISIONS.md) resolve rules/scope conflicts; [technical design](../TECH_DESIGN.md) provides detailed contracts. This ADR allocates ownership and acceptance evidence. It does not certify an installed engine feature or a finished build.

## Decision

Content import produces versioned immutable assets from stable typed IDs. Reject invalid schema, duplicate/unknown IDs, missing required values, nonfinite scalars, unit/range violations, dangling references and illegal face lists. Predicates live in Core; numeric CSV contains parameters only. Encounters, choices, dialogue and future ability records are structured data, never arbitrary runtime expressions. Hash the generated content alongside rules/build versions.

Author the jam as a small explicit graph: rescue→Naming→solo Hound→Vesper→two-hero Hound→one free charm→Varro→mercy/roof→results. Choice acceptance and unlocks are transactions. Authored tutorial stops are named overrides rather than alleged random results. Future screens/offers stay unavailable until their individual system gates pass.

Expansion supports typed wheel/enhancement, economy, Ink, sticks, Karma, gems, tree, Deals, loop and bounded custom recruit records. The registry maps each family separately. Localization uses stable namespaces/IDs, placeholders/context and per-locale font/shaping/layout gates; critical text remains outside generated images.

## Requirements addressed

IDs remain stable in [the registry](tr-registry.json); requirement source and required proof are in [traceability](traceability.md).

|Requirement ID|Contract|Acceptance gate|
|---|---|---|
|TR-CONTENT-001|Import exact schema/version, unique required keys, finite scalar ranges/units and valid references; fail invalid build content.|Q-CONTENT|
|TR-CONTENT-002|Keep predicates in Core and numeric inputs in tuning CSV; structured faces/encounters cannot be executable formula strings.|Q-CONTENT|
|TR-CONTENT-003|Record rules/content/build version, pinned PRNG streams, accepted face/tick/order and settings/tutorial overrides.|Q-REPLAY|
|TR-CONTENT-004|Authored graph covers rescue, Naming, solo Hound, recruit, two-hero Hound, one charm, Varro, mercy/roof and results.|Q-SMOKE|
|TR-CONTENT-005|Unavailable future map/market/camp/gear/gauge screens remain disabled until domain gates and wireframes pass.|Q-CONTENT|
|TR-CONTENT-006|Teach one rule, let player demonstrate it, then combine; authored outcomes are explicit tutorial exceptions.|Q-SMOKE|
|TR-CONTENT-007|Wheel enhancements have explicit faces, min4 remaining, stacking/expiry/shatter IDs and actual-versus-scoring domains.|F-WHEEL|
|TR-CONTENT-008|Economy uses bounded per-node payouts/caps and explicit faucets/sinks; no UI/timer/retry income.|F-ECON|
|TR-CONTENT-009|Ink consumes one declared scoring replacement without replaying actual landing or charge.|F-INK|
|TR-CONTENT-010|Oracle sticks have24 authored poems/boons/visible prices, deterministic offers and safe decline.|F-STICK|
|TR-CONTENT-011|Karma gains once per event, caps9, prices reroll/guard explicitly and cannot create a lethal-guard loop.|F-KARMA|
|TR-CONTENT-012|Gem levels use owned stable IDs and rational deltas/caps that materially differ from baseline.|F-GEM|
|TR-CONTENT-013|Seven tree branches use node IDs, prerequisites and unique costs/rewards; graph cannot cycle or soft-lock required path.|F-TREE|
|TR-CONTENT-014|Deals have12 authored boon/real-price records, safe decline and rollback without negative/inaccessible wheels.|F-DEAL|
|TR-CONTENT-015|House loops retain party build/stake, reset declared enemy/reel state everythird round, cap3 then final phase.|F-LOOP|
|TR-CONTENT-016|Custom recruits use bounded authored name/look/kit templates and cannot gate the central ending.|F-CUSTOM|
|TR-CONTENT-017|String/asset importer uses stable IDs, context, variables, fallback and duplicate/placeholder validation.|L-IMPORT|
|TR-CONTENT-018|Bundle licensed fonts; validate real glyph shaping/fallback/atlas memory on pinned engine, not assumed conjunct support.|L-FONT|
|TR-CONTENT-019|Enable each locale only after placeholder, overflow, shaping, focus, skip and memory gates; save stable locale ID.|L-ENABLE|
|TR-CONTENT-020|Expansion encounters model target groups/pools, legal target previews, phase thresholds, replacement/armour tags and declared overflow; each required party retains a counter.|F-ENCOUNTER|
|TR-CONTENT-021|Keeper trials use separate nonlethal objectives/progress, supplied safe resources, retry/help and protected-item alternatives rather than human damage/death state.|F-TRIAL|
|TR-CONTENT-022|Scene/recruit/ending flags are prerequisite-checked and idempotent; catch-up core recruits/pieces and six-Seal-plus-resonance finale remain reachable without secret recruits or epilogue events.|G5|

## Consequences and open evidence

The Python model imports scalar CSV. Browser defaults are explicit tested values and are not an importer. Unity importer/localization tables/encounter graph are unimplemented. Candidate catalogue pitches are insufficient records: exact amounts, targets, limits, prices, prerequisites and overlaps must be authored before enable. No runtime AI-generated kit/lore or arbitrary custom mechanic is authorized.

## Verification

Run `python tools/check_docs.py` for source/ADR/link/data integrity. Existing reference checks and missing Unity evidence are recorded per requirement in the registry. A mapped requirement remains **specified** until the named runtime gate has actual evidence. [Architecture overview](architecture.md) defines layer ownership and the next integration gate.
