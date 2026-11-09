# ADR-0006: Reproducible AI production and evidence

Status: **adopted specification** · Updated8November2026 IST · Unity implementation: **not started**.

## Context

The jam is the Meridian Prologue. [Canonical decisions](../DECISIONS.md) resolve rules/scope conflicts; [technical design](../TECH_DESIGN.md) provides detailed contracts. This ADR allocates ownership and acceptance evidence. It does not certify an installed engine feature or a finished build.

## Decision

Use AI-authored source scripts and installed/free tools as the default production route. Optional generators require actual account/quota/cost evidence; never resubmit an uncertain charged job blindly. Record per-file source/provider/process, reference/input hashes, intended use, exclusions and readiness. Keep meaningful text/digits code-native. No mandatory human finishing or runtime AI service is part of the pipeline.

Markdown is canonical. Derivative books and manga retain offline source-linked manifests, explicit source/native/export resolution, clean/text separation and truthful captions. Check/link/data scripts enforce integrity but never promote a candidate to accepted runtime art. Preserve historical baseline inventories as historical: their old hashes and defect prose are not current assertions.

Exact expected state fixtures precede simulation statistics. Required production gates cover importer, smoke, retry, replay and actual hosted Web performance. Record allten digits/three rewards/input/settings/storage routes, actual build/content/source hashes, unresolved S1/S2 defects and player observations. Jam telemetry is local and explicitly exported; any future service remains default-off behind consent/security/privacy review.

## Requirements addressed

IDs remain stable in [the registry](tr-registry.json); requirement source and required proof are in [traceability](traceability.md).

|Requirement ID|Contract|Acceptance gate|
|---|---|---|
|TR-TOOL-001|Each asset carries stable ID/version, canon locks, source/reference hash, dimensions/camera, provider/process and candid readiness.|A-PROVENANCE|
|TR-TOOL-002|AI authors/scripts every production stage; installed/free tools default; no mandatory human finishing or runtime generation.|A-PROVENANCE|
|TR-TOOL-003|Book builders provide check/html-only/output-dir, offline fonts and blocked remote requests; derivative manifests hash inputs.|D-EXPORT|
|TR-TOOL-004|A generated file/job or render establishes candidate existence; accepted runtime status needs import/motion/readability/budget/provenance.|A-ASSET|
|TR-TOOL-005|Maintain independent exact rule fixtures/shared examples before statistics; reference tests do not certify DOM or Unity.|Q-CORE|
|TR-TOOL-006|Automate content, smoke, retry, replay and hosted Web gates with explicit artifact evidence.|Q-SMOKE|
|TR-TOOL-007|Test allten choices and allthree charms, both two-hero orders, jar expiry with extra turns and blocked storage.|Q-SMOKE|
|TR-TOOL-008|No required-path S1/S2; preserve source/content/build hashes and exact submitted artifact; no inferred playtest approval.|Q-RELEASE|
|TR-TOOL-009|Jam uses local explicit replay export and observer notes; no automatic telemetry/network calls or install IDs.|Q-WEB|
|TR-TOOL-010|Any future service needs purpose/schema, default-off consent, retention/deletion/security/privacy review before collection.|T-SERVICE|
|TR-TOOL-011|Validate later-act power/phase pools using legal NIL-containing parties, actual passives/defence/offers and stated aim/seed assumptions; formula arithmetic alone cannot establish fight length or synergy necessity.|F-BALANCE|

## Consequences and open evidence

Automated local checks establish only their stated domains. Final book/PDF page counts, image integrity and layout acceptance belong to dated generation reports; no total is guessed here. No cultural approval, rights clearance, player success, accessibility certification, Unity build or release submission is created by a manifest or this ADR. Release requires the exact uploaded artifact and a preserved source/tag/hash.

## Verification

Run `python tools/check_docs.py` for source/ADR/link/data integrity. Existing reference checks and missing Unity evidence are recorded per requirement in the registry. A mapped requirement remains **specified** until the named runtime gate has actual evidence. [Architecture overview](architecture.md) defines layer ownership and the next integration gate.
