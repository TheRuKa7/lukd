# ADR-0004: Versioned checkpoints and journal reconciliation

Status: **adopted specification** · Updated8November2026 IST · Unity implementation: **not started**.

## Context

The jam is the Meridian Prologue. [Canonical decisions](../DECISIONS.md) resolve rules/scope conflicts; [technical design](../TECH_DESIGN.md) provides detailed contracts. This ADR allocates ownership and acceptance evidence. It does not certify an installed engine feature or a finished build.

## Decision

Keep a versioned save envelope with content version and validated settings/checkpoint payload. Jam stores resonance, encounter index, chosen charm or null and unique story-event IDs; no mid-fight save. Retry restores the complete encounter stake/seed/actors and resets Favour, jar and once-per-fight flags together. A selected charm is retained and cannot be re-awarded. Continue requires a compatible validated checkpoint.

Write through a recoverable last-good checkpoint. Test malformed/incompatible/blocked/interrupted storage and true hosted-iframe restrictions; memory-only settings and safe New Game remain usable. Do not claim atomic browser persistence from a PlayerPrefs call alone.

Campaign snapshots and journals are distinct: rollback all act-start gameplay including inventory/equipment/faces/gems/currencies/XP/RNG, then reconcile permanently retained unlock evidence by unique event/reward ID. Explicitly define each retained event’s gameplay consequence. Reader bookmarks remain separate. Future scene adapters stop at live choices/combat and skip only completed idempotent story commits.

## Requirements addressed

IDs remain stable in [the registry](tr-registry.json); requirement source and required proof are in [traceability](traceability.md).

|Requirement ID|Contract|Acceptance gate|
|---|---|---|
|TR-SAVE-001|Persist version/content version, resonance, encounter checkpoint, selected charm, settings and journal IDs; no mid-fight save.|Q-RETRY|
|TR-SAVE-002|Retry restores full stake/seed/actor eligibility and clears jar/Favour/transient charges; selected reward persists exactly once.|Q-RETRY|
|TR-SAVE-003|Atomic last-good recovery, safe repair/New Game and memory settings fallback handle unavailable/corrupt browser storage.|Q-RETRY|
|TR-SAVE-004|Continue is available only for a validated compatible checkpoint.|Q-RETRY|
|TR-SAVE-005|Campaign retains roster/verbs/bonds/faces/gems/level; act transition selects3 active charms and stashes others, floors fenhalf/Karma75%.|G3|
|TR-SAVE-006|Campaign defeat restores complete immutable checksummed act snapshot and reconciles retained unlock journal by unique event/reward IDs.|G3|
|TR-SAVE-007|Mode/challenge flags and reward policy are explicit and versioned; assistance cannot corrupt normal save achievements.|A-MOTOR|
|TR-SAVE-008|Reader bookmarks are separate from campaign checkpoints; read-only reference pages never grant rewards or mutate resonance.|M-READER|
|TR-SAVE-009|Future adaptive cutscenes stop at unresolved live choices/combat and commit only idempotent actual completed events on skip.|M-ADAPTER|

## Consequences and open evidence

The sandbox retries in volatile state and persists only mute. No production save, migration, transaction journal or Unity reader exists. A save corruption test needs an actual serializer/storage adapter. Version migrations, checksums and retained-journal conflict policies must be designed alongside the first full campaign act, before adding markets or durable custom recruits.

## Verification

Run `python tools/check_docs.py` for source/ADR/link/data integrity. Existing reference checks and missing Unity evidence are recorded per requirement in the registry. A mapped requirement remains **specified** until the named runtime gate has actual evidence. [Architecture overview](architecture.md) defines layer ownership and the next integration gate.
