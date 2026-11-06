# ZERO-SUM: OMEN
### Game design document · Official Unity Game Jam 2026 · Theme: **Lucky Number**

> *"Every number in this city is spinning. You're the only one who can stop them."*

A cinematic 2.5D squad roguelite with **one verb**. Every number in New Babylon spins like a slot reel, and you **tap to stop it**. Your heroes' attacks, the enemy's blows, even the city's judgement of you: you stop them all. Land three matching digits on the giant neon **Karmic Reel** and the screen explodes into a full-squad cinematic.

Playable feel prototype: [`prototype/index.html`](../prototype/index.html). Open it in any browser. Tap or Space to stop, tap a hero (or press 1/2/3) to choose who acts.

---

## 0. Design pillars (in priority order)

1. **Spectacle drives the game.** Animation, motion graphics and cinematics *are* the feedback. If something can be shown with a camera move, a cut-in or a number flying through the air, it is never shown as text or a panel.
2. **Minimum cognitive load.** One verb (**stop**), one light choice (**who acts next**), five patterns that announce themselves on screen. A new player understands the game after one round, without reading.
3. **No HUD. Everything is diegetic.**
   - **HP is the Omen Index**, the number that floats over every character's head. It already exists in the fiction.
   - The **Karmic Reel is a neon sign** hanging in the world, not a UI widget.
   - The only screen-space elements are cinematic overlays (letterbox, cut-ins, pattern titles) and a sound toggle.
4. **The theme is in every frame.** Numbers are characters, set dressing, sound and story. Theme counts double in judging (§1).
5. **Fun first, math hidden.** Damage is always *tens + the digit you stopped* (40 + 7 = 47), so the number you stop is literally the number that flies to the reel. No arithmetic is ever asked of the player.

### What changed from the previous draft, and why
| Previous draft | Now | Why |
|---|---|---|
| Dice tray, operator buttons, motherboard grid, forecast panel | **Gone.** One timing verb plus picking a hero by tapping them | Minimum UI, maximum visuals. Judges play for 5–15 minutes and must "get it" by watching. |
| 8 reel patterns plus faction modifiers in a table | **5 patterns**, each with its own cinematic: Jackpot, Omen Overwrite, Cascade, Zero-Sum, Reaper's Toll (+ a small Pair flourish) | Each pattern is a *spectacle reward*, not a rule to memorise. |
| Shield and parity points | **Defence uses the same verb.** The enemy's attack number spins; stop it on **0** to parry, or on **your lucky number** to reflect it | One verb for offence and defence makes the game learnable in seconds. |
| Factions as rule text | **Factions have readable wheels you see.** The Tetrad's 4 is wide and red; the Prime Synod's wheel has *only* 2, 3, 5, 7 (no 0, so no parry); the Ouroboros wheel speeds up every loop | Enemy identity through motion, not tooltips. |
| 18 cartridges with left-to-right ordering | **Charms as tarot cards** between fights (pick 1 of 3). Each one changes how the wheels *look and move* (wider 7s, slower spin, wider 0 on enemy wheels) | The upgrade is visible on the next spin. |

Kept from the original pitch: the lucky number chosen by the player, the Nixie reel, digits detaching from damage numbers and slamming into tubes, hit-stop and pitch-up chimes, New Babylon, the factions, and the story.

---

## 1. The jam: facts that shape every decision

