# ZERO-SUM: OMEN — Asset List and Specs (Gate A6)

Art is the bottleneck. Every asset in the jam slice has an id, an owner, a spec and a due day before anyone generates, paints or rigs. Status: ☐ not started · ◐ in progress · ☑ done. Due days follow [`PRODUCTION_PLAN.md`](PRODUCTION_PLAN.md) §3.3.

---

## 1. Specs by type

| Type | Format | Size | Layers / states | Notes |
|---|---|---|---|---|
| Character (rigged) | PSB for Unity 2D Animation | 2048 px tall master; atlas ≤ 2048² | head, hair_front, hair_back, torso, arm_L_upper/lower/hand, arm_R_…, leg_…, coat_tail_L/R, props; 3 expressions on the head | Flat cel, 2 tones + 1 rim; coloured lines (Art Direction §2.2) |
| Character poses | PSB frames | as above | idle (rig), attack key poses ×3, hurt, victory, ultimate start/end | Smear frames drawn |
| Enemy (sprite) | PNG sheet | 1024 px tall | idle, attack, hurt (3 poses) | |
| Boss (rigged) | PSB | 2560 px tall | per boss sheet | Tamamo's tails on spring bones |
| Battle stage | PSD → PNG layers | 3840×2160 | sky, far, mid, near, floor, foreground (6 layers) | Empty plates; deck clear for actors |
| Reel object | PSD → PNG | 1200×500 | frame, 3 tube backs, glass, glow | Digits rendered in engine (TextMeshPro) |
| Cut-in band | PNG + shader | 3840×900 | 2–3 layers | Land-styled |
| VFX | Flipbook PNG | 1024² per sheet, 4×4 | — | Hand-drawn, flat shapes |
| Story still | PNG | 3840×2160 | 2–4 layers for motion graphics | |
| Video cinematic | MP4 H.264 | 1280×720, ~2.5 Mbps | — | Streamed from StreamingAssets |
| UI | PNG atlas | 2048² | — | 9-slice where possible |
| Icons (charms, emblems) | SVG → PNG | 256² | — | From `art/graphics/` |

**Naming:** `{type}_{id}_{variant}_{version}.{ext}`, e.g. `chr_nil_attack01_v02.psb`, `stg_moonpier_mid_v01.png`. **Folders:** `Assets/Art/{Characters,Enemies,Bosses,Stages,Reels,VFX,UI,Story,Video}`.
**Pipeline per asset** (Art Book Production §4): 3D base → paint pass → overpaint → layer split → engine. AI use is logged in [`AI_DISCLOSURE.md`](AI_DISCLOSURE.md).

## 2. Jam slice list

### Characters and enemies
| Id | Asset | Tag | Owner | Due | Status |
|---|---|---|---|---|---|
| chr_nil | NIL: rig, 3 attacks, hurt, victory, ultimate | M | Char artist | Sun 8 | ☐ |
| chr_vesper | Vesper: as above | M | Char artist | Sun 8 | ☐ |
| chr_hina | Hina + umbrella (separate rig with its own expressions) | M | Char artist | Mon 9 | ☐ |
| chr_maeve | Maeve: as above | S | Char artist | Tue 10 | ☐ |
| boss_varro | Varro: rig, jars as separate parts, 2 phases | M | Char artist | Mon 9 | ☐ |
| boss_tamamo | Tamamo: rig, 9 tails (spring bones), giant-fox phase still | M | Char artist | Tue 10 | ☐ |
| enm_debthound / enm_collector / enm_chochin / enm_kasa | 3-pose sprites | M | Char artist | Mon 9 | ☐ |
| enm_kitsune_twins | 3-pose sprites ×2 | S | Char artist | Tue 10 | ☐ |
| npc_* | Ama, Tobi, Brother Nought, Gus, Ofuku, Tetsu: portrait busts for story | M | Char artist | Tue 10 | ☐ |

### Stages and reels
| Id | Asset | Tag | Due | Status |
|---|---|---|---|---|
| stg_rainalley | Rain Alley 9 (from the Wards 3D base + colour key) | M | Sun 8 | ◐ base + key done |
| stg_draingates | Drain gates (Varro) | M | Mon 9 | ☐ |
| stg_moonpier | Moon Pier (3D base + colour key exist) | M | Sun 8 | ◐ base + key done |
| stg_foxpalace | Tamamo's foxfire palace | M | Tue 10 | ☐ |
| reel_meridian / reel_hyakki | Nixie sign; torii with three lanterns | M | Sun 8 | ◐ vector designs in `art/graphics/` |

### VFX and UI
| Id | Asset | Tag | Due |
|---|---|---|---|
| vfx_stop, vfx_hit, vfx_parry | Stop flash, hit spark, parry ring | M | Sun 8 |
| vfx_pattern_* | Pair, Zero-Sum, Cascade, Jackpot, Reaper, Overwrite | M | Mon 9 |
| vfx_foxfire, vfx_rain, vfx_fireflies | Land VFX | M | Mon 9 |
| ui_* | Title, Naming tubes, map (Meridian wall map, Hyakki scroll), market stall, teahouse, results receipt, pause ledger, Codex | M | Tue 10 |
| ico_charms ×12, ico_landlaw ×2, ico_intent ×6 | Icons | M | Mon 9 |

### Cinematics and stills
| Id | Asset | Tag | Due |
|---|---|---|---|
| cin_intro | Intro montage (~45 s video) | M | Mon 9 |
| cin_vesper, cin_mapreveal, cin_hina, cin_tamamo_end, cin_ending | Stills + motion graphics | M | Tue 10 |
| cin_hapdream0 | Hap's Dream 0 (15 s) | S | Wed 11 |
| ult_* | Ultimates: NIL, Vesper, Hina (M), Maeve (S); Link Arts: Midnight Parade (M), Lucky Strike (S) | M/S | Mon 9–Tue 10 |

### Audio (see [`AUDIO.md`](AUDIO.md))
Meridian theme, Hyakki theme, Tamamo theme (M); SFX vocabulary (M); stems (S).

**Done when:** every Must item from [`JAM_SLICE.md`](JAM_SLICE.md) has a row, an owner and a due day, and the status column is updated at each stand-up.
