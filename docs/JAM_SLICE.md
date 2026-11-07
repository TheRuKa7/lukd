# ZERO-SUM: OMEN — Jam Slice Spec and Cut List (Gate A3)

**Rescoped Nov 7 (after the refinement review): "Prologue: NaN".** Ship one complete, polished **10–15 minute Meridian Prologue** with **NIL, Vesper and Varro**. Act I (Hyakki) is a **stretch goal** that starts only after the Prologue passes the gate in §1A. The first engineering milestone is **one correct, readable Audit running in the browser in Unity WebGL**. Deadline: **Sat 14 Nov 2026, 12:00 UTC (17:30 IST)**; we submit **Fri 13 Nov**. AI use disclosed; WebGL build required.

Tags: **M** = must (no ship without it) · **S** = should (cut on the date shown if not working) · **C** = could (only if everything else is done).

---

## 1A. The gate before any Hyakki work
All of these must be true in the WebGL build on the private itch page:
- [ ] One full Audit is correct (scoring matches GDD §1.3 and `node tools/test_scoring.js`) and readable at a glance
- [ ] Beats 1–12 play start to finish in 10–15 minutes with no blocker
- [ ] GAME_FEEL §2 timings in place; 4 of 5 testers say stopping a wheel feels good
- [ ] Varro's Versus card, phases and Vesper's ultimate work (Art Direction v3 §0.4–§0.5)
- [ ] Load to first tap ≤ 20 s; 60 fps on the reference laptop

## 1. Player journey (Prologue 10–15 min, then Act I as stretch)

| # | Beat | Content | Tag | Cut date |
|---|---|---|---|---|
| 1 | Title | Logo, tap to start, audio unlock, settings | M | — |
| 2 | Intro cinematic | Shots 1–4 of World Bible §8 (myth montage + title), ~45 s | M (shortened) | — |
| 3 | Rain Alley 9 | Ama's Omen drops to 01; NIL stops it on 07 (scripted interactive stop) | M | — |
| 4 | Naming shrine | Brother Nought; **choose your lucky number**; REMAINDER DETECTED | M | — |
| 5 | Fight 1 | Debt Hounds ×2; NIL alone; scripted Jackpot | M | — |
| 6 | Vesper joins | Rescue scene (stills + motion graphics) | M | — |
| 7 | Fight 2 | Debt Hounds ×3; choose strikers; Cascade/Zero-Sum | M | — |
| 8 | Maeve's forge | Defend the forge (Big Audit: Collectors) → Maeve joins | C | Tue 10 |
| 9 | Charm stall | Gus Mendoza: pick 1 of 3 charms | M | — |
| 10 | Boss: Varro | Versus card (Art Direction v3 §0.5), Debt Jar rule, 2 phases, Vesper's Requiem | M | — |
| 11 | World-map reveal | Six lands light up; Seal 1 | M | — |
| 12 | Hap's Dream 0 | 15 s dream: "Pick a number…" | S | Wed 11 |
| 13 | Ferry → Moon Pier | Fight 3: Chōchin-obake on the pier | Stretch | after §1A gate |
| 14 | Night Parade | Hina joins (party of 3, bonds) | Stretch | after §1A gate |
| 15 | Map choice | Ofuku's shrine (charm + sets) **or** fox-wedding Whisper | Stretch | after §1A gate |
| 16 | Fight 4 | Kasa-obake pack | Stretch | after §1A gate |
| 17 | Teahouse | Party swap; one bond scene (Vesper + Hina) | Stretch | after §1A gate |
| 18 | Market / Elite | Kappa market (Kyūsuke cameo) **or** Kitsune twins elite | Stretch | after §1A gate |
| 19 | Enma's trial | Keeper trial (no parry, 4 rounds); NIL learns Carry | Stretch | after §1A gate |
| 20 | Boss: Tamamo | Nine tails, illusion faces, Shi and Ku; *Hundred Demons' Night* vs *Hundred-Year Night* | Stretch | after §1A gate |
| 21 | Ending | Seal 9; Thale's line "The Remainder is learning to count"; "To be continued: the River Empire" | Stretch | after §1A gate |
| 22 | Results | Biggest number, patterns found, time; "Play again with a new number" | M | — |

**Minimum lovable slice** (if everything goes wrong by Wed 11): beats 1–7, 9–11, 22 (the Prologue alone, ~10 minutes). **Full jam target:** beats 1–12 + 22. **Stretch:** beats 13–21 (Act I) only after the §1A gate. If Act I is not built, the Prologue ends after beat 11 (or Hap's Dream 0) on a manga splash card: **"TO BE CONTINUED: THE NIGHT PARADE"**, then Results.

## 2. Systems in the slice

| System | Tag | Notes |
|---|---|---|
| Fate Wheels (8-face starters), reel, all 7 patterns, priority | M | GDD §1, SYSTEMS §2.1–2.2 |
| Pattern Sight | M | Biggest single fix for Busts (TUNING §2) |
| Hap's Favour (warm + Hap's Hand) | M | Removes 3-Bust streaks |
| Parry / Fortune on enemy strikes | M | |
| Omen over a Balance, party Balance | M | GDD §1.6 |
| Heroes: NIL, Vesper, Hina (M); Maeve (S) | M/S | Party of 3 max |
| Ultimates for every hero in the slice | M | Video or in-engine; 3–5 s |
| Bonds: Complements, Neighbours, Twins | M | Constellation lines in the Teahouse |
| Link Arts: *Midnight Parade* (M), *Lucky Strike* (S) | M/S | |
| Charms: 12 (Hyakki 6 + Meridian/Crossroads 6), 3 slots, sets | M | SYSTEMS §7 |
| Land Laws: Debt (Meridian), Shi and Ku (Hyakki) | M | |
| NIL verbs: Splice (M), Carry (S) | M/S | |
| Wheel crafting: Remove + Gold/Jade/Glass at Ofuku's shrine | S | Tue 10 |
| Hap's Whispers (1 per act) | S | Wed 11 |
| Tsukumogami faces | C | |
| Economy beyond fen rewards, oracle sticks, Ink, Karma, gems, Awakenings, Deals | ✗ | Not in jam |

## 3. Assets in the slice (owners and specs in [`ASSET_LIST.md`](ASSET_LIST.md))
- **Characters (rigged, 2D):** NIL, Vesper, Hina (M); Maeve (S). Bosses: Varro, Tamamo (M). Enemies (3-pose sprites): Debt Hound, Collector, Chōchin-obake, Kasa-obake (M); Kitsune twins (S).
- **Stages (parallax):** Rain Alley 9, drain gates (Meridian); Moon Pier, foxfire palace (Hyakki). 4 stages (M).
- **Reel objects:** Nixie sign, torii with three lanterns (M).
- **Cinematics:** intro (M, ~45 s), Vesper rescue (M, stills), world-map reveal (M), Hina's entrance (M), Tamamo defeat (M), ending (M); Hap's Dream 0 (S).
- **Music:** Meridian theme, Hyakki theme, Tamamo boss theme (M); stems (S).

## 4. Rules for change
1. New content needs a matching cut of equal size, agreed in the daily stand-up.
2. A **Should** that isn't working on its cut date is cut, not "nearly done".
3. Feature freeze **Tue 10 Nov**; content lock **Wed 11 Nov**; bugs only from **Thu 12 Nov**.
4. Every day ends with a build on the private itch page.

**Done when:** the team has signed this list (names below) and the Day 2 build matches beats 1–7.

Signed: ______ (design) · ______ (code) · ______ (art) · ______ (audio/cinematics)
