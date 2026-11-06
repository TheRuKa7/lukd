# ZERO-SUM: OMEN
### Game design document · Official Unity Game Jam 2026 · Theme: **Lucky Number**

> *"You don't pray to RNG. You audit it."*
> A 2.5D squad roguelite where fate deals you random digits, then everything after is exact math. You rig that math so the last digit of every hit lands in a three-tube Nixie reel, and the reel pays out.

Playable rules prototype: [`prototype/index.html`](../prototype/index.html). Open it in any browser. It is the source of truth for the combat rules below; port it to C# on Day 1.

---

## 0. TL;DR: what changed from the original pitch, and why

| # | Original pitch | Refined for the jam | Why |
|---|---|---|---|
| 1 | Protagonist has a fixed Lucky Digit | **The game asks the player for their own lucky number (0–9) before the title card.** It becomes NIL's digit and selects one of 10 **Fates** (run modifiers rooted in real numerology). | The jam defines the theme as *"a number that a person believes brings them good fortune."* Asking the player for theirs is the most literal possible hit on the only double-weighted judging criterion. It also gives 10 replayable "decks" for free. |
| 2 | Zero random damage; you tune fixed numbers | **Random input, deterministic output.** Each turn you roll 5 **Omen Dice** (d10, faces 0–9). After the roll, every outcome is exact and shown in a live forecast before you commit. | Pure determinism gets solved and invites analysis paralysis. Balatro-style tension comes from a random hand resolved by exact, previewable scoring. The "press Execute and watch it cascade" moment is the hook. |
| 3 | Reel fires for "the side that completed it" | **The reel is shared, and enemy intents show their exact damage digit.** You can steal a jackpot, poison their pattern, or block a hit to 0 to break it. | Turns every turn into a tug-of-war puzzle. Shields stop being boring: unused dice become Shield, and a fully blocked hit drops a **0**, the pattern-breaker. |
| 4 | "Zero-Sum" was only the title | **Zero-Sum is a pattern:** reel digits summing to a multiple of 10 cancel the opponent's action. It is also the story's thesis: every lucky citizen makes someone else unlucky. | Concept & Cohesion is a judged criterion. The title, a mechanic and the plot twist should all say the same thing. |
| 5 | Gacha, 10-star ascension, 100-floor tower, 3 factions × full roster | **One 20-minute run:** 3 districts × (2 fights + boss) + finale. Meta = 7 Omen Stakes (difficulty tiers) + cartridge unlocks + 3 endings. The "digit nodes" fantasy survives *in-run*: the Nixie HUD grows a new tube each time your max hit gains a digit. | 7 days. Judges play 5–15 minutes. Gacha is irrelevant to a jam, and Balatro-like players are hostile to it (see §13). |
| 6 | Bit-shift operators: ±1, Mod Clamp, Concatenate | **Operators: Bump ±1, Segment Flip (2↔5, 6↔9 like a seven-segment display), Reroll, Mod-10 Clamp.** Concatenate became NIL's whole identity (the Splicer). | Each operator now does something the others can't, and the Nixie/seven-segment flavour is mechanical, not just cosmetic. |
| 7 | Volumetric 3D dioramas, HDRP-feel | **Same look, built to run in a browser:** URP + baked lighting + fake volumetrics + a short post stack + extreme UI juice. A WebGL build is required for prizes. | Must run at 60 fps in a judge's Chrome tab on a laptop. |

**Core design pillar, in one line:** *Tens are safe, ones are fate.* Adding multiples of 10, or multiplying by 11, 21, 31…, never changes the last digit. Every other operation rewrites it. Every cartridge is labelled **Keeps digit** or **Rewrites digit**, so players learn to build engines that scale *and* still hit their numbers. This is what keeps the math readable, so it never feels like a spreadsheet.

---

## 1. The jam: facts that shape every decision