Source: [itch.io/jam/official-unity-game-jam-2026](https://itch.io/jam/official-unity-game-jam-2026). The page links an official rules PDF on Google Drive. **Read it before submitting.**

| Item | Value |
|---|---|
| Theme | **Lucky Number.** "A number that a person believes brings them good fortune" / "a number that holds positive cultural, religious or symbolic meaning." Prompt: *"How will you bring luck, fate, or superstition into your game's mechanics, art, and sound?"* |
| Recommended finish | End of jam day 7 (~12 Nov 00:00 UTC). The buffer after it is for packaging only. |
| **Hard deadline** | **Sat 14 Nov 2026, 12:00 UTC.** No late submissions. |
| Community rating | 14–21 Nov. Categories: Fun, Art, Sound, Uniqueness/Creativity, **Narrative**. |
| Build | **A WebGL build playable in the browser is required to be eligible.** Upload cap 1 GB. |
| Generative AI | Allowed, **but it must be disclosed on the page, including how it was used.** Otherwise no prizes. |
| Other rules | Original work only; credit all assets; no file changes after the deadline; teams of 1–5. |

### Unity panel judging (decides prizes)
| Criterion | Weight | How this design wins it |
|---|---|---|
| **Jam Theme** | **×2 (10 pts)** | The player states their lucky number; every number in the world spins and is rigged; lucky and unlucky numbers are the factions, the patterns and the story. |
| Design Implementation | ×1 | One verb, readable wheels, instant cinematic feedback. Nothing to misunderstand. |
| Art & Audio Coherence | ×1 | Single neon-noir palette; every sound is a mechanical tick, relay thock, bell or slot chime tied to digits. |
| Concept & Cohesion | ×1 | "Zero-Sum" is the title, a pattern, and the story's twist. |

---

## 2. The first 90 seconds (this is what the judges see)

| Time | What happens on screen | Player does |
|---|---|---|
| 0:00 | Rain, black. Title logo flickers on like a Nixie tube. | Taps to enter |
| 0:03 | **Kinetic-type cold open** (≤ 15 s, skippable by tap). "NEW BABYLON." → "EVERY CITIZEN WEARS A NUMBER." → "IT DECIDES WHO LIVES." → "YOURS READS" → glitching **NaN**. | Watches |
| 0:20 | The Basilica's voice: **"STATE YOUR LUCKY NUMBER."** Ten Nixie tubes. Hovering shows the number's cultural meaning. | Picks one (the only menu in the game) |
| 0:30 | Logo slam with their digit burned in gold. Camera drops into Rain Alley. Three heroes, one enemy, a neon reel sign overhead. | — |
| 0:35 | Heroes glow. Floating hint: **TAP A HERO.** | Taps |
| 0:37 | Camera punches in, letterbox in, **Persona-style diagonal cut-in** with the hero's name. Over their head a giant number appears, the tens fixed and **the ones digit spinning like a slot reel**. Hint: **TAP TO STOP.** | Stops it on 7 |
| 0:40 | The lock-in flashes, the hero dashes across the screen and hits; **hit-stop**; the damage pops as "4**7**". The **7 tears off, spins through the air and slams into the neon sign** with a thock and a chime. | — |
| 0:50 | Two more heroes. If the three digits match: **JACKPOT**. The screen cracks, three hero panels slash down, the multiplier counts up, and the enemy takes a giant number. | Gets hooked |
| 1:10 | The enemy winds up; *its* number spins. Hint: **STOP ON 0 TO PARRY.** | Learns defence with the same verb |

Every instruction in the whole game is one of those three floating hints, shown once.

---

## 3. Core loop

| Loop | Length | Beats |
|---|---|---|
| **Round** | 20–30 s, mostly cinematic | Pick a hero → stop their wheel → attack cinematic → digit flies to the reel. ×3. Then the reel resolves (a pattern cinematic or a bust). Then the enemy attacks, and you stop its wheel to defend. |
| **Fight** | 1.5–3 min | 2–4 rounds. The enemy enters with a cut-in, exits with a shatter and "SETTLED". |
| **Run** | 15–20 min | 3 districts × (2 fights + boss) → The Basilica. Between fights: **tarot pick** (1 of 3 charms) as a short card-deal animation. |
| **Meta** | across runs | 10 lucky numbers × difficulty tiers, charm unlocks, 3 endings, Daily Omen seed. |

**The one strategic layer:** *which hero acts next.* Each hero's wheel spins at a different speed and favours a different digit, so chasing 7-7-7 or a 7-8-9 run means sending the right hero at the right time. You can *see* this. Vesper's 7s are wide on her fast wheel; Ba's 8s are wide on her slow one.

---

## 4. Rules (implemented in the prototype)

### 4.1 The wheel
- A vertical strip of digits scrolls in a window above the actor. **Each digit's cell height is its odds**, so a "weighted" digit is literally a bigger number that stays in the window longer. Players read the odds by eye.
- Tap (or Space) to stop. The strip eases into the nearest cell; lock flash; relay thock.
- Each passing digit plays a pitched tick (digit 0 lowest, 9 highest). The rhythm is a timing aid. **In the Unity build, sync the tick rate to the music's 8th notes** so stopping feels like hitting a beat.
- **Your lucky number is gold on every wheel.**

### 4.2 Heroes (3)
| Hero | Lucky | Wheel | Hits for |
|---|---|---|---|
| **NIL** (you) | *yours* | Medium speed; your digit is double-wide ("magnetic") | 40 + digit |
| **Vesper Sette**, ex-croupier gunslinger | 7 | **Fast**; 7 double-wide | 30 + digit |
| **Madame Ba**, fortune-teller and loan shark | 8 | **Slow**, precise; 8 double-wide | 20 + digit |

Bases grow by +10 after each fight ("your Omen rises"). Tens never change the last digit, so the reel game stays the same while the numbers get bigger.

### 4.3 The Karmic Reel: five patterns, five cinematics
The three digits from a round's three attacks land on the sign. Then:

| Pattern | Example | Payoff | Cinematic |
|---|---|---|---|
| **Omen Overwrite** | your number ×3 | Round damage × digit × 3 | Gold everything: bells ring your number of times, full-squad slash panels, screen crack, slow count-up |
| **Jackpot** | 7-7-7 | Round damage × digit (min ×2) | Squad panels slash down, screen crack, count-up |
| **Cascade** | 3-4-5 / 9-8-7 | Extra round; the enemy waits | Time-slow, teal bands, "THE SEQUENCE HOLDS" |
| **Zero-Sum** | sums to 10 or 20 | Enemy's next move erased + squad heals | Mirror-wipe transition, ledger-balance chime |
| **Reaper's Toll** | 4-4-4 | Every Omen *containing a 4* loses 44%, yours included | Four bells toll, red wash. It is a gamble, and Fate 4 is immune. |
| Pair | 7-1-7 | Round damage again | Small flourish, no letterbox |
| Bust | — | Nothing | The tubes flicker out |

### 4.4 Defence (the same verb)
The enemy's attack number spins over it. Stop it on:
- **0 → PARRY**: no damage, teal flash.
- **Your lucky number → FORTUNE**: the blow is reflected onto the enemy.
- Anything else → take *tens + digit*.

### 4.5 Factions you read by their wheel
| Faction | Numerology | Wheel | Effect |
|---|---|---|---|
| **The Tetrad** | 4 (四 *sì* sounds like 死 *sǐ*, death) | The 4 is triple-wide and red | Landing it = **DEATHMARK ×2** |
| **The Prime Synod** | 2, 3, 5, 7 | Only primes on the wheel | No 0, so you can't parry. Hit hard first. |
| **The Ouroboros** | 8 & 9 | Speeds up every loop | Stop early or lose control |
| **The Basilica** (final boss) | *yours* | **Your** lucky number is triple-wide and red | It learned your number: landing it hits ×3 |

### 4.6 Lucky numbers (Fates)
The player's pick sets NIL's digit, the gold digit on every wheel, and the Omen Overwrite target. In the jam build each also gets **one** visible perk (keep it to one line each). The prototype implements all of them except Trinity's re-spin.

| # | Name | Perk | Note shown at pick |
|---|---|---|---|
| 0 | Null | Secret-ending route; 0-0-0 becomes Omen Overwrite | The number the Basilica cannot divide by |
| 1 | Ace | Your wheels start 15% slower | First place, first light |
| 2 | Pair | Pairs pay ×3 | 好事成双: good things come in pairs |
| 3 | Trinity | One free re-spin per fight | Cantonese 三 echoes 生, life |
| 4 | Defiance | Reaper's Toll spares you and counts as Overwrite | 四 sounds like 死. Wear it anyway. |
| 5 | Hamsa | Your 0s on enemy wheels are double-wide | The hand that wards off the evil eye |
| 6 | Flow | Runs count in any order | 六六大顺: may everything go smoothly |
| 7 | Jackpot | All Jackpots pay ×7 | Lucky seven |
| 8 | Prosperity | Tarot shows 4 cards | 八 rhymes with 发, to prosper |
| 9 | Longevity | Heal 9 after every round | 九 echoes 久, lasting; in Japanese, 九 *ku* echoes 苦, suffering |

### 4.7 Charms (tarot between fights)
Each changes what the wheels **look like**, so the upgrade is felt on the next spin. Jam pool: 12. The prototype has 8 (✅).

✅ **Loaded Seven** (7s twice as wide) · ✅ **Slow Hand** (your wheels −25% speed) · ✅ **Ward of Zero** (enemy 0 ×3 wide) · ✅ **Golden Ratio** (Fibonacci triples are Cascades) · ✅ **Compound Interest** (+3 to Jackpot multipliers) · ✅ **Mirror Bus** (your first digit each round widens on the next two wheels) · ✅ **Omen Bond** (+10 to every hero) · ✅ **Scales of the Ledger** (Zero-Sum also deals round damage ×2) · Black Cat (first bust each fight becomes a Pair) · Thirteenth Floor (13 on enemy wheels hurts them) · Second Sight (see the enemy's next wheel during your round) · Double or Nothing (×2 damage, but your wheels speed up 30%)

---

## 5. Story & cinematics

### 5.1 Premise
New Babylon runs on **The Basilica**, a cathedral-mainframe that floats an **Omen Index** (00–99) over every citizen's head. It decides loans, jobs and who survives the night. Its hidden law is **zero-sum**: every lucky index is paid for by an unlucky one. **NIL**, a Basilica actuary who found that clause, was "rounded to zero" and wakes in Rain Alley 9 reading **NaN**. Incomputable, NIL can stop the spinning numbers everyone else is subject to. The Basilica asks for the one input it is missing: **your lucky number.**

### 5.2 Cast
NIL (yours) · **Vesper Sette** (7, ex-croupier) · **Madame Ba** (8, profits from the zero-sum; mid-game reveal) · **Shiro of the Fourth Gate** (4, Tetrad executioner, Act 1 boss) · **Cardinal Seventeen** (Prime Synod, Act 2 boss) · **The House / Mr. Eighty-Nine** (Ouroboros, Act 3 boss) · **The Basilica** (your number, final boss).

### 5.3 How cinematics *are* the game
There are three tiers of cinematic, and the player sees Tier 1 every few seconds:

| Tier | Length | Used for | Built with |
|---|---|---|---|
| **1 · Combat cinematics** | 0.5–2.5 s | Every hero pick (cut-in), every stop (lock-in), every hit (dash, hit-stop, digit flight), every pattern (full-screen motion graphics) | Cinemachine impulse + camera blends, Timeline-free code sequences (async/coroutines + PrimeTween) |
| **2 · Story beats** | 15–40 s | Fight intros and outros, recruits, boss entrances | **Motion comic**: painted layers at depth in 3D, Cinemachine dolly, kinetic typography, diagonal cut-ins. Timeline. |
| **3 · Set pieces** | 40–60 s | Cold open, midpoint reveal, finale and endings | Same toolkit, longer, with one fully animated character moment each |

| ID | When | Length | Beats |
|---|---|---|---|
| C0 | Cold open | 15 s + lucky-number pick | Kinetic type over rain, then NaN glitch, then **STATE YOUR LUCKY NUMBER** |
| C1 | After fight 1 | 20 s | Vesper cornered, her index ticking toward 44; NIL stops it. She joins. |
| C2 | Act 1 boss | 25 s | Shiro: four lanterns go out one by one; his wheel appears with a giant red 4 |
| C3 | Midpoint | 40 s | Madame Ba shows the ledger: every Jackpot you hit lowered strangers' numbers. The camera pans across a crowd whose indices tick down. |
| C4 | Act 3 boss | 25 s | The House deals your own digits back to you |
| C5 | Finale | 40 s | The Basilica speaks in your number; its wheel shows your digit in red. Choice: **BALANCE** or **OVERFLOW**, made by stopping one last wheel. |
| C6a/b/c | Endings | 30 s each | Balance (NIL becomes 00 so the city rises by one) · Overflow (every index reads NaN) · **Divide by Zero** (secret: Lucky 0 plus a 0-0-0 finisher crashes the Basilica into a blue-screen credits roll) |

Even the final choice uses the core verb. **There are no dialogue menus in the game.**

---

## 6. Art & motion direction: "Occult Acid-Noir 2.5D"

### 6.1 Look
Wet asphalt, brass, obsidian, sodium-orange Nixie glow against cold teal rain. Hand-painted 2D characters with strong silhouettes and neon rim light, standing in shallow 3D dioramas.

Palette: obsidian `#0E0B10`, Nixie amber `#FF7A2C`, blood `#FF3D5A`, rain teal `#5FE3F0`, lucky gold `#FFD27A`, violet `#B77BFF`. Each hero owns one neon colour and every cut-in, trail and spark uses it, so colour alone identifies the actor.

### 6.2 Motion-graphics language (Persona 5 / Reverse: 1999 inspired, our own grammar)
- **Diagonal everything.** Cut-ins, bands and panels enter at −6° to −14°. Never use a horizontal wipe.
- **Kinetic numbers.** Digits are the stars: they scale in with overshoot, tear off, spin and slam. A number is never just displayed; it always arrives.
- **Three-speed timing.** Snap (80–120 ms) for impacts, glide (300–550 ms) for camera, hang (hit-stop 40–120 ms) before payoffs.
- **Letterbox = "this matters."** Bars slide in for every cinematic beat and out for the decision moment.
- **Colour budget per beat.** At most 2 neon colours on screen during a cinematic, plus white for impacts.

### 6.3 Juice timing spec (from the prototype, tuned)
| Moment | Spec |
|---|---|
| Hero picked | Camera blend to the hero (0.55 s, scale 1.35) + letterbox + diagonal cut-in (0.95 s total, holding at 22–78%) + whoosh |
| Wheel | Pops in with overshoot (0.25 s); motion blur while spinning; tick per digit |
| Stop | Ease to cell centre (8 frames); lock flash and scale 1.18; relay thock |
| Hit | Dash 230 ms ease-in → flash 0.35 → **hit-stop 40 ms × reel slot** → sparks in the hero colour → damage pops (scale 0.3 → 1.3 → 1) |
| Digit flight | The ones digit detaches and arcs to its tube (520 ms, 720° spin); the tube depresses; chime pitched **+2 semitones per filled tube** |
| Pattern | Letterbox; full-width diagonal bands; title letters stagger in (35 ms apart, overshoot); count-up with ticks; Jackpot/Overwrite adds screen crack, white flash, shake and squad panels |
| Enemy defeat | Brightness 5×, blur, scale 1.3, spark burst, kinetic "SETTLED" |
| Accessibility | Reduced-motion mode (no zoom/shake, short anims); max 3 full-screen flashes per second; optional "Assist" (all wheels −30% speed) |

### 6.4 Building it in Unity, WebGL-safe
| Layer | How |
|---|---|
| Pipeline | URP. HDRP does not run on the web. |
| Characters | Painted PSB → **2D Animation** bones; idle, wind-up, dash, hit, hurt, victory. On quads with a Shader Graph Lit alpha-clip material + a rim-light term in the hero's colour. |
| World | 3 shallow dioramas (alley, cathedral, casino) + the Basilica, built from one ProBuilder kit; **baked lightmaps**; emissive neon; Shuriken rain and sparks. VFX Graph needs compute shaders, which plain WebGL 2 lacks. |
| The neon reel sign | A world-space mesh with 3 Nixie tube meshes; digits are TextMeshPro with a glow material. It is the most important asset in the game: give it an extra day. |
| Camera | **Cinemachine 3**: one virtual camera per framing (wide, hero close-up, enemy close-up, sign), blend presets for snap and glide; Impulse for shake |
| Overlays | One screen-space canvas for letterbox bars, cut-ins and pattern titles: prefabs animated with **PrimeTween**. Kinetic type uses TMP with per-character vertex animation. |
| Post | Bloom (carries the neon), ACES + a custom LUT, vignette, grain, chromatic-aberration pulse on hits |
| Story beats | **Timeline** + Cinemachine dolly + a `MotionComicPanel` prefab (painted layer stack with parallax) + `KineticText` signal track |

### 6.5 Art production & AI policy
- Lock a **style frame** on Day 2: one finished combat screenshot. Judge every asset against it.
- Generative AI is allowed. Use it for concept, backgrounds or texture plates, then **paint over to the palette** for coherence. Log every use in `docs/AI_DISCLOSURE.md` and paste it into the submission page.
- Spend human art time on the **3 hero sprites, the cut-in portraits and the reel sign**, the things on screen every second.

---

## 7. Audio: the reel is the score
- **Adaptive music in 4 stems.** The base loop always plays; **stems 2–4 enter as each reel tube fills**; a pattern triggers a stinger in key; a bust cuts to the base loop.
- **Wheel ticks are on the beat grid** (8th notes at the track BPM), so stopping a number feels like playing an instrument.
- **SFX vocabulary:** relay thock (lock), Nixie hum (sign), slot bell ×N (Jackpot rings N bells), cathedral bells (Overwrite), four low tolls (Reaper), crystal ping (parry), whoosh (cut-ins).
- **Voices:** per-character pitched blips. One processed Basilica line: "STATE YOUR LUCKY NUMBER."
- WebGL: audio starts on the title tap.

---

## 8. Technical plan (Unity)

**Engine:** Unity 6 LTS (6000.3) is the safe choice. Unity 6.6 reportedly makes WebGPU production-ready for web builds (check Unity's release notes), but **design for WebGL 2.** Everyone installs the exact same version on Day 1.

```
Assets/_Project/
  Core/          # pure C#, no UnityEngine: Wheel odds, PatternEvaluator, Round/Fight/Run state, deterministic RNG. EditMode tests.
  Sequencing/    # Async beat sequences: HeroAttackSequence, EnemyAttackSequence, PatternSequence. The game "script".
  Presentation/  # WheelView, ReelSignView, ActorView (2D Animation), FloatingOmen, Cutin, Letterbox, KineticText
  Cameras/       # Cinemachine rigs + CameraDirector (named shots: Wide, Hero(i), Enemy, Sign)
  Data/          # ScriptableObjects: HeroDef, EnemyDef (wheel digits/weights/speed/accel), CharmDef, FateDef
  Cutscenes/     # Timeline assets, MotionComicPanel prefab
  Audio/         # MusicStemController (reel-driven), BeatClock (wheel ticks), SfxBank
```
- **The game is a sequence of beats.** `async` methods (Awaitable in Unity 6) chain camera shots, tweens and waits, exactly like the prototype's `heroAttack()` / `enemyTurn()` / `resolveReel()`. The rules in `Core` only decide outcomes; the sequences decide how they look.
- **Input:** one action ("Stop/Confirm": mouse, touch, Space) plus picking a hero (click the sprite, or 1/2/3). Input System package.
- **Skip and speed:** tap during any Tier 1 cinematic after its first play to fast-forward ×2. Long runs stay snappy for repeat players and judges.
- **Save:** PlayerPrefs (IndexedDB on web) for unlocks, endings and best run.

### WebGL build checklist
- [ ] WebGL 2; **Gzip + Decompression Fallback ON** (itch.io has not reliably served Brotli headers), or Disabled
- [ ] IL2CPP "Optimize size", stripping High; sprite atlases with Crunch; music streamed Vorbis; **< 60 MB**
- [ ] No VFX Graph / compute / threads / HDRP; at most 1 realtime light
- [ ] 1280×720 embed + fullscreen button; title tap gates audio
- [ ] 60 fps on an integrated-GPU laptop in Chrome; test the *uploaded* build daily from Day 1

---

## 9. Why it's addictive (and fair)
1. **Skill + luck in every second.** The wheel is fair and readable; getting better at stopping numbers is real mastery, and the weighted cells give you just enough luck to hope.
2. **Constant, escalating spectacle.** A small cinematic every 3 seconds, a big one every round, a massive one on Jackpots.
3. **Chasing patterns.** After the first digit lands, players instantly start chasing the next two. That is the "one more spin" feeling without any real gambling.
4. **Numbers go up.** Bases climb every fight, multipliers stack, and the Basilica's Omen is 4,444 (on purpose).
5. **Short runs, instant restart, 10 lucky numbers** to try. Daily Omen seed with a copyable result line for sharing.
6. **No real money, no loot boxes, no gacha.** The casino is the aesthetic, not the business model. Balatro was initially rated PEGI 18 for gambling imagery, so keep real-money language out.

---

## 10. Jam scope (cut lines)
| Area | Must | Should | Could |
|---|---|---|---|
| Heroes | 3, with idle/attack/hurt | Victory poses, Resonance glow | — |
| Enemies | 4 (one per faction + Basilica) | 6 + 3 bosses | Second boss phases |
| Patterns | All 5 cinematics | Unique Overwrite per lucky digit (bell count, colour) | — |
| Charms | 8 | 12 | — |
| Story | C0 + C5 + 1 ending | C1–C4, 2 endings | Secret ending |
| Dioramas | 1 (alley) + Basilica | 3 districts | — |
| Music | 1 track in 4 stems | Boss track | — |

---

## 11. 7-day schedule
Dates are UTC. **Feature freeze end of Day 5 · content lock end of Day 6 · submit Nov 13.** More time goes to motion than to systems.

| Day | Date | Code / Sequencing | Art / Motion | Audio / Story | Exit test |
|---|---|---|---|---|---|
| **1** | Fri 6 Nov | Project + version lock; `Core` (wheel odds, patterns) with tests; **empty WebGL build on a private itch page** | Mood board, palette, hero silhouettes | Script outline | Build loads on itch |
| **2** | Sat 7 Nov | WheelView + stop input; HeroAttackSequence with greybox; reel sign; CameraDirector shots | **Style frame locked**; reel sign model | BeatClock + tick SFX on the beat | Stopping a number and seeing it fly to the sign feels great *with greybox* |
| **3** | Sun 8 Nov | Enemy defence sequence; PatternSequence (all 5); fight loop | 3 hero rigs (idle/attack/hurt); cut-in portraits | Music stems v1, thock/chime/bells | A full fight with a Jackpot cinematic |
| **4** | Mon 9 Nov | Run flow, tarot, lucky-number pick; faction wheels | Alley diorama; enemy sprites; motion-graphics pass (bands, kinetic text) | C0 cold open in Timeline | Someone outside the team plays a full run without instructions |
| **5** | Tue 10 Nov | Basilica boss; endings; skip/fast-forward; save. **FEATURE FREEZE** | Basilica + boss art; pattern-specific VFX | C5 finale, ending(s) | A new player understands the game in 1 round |
| **6** | Wed 11 Nov | Balance (wheel speeds/weights) with 5 playtests; perf on a low-end laptop. **CONTENT LOCK** | Polish: hit sparks, rim light, title screen; capture GIFs | Final mix | 60 fps; zero blockers |
| **7** | Thu 12 Nov | Bugs only; reduced-motion and assist options; release candidate | itch page art | Credits + AI disclosure | RC on the private page |
| Buffer | Fri 13 Nov | **Submit.** Rate your 3-game queue. | — | — | Submitted |
| Deadline | **Sat 14 Nov 12:00 UTC** | | | | |

Team of 3: Sequencing/Code · Art/Motion · Audio/Story/Design. Team of 5: add a motion-graphics/UI animator and an environment artist. Solo: the "Must" column only, and C0 + C5 as kinetic type with no painted panels.

---

## 12. Risks
| Risk | Mitigation |
|---|---|
| Cinematics get repetitive | Vary camera angles per hero (3 shot variants each); fast-forward after first view; big cinematics only for patterns |
| Timing feels unfair | Odds are visible (cell size), the tick is on the beat, Assist mode exists, and the first spin is slowed |
| Too easy with button-mashing | Weighted cells only *help*; balance enemy wheel speeds so random stops lose by the Basilica |
| Animation scope | The motion-graphics grammar (§6.2) is reusable: one cut-in prefab, one band prefab, one kinetic-text component drive every beat |
| WebGL performance | Baked lighting, no compute, test on itch daily |
| Cultural notes | Present beliefs as folklore, never mockery; have native speakers check the Chinese and Japanese notes |

---

## 13. Submission checklist
- [ ] WebGL build, "playable in browser"
- [ ] First sentence of the description: *"Every number in the city spins. Tap to stop them, and tell the game your lucky number first."*
- [ ] Controls: tap/click/Space to stop · tap a hero or press 1/2/3 to choose who acts
- [ ] Credits, team, **generative AI disclosure**
- [ ] Cover image of the neon reel sign; a GIF of a Jackpot cinematic; 5 screenshots
- [ ] No file changes after the deadline

## 14. After the jam
A jam build can win the jam and prove the hook. The path to something bigger: a Steam page within 2 weeks of results, built around the Jackpot cinematics as the trailer; then more heroes and factions (13, 666, 108), a 100-floor Babel Spire mode, and a premium price with no gacha.
