# ADR-0001: Engine and Web viability

Status: **adopted specification** · Updated8November2026 IST · Unity implementation: **not started**.

## Context

The jam is the Meridian Prologue. [Canonical decisions](../DECISIONS.md) resolve rules/scope conflicts; [technical design](../TECH_DESIGN.md) provides detailed contracts. This ADR allocates ownership and acceptance evidence. It does not certify an installed engine feature or a finished build.

## Decision

Use the installed **Unity6000.4.11f1 plus Web module** for the first empty-project viability build. This is the selected test target; package compatibility, licence success and a usable game have not been established. Pin Editor/packages only after that build. Create a plain Core/Content/Flow/Presentation/Meta project boundary with one encounter sequencer. No backend, runtime generation, ECS or remote asset lookup is needed for the jam.

Track Assets plus metadata, ProjectSettings, Packages manifests/lock and reproducible build entry point. Exclude generated player/caches. Select a single host-compatible compression format and test its headers or JS fallback in the actual itch iframe. Desktop WebGL2 leads; mobile/Safari platforms require independent evidence.

The50MB total/25MB initial/512MiB/60fps figures remain planning budgets. Measure network bytes, cold download, Start-to-action separately, load peaks and frame-time distributions on named hardware. Prefer cutting assets/shader/particle scope to silently increasing budgets.

## Requirements addressed

IDs remain stable in [the registry](tr-registry.json); requirement source and required proof are in [traceability](traceability.md).

|Requirement ID|Contract|Acceptance gate|
|---|---|---|
|TR-ENG-001|Separate pure Core, typed Content, single Flow owner, replaceable Presentation and Meta; no Unity clock or rendering in rules.|Q-CORE|
|TR-ENG-002|Offline assets only; jam has no backend, runtime LLM, ECS or paid service dependency.|Q-WEB|
|TR-ENG-003|Pin successful Editor, packages, lock, project settings, Assets/meta and clean build script; ignore generated caches.|Q-WEB|
|TR-ENG-004|Desktop WebGL2 first; mobile remains independently unverified.|Q-WEB|
|TR-ENG-005|One chosen compression format with correct host headers or its tested JS fallback; no inferred alternate-format fallback.|Q-WEB|
|TR-ENG-006|Plan total compressed<=50MB, initial<=25MB, peak<=512MiB and desktop60fps; measure on named hardware.|Q-WEB|
|TR-ENG-007|Budget atlases, shader set, transparency, particles and load allocations from actual target profiling.|Q-WEB|
|TR-ENG-008|Sequence empty build, fixtures/importer, greybox Audit, Prologue, release verification and immutable artifact evidence.|Q-SMOKE|

## Consequences and open evidence

A clean-checkout empty hosted build is the first hard gate. No version-specific API/package claim is accepted from this ADR alone. Current upstream Unity links in TECH_DESIGN span manual versions; validate each used feature against the installed Editor before adoption. No renderer pipeline/package selection is yet implemented. A commercial/console platform and CI licence are later decisions.

## Verification

Run `python tools/check_docs.py` for source/ADR/link/data integrity. Existing reference checks and missing Unity evidence are recorded per requirement in the registry. A mapped requirement remains **specified** until the named runtime gate has actual evidence. [Architecture overview](architecture.md) defines layer ownership and the next integration gate.
