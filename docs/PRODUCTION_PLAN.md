# ZERO-SUM: OMEN — Production Plan

How we get from today (Fri 6 Nov 2026, jam day 1) to a polished jam slice by **Fri 13 Nov**, then to a full game. Read with [`GDD.md`](GDD.md) and [`WORLD_BIBLE.md`](WORLD_BIBLE.md).

**Hard jam deadline: Sat 14 Nov 2026, 12:00 UTC. A WebGL build is required. AI use must be disclosed** (log it in [`AI_DISCLOSURE.md`](AI_DISCLOSURE.md) as you go).

---

## 1. Reality check

The full vision (7 regions, 9 playable heroes, ~25 enemies, 7 bosses, 4 endings, ~20 minutes of cinematics) is a **12–15 month** production for a small team. In 7 days the right move is a **vertical slice** that looks finished. Make a short game that feels like the opening of a AAA anime RPG, not a long game that looks like a jam game. The jam judges and players will see 20–30 minutes; make every one of them look like the trailer.

| Approach | Verdict |
|---|---|
| All 7 acts, rough | ❌ Loses on art, polish and cohesion |
| **Intro + Prologue + Act I, polished, ending on a cliffhanger** | ✅ Wins on theme (lucky number in the first minute), art, narrative and fun |
| Intro + Prologue only | ✅ Fallback if the team is 1–2 people |

---

## 2. Phases

| Phase | Dates | Goal | Exit criteria |
|---|---|---|---|
| **0 · Pre-production & look-dev** | Fri 6 Nov (today) | Lock story, systems, style; prove the art pipeline | Bibles merged ✅ · style anchor image chosen · NIL key art approved · Unity WebGL "hello" build loads on a private itch page |
| **1 · Jam vertical slice** | Sat 7 – Fri 13 Nov | Ship *"Chapter 0–I: The Remainder and the Fourth Gate"* | Submitted, with disclosure, by Fri 13 Nov |
| **1.5 · Jam rating** | 14 Nov – 10 Dec | No build changes (jam rule). Collect feedback; prep Steam page; R&D | Feedback log; Act II design locked; Steam page draft |
| **2 · Demo: Acts 0–II** | Dec 2026 – Mar 2027 | Bāfā Harbor, the economy, wheel crafting, oracle sticks, 5 heroes, NIL's *Borrow* | Public demo for the next Steam Next Fest; trailer; wishlists |
| **3 · Production: Acts III–V** | Apr – Sep 2027 | Ten Courts, Sieve, Ouroboros; full roster of 8; Ink, Awakenings, Wagers, Ledger Tree; VO; Chinese localisation | Content complete through Act V |
| **4 · Finale, endgame, launch** | Oct 2027 – Jan 2028 | Meridian, 4 endings, Endless Ledger, Omen Levels, Daily Omen, QA | Launch on PC; mobile (the one-tap verb suits touch) after |

---

## 3. The jam slice (Phase 1) in detail

### 3.1 Content list
| Category | Items |
|---|---|
| Cinematics | Intro (≈2:30, §8 of the World Bible) · Prologue end: world-map reveal (≈30 s) · Act I end: Bai Si's turn + Thale teaser (≈45 s) · 2 Link Arts (4 s each) · ultimates for NIL, Vesper, Ling, Bai Si (3 s each) |
| Playable heroes | **NIL** (Splice, Carry), **Vesper** (Prologue), **Ling** (Act I); **Bai Si** joins after the boss for a final victory lap |
| Bosses | **Varro the Ledgerhound** (debt jar) · **Bai Si** (Fourth Gate death spins, 4 lanterns) |
| Enemies | Wards: Debt Hound, Collector, Noiseling · Sì Shan: Jiangshi, Paper Effigy, Tetrad Acolyte |
| Regions | Remainder Wards (battle stage + map scroll) · Sì Shan (2 battle stages: mountain path, Fourth Gate; map scroll) · Naming shrine (intro) |
| Systems | Everything in GDD §9: verb, reel, 7 patterns, parry, bonds (Complements/Neighbours/Twins/Void), 12 Fu Talismans (3 slots), Shrine face crafting (Remove, Gold, Jade, Glass), ultimates |
| Audio | Wards theme (synth noir), Sì Shan theme (guzheng + erhu over synth pads), boss theme; each in 4 stems that fill with the reel; SFX vocabulary; optional AI voice for the Basilica and Thale (disclose it) |
| Length | 25–35 minutes |

