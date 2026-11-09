# ADR-0005: Input, presentation and accessibility

Status: **adopted specification** · Updated8November2026 IST · Unity implementation: **not started**.

## Context

The jam is the Meridian Prologue. [Canonical decisions](../DECISIONS.md) resolve rules/scope conflicts; [technical design](../TECH_DESIGN.md) provides detailed contracts. This ADR allocates ownership and acceptance evidence. It does not certify an installed engine feature or a finished build.

## Decision

Flow owns a monotonic gameplay clock and command eligibility. Capture the face actually under the stop line at the accepted input; deceleration only presents the result. Pause/focus loss freezes gameplay time and clears stale presses; resume requires deliberate input. One wheel accepts one stop, and hold-release cannot leak into a later wheel.

Presentation consumes immutable results for character motion, hit contact, UI, audio and camera. Skip/Fast/Pause never grant damage/rewards. Show distinct identity/resonance/Audit frames, actual versus resolved digits, legal actor state, intent and the jar token/progress. Word/shape/colour all communicate patterns. Required paths work by keyboard, mouse and touch independently, with assist0.7, hold-to-stop,150% text, subtitles and reduced motion. Audio unlocks on gesture; optional Web video has static/error fallback and cannot determine gameplay events.

Treat source art, game sprites, actual model turnarounds, environment plan/cameras and manga panels as different products with honest status. Keep exact text/digits separate. Asymmetry,64px silhouette, world scale, hidden surfaces, pivots/contact and animation need source plus in-engine checks. Current manga production is Mangaka-native22x30 B&W story pages, governed by the revised user policy and docs/manga hierarchy. Ordinary-image20-page artifacts are user-rejected studies. Native output formats/layers must be verified before new-series pages/panels/dialogue/transcript are adapted; a read-only collectible stays isolated from campaign state and uses spoiler-aware unlocks.

## Requirements addressed

IDs remain stable in [the registry](tr-registry.json); requirement source and required proof are in [traceability](traceability.md).

|Requirement ID|Contract|Acceptance gate|
|---|---|---|
|TR-VIEW-001|Use monotonic gameplay clock and accepted command eligibility; pause/focus loss freeze time and clear stale input.|Q-REPLAY|
|TR-VIEW-002|In-engine skippable/speedable gameplay feedback reads immutable results and never changes damage or RNG.|Q-SMOKE|
|TR-VIEW-003|Optional URL-backed bundled video has subtitles and immediate still/error fallback; no event relies on frame accuracy.|Q-WEB|
|TR-VIEW-004|Title gesture unlocks audio; mute/background resume and platform load settings are tested.|Q-WEB|
|TR-VIEW-005|Every required screen exposes readable state, valid focus and mouse/touch/keyboard path; Naming confirms choice.|Q-SMOKE|
|TR-VIEW-006|Separate NIL identity/resonance from shared Audit frame; actual/scoring reel, jar progress and enemy intent remain legible.|Q-SMOKE|
|TR-VIEW-007|Design1080p with5% safe area, body28px target and text100/125/150%; no generated/baked critical text.|A-VISION|
|TR-VIEW-008|One accepted stop per eligible active wheel; hold release belongs to that wheel; skip cannot masquerade as stop.|Q-SMOKE|
|TR-VIEW-009|Word/shape/colour pattern labels, subtitles/speakers, pause/skip, assist0.7 and hold-to-stop form jam baseline.|Q-SMOKE|
|TR-VIEW-010|No timed reading/choice or compulsory manual; settings changes record events without silently moving active phase.|Q-REPLAY|
|TR-VIEW-011|Reduced Motion removes shake/spins/parallax wobble/full-screen flash; effects preserve accepted-digit readability.|A-MOTION|
|TR-VIEW-012|Accessibility acceptance records actual device, mode, settings and recovery evidence, including150% text and focus loss.|Q-SMOKE|
|TR-VIEW-013|Future rebind, slower tiers, one-switch and strategy legal-face mode preserve scoring/input/replay semantics.|A-MOTOR|
|TR-VIEW-014|Future screen reader needs supported engine API, names/order/live summaries and avoids announcing every scrolling face.|A-READER|
|TR-VIEW-015|Turnarounds use actual anatomical front/left/right/back, scale and asymmetry; no mirrored front substituting unseen surfaces.|A-ASSET|
|TR-VIEW-016|Environment has coherent plan/2.5D/front views, metric grid and clear24x6m battle floor.|A-ASSET|
|TR-VIEW-017|Layered actors, pivots/contact/hidden surfaces and exact separate lettering are required beyond concept/blockout existence.|A-ASSET|
|TR-VIEW-018|Produce49 Mangaka-native B&W chapters of22 story pages each (1,078 total), in seven sequential volumes of seven chapters, with English LTR reading order and separate colour supplements; ordinary image jobs cannot produce story pages.|M-SERIES|
|TR-VIEW-019|Adapt accepted native-series exports into stable page/panel/dialogue metadata, transcript/localization, crops and a read-only spoiler-aware reader; clean/lettered separation needs actual supported output or validated processing.|M-ADAPT|
|TR-VIEW-020|Display accepted-input feedback within one rendered frame and target<=50ms end-to-end; keep digits readable and mandatory noninteractive waits<=3s with immediate skip.|Q-FEEL|

## Consequences and open evidence

The renderer/UI framework, supported accessibility API, input binding implementation and runtime rig have not been selected/verified. Screen reader, strategy mode, locales and adaptive comic adapter are separate future gates. Source blockouts and clean/lettered comic exports are useful evidence of artifacts, not gameplay acceptance. Final flash analysis, disabled-player feedback and all native-series chapters’ visual review cannot be inferred from file checks.

## Verification

Run `python tools/check_docs.py` for source/ADR/link/data integrity. Existing reference checks and missing Unity evidence are recorded per requirement in the registry. A mapped requirement remains **specified** until the named runtime gate has actual evidence. [Architecture overview](architecture.md) defines layer ownership and the next integration gate.
