# ZERO-SUM: OMEN — UX and onboarding contract

Updated 7 November 2026 IST. **Specified, not implemented in Unity.** Current jam is the Meridian Prologue in JAM_SLICE; advanced world-map/market/camp screens are expansion gates.

## 1. Principles

At a glance: eligible actor, accepted digit, resolved pattern, enemy intent, party stake and separate NIL identity. Diegetic art supplies framing, while readable semantic UI carries mechanics. Colour is never the only cue. Two lines is a dialogue pacing target, not a ban on accessible help, settings or a readable rules log. Critical information is not hidden behind hover/long-press.

## 2. Required jam flow

Title (Settings/Credits) → interactive Rain Alley rescue → Naming → solo Hound → Vesper joins → two-hero Hound → one free charm choice → Varro → mercy/rooftop map ending → Results/Replay. Pause and settings are available throughout. Continue appears only for a valid saved checkpoint. No mandatory myth montage before first input. Targets: Start→first action≤20 s; Start→lucky choice≤60 s; cold download measured separately.

## 3. Required screens and controls

|Screen |Always readable |Mouse/touch |Keyboard |
|---|---|---|---|
|Title |Start/validated Continue/Settings/Credits; sandbox label where applicable |Tap/click |Tab/arrows+confirm |
|Naming |All 10 digits, selected resonance, one-line description, confirm/back |Select thenconfirm |Focusdigit+confirm; Back |
|Audit |NILNa N identity, shared Audit Omen+Balance, enemy stake/intent, actor eligibility, actual/scoring reel, Favour state |Tapactor, tapstop |1/2 actor, Space/Enterstop |
|Charm choice |Three names/effects; single choice; no prices |Tapitem+confirm |Focusitem+confirm |
|Varro jar |Stored digit, active substitution, rounds/defences to expiry, restoration cue, phase warning |On-demand extra help optional |Help binding optional |
|Story |Speaker, subtitles, advance/skip, readable text |Advance/Skipbuttons |Confirm/Skip |
|Pause |Resume/Settings/Restartcheckpoint/Title |Tap |Keyboardfocus+Back |
|Results |Win/loss, biggest finalized damage, encounter outcome, retry/replay/newnumber |Tap |Focus+confirm |
|Settings |Audio, Reduced Motion, Assist, hold-to-stop, text scale, fast presentation; clear saved state |Standardcontrols |Fullfocuspath |
|Credits/disclosure |Creators/tools/sources/provenance and AIuse |Scroll |Scroll/back |

Naming confirmation avoids accidental permanent selection; combat focus never traps the player in an unfocused canvas. Tooltips cannot cover the stop line. Required story advance is user-paced; optional log may scroll. A Restart confirmation names exactly which checkpoint progress resets; it is ordinary product UX, not an assistant approval flow.

## 4. Layout and text

1920×1080 design with 5%safe area, tested at 1280×720 and common embedded ratios. Top: land reel/Favour and concise intent; left:party/right:enemy; lower unobstructed action prompts and settings/pause access. Keep NILidentity and party Audit in visibly different frames. The chosen resonance digit is not a health value.

Target minimum body 28 px at 1080 p (about 19 px at 720 p), high-contrast tabular Omens 44 px+, damage 64 px+; test actual visual size, text scales 100/125/150%. Large values use locale-aware grouping and full-value details; never hide the stopped digit in rounding. Big Shoulders Display/Barlow Semi Condensed are candidates, with bundled licensed fonts and complete fallback chains. No critical text baked into generated art.

## 5. Input states

Only eligible actors can be chosen; two-person round must use both. One stop per active wheel; hold-to-stop releases only that wheel. During presentation, Skip/Fast controls work; during active wheel they do not masquerade as stops. Pause/focus loss freezes Coreclock and clears pending pointer states. Resume shows a short recap and waits for deliberate input. Hover and long-press are optional help, never the only way to learn a counter.

Reference sandbox supports actual rule testing but lacks the complete story/UI/settings/save path. Its plain buttons/placeholder SVG are not final UX acceptance evidence.

## 6. Accessibility baseline

Required implementation: keyboard-only, mouse-only and touch-only critical path; no simultaneous actions; named/focused controls; Reduced Motion/no full-screen flash, assist speed×0.7, hold-to-stop, text scale, non-colour pattern names/shapes, subtitles/speakers, skip and pause. No essential timed text. Actual accepted stop remains visually honest under every setting. ACCESSIBILITY defines broader options and evidence.

## 7. Expansion screen gates

Map, market, shrine/forge, camp swap, bonds, gear, codex, charged ultimate portraits and extended-reel UI are disabled until their SYSTEMS domain gates and corresponding wireframes/interaction tests exist. Market requires transactional prices/offers; camp requires active NIL+two legalslots and separate narrative/mathematical bond readouts; advanced preview must use the same Coreevaluator. Do not expose empty tabs or nonfunctional prompts in jam.

## 8. Acceptance

Required wireframes and final captures belong to accepted asset IDs in ASSET_LIST. Test all 10 chosen digits, one-handed input modes, storage unavailable,150%text, reduced motion, focus loss, first-time player comprehension and rerun/retry. A document or missing wireframe path is not evidence of a finished screen. Record findings under PLAYTEST/QA; no sessions are claimed here.