### 3.2 Team shape
| Size | Roles | Scope |
|---|---|---|
| **5** (ideal) | Lead dev (combat/sequencing) · Dev 2 (UI, map, data, build) · Character artist/animator · Environment + VFX artist · Cinematics/audio/writing | Full slice |
| **3** | Dev · Art/animation · Cinematics/audio/design | Full slice, with 1 Link Art and enemies as 3-pose sprites |
| **1–2** | Everything | Intro + Prologue (NIL + Vesper, Varro), then a "to be continued" Sì Shan teaser |

### 3.3 Day-by-day (all dates UTC)
| Day | Date | Code | Character art & animation | Environments & VFX | Cinematics, audio, writing | Exit test |
|---|---|---|---|---|---|---|
| **1** | Fri 6 | Unity 6 project, URP, WebGL; **empty build on a private itch page**; port the prototype's rules to the C# `Core` with tests | Higgsfield look-dev: style anchor, **NIL key art**, Vesper, Ling, Bai Si concepts (§4) | Remainder Wards + Sì Shan establishing concepts | Intro script and shot list final; temp music | Build loads on itch; style anchor chosen |
| **2** | Sat 7 | Combat greybox with wheels, reel, patterns, parry, hero picking, scoring formula | NIL / Vesper / Ling: turnarounds, expressions, **layered PSDs** | Wards battle stage split into parallax layers; in-world neon reel | Intro storyboard frames (stills); generate intro video shots batch 1 | A fight is fun with greybox art |
| **3** | Sun 8 | Map scroll + nodes; talismans (ordered effect pipeline); bonds | **Rig** NIL / Vesper / Ling (2D Animation); attack key poses ×3 each | Sì Shan stages ×2 (layers); ink-brush VFX; stone-stele reel | Intro shots batch 2; edit intro v1 | Prologue playable start-to-finish |
| **4** | Mon 9 | Ultimates and Link Arts (video + in-engine); NIL's Splice and Carry; enemy wheel profiles | Varro + Bai Si boss rigs; 6 enemies (3-pose sprite animation) | Region-styled cut-in bands (neon vs ink brush); hit sparks | Ultimate clips; Link Art clips; music stems v1 | Act I playable with placeholder bosses |
| **5** | Tue 10 | Boss rules (debt jar, death spins, lanterns); Shrine face crafting; Teahouse party select. **FEATURE FREEZE** | Secondary motion (hair/cloth springs), blinks, reactions to the reel | Lighting pass, post-processing, weather | Prologue-end + Act I-end cinematics; SFX pass | Full slice playable |
| **6** | Wed 11 | Balance (wheel speeds, targets) with 5 playtests; WebGL perf + size. **CONTENT LOCK** | Polish poses, victory animations | Polish, optimisation (atlases, compression) | Final mix; subtitles; credits | 60 fps; < 250 MB; no blockers |
| **7** | Thu 12 | Bugs only; reduced-motion + assist modes; release candidate | Capture GIFs and screenshots | itch page art | AI disclosure finished; page copy | RC on the private page |
| Buffer | Fri 13 | **Submit.** Rate your 3-game queue. | | | | Submitted |

---

## 4. Art pipeline with Higgsfield

### 4.1 What's available
| Need | Higgsfield tool | Notes |
|---|---|---|
| Character and environment stills | **3D Jutsu → `generate_angles`** (Seedream V5 Pro) from a blockout render; or the Higgsfield web app's image models (Nano Banana Pro, GPT Image 2.6, Seedream, Cinema Studio) | The blockout fixes pose and framing, which keeps the roster consistent |
| Consistent characters across images and videos | **Elements** (reusable reference characters/environments) | Create one per hero from the approved key art, then use it in every later prompt |
| Video cutscenes | **3D Jutsu → `generate_video`** (Seedance 2.5: text-to-video or start image), or the web app (Seedance 2.0, Kling 3.0 with a start frame, Cinema Studio Video 3.0) | 720p, 4–30 s per clip; use start frames or Elements for consistency |
| Animated idle loops (optional) | Genjutsu motion presets on a character sheet | For dialogue portraits; check loop seams |

