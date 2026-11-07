# ZERO-SUM: OMEN — Accessibility plan

Updated 7 November 2026 IST. This is a **specified testable contract**, not a claim of guideline certification or completed accessibility testing. Jam baseline is UX_SPEC §6; broader features are gated expansion. No AI-only production rule removes player validation.

## 1. Motor and input

Jam: mouse-only/touch-only/keyboard-only path; no simultaneous inputs; assist speed×0.7; hold-to-stop (press/release) alternative; pausing during spin; visible Skip/Fast controls during presentation. No essential action requires a long hold or hover. Focusloss freezes the gameplay clock and clears stale presses. Resume waits for deliberate input. Verify button targets at actual embedded size and repeated/tremor input.

Expansion gate A-MOTOR: rebind all actions, slower tiers×0.5/0.3, one-switch scanning and an explicit strategy stop mode. Strategy mode lets the player select an available face from the actual wheel, rather than always stopping the hero's own digit (which can produce worse patterns). It uses the same scoring and no hidden probability boost. Acceptance: independent players can complete the critical path in the chosen mode; exact accepted outcomes/replays remain valid. Settings unavailable in a build are not advertised as working.

## 2. Vision and reading

Patterns use word+shape+colour; party/identity frames distinguish NaN, resonance and Audit stake. Textscale 100/125/150%jam;200%and high-contrast palette expansion. Preserve layout/focus without obscuring the stop line. Information available on hover is also available through focus and a visible Help route. Test tabular digits, small screens, colour simulators and actual low-vision feedback when available; a simulator is not community sign-off.

Screen-reader support is an explicit expansion gate A-READER: selected Unity accessibility API/package validated against the installed Editor/platform, named controls, focusorder, live combat/result announcements and no repeated speech every scrolling face. It is not promised as implemented at launch without platform tests. Do not insert an unverified third-party plugin into required jam scope.

## 3. Hearing

Subtitles on by default, speaker names and captions for rule-relevant sounds. Every telegraph has a visual label/icon; the stop/result is understandable muted. Separate master/music/SFXcontrols for jam; voice and mono controls become required only when those assets/routes exist. Subtitles survive skip/fastmode without changing story flags.

## 4. Cognitive and timing

Teach one rule at a time, demonstrate and test before combination. No timed reading/choice, no mandatory manual before the first action. Pause anywhere safe including cinematics; checkpoint retry and short resume recap. Explain Varro's stored digit/substitution/counter numerically. Assistance can change during a fight as a recorded settings event, with no mid-input silent phase jump.

Future Story Mode uses explicit data: slower selectable speeds, enemy stake reduction and loss→roundretry; separate mode flag and tested save/reward policy. No central story resolution requires perfect timing or a secret post-ending recruit. A codex is useful only after entries and accessible navigation are implemented.

## 5. Motion and photosensitivity

Reduced Motion disables shake, full-screen flashes, camera spins, parallax wobble and slow-motion; shortens noninteractive reveals. Screen-shake/flash intensity can be adjusted independently. Effects cannot hide accepted digits. Do not treat “≤3 flashes/second” as sufficient safety validation: area/luminance/contrast/pattern also matter. Record analysis tool/version/settings and capture results for each final effect/cutscene. Until performed, status is unverified; no medical/safety certification is claimed.

## 6. Acceptance evidence

QA records input mode, device/browser, setting values, capture and failure/recovery steps. Cover 150%text, muted play, reduced motion, held input/focus loss, repeats, slow-frame conditions and iframe embedding. Invite relevant disabled-player feedback as validation when possible, without outsourcing required asset/code production. Log gaps precisely; do not infer accessibility from a written checkbox. QUALITY_BAR controls release evidence.
