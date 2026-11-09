# ADR-0002: Deterministic Audit rules

Status: **adopted specification** · Updated8November2026 IST · Unity implementation: **not started**.

## Context

The jam is the Meridian Prologue. [Canonical decisions](../DECISIONS.md) resolve rules/scope conflicts; [technical design](../TECH_DESIGN.md) provides detailed contracts. This ADR allocates ownership and acceptance evidence. It does not certify an installed engine feature or a finished build.

## Decision

A pure synchronous Core takes validated state plus accepted commands and returns a complete immutable result/ledger. Unity presentation never recomputes damage. State contains separate actual/scoring digits, source-tagged effects, current Balance snapshot, actor eligibility and terminal status. Use checked bounded integer arithmetic; future rational modifiers use fixed-point thousandths and the declared final rounding stage.

Resolve exactly in SYSTEMS order. Three actual stops precede single atomic settlement; Vesper reconciles all provisional strikes, Reaper reads pre-damage current Balance and simultaneous party zero loses. Terminal state rejects later commands/events. Pattern Sight invokes a pure preview of the same evaluator without consuming RNG/charges. Varro is an explicit idle/holding/restoring/spent token state machine; cancelled enemy actions cannot hide expiry or consume the phase warning.

Pin named gameplay RNG streams and accepted-face/tick command replay; visual noise uses a separate generator. A random-phase exposure model is not a human timing model. Optional abilities use typed event/domain/reset/cap contracts and generated effects cannot recursively re-enter their source.

## Requirements addressed

IDs remain stable in [the registry](tr-registry.json); requirement source and required proof are in [traceability](traceability.md).

|Requirement ID|Contract|Acceptance gate|
|---|---|---|
|TR-RULE-001|Keep resonance, Civic Omen, Balance and normalized Audit Omen distinct with valid integer bounds.|Q-CORE|
|TR-RULE-002|Store actual and scoring digits separately with immutable round ledger and effect provenance; settle once after three stops.|Q-CORE|
|TR-RULE-003|Order replacements, repair, wilds, bonuses, modifiers and atomic damage; check intermediate bounds and floor at declared stage.|Q-CORE|
|TR-RULE-004|Evaluate one base pattern by exact priority with chosen4 Overwrite, no-wrap Cascade and sum10/20 Zero-Sum.|Q-CORE|
|TR-RULE-005|Snapshot current balances/Omens for Reaper; simultaneous party zero loses; no events after terminal state.|Q-CORE|
|TR-RULE-006|Parry, Fortune, chosen-zero overlap and Ofuda emit one defended event with exact reflection policy.|Q-CORE|
|TR-RULE-007|NIL required; legal solo/two/three-actor selection; active Vesper7 retroactively adds7 to every strike per actual7.|Q-CORE|
|TR-RULE-008|Varro capture occurs once after first nonterminal round; holding/release/restoration survives skipped enemy actions.|Q-CORE|
|TR-RULE-009|Varro half-stake phase telegraphs one remaining40 action before80; cancelled action does not consume warning.|Q-CORE|
|TR-RULE-010|Starter face IDs/lists preserve actual zero/chosen digit, widths and logical motion units; target absent faces is invalid.|Q-CONTENT|
|TR-RULE-011|Latch displayed face on accepted input and preserve it during deceleration; gameplay RNG separate from visual RNG.|Q-REPLAY|
|TR-RULE-012|Pattern Sight previews each legal third face through replacements/repair without consuming state or RNG.|Q-CORE|
|TR-RULE-013|Favour warm/recovery and Black Cat visibly replace scoring third-to-first once, with Black Cat precedence and retry reset.|Q-CORE|
|TR-RULE-014|Only one free choice from three typed jam charms; selection and retries never duplicate the reward.|Q-RETRY|
|TR-RULE-015|Wild assignment chooses priority, multiplier then lexical order; actual landing domain remains unchanged.|F-KIT|
|TR-RULE-016|Extended reels score entire4/5-digit domain with zero-strike extra slots, declared priority and bounded numeric validation.|F-REEL|
|TR-RULE-017|Every future ability/passive needs owner/unlock, input domain, cap, duration, replacement/reset policy and exact counter.|F-KIT|
|TR-RULE-018|Awakening benefits differ from baseline; branch/respec choices persist by ID and cannot age Hina early.|F-AWAKEN|
|TR-RULE-019|Evaluate active mathematical bonds separately from narrative bonds; zero is not ordinary Complement; all parties include NIL.|F-BOND|
|TR-RULE-020|Link Arts and generated effects use tagged bounded bundles; one activation and depth1 prevent recursive attack/charge chains.|F-LINK|
|TR-RULE-021|Party charm sets count separate personal gear;3/5 equipped thresholds; each of63 candidates needs exact typed event data.|F-CHARM|
|TR-RULE-022|Land Laws require typed entry/exit scope, event/domain, exact modifier/order/stack/reset, readable intent and accessible same-land counter; narrative briefs are not numeric runtime data.|F-LAND|

## Consequences and open evidence

Node/Python references and authored fixtures exist; they do not establish C# or editor/Web parity. Port expected outcomes before porting UI. Wilds,4/5 reels, bonds, Link Arts, awakenings and full charm catalogue remain disabled candidates. Per-ability numeric limits, content records and balance/playable-counter evidence remain open even though the Core extension boundary is mapped.

## Verification

Run `python tools/check_docs.py` for source/ADR/link/data integrity. Existing reference checks and missing Unity evidence are recorded per requirement in the registry. A mapped requirement remains **specified** until the named runtime gate has actual evidence. [Architecture overview](architecture.md) defines layer ownership and the next integration gate.
