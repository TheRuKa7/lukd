# The Remainder: jam build (Official Unity Game Jam 2026)

A 10–15 minute Meridian Prologue for ZERO-SUM: OMEN, built in Unity 6 (6000.4.11f1) for WebGL. The scope, beats and line text follow [JAM_SLICE](../docs/JAM_SLICE.md) and [JAM_SCRIPT](../docs/JAM_SCRIPT.md); numbers follow [jam_tuning.csv](../tuning/jam_tuning.csv). This is a separate, time-boxed track from the [pre-production plan](../docs/PREPRODUCTION_PLAN.md) and does not change canon.

**Deadline:** 14 November 2026, 17:30 IST (12:00 UTC). Unity and a WebGL build are required; AI use must be disclosed.

## What is in the build

Title, settings and credits → Ama's rescue (authored 07 stop, six units returned) → the Naming (choose 0–9) → a solo Audit against a Debt Hound (scripted tutorial Jackpot, then honest wheels) → Vesper joins and a two-hero Audit (choose who strikes, Pattern Sight) → Gus's free charm (Horseshoe, Black Cat or Ofuda) → Varro and his Debt Jar (slot 3 captured, three rounds or three defences, phase two at half) → mercy, Seal 1 and the rooftop → results, retry or new number.

Systems: the seven base patterns with priority, defence (0 parries, your number reflects), Favour (slower wheels and wider repeated faces after a Bust; Hap's hand repairs after two), the three charms, the jar, retry from the fight checkpoint, chapter checkpoints with Continue, Assist mode, reduced motion, instant text, volume, pause, scene skip, keyboard and mouse.

## Layout

| Path | What |
|---|---|
| `RemainderJam/Assets/Scripts/Rules.cs` | Port of `prototype/rules.js` (patterns, damage, defence, jar, RNG) |
| `RemainderJam/Assets/Scripts/Combat.cs` | The Audit: wheels, rounds, enemy actions, HUD |
| `RemainderJam/Assets/Scripts/Story.cs` | Chapters, with JAM_SCRIPT line IDs in comments |
| `RemainderJam/Assets/Scripts/Game.cs` | Boot, canvas, dialogue, settings, save, title, results |
| `RemainderJam/Assets/Scripts/UI.cs`, `Sfx.cs` | UI builders and the Nixie wheel; synthesised audio |
| `RemainderJam/Assets/Editor/RulesParity.cs` | 16,060 parity checks against fixtures from the JS rules |
| `RemainderJam/Assets/Editor/JamBuild.cs` | Batch WebGL and Windows builds |
| `RemainderJam/Assets/Resources/Art` | Sprites and the street plate cut from the concept boards by `tools/jam_extract_sprites.py`; `plates/{shrine,bazaar,drain,rooftop}.jpg` and `icons/` generated with Meshy (45 + 9 credits, 9 Nov) |

## Commands

```bash
python tools/jam_extract_sprites.py
node tools/jam_rules_fixtures.js
"C:/Program Files/Unity/Hub/Editor/6000.4.11f1/Editor/Unity.exe" -batchmode -nographics -projectPath jam/RemainderJam -executeMethod RulesParity.Run -logFile -
"C:/Program Files/Unity/Hub/Editor/6000.4.11f1/Editor/Unity.exe" -batchmode -nographics -projectPath jam/RemainderJam -buildTarget WebGL -executeMethod JamBuild.Build -logFile -
python -m http.server 8765 --directory jam/build/web
```

Debug URL parameters (local testing only): `?cp=N` jumps to chapter N (0 alley … 6 ending), `&res=D` sets the lucky number, `&charm=charm_ofuda`, and `&auto=1` plays itself at 3× speed and logs `JAM:` lines to the console.

## itch.io page (draft)

**Title:** The Remainder: a ZERO-SUM: OMEN prologue

**Short description:** Everyone in Meridian wears their luck as a number. You have none. Stop the wheels, make patterns, and get a stranger's family out of a debt they already paid.

**Controls:** Space, Enter, Z or click to stop a wheel and advance. 1/2 choose who strikes. P pauses. Tab skips a scene. Settings has Assist (slower wheels), Reduced motion and Instant text. Sound is optional; every cue is on screen.

**AI disclosure:** Character art and the Meridian street come from concept boards generated with Higgsfield image models from the team's written designs; a script cut them into sprites. The shrine, bazaar, drain-gate and rooftop backgrounds and the three charm icons were generated with Meshy (Nano Banana Pro), using the street plate as a style reference. Music and sound effects are synthesised in code. Game code, the C# rules port and the synthesised audio were written with an AI coding assistant (Claude) under the creator's direction, checked against the team's own JavaScript rules with 16,060 parity cases. Story, world, characters and design are original to ZERO-SUM: OMEN.

**Upload:** zip the contents of `jam/build/web` (index.html at the zip root), upload as an HTML game, tick "This file will be played in the browser", set the viewport to 1280 × 720, and enable the fullscreen button. The build uses gzip with decompression fallback, so no server headers are needed.

## Balance decisions

- **Overwrite against Varro, kept as tuned (9 November 2026).** With `jam_tuning.csv` values, three stops on the lucky number in the first round (before the jar captures slot 3) score Overwrite ×21, enough to end the Varro fight in one round. The creator chose to keep this as the reward for precise play; no boss damage cap is applied.