Composition guides already rendered (free) in this repo: `art/lookdev/pose_blockout.png` (full-body hero pose, 2:3) and `art/lookdev/street_blockout.png` (deep street with a tower, 16:9). The 3D Jutsu project is **"ZERO-SUM OMEN - Look Dev"**.

### 4.2 Character pipeline (per hero, ~1 day for a 2D artist plus AI)
1. **Key art.** Use the 3D Jutsu pose blockout and the prompt from `art/HIGGSFIELD_PROMPTS.md`. Generate 4 variations and pick 1.
2. **Element.** Create a Higgsfield Element from the approved image (name it after the hero).
3. **Sheets.** Using the Element: front/side/back turnaround, 6 expressions, 3 attack key poses, hurt, victory, ultimate splash.
4. **Paint-over.** Fix hands, the costume's signature details (NIL's decoder is on the *right* wrist; Vesper's cylinder has 7 chambers) and the palette. This is where AI art becomes *our* art, and where coherence is won.
5. **Layer split.** Separate hair front/back, face, eyes, mouth, torso, arms, coat tails and weapon into a PSB (manual + segmentation tools; ~2–3 h).
6. **Rig.** Unity 2D Animation bones + mesh deformation (a Live2D-style idle: breathing, hair and coat on spring bones, blinks).
7. **Action.** Anime *limited animation*: snap between the 3 drawn key poses with smear frames, holds on 2s/3s, impact frames, VFX and camera. This is a genuine anime technique, not a shortcut, and it reads as high-end.
8. **Ultimate.** A 3–4 s video from the splash illustration (image-to-video), played full-screen.

**Making characters feel alive:** they **react to numbers**. Vesper grins and spins her cylinder when a 7 lands; Bai Si closes his eyes on a 4; Ling smiles at a 0; everyone flinches on a Bust; idle barks reference the reel. Reaction poses are cheap, and they make the theme personal.

### 4.3 Environment pipeline (per stage, ~half a day)
1. Blockout in 3D Jutsu with the battle camera (heroes left, enemy right, reel object top-centre).
2. Generate the painting at 2k using the region's style prompt.
3. Split into 3–5 depth layers (depth estimation + inpaint the hidden areas).
4. In Unity: layered planes at depth, Cinemachine moves give real parallax; add particles (rain, mist, lanterns, joss paper, petals) and shader motion (water, flags, flicker).

### 4.4 Cinematic pipeline
1. Storyboard each shot as a still (image generation, same Elements).
2. Animate with Seedance 2.5 or Kling 3.0 from that still as the **start frame**, 5–10 s per shot, 720p.
3. Edit, then grade to the region palette, add sound design, music and subtitles.
4. Export H.264 720p; play via Unity `VideoPlayer` from `StreamingAssets` (WebGL plays video from a URL; audio is unlocked by the title-screen tap).
5. Mix video with in-engine shots: the Naming terminal choice and the logo slam must be in-engine so they use the player's digit.

### 4.5 Consistency rules (pin these up)
- Always reference the hero's **Element**, and append the **style suffix** from the prompt pack, unchanged.
- One palette per region; every hero keeps their signature colour (NIL orange-teal, Vesper crimson, Ling grey-ink, Bai Si white-black, Varro rust).
- QC every image: hair streak, eye colour, signature prop, handedness, digit glyphs readable.
- Keep a log: every generation that ships goes in `AI_DISCLOSURE.md` (tool, model, what, how it was edited).

### 4.6 Credit budget
Paid generations spend Higgsfield credits. Rough counts for the slice: **~150–250 images** (including iterations) and **~35–45 video clips** (intro ~10, other cinematics ~10, ultimates/Link Arts ~6, iterations). Check current pricing in your Higgsfield plan before starting, and confirm commercial-use rights for your plan before any post-jam release.

