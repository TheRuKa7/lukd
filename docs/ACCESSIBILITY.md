# ZERO-SUM: OMEN — Accessibility Plan (Gate B9)

A timing game must be playable by everyone. The jam baseline is in [`UX_SPEC.md`](UX_SPEC.md) §6–§7; this is the full-game plan, checked against the Game Accessibility Guidelines and the Xbox Accessibility Guidelines.

---

## 1. Motor
| Option | What it does |
|---|---|
| **Assist speed** | Wheels −30% / −50% / −70% |
| **Hold-to-stop** | Press and release instead of a tap; stop on release |
| **Auto-stop on your digit** | Wheels stop themselves on the hero's lucky digit (pure strategy mode); patterns still matter |
| **Input remapping** | Every action rebindable; one-switch mode (a single button cycles heroes and stops) |
| **No simultaneous inputs** | Nothing in the game needs two buttons at once |
| **Timing window display** | Optional: a soft ring shows when the aimed face is under the stop line |

## 2. Vision
- **Colour-safe digits**: every pattern colour also has a shape (dot, ring, chevron, star) and a word.
- Colour-blind presets (protanopia, deuteranopia, tritanopia) for land palettes' key cues; tested with simulators.
- Text size 100–200%; high-contrast UI mode; damage-number size option.
- Screen-reader support for menus (Unity accessibility plugin / OS text-to-speech) post-launch.

## 3. Hearing
- Subtitles on by default, with speaker names and [sound captions] for meaningful sounds ("[four bells toll]").
- Every audio cue has a visual cue (pattern banners, the Open Hand sigil lights, telegraph icons).
- Separate volume sliders; mono audio option.

## 4. Cognitive
- **Codex** with a GIF for every mechanic; **recap** card when resuming a save.
- Hold on any object for its rule (two lines); never timed text.
- **Story mode**: assist speed + enemy Balance −50% + no game over (Settle → retry the round).
- Pause anywhere, including during cinematics.

## 5. Photosensitivity and motion
- No more than 3 flashes per second; full-screen flashes below the luminance threshold; validated with a PEAT-style tool on every cinematic.
- **Reduced Motion** turns off camera shake, slow-mo, full-screen flashes and parallax wobble; shortens cinematics.
- Screen-shake intensity slider.

## 6. Testing
Include disabled players in playtests from the full slice onward (motor, low vision, deaf/hard of hearing). Log issues in the QA tracker with the tag `a11y`.
