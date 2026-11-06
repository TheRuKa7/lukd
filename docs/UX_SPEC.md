# ZERO-SUM: OMEN — UX, Menus, Diegetic UI and Accessibility (Gate A5)

Minimal UI only works if every state is still readable. Every screen is an object from the world (GDD §8); every piece of information has one place. Accessibility for the full game is in [`ACCESSIBILITY.md`](ACCESSIBILITY.md); this is the jam-ready baseline.

---

## 1. Rules
1. **Diegetic first.** If it can be an object in the world, it is (the reel is a sign, the map is a scroll, the shop is a stall).
2. **One glance.** In combat the player can always answer at a glance: whose turn, which hero is next, what the enemy will do, how much Balance is left.
3. **Two lines max** of text at a time; no tooltips during a spin.
4. **Colour never carries meaning alone:** every colour cue has a shape or a number.
5. **Everything is reachable with one hand**: tap/click, Space/Enter, number keys 1–3, Esc.

## 2. Screen flow

```
Title ─► (New game) Intro ─► Naming shrine ─► Combat ⇄ Map ─► Market / Shrine / Teahouse / Story ─► Boss ─► Act end ─► Hap's Dream ─► next act
  │                                                                                                         │
  └─► Continue ─► Map              Pause (any time): Resume · Codex · Settings · Quit to title           Results / Game over ─► Retry act / New number
```

## 3. Screens

| Screen | In-world object | Always visible | On demand | Input |
|---|---|---|---|---|
| **Title** | A rain-wet Nixie sign: ZERO-SUM: OMEN; NaN flickers | Start / Continue / Settings | Credits | Tap |
| **Naming shrine** | Ten Nixie tubes in a shrine niche | The ten digits | One line per digit on hover | Tap a tube; confirm by tapping again |
| **Combat** | The diorama stage; the land's reel object at top centre; charms pinned to its frame | Omens over every head (two digits); the reel; whose turn (the active hero steps forward and glows); enemy intent icon over the enemy (one icon); Open Hand sigil; Land Law icon | Hold a hero: their wheel, passive and ultimate gauge. Hold the enemy: its rule. Hold a charm: its rule | Tap hero / 1–3 to choose; tap / Space to stop; hold to fast-forward |
| **Ultimate ready** | The hero's portrait card flips gold at the screen edge | Gauge as a ring around the portrait | — | Tap the portrait |
| **Map** | Land-styled (scroll, palm leaf, mosaic, road map) | Nodes as icons; your path; the boss at the end | Hold a node: one line | Tap a node |
| **Market** | A stall with wares on the table | 3–5 items with price tags | Hold an item: rule + flavour line | Tap to buy; tap the bell to re-roll |
| **Shrine / Forge** | Ofuku's shrine / Maeve's anvil | One choice of 2–3 | — | Tap |
| **Open Hand shrine** | A stone hand with a die | Re-deal · Pray · Offer | — | Tap |
| **Teahouse / Campfire** | Heroes sit around a fire; NIL at centre | Party slots beside NIL; constellation lines between digits (bonds) | Hold a hero: kit card | Drag a hero beside NIL, or tap to cycle |
| **Story** | Full-screen stills + motion graphics, or video | Speaker name tab + 2 lines | Log (last 20 lines) | Tap to advance; hold to fast-forward |
| **Results** | A receipt printed by a Basilica terminal | Biggest number, patterns found, rounds, time | — | Tap |
| **Game over** | Your Omen flips to 00 like a departure board; "SETTLED" stamp | Retry act (keep the build you had at act start) · New number | — | Tap |
| **Pause** | The ledger book closes over the screen | Resume · Codex · Settings · Quit | — | Esc / tap the corner |
| **Codex** | NIL's notebook | Patterns, charms seen, enemies met, people met, lore, each with a GIF or sketch | — | Tabs |

## 4. Combat layout (1920×1080 reference; scales to 16:9 and 16:10; safe area 5%)
- **Top centre:** reel object (3 tubes), Land Law icon left of it, Open Hand sigil right of it, charms along its frame.
- **Left half:** party (up to 3), standing; Omens over heads; ultimate portraits in the lower-left corner.
- **Right half:** enemy (or bosses that fill the right two-thirds); its Omen and intent icon above it.
- **Centre:** the active wheel appears over the striker.
- **Bottom:** clear (the hit numbers and Link Art bands need it).

## 5. Text and numbers
- Fonts: display Big Shoulders Display (numbers, banners), body Barlow Semi Condensed, code-ish JetBrains Mono (ledger/receipts); Noto for CJK and Devanagari.
- Minimum sizes at 1080p: body 28 px, numbers over heads 44 px, damage numbers 64 px+.
- Numbers: tabular figures; Omens always two digits ("07"); large damage numbers use thin spaces (12 000 000) and switch to short form above a billion (1.2 B) with the full number on hold.

## 6. Settings (jam)
Master/music/SFX/voice volume · **Reduced motion** (no shake, no flashes, short cinematics) · **Assist** (wheels −30%, hold-to-stop) · **Text size** (100/125/150%) · **Colour-safe digits** (shapes on pattern colours) · Subtitles (on by default) · Fast cinematics · Screen shake intensity · Language (English for the jam).

## 7. Accessibility baseline (jam must-haves)
- Reduced motion; flash limit (no more than 3 flashes per second; checked with a photosensitivity tool).
- Assist mode and hold-to-stop for players who can't time taps.
- Every pattern has a shape and a sound, not just a colour.
- All story text is subtitled; speaker names always shown.
- Full mouse-only, touch-only and keyboard-only play.

**Done when:** each screen above has a wireframe in `art/ui/wireframes/` and every setting in §6 works in the jam build.