---

## 5. Technical plan

| Area | Decision |
|---|---|
| Engine | Unity 6 LTS (6000.3); WebGL 2 baseline (WebGPU optional on 6.6+ only if tested in every major browser) |
| Rendering | URP; 2D characters on lit quads (Shader Graph, alpha clip + rim light); baked or unlit painted backgrounds; Bloom/LUT/vignette/grain |
| Characters | Unity 2D Animation (PSB importer, bones, Sprite Skin), spring bones for hair and cloth |
| Camera & cutscenes | Cinemachine 3, Timeline, VideoPlayer (StreamingAssets URLs) |
| Tweening | PrimeTween |
| Code layout | `Core/` (pure C#: wheels, reel, patterns, scoring, bonds, talisman pipeline, deterministic RNG; EditMode tests) · `Sequencing/` (async beat scripts: HeroStrike, EnemyStrike, PatternPayoff, LinkArt, Ultimate) · `Data/` (ScriptableObjects: HeroDef, WheelDef, FaceDef, TalismanDef, EnemyDef, BossRuleDef, ActMapDef) · `Presentation/` · `Audio/` (stem controller, beat clock) |
| Save | PlayerPrefs (IndexedDB on web): act checkpoints, bonds, codex |
| WebGL budget | < 250 MB total; character atlases ≤ 2048²; Crunch compression; music streamed Vorbis; videos 720p H.264 at ~2.5 Mbps; Gzip with decompression fallback; first fight playable within 20 s of load |
| Accessibility | Reduced motion, assist (slower wheels), subtitles, colour-independent signals |

The **rules core comes straight from the prototype** (`prototype/index.html`: wheel odds, pattern evaluation, round flow). Port it on Day 1 so art can land on working gameplay from Day 2.

---

## 6. Risks

| Risk | Likelihood | Mitigation |
|---|---|---|
| AI art inconsistency across poses/videos | High | Elements + paint-over + QC checklist; start frames for every video shot |
| Animation scope (rigs take longer than planned) | High | Limited-animation key poses; enemies as 3-pose sprites; cut Link Arts to 1 |
| WebGL size and performance with high-res art and video | Medium | Budgets in §5; test the uploaded build daily from Day 1 |
| Some community raters dislike visible AI art | Medium | Heavy paint-over on heroes; disclose honestly; let the hand-built motion, systems and writing carry the identity |
| Cultural inaccuracy (Chinese regions) | Medium | Native-speaker review of names, calligraphy and terms; folklore treated with respect |
| Theme too buried under RPG systems | Low | The lucky-number choice comes in minute one, the reel is on screen every second, and bonds are digit relationships |
| Credits run out mid-week | Medium | Day 1 look-dev decides the style before mass generation; batch only approved prompts |

---

## 7. Step-by-step: the next 24 hours
1. **Approve Higgsfield spending.** Claude was blocked from paid generation in this session (see the note below). Either approve it in this session, or run the Day 1 prompts yourself from `art/HIGGSFIELD_PROMPTS.md` §2–§4.
2. **Pick the style anchor**: generate the 4 "style anchor" variations, choose 1, and save it as `art/lookdev/style_anchor.png`.
3. **NIL key art → Element**, then Vesper, Ling and Bai Si.
4. **Unity:** project, URP, WebGL settings; upload an empty build to a private itch page; confirm it loads.
5. **Port `Core`** from the prototype with tests (wheel, reel, patterns, scoring formula from GDD §1.2).
6. **Lock the intro script** (World Bible §8) and generate its storyboard stills.
7. End-of-day review: one screenshot-quality mock of a Sì Shan battle made from the approved art. If it doesn't look like a AAA trailer frame, fix the style before anything is mass-produced.

> **Note on Higgsfield in this session:** the 3D Jutsu layouts were built and rendered for free. The first paid image generation (NIL key art) was refused by the session's safety check because it spends credits. Nothing was charged. If you want Claude to run the generations, say so explicitly (and ideally give a credit budget). Otherwise the prompt pack is written so anyone on the team can paste it into Higgsfield directly.