Source: [itch.io/jam/official-unity-game-jam-2026](https://itch.io/jam/official-unity-game-jam-2026). The page links an official rules PDF on Google Drive. **Read it before submitting.**

| Item | Value |
|---|---|
| Theme | **Lucky Number.** "A number that a person believes brings them good fortune" / "A number that holds positive cultural, religious or symbolic meaning." Prompt: *"How will you bring luck, fate, or superstition into your game's mechanics, art, and sound?"* |
| Kick-off | Thu 5 Nov 2026, 17:00 UTC |
| Recommended finish | End of jam day 7. The page's buffer table puts this at 12 Nov 00:00 UTC; the buffer after it is for packaging only ("Don't use this time to keep adding features"). |
| **Hard deadline** | **Sat 14 Nov 2026, 12:00 UTC.** No late submissions. |
| Community rating | 14–21 Nov. Categories: Fun, Art, Sound, Uniqueness/Creativity, **Narrative**. You must rate 3 random games before rating freely. |
| Unity judging | 14 Nov – 7 Dec. Results stream 10 Dec. |
| Team | 1–5 people, one submission. |
| Build | **A playable-in-browser WebGL build is required to be eligible.** Upload cap 1 GB. If you ship Linux, also ship Windows and/or Mac. |
| Generative AI | Allowed for anything, **but it must be disclosed on the submission page, including how it was used.** Not disclosing disqualifies you from prizes. |
| Originality | Must be new. Nothing made before the event or for another jam. |
| Assets | Must have legal rights, and you must credit authors. Page must include build, short description, controls, credit list and team members. |
| After deadline | No file updates of any kind during judging. The page text and screenshots may still change. |

### Judging math (the Unity panel decides the prizes)

| Criterion | Weight | Max | What it means for us |
|---|---|---|---|
| **Jam Theme** | **×2** | **10** | 40% of the score. The lucky number must *be* the mechanics, the art, the sound and the story. |
| Design Implementation | ×1 | 5 | Clarity of rules, feedback, control and pacing. A math game lives or dies on onboarding and previews. |
| Art & Audio Coherence | ×1 | 5 | "Source of assets is irrelevant": coherence beats fidelity. |
| Concept & Cohesion | ×1 | 5 | Title, mechanic and story all argue "Zero-Sum". |

**How we score 10/10 on Theme.** Lucky numbers appear on all four channels the prompt names:
- **Mechanics:** the player's own number; factions built on 4 / primes / 8-9; patterns built on repdigits, Fibonacci and the zero sum.
- **Art:** Omen Index digits float over every NPC, the Nixie HUD, and dice faces that glow in your digit.
- **Sound:** a semitone-up chime per chained digit; each music stem enters as a reel slot fills.
- **Superstition:** every Fate cites a real cultural belief, and the Tetrad's tetraphobia is the Act 1 villain mechanic.

---

## 2. Player fantasy & hook (first 60 seconds)

1. **0:00** Black screen, rain audio. A Nixie tube flickers: `N` `a` `N`.
2. **0:05** Cold-open motion comic (≤45 s, skippable). New Babylon, crowds with floating two-digit Omen Indices. NIL wakes in an alley; their index reads **NaN**.
3. **0:50** The Basilica's voice fills the screen: **"SUBJECT UNDEFINED. STATE YOUR LUCKY NUMBER."** The player picks 0–9. Each button shows the Fate's name, its effect and a one-line cultural note.
4. **1:00** Title card slams in with the chosen digit burned into the logo: `ZERO-SUM: OMEN · 7`.
5. **1:05** The tutorial fight starts. The first roll is rigged so the player can land 7-7-7 by the third hit.

Judges should feel the theme within a minute and get a jackpot within two.

---

## 3. Core loops

| Loop | Length | Beats |
|---|---|---|
| **Micro (turn)** | 20–40 s | Roll 5 dice → place them on heroes / bump / flip / clamp → read the exact forecast → **Execute** → digits fly into the reel → patterns fire → enemy acts (its digits enter too) |
| **Fight** | 1.5–3 min | 3–6 turns. One enemy (bosses have 2 phases). The reel persists between fights, so finishing a fight with 2 digits loaded is a strategy. |
| **Run** | 15–20 min | 3 districts (Tetrad Quarter → Synod Cathedral → Ouroboros Casino) × 2 fights + 1 boss, then the Basilica. Between fights: a **Pawnshop** (pick 1 of 3 cartridges) or a **Confessional** (heal, or remove a cartridge for an extra Parity Point). |
| **Meta** | across runs | 10 Fates × 7 Omen Stakes, cartridge pool unlocks (18 → start with 6), 3 endings, a Daily Omen seed. |

---

## 4. Combat rules (implemented in the prototype)

### 4.1 Turn
1. **Roll** 5 Omen Dice (Fate 3: 6). Dice showing your lucky number glow gold.
2. **Assign** dice to hero slots. Heroes always act in order **NIL → Vesper → Ba**; order is information.
3. **Unused dice → Shield** equal to their face total (Fate 5: ×2).
4. **Parity Points:** 3 per turn.

| Operator | Cost | Effect |
|---|---|---|
| Bump +1 / −1 | 1 PP | 9 wraps to 0 and back |
| Segment Flip | 1 PP | 2↔5, 6↔9 (mirror digits on a seven-segment display) |
| Reroll | 1 PP | New random face |
| Mod-10 Clamp | 2 PP | The enemy's next attack keeps only its last digit (99 → 9) |

5. **Execute.** Each hit resolves through: **base → Resonance → Motherboard cartridges (left to right) → faction modifiers**. The final number's ones digit detaches and drops into the reel.
6. **Enemy phase.** Its intent was shown all turn with exact numbers. Shield absorbs first. **HP damage actually dealt** drops its digit, so a fully blocked hit drops a 0.

### 4.2 Heroes (jam roster: 3)
| Hero | Lucky | Class | Skill |
|---|---|---|---|
| **NIL** (you) | *player's choice* | Splicer | Two dice become one number: tens 4 + ones 7 = **47**. Precision control of the ones digit. |
| **Vesper Sette**, ex-croupier gunslinger | 7 | Adder | *Fan the Hammer*: up to 3 dice, sum + 10. Reliable. |
| **Madame Ba**, fortune-teller and loan shark | 8 | Multiplier | *Compound Interest*: die × die. Spiky; 0 × anything drops a deliberate 0. |

**Resonance:** each die equal to the hero's lucky digit adds +10 (keeps the digit). In the Unity build this also swaps the sprite into its Resonance pose and changes the voice bark.

### 4.3 The Karmic Reel: patterns (priority order)
*Pot* = the sum of the three hits that fed the reel. Patterns go to **whoever placed the third digit**.

| Pattern | Example | You complete it | Enemy completes it |
|---|---|---|---|
| **Lucky Triple** | your digit ×3 | Pot × digit × 3 true damage, plus the full "JACKPOT" cutscene sting | — |
| **Triple** | 7-7-7 | Pot × digit (min ×2) | Pot × 2 to the squad |
| **Cascade** | 3-4-5, 9-8-7, Fibonacci 1-1-2 / 1-2-3 / 2-3-5 / 3-5-8 | Extra turn; the enemy waits | Enemy strikes again |
| **Null Void** | 0-0-0 | Erase the enemy's action | You roll 3 dice next turn |
| **Reaper's Toll** | 4-4-4 | Every unit whose current HP *contains* a 4 loses 44% of max HP, on both sides | same |
| **Zero-Sum** | sums to 10/20 | Cancel the enemy's action | 0 PP next turn |
| **Prime Trio** | 2-7-3 | Pot × 3 | Pot to the squad |
| **Pair** | 7-1-7 | Pot × 1 | ½ pot to the squad |
| Bust | — | reel clears | reel clears |

### 4.4 Factions = enemy AI personalities you can read
| Faction | Numerology | Rule | What the player learns |
|---|---|---|---|
| **The Tetrad** | 4 (East Asian tetraphobia: 四 *sì* sounds like 死 *sǐ*) | Every hit they throw ends in 4; they are always building toward 4-4-4. Your hits ending in 4 gain +40. | Read intents, then use Shield to change their dropped digit. |
| **The Prime Synod** | 2, 3, 5, 7, 11, 13 | Plate armour: non-prime hits are halved. | Aim for prime totals; Prime Amplifier becomes a power pick. |
| **The Ouroboros** | 8 & 9 | Loop: strikes twice if an 8 or 9 sits on the reel. | Manage what you leave on the reel between turns. |
| **The Basilica** (final) | *your* number | Every hit it throws ends in **your** lucky digit, so it is building *your* Lucky Triple against you. | Payoff: you must win using your squad's luck, not your own. |

### 4.5 Motherboard (Balatro-style relics)
5 slots (Fate 8: 6), executed **left to right**. Each cartridge is tagged **Keeps digit** or **Rewrites digit**.

Jam pool of 18. The 11 marked ✅ are in the prototype.

| Cartridge | Tag | Effect |
|---|---|---|
| ✅ Mirror Bus | keeps | Copy the ones digit into the tens place (47 → 77, 7 → 77) |
| ✅ Seven-Segment Overclock | keeps | +70 if the hit ends in 7 |
| ✅ Interest Bus | keeps | +10 per digit already on the reel |
| ✅ Lucky Charm | keeps | +100 if your number appears anywhere in the hit |
| ✅ Digit-Sum Siphon | keeps | +10 × digit sum |
| ✅ Palindrome Engine | keeps | ×11 on palindromes (×11 never changes the last digit) |
| ✅ Actuary's Round-Up | rewrites | Round up to the next 10, which drops a 0 (Void / Zero-Sum enabler) |
| ✅ Prime Amplifier | rewrites | ×3 if prime |
| ✅ Fibonacci Gear | rewrites | ×8 if Fibonacci |
| ✅ Double Down | rewrites | ×2 always |
| ✅ Spare Parity | passive | +1 PP per turn |
| Twin Engine ×21 | keeps | ×21 if the hit's two last digits match |
| Debt Spiral | rewrites | ×(number of turns this fight) |
| Thirteenth Floor | rewrites | ×13; costs 13 HP per hit |
| Hedge Fund | passive | Overkill damage carries to the next enemy |
| Black Cat | passive | The first Bust each fight counts as a Pair |
| Seven Gods Charm | keeps | +7 × 10 per 7 currently on screen (HP, turn counter, reel) |
| Basilica Backdoor | passive | Once per fight, set any reel tube to any digit |

**Example engine** (Fate 7, board = Mirror Bus · Overclock · Palindrome · Lucky Charm): NIL places a lone ONES die showing 7 → **7** → Mirror Bus **77** → Overclock **147** → Palindrome? no → Lucky Charm (a 7 appears) **247**. It still ends in 7, so it still feeds 7-7-7. Swap Palindrome to slot 2 and the 77 becomes **847** before Overclock, giving 847 → 917 → 1,017. Order matters.

### 4.6 Fates (player's lucky number = run modifier)
Cultural notes appear in-game. Keep them respectful and accurate, and have someone from each culture read them before shipping (see §12).

| # | Fate | Effect | Note shown in game |
|---|---|---|---|
| 0 | Null | Your 0s are wild when you complete the reel | The number the Basilica cannot divide by. (Secret-ending route.) |
| 1 | Ace | +1 PP per turn | First place, first light. |
| 2 | Pair | Pairs pay pot × 3 | 好事成双: good things come in pairs. |
| 3 | Trinity | 6 dice | Cantonese 三 *saam* echoes 生 *saang*, life. |
| 4 | Defiance | Immune to Reaper; your 4s gain +40 | 四 sounds like 死. Wear it anyway. (Hard mode.) |
| 5 | Hamsa | Double Shield | The five-fingered hand against the evil eye. |
| 6 | Flow | Runs count in any order | 六六大顺: may everything go smoothly. |
| 7 | Jackpot | Triples pay ×7 (×21 on 7-7-7) | Lucky seven, slot-machine sevens. |
| 8 | Prosperity | +1 Motherboard slot; Pawnshop shows 4 | 八 *bā* rhymes with 发 *fā*, to prosper. |
| 9 | Longevity | Heal 9 per turn; enemy 9s hit +9 | 九 *jiǔ* echoes 久 (lasting); Japanese 九 *ku* echoes 苦 (suffering). |

### 4.7 Numbers go up (the addiction curve)
Enemy HP grows roughly **×2.2 per fight** (160 → ~10k by the Basilica → millions on high Stakes). The HUD's damage readout is a row of Nixie tubes that **physically grows a new tube** (spark, clank, camera punch-in) the first time a hit reaches 4, 5, 6… digits. That is the original "break the 999 cap" ascension fantasy, delivered inside a single run.

---

## 5. Story & cutscenes

### 5.1 Premise
**New Babylon** runs on **The Basilica**, a cathedral-mainframe that assigns every citizen an **Omen Index** (00–99) floating above their head. Your index decides your loans, your job, your odds of surviving the night. The Basilica's hidden law is **zero-sum**: for the city's total luck to balance, every fortunate index must be paid for by an unfortunate one.

**NIL** was a Basilica *actuary* who found the zero-sum clause, tried to publish it, and was "rounded to zero": deleted from the ledger. They wake in Rain Alley 9 with an index of **NaN** and a cracked decoder pendrive in their wrist. The Basilica can't compute NIL, so NIL can edit everyone else's numbers. The first thing the Basilica does is ask NIL for the one input it is missing: **their lucky number.**

### 5.2 Cast
| Character | Number | Role | Arc in one line |
|---|---|---|---|
| **NIL** | player's | Protagonist, Splicer | From "fix my number" to "nobody should have a number." |
| **Vesper Sette** | 7 | Squad | Ex-croupier who rigged games for the Ouroboros; joins after you save her from a 4-4-4 execution. |
| **Madame Ba** | 8 | Squad | Fortune-teller and loan shark who *profits* from the zero-sum; reveals it mid-game. Possible betrayal on the Balance ending. |
| **Shiro of the Fourth Gate** | 4 | Act 1 boss | Tetrad executioner. Believes 4 is honest: "Everyone dies. I just keep count." |
| **Cardinal Seventeen** | 17 | Act 2 boss | Prime Synod inquisitor; only "indivisible" souls may pass. Phase 2: immune to composite damage. |
| **The House (Mr. Eighty-Nine)** | 8 & 9 | Act 3 boss | The Ouroboros croupier. 89 is a Fibonacci number; his phase 2 loops your Cascades back on you. |
| **The Basilica** | yours | Final boss | Learns your number and turns it against you. |

### 5.3 Cutscene plan (all in-engine, all skippable, ≤ 5 min total)
Format: **motion comic**. Layered 2D painted cards placed at different depths in 3D space, with a Cinemachine dolly moving through them, Persona-style diagonal portrait cut-ins, and typewriter text with per-character "blip" voices. Timeline drives it all. One person can build each scene in about 2 hours once the template exists.

| ID | When | Length | Beats |
|---|---|---|---|
| C0 | Cold open | 45 s | City wide shot, Omen Indices over a crowd → NIL wakes → index flickers to NaN → **"STATE YOUR LUCKY NUMBER"** (interactive) → title slam |
| C1 | Fight 1 end | 20 s | Vesper, cornered by the Tetrad, her index ticking toward 44. NIL edits it. She joins. |
| C2 | Act 1 boss | 30 s | Shiro's introduction: four lanterns go out one by one. |
| C3 | Act 2 start | 40 s | **Midpoint reveal:** Madame Ba shows the ledger. Every jackpot you landed lowered someone's index. The camera pans over a crowd whose numbers drop. |
| C4 | Act 3 boss | 30 s | The House deals a hand of your own dice. |
| C5 | Finale | 40 s | The Basilica speaks in your number. Choice: **BALANCE** or **OVERFLOW**. |
| C6a | Ending: Balance | 30 s | NIL becomes the counterweight: everyone's index rises by one and NIL's falls to 00. Bittersweet. |
| C6b | Ending: Overflow | 30 s | Every index in the city reads NaN. Chaos and freedom; Vesper laughs for the first time. |
| C6c | Secret: Divide by Zero | 30 s | Fate 0 (Null) and finishing the Basilica with 0-0-0 crashes it. The screen blue-screens into the credits. |

Writing rules: one idea per line, maximum 2 lines on screen, and every scene must mention a number. Total script ~1,200 words.

---

## 6. Art direction: "Occult Acid-Noir 2.5D" that runs in a browser

**Look:** gothic-cyberpunk. Wet asphalt, brass, obsidian, sodium-orange Nixie glow against cold teal rain. Hand-painted 2D characters standing in simple 3D dioramas.

| Layer | How (WebGL-safe) |
|---|---|
| Render pipeline | **URP** (Forward+ or Forward). HDRP does not support web. |
| Characters | 2D illustrated sprites rigged with the **2D Animation** package (PSB import, bones). States: idle loop, attack, hurt, Resonance pose. Placed on quads with a **Shader Graph Lit, alpha-clip** material so they receive the 3D lights and cast shadows. |
| Dioramas | ProBuilder blockout + a small trim-sheet texture set. **Baked lightmaps** (GPU lightmapper) give a rich look for almost no runtime cost. One realtime directional light at most, plus emissive neon. |
| Fake volumetrics | Additive cone meshes with a scrolling-noise Shader Graph material, a height-fog shader, dust and rain via **Shuriken** particles. VFX Graph needs compute; avoid it unless you go WebGPU (see §8). |
| Wet floor | Glossy material + baked reflection probe + stretched light-streak decal quads. |
| Post stack | Bloom (does most of the work on the Nixie glow), ACES tonemapping with a custom LUT, vignette, film grain, chromatic-aberration pulse on hits, Gaussian DoF in cutscenes only. |
| Camera | **Cinemachine**: slow idle orbit in combat, punch-in plus Dutch tilt on jackpots, dolly tracks for cutscenes. |
| HUD | **The HUD is the hero asset.** A brass-and-obsidian Nixie reel bolted to the top of the viewport; dice and operator keys styled as chunky mechanical calculator switches at the bottom. TextMeshPro Nixie font with glow material and a glass-tube sprite, plus a flicker shader. |
| Palette | Obsidian `#0E0B10`, brass `#CAA45D`, Nixie amber `#FF7A2C`, blood `#E2455C` (enemy), rain teal `#88D2E0` (shield/party), lucky gold `#FFD27A`. |

### Juice spec (the "2026 feel" is mostly timing)
| Moment | Spec |
|---|---|
| Hit lands | Damage number scales in (0.4 → 1.25 → 1.0 in 120 ms). **The ones digit detaches**, spins along an arc (≈320 ms ease-in) and slams into the reel tube. |
| Digit lands | **Hit-stop 40 ms × chain index** (capped at 6). Tube depresses 3 px. "Thock" (low sine sweep plus a band-passed click). Chime **+1 semitone per chained digit**. |
| Pattern fires | 300 ms freeze, banner slams in (overshoot ease), **glass-crack overlay** on big patterns, camera punch-in, chromatic aberration pulse, then the bonus number counts up over 0.8 s with accelerating ticks. |
| Jackpot | All of the above, plus music drops to a single layer, coin-burst particles in the player's digit, and the multiplier text spills out of its frame. |
| New Nixie tube | Spark particles, metal clank, HUD shakes, tube warms up from dark to amber over 400 ms. |
| Accessibility | "Reduce shake/flash" toggle; never more than 3 full-screen flashes per second (photosensitivity guidance); colour is never the only signal (enemy digits also carry "ENEMY"). |

**Tooling:** PrimeTween (free, zero-alloc) or DOTween for all UI motion; Feel/MMFeedbacks if someone already owns it.

### Art pipeline & AI policy
- Lock a **style frame** on Day 2 (one finished combat screenshot) and judge every asset against it.
- If you use generative AI (allowed), use it for concept, reference, background plates and voice blips, then **paint over or recolour everything to the locked palette** so it reads as one style. Art & Audio *coherence* is what is judged.
- Log every AI use in `docs/AI_DISCLOSURE.md` as you go, and paste it into the submission page. Undisclosed AI = no prizes.
- Expect some community raters to mark down visibly AI-generated art. Hand-made or heavily painted-over hero portraits are the safest place to spend human art time.

---

## 7. Audio
- **Adaptive score in 4 stems** (bass/pulse, percussion, synth lead, choir). Stem 1 always plays; **stems 2–4 fade in as reel tubes 1–3 fill**, and all drop out when the reel clears. The music literally *is* the reel.
- **SFX palette:** mechanical (relays, calculator keys, Nixie hum), casino (coin, slot bell), cathedral (bells, choir stabs). A 7-7-7 rings 7 bells; 4-4-4 tolls 4 low bells.
- **Voices:** per-character pitched blips (no VO), plus a single processed "Basilica" voice line ("STATE YOUR LUCKY NUMBER"). If it is AI-generated, disclose it.
- **WebGL note:** audio cannot start before a user click. The title screen's "click to begin" covers this. Use Vorbis and "Load in background" for music.

---

## 8. Technical plan (Unity)

**Engine:** **Unity 6 LTS (6000.3)** for stability. **Unity 6.6** added production WebGPU support for web builds in Sept 2026 (per secondary coverage; check Unity's release notes before relying on it). WebGPU unlocks compute and VFX Graph in the browser, but **target WebGL 2 as the baseline.** Judges' browsers vary, and Unity falls back from WebGPU to WebGL only if you design for it. Pick one version on Day 1, and everyone on the team installs the *exact* same one.

### Architecture
```
Assets/_Project/
  Core/            # OmenCore.asmdef. Pure C#, NO UnityEngine. Rules engine ported from prototype/index.html
    BattleState.cs, Dice.cs, Reel.cs, PatternEvaluator.cs, Cartridges/*.cs, Simulator.cs
    Events: HitResolved, DigitDropped, PatternFired, ShieldGained, EnemyStruck, Defeated
  Data/            # ScriptableObjects: HeroDef, EnemyDef (intents), CartridgeDef (id → effect + art), FateDef, RunMapDef
  Presentation/    # MonoBehaviours that consume the event list and animate it (BattlePlayback.cs is the heart)
  UI/              # uGUI + TextMeshPro; NixieTube, DiceTray, HeroCard, Motherboard, Forecast
  Cutscenes/       # Timeline assets + MotionComicPanel prefab + DialogueSignalReceiver
  Audio/           # MusicStemController (reel-driven), SfxBank
  Tests/           # EditMode tests on Core (pattern table, cartridges, forecast == execution)
```
- **Simulate, then play back.** `Simulator.Run(state)` returns the full event list without mutating state. The **forecast UI** and the **real execution** both use it, so the preview is exact by construction. `BattlePlayback` walks the list with awaits and juice; the final state is committed at the end. This is exactly how the prototype works, and it lets art and juice be added on Days 4–7 without touching the rules.
- **Deterministic RNG** (xorshift with a seed) per run, so the **Daily Omen** (seed = UTC date) and shareable seeds come free.
- **Data-driven content:** designers add enemies, cartridges and Fates in ScriptableObjects without touching code. Effects are small C# classes registered by id.
- **Save:** `PlayerPrefs` (IndexedDB on web) for unlocks, best Stakes and endings seen. Call `PlayerPrefs.Save()` after writes.
- **UI:** uGUI over UI Toolkit, because tweening and world-space juice are more mature in uGUI.

### WebGL build checklist
- [ ] Graphics API: WebGL 2 (optionally add WebGPU first in the list on 6.6, *only* if tested in Chrome, Firefox and Safari).
- [ ] **Compression: Gzip with Decompression Fallback ON**, or Disabled. itch.io has historically not served Brotli headers; test the real itch page on Day 1.
- [ ] Code stripping: High. IL2CPP code generation: "Optimize size". Exceptions: "Explicitly thrown" only.
- [ ] Sprites in atlases with Crunch compression. Music streamed Vorbis. **Target < 60 MB download.**
- [ ] No VFX Graph / compute / threads / `System.IO` writes / HDRP.
- [ ] 1280×720 embed with the fullscreen button enabled on itch, and the "click to start" gate.
- [ ] Perf target: 60 fps on an integrated-GPU laptop in Chrome. Budget: < 150 draw calls, 1 realtime light, post stack ≤ 5 effects.
- [ ] Test the uploaded build (not localhost) every day from Day 1.

---

## 9. Addictive, ethically
What makes "one more run" here, and what we deliberately avoid:
1. **The Execute moment.** A full forecast, then watching it cascade. Anticipation is the reward.
2. **Exponential readout** plus the growing Nixie row. You can *see* progress.
3. **Short runs (≤ 20 min), instant restart**, and a new cartridge or Fate note unlocked every run.
4. **10 Fates × 7 Stakes**: "I beat it on 7, now try 4 (Defiance)."
5. **Daily Omen:** the same seed worldwide, from the date, and a copyable text result (`OMEN 2026-11-20 · Lucky 7 · 4,777,213`) for Discord. No server needed.
6. **Near misses are teaching tools, not lures.** After a 7-7-6 bust the log shows "Bump on Ba's die would have made 7-7-7", explaining what to do differently.
7. **No real money, no loot boxes, no gacha.** Slot-machine *imagery* is the theme, but nothing is purchasable. Note: Balatro was initially rated PEGI 18 for gambling imagery, so keep "casino" as aesthetic and avoid real-money language anywhere.

---

## 10. Content list (jam scope)
| Type | Must | Should | Could |
|---|---|---|---|
| Heroes | 3 (NIL, Vesper, Ba) | — | Shiro as a 4th unlock after Act 1 |
| Enemies | 6 (2 per faction) | 9 | — |
| Bosses | 3 + Basilica | 2-phase bosses | — |
| Cartridges | 12 | 18 | 24 |
| Fates | 10 (cheap: mostly rule flags) | — | — |
| Districts / dioramas | 3 + Basilica (reuse with relight) | — | — |
| Cutscenes | C0, C3, C5, 1 ending | All of §5.3 | Voiced Basilica |
| Meta | Unlocks, endings | Omen Stakes 1–7 | Daily Omen |
| Music | 1 combat track in 4 stems + title | Boss track | Per-district variants |

---

## 11. 7-day production schedule
Dates in UTC. **Feature freeze end of Day 5 · content lock end of Day 6 · submit on Nov 13** (24 h before the hard deadline).

| Day | Date | Code | Art | Audio / Writing | Exit test |
|---|---|---|---|---|---|
| **1** | Fri 6 Nov | Unity project, version lock, repo + LFS. Port `Core` from the prototype, with EditMode tests for the pattern table. **Empty WebGL build uploaded to a private itch page.** | Mood board, palette, style-frame sketch | Script outline, Fate notes reviewed | Tests green; itch build loads in the browser |
| **2** | Sat 7 Nov | Greybox battle: dice tray, hero slots, operators, forecast, reel, enemy intents, simulate/playback | **Style frame locked** (one finished combat screenshot), Nixie tube asset | Music stems sketched; C0 script final | A full fight playable with placeholders |
| **3** | Sun 8 Nov | Run map, Pawnshop, Fate select, cartridges as data, enemy/faction rules | 3 hero rigs (idle/attack/hurt), district 1 diorama | SFX pass 1 (thock, chime, hits) | A full run start-to-finish with placeholder art |
| **4** | Mon 9 Nov | Juice pass 1 (detach-and-fly, hit-stop, banner, crack), music-stem controller, save | Districts 2–3 (reuse kit + relight), enemy sprites | Cutscene animatic for C0/C3/C5 | Someone outside the team plays a full run |
| **5** | Tue 10 Nov | Bosses, Basilica rule, endings flow, tutorial fight with rigged first roll. **FEATURE FREEZE** | Boss art, portraits for cut-ins | Cutscenes C0–C5 in Timeline | Theme reads in the first 60 s (watch a new player) |
| **6** | Wed 11 Nov | Balance (spreadsheet + 5 external playtests), Stakes, perf pass on a low-end laptop. **CONTENT LOCK** | Polish: Resonance poses, title screen, itch banner/screenshots | Final mix, endings | 60 fps on the low-end machine; no blockers |
| **7** | Thu 12 Nov | Bugs only. Accessibility toggles. Final build. | GIF capture for the page | Credits, AI disclosure doc | Release candidate on the private itch page |
| Buffer | Fri 13 Nov | Upload, set page public, **submit**. Rate games in your queue. | — | — | Submitted |
| Hard deadline | **Sat 14 Nov 12:00 UTC** | — | — | — | — |

**Team mapping.** Solo: cut to the "Must" column and use the motion comic for every story beat. Team of 3: Code / Art / Audio-Writing-Design. Team of 5: add a second artist (environments) and a dedicated juice & UI programmer.

---

## 12. Risks & mitigations
| Risk | Mitigation |
|---|---|
| "Too much math" for raters | The forecast panel shows every outcome in plain words; a rigged first roll lands a jackpot; at most 1 new concept per fight during Act 1; patterns teach themselves through banners. |
| Scope creep | The cut table in §10. Feature freeze end of Day 5. Every new idea goes to `docs/POST_JAM.md`. |
| WebGL performance or loading | Build to itch on Day 1 and every day after; < 60 MB; baked lighting; no compute. |
| Art incoherence (mixed sources/AI) | Locked style frame + palette LUT + paint-over rule. |
| Cultural numerology handled carelessly | Present beliefs as folklore, not mockery; no real religious figures; ask native speakers to check the Chinese and Japanese notes. |
| Rules ambiguity | Read the official rules PDF; disclose AI; credit every asset; follow Unity brand guidelines on the itch page. |
| Build breaks at the deadline | Submit a release candidate on Nov 13; keep the last good build zipped. |

---

## 13. Submission checklist
- [ ] Playable **WebGL** build marked "playable in browser" (plus an optional Windows build)
- [ ] Short description that states the theme in sentence one: *"Fate rolls the digits. You rig the math. The game asks for **your** lucky number and builds the run around it."*
- [ ] Controls (mouse/touch; keyboard shortcuts 1–5 for dice, Q/W/E heroes, Space = Execute)
- [ ] Credits for every asset and tool; team members
- [ ] **Generative AI disclosure** (what, where, how)
- [ ] 5 screenshots + 1 GIF of a jackpot cascade; cover image with the Nixie reel
- [ ] Nothing that requires downloads outside the itch page
- [ ] No file changes after the deadline

---

## 14. Beyond the jam: the honest path to "Game of the Year"
A 7-day build is not a GOTY. It can be a **jam winner and a proof that the hook works**. Balatro and Vampire Survivors both started as small solo projects with one great loop. The plan:
1. **Win the jam** with a tight 20-minute slice (this document).
2. **Within 2 weeks of results:** Steam page plus a trailer built from the jackpot moments; collect wishlists from the jam audience.
3. **Expand** to 6 heroes, 3 more factions (13 / 666 / 108), 150 cartridges, a 100-floor Babel Spire endless mode, and Floor 1111 as the true ending.
4. **Business model: premium** ($15–20). No gacha: it conflicts with the "earned luck" theme and with the audience this genre attracts.
5. **Demo** for the next Steam Next Fest.

---

*Prototype controls:* tap a die, then a hero slot · operators act on the selected die · Execute. The forecast panel shows the exact outcome before you commit.
