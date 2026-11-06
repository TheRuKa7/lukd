# ZERO-SUM: OMEN — Game Design Document

> *"Every number in this world is spinning. You're the only one who can stop them."*

An anime 2.5D party RPG where every number spins like a slot reel and you **tap to stop it**. Travel seven lands of the Tally with NIL and two of eight companions, build Balatro-style synergies between heroes, talismans and wheel faces, and break the seven seals on the road to the Comptroller.

- Story, world and characters: [`WORLD_BIBLE.md`](WORLD_BIBLE.md)
- Phases, schedule, art/animation pipeline: [`PRODUCTION_PLAN.md`](PRODUCTION_PLAN.md)
- Higgsfield prompt pack: [`../art/HIGGSFIELD_PROMPTS.md`](../art/HIGGSFIELD_PROMPTS.md)
- Feel prototype (core verb only): [`../prototype/index.html`](../prototype/index.html)

---

## 0. Pillars (in priority order)

1. **Anime spectacle drives the game.** Cut-ins, camera, animation and motion graphics *are* the feedback. Every system pays out in something you watch.
2. **One verb, deep consequences.** Stop the number. Everything else (who acts, what's on your wheels, which talismans you hold, who's in your party) changes *what that one action can do*.
3. **Complexity is earned, one layer at a time.** The game starts with a single wheel and ends with a team-synergy engine. Each act adds one or two systems, introduced through story and taught by doing (§5).
4. **Diegetic first.** Omen (HP) floats over heads; the reel is an in-world object styled per region; menus are in-world objects (map scroll, market stall, teahouse table).
5. **The theme is the math.** Lucky numbers, superstition, number theory and the zero-sum law drive the story, the mechanics and team-building. Theme counts double in jam judging.

---

## 1. Core combat (the Audit)

### 1.1 One round
1. **Your three strikes.** Tap a hero (or press 1/2/3) to choose who strikes next. Their **Fate Wheel** appears over their head: tens fixed, the ones digit spinning. **Tap to stop.** The hero attacks (anime cut-in, dash, hit-stop) and the stopped digit tears off the damage number and slams into the **reel** (3 tubes).
   - Party of 1 (the opening): NIL strikes 3 times. Party of 2: choose an order, and one hero strikes twice. Party of 3: each strikes once.
2. **The reel resolves** into a pattern, which multiplies the round (§1.3) with a full-screen cinematic.
3. **The enemy strikes.** Its wheel spins over it. Stop on **0** to parry; stop on your lucky digit to reflect; anything else hurts.

### 1.2 The number (Balatro's chips × mult, made visible)
```
Strike value  = Tens (hero level + gear) + Digit stopped + face bonus
Round damage  = (Σ strike values + flat bonuses)  ×  Mult
Mult          = Pattern mult  + additive mult (talismans, faces)  then  × each ×Mult talisman
```
On screen: strikes land as small white numbers as they happen. Then the reel resolves, the pattern title slams in, and a **× Mult** counts up into one huge gold number that crashes into the enemy. That gives a small payoff every 3 seconds and a big one every round.

**Design rule: tens are safe, ones are fate.** Everything that adds to the *tens* (levels, gear, flat bonuses) never changes the digit you stopped. Players scale freely without breaking their reel plans.

### 1.3 Reel patterns (base mult)
| Pattern | Example | Base mult | Extra effect | Cinematic |
|---|---|---|---|---|
| Bust | 2-9-5 | ×1 | — | Tubes flicker out |
| Pair | 7-1-7 | ×2 | — | Small flourish |
| Zero-Sum | 3-3-4 (sums to 10/20) | ×2 | Enemy's next action cancelled | Mirror wipe, ledger chime |
| Cascade | 3-4-5, 9-8-7 | ×3 | Extra round (the enemy waits) | Time-slow teal bands |
| Jackpot | 7-7-7 | ×digit (min ×2) | — | Squad panels slash down, screen crack |
| **Omen Overwrite** | your digit ×3 | ×3·digit | Charges every ultimate | Gold everything, bells ring your number of times |
| Reaper's Toll | 4-4-4 | ×4 | Every Omen *containing a 4* loses 44%, **yours included** | Four bells toll, red wash |

### 1.4 Defence
The enemy's wheel shows its odds by cell size. Stop on **0 → Parry** (no damage, counter flash); on **your digit → Fortune** (reflect); otherwise take tens + digit. Some enemies have no 0 on their wheel (Prime Synod), so the party must win the race instead.

### 1.5 Wheels show the odds
A wheel is a strip of **faces**. A face's height is its odds. Players read probability by looking, never by reading a number.

---

## 2. The party

**NIL plus 2 of 8 companions.** You can swap companions at a Teahouse node or before a boss.

### 2.1 What every hero has
| Element | Example (Vesper Sette, 7) |
|---|---|
| **Fate Wheel** (speed + faces) | Fast; 7 double-wide |
| **Base tens** | 30, grows with level |
| **Passive** | *Lucky Seven*: each 7 on the reel adds +7 to every strike this round |
| **Ultimate** (charged when their digit lands on the reel ×3, or by an Overwrite) | *Seven-Chamber Requiem*: 7 rapid auto-stopping mini-wheels; each 7 doubles the shot |
| **Synergy digit** | 7 |
| **Awakening** (Act IV, choose one of two) | *Dead Man's Hand* (crits on 8s and As) or *Blackjack* (bonus when a round's strikes total 21, 210, 2,100…) |
| **Bond arc** (4 Teahouse scenes) | Unlocks a second passive and the true ending |

### 2.2 Roster kits
| Hero | Digit | Wheel | Passive | Ultimate |
|---|---|---|---|---|
| **NIL** | yours | Medium; your digit double-wide; **Splice** (two wheels: tens *and* ones) | Grows by act (§6) | *Remainder Release*: the reel gains a 4th tube for this round |
| Vesper Sette | 7 | Fast | Lucky Seven (+7 per 7) | Seven-Chamber Requiem |
| Ling | 0 | Slow; 0 triple-wide | *Emptiness*: 0s on the reel are wild for Pairs and Jackpots | *Ensō*: cancel the enemy's action and set one reel tube to 0 |
| Bai Si | 4 | Medium; 4 triple-wide | *Fourfold*: every 4th strike of a fight marks the enemy (×1.44 damage taken) | *Four Lanterns Out*: Reaper's Toll that spares the party |
| Ba Jinling | 8 | Slow; 8 double-wide; Gold faces | *Compound*: +0.8 Mult per consecutive patterned round | *Eight Bells*: ×1.1 Mult per bell (×2.14) and +8 coins each |
| San | 3 | Fast; has a *Steal* face | *Third Time Lucky*: the round's 3rd strike counts double if San made it | *Three Moons Heist*: put the enemy's next wheel result onto your reel |
| Meng Lan | 9 | Medium | *Long Life*: heal 9 when a 9 lands; soups cleanse curses | *Soup of Forgetting*: the enemy forgets its buffs and last pattern; your reel refunds |
| Sister Prima | 2 | Only 2-3-5-7 + one 0 | *Indivisible*: prime strikes pierce armour; +1 Mult per prime on the reel | *Sieve of Light*: shatter all composite numbers on screen (enemy shields, armour) |
| Fibi Leone | Fibonacci | Her lucky digit **advances every round** (1, 1, 2, 3, 5, 8, 3, 1…) | *Golden Ratio*: Cascades give ×1.618; Fibonacci triples count as Cascade | *Spiral Deal*: the reel extends to 5 tubes this round (Full House, Five-Run…) |

### 2.3 Synergy is number theory (no trait UI)
Team synergies come from the **relationships between lucky digits**. The party-select screen draws constellation lines between the heroes' digits; that's the whole interface.

| Bond | Rule | Effect | Example comps |
|---|---|---|---|
| **Complements** | Digits sum to 10 | Zero-Sum becomes ×4 and triggers their **Link Art** (duo cinematic) | Vesper 7 + San 3 · Ba 8 + Prima 2 · Meng Lan 9 + Fibi (when on 1) · Bai Si 4 + NIL 6 |
| **Neighbours** | Consecutive digits | Two-digit runs count as a Cascade | Vesper 7 + Ba 8 · Ba 8 + Meng Lan 9 · Prima 2 + San 3 · San 3 + Bai Si 4 |
| **Twins** | Same digit (NIL picked a companion's digit) | That digit's Jackpot ×2, plus a shared ultimate gauge | NIL 7 + Vesper |
| **Prime Party** | All three digits prime | Every strike pierces; Prime Trio pattern unlocked (×5) | Prima 2 + San 3 + Vesper 7 |
| **Powers of Two** | Digits are powers of two (1/2/4/8) | Each pattern *doubles* the next round's mult | Prima 2 + Bai Si 4 + Ba 8 |
| **Void** | Ling in the party | 0 is wild for every bond above | Ling + anyone |

**Why it's deep:** the player picks NIL's lucky number in the intro *before knowing any of this*. That choice quietly decides which companions will synergise with NIL all game: pick 3 and Vesper is your Complement; pick 2 and you're Ba's; pick 6 and only Bai Si completes you. It gives a strong reason to replay.

### 2.4 Link Arts (duo anime cinematics)
Every Complement and Neighbour pair has a 3–5 s combination attack that fires when its bond triggers. Examples: Vesper + San *Hat Trick* (she tosses San the hat, and three shots from three angles); Ba + Prima *Golden Sieve* (coins fall through Prima's shield as golden spears); Bai Si + Meng Lan *Last Rites* (lanterns float down a river of soup). These are the game's big trailer moments and the reward for team-building.

---

## 3. Build systems (the Balatro layer)

| System | Balatro analogue | What it is here | Introduced |
|---|---|---|---|
| **Fu Talismans** (符) | Jokers | Paper talismans with passive rules. Slots 3 → 6. Ordered left to right. | Act I |
| **Wheel crafting** | Deck building + card enhancements | Remove, duplicate or **enhance** faces on each hero's wheel | Act II |
| **Oracle sticks** (求签) | Tarot / planet cards | Shake the cylinder and a fortune stick falls: a one-shot effect plus a fortune poem | Act II |
| **Ink** | Spectral cards | Rewrite one reel digit after it lands (Judge's Brush) | Act III |
| **Wagers** | Stakes / skip tags | Bet Omen or coins before a fight for bigger rewards | Act V |
| **Omen Levels** | Stakes | Difficulty tiers 1–8 (post-game) | Post-game |

### 3.1 Fu Talismans: sample pool (jam needs 12, full game ~80)
East and West superstitions side by side, which is the jam prompt in miniature.

| Talisman | Type | Rule |
|---|---|---|
| Seven Stars of the Dipper (北斗七星) | +Mult | +7 Mult if any 7 is on the reel |
| Door God (门神) | Defence | The first enemy strike each fight is parried |
| Red Envelope (红包) | Economy | +8 coins on a Jackpot |
| Lucky Cat (招财猫) | Economy | +1 coin per strike ending in your digit |
| Peach-Wood Sword (桃木剑) | ×Mult | ×2 Mult against ghosts and Noiselings |
| Paper Effigy (纸人) | Defence | Once per fight, survive Settlement at 1 |
| Kitchen God's Report (灶神) | Economy | End of act: coins for every fight won without damage |
| Mirror of Yin and Yang | Rule | Pairs also count as Zero-Sum |
| Four-Leaf Clover | Wheel | One free re-spin per fight |
| Horseshoe | Wheel | Your digit's cells +50% wider |
| Black Cat | Rule | The first Bust each fight becomes a Pair |
| Broken Mirror | ×Mult | ×3 Mult, but your wheels spin 30% faster |
| Thirteenth Floor | ×Mult | ×13 Mult if the round total ends in 13 |
| Zodiac set (12) | Mixed | Each triggers on its zodiac turn (round number mod 12); collect several for chains |
| Abacus Bead | Chips | +10 tens per Wealth talisman owned |
| Ladder of Knives | Risk | +4 Mult per point of Omen below 44 |

### 3.2 Wheel crafting (faces)
Every hero's wheel starts as 0–9. At Markets and Shrines you can:
- **Remove** a face: removing 1 and 2 from Vesper makes her 7 even more likely.
- **Duplicate** a face: two 8s, three 8s.
- **Enhance** a face:

| Face | Look on the wheel | Effect when stopped |
|---|---|---|
| Gold | Gold-leaf digit | +3 coins |
| Jade | Green glow | +4 Mult |
| Glass | Translucent | ×2 strike; 1-in-4 chance it shatters and is removed |
| Iron | Riveted plate | +20 tens to every strike *while it's on the wheel but not stopped* |
| Lantern | Glowing red | The wheel slows while passing it |
| Ink (Act III) | Black brush stroke | Wild: becomes the digit you need when it lands |
| Cursed (risk) | Black-red | +50 tens, but curses the striker |

All of this is visible on the wheel itself, so upgrades are *seen* on the next spin.

### 3.3 Economy
Coins (*fen*) come from fights (plus interest: 1 per 5 held, capped), talismans and gold faces. They buy talismans, oracle sticks, face crafting and rerolls at Markets. Bāfā Harbor (Act II) teaches the economy through the story.

---

## 4. Structure: acts, levels and bosses

### 4.1 An act is a map of ~8 nodes ending in a boss (Balatro's antes)
The map is an unrolled scroll in the region's art style. Paths branch:

| Node | Purpose |
|---|---|
| **Small Audit** | Regular fight |
| **Big Audit** | Harder fight, better reward |
| **Elite** | Named enemy with a modifier (a "Noise storm" fight) |
| **Market** | Buy talismans, sticks; craft faces |
| **Shrine** | Free talisman or free face enhancement (choose 1 of 3) |
| **Teahouse** | Swap party, bond scenes, rest |
| **Story** | Cutscene + choice |
| **Boss Audit** | The region's Auditor and its unique rule |

Each act ≈ 25–35 minutes. The full campaign ≈ 6–8 hours.

### 4.2 Difficulty curve (exponential, like Balatro's blinds)
| Act | Small / Big / Boss target Omen |
|---|---|
| Prologue | 300 / 500 / 1,200 |
| I | 1,500 / 2,500 / 6,000 |
| II | 8,000 / 14,000 / 35,000 |
| III | 50k / 90k / 200k |
| IV | 300k / 600k / 1.5M |
| V | 2.5M / 5M / 12M |
| Finale | 99,999,999 ("the whole Ledger") |

Linear growth (tens) can't keep up past Act II. Players **must** build multiplier engines (talismans, Jade faces, bonds, Overwrites), exactly like Balatro. Losing a fight returns you to the act start with the build you had there, so you rebuild differently with new offers.

### 4.3 Bosses: each changes the rules
| Boss | Rule (the "boss blind") | Counter-play it teaches |
|---|---|---|
| Varro, the Ledgerhound | Steals your last reel digit into a debt jar; 3 parries shatter it | Defence matters |
| Bai Si, the White Executioner | Every 4th spin is a Death Spin; 4 lanterns count down to an execution | Plan around a timer; curses |
| Jin Chan, the Golden Toad | His Omen gains interest every round; he taxes your Jackpots; phase 2 he swallows a hero (land a Pair to free them) | Burst damage; economy |
| Judge Cui | Declares a required pattern each round (3 verdicts); his wheels replay your past digits | Flexibility over one combo |
| Cardinal Seventeen | Strikes digits off *your* wheels each round (Sieve of Eratosthenes: 2s, then 3s…) | Wheel crafting; Prima's primes |
| The House | Time rewinds every 3 rounds, but your reel and talismans persist; he copies your last pattern | Finish within one loop |
| Comptroller Thale | P1 Regression to the Mean (wheels compress toward 5); P2 Fixed Fate (wheels don't spin: a puzzle); P3 Zero (NIL alone; companions return as Link Arts) | Everything you've learned |

### 4.4 Variability
- Enemy pools per region, each with a distinct wheel (Jiangshi wheels *skip* digits, Golden Koi multiply when hit, Ox-Head and Horse-Face must die in the same round).
- Random talisman, stick and face offers; branching maps; Elite modifiers ("Noise storm: all wheels reversed").
- Party composition: 28 possible pairs of companions, times 10 possible NIL digits.
- Post-game **Endless Ledger**: all regions shuffled into a true roguelike, Omen Levels 1–8, and a Daily Omen seed.

---

## 5. The complexity ladder (what unlocks when)

New systems arrive one at a time, through the story, taught by doing, with at most one floating hint each.

| When | New | How it's introduced |
|---|---|---|
| Prologue, fight 1 | Stop the wheel; reel; Jackpot/Pair/Bust; Parry | NIL alone vs Debt Hounds |
| Prologue, fight 2 | Choose who strikes; hero wheels differ; Cascade, Zero-Sum | Vesper joins |
| Prologue, boss | Ultimates | Vesper's first Requiem saves NIL |
| Act I | **Fu Talismans** (3 slots); curses; Reaper's Toll | The Tetrad's mountain shrines are full of talismans |
| Act I, end | **Party of 3; bonds and Link Arts** | Ling + Bai Si; the first Link Art plays in a cutscene |
| Act II | **Coins, Markets, Wheel crafting, Oracle sticks**; talisman slots 4 | The Luck Exchange: Jinling teaches the economy |
| Act III | **Ink** (Judge's Brush); NIL's **Ledger Tree** | The Brush is the story's MacGuffin |
| Act IV | **Awakenings** (hero class branches); number properties (prime, square, palindrome) | Synod trials |
| Act V | **Wagers**; loops | The casino |
| Finale | Everything, then taken away | Thale freezes your wheels |
| Post-game | Endless Ledger, Omen Levels, Daily Omen | — |

---

## 6. NIL's growth (the most important progression)

NIL gains **a new verb every act**, plus a **Ledger Tree** (Act III+) fed by the memory digits recovered from each boss.

| Act | Verb | What it does |
|---|---|---|
| Prologue | **Splice** | NIL's wheel shows two strips (tens and ones); stopping both gives high-variance, high-control strikes |
| I | **Carry** | A strike over 50 carries +1 to the next hero's digit (lets you "nudge" the reel) |
| II | **Borrow** | Once per fight, take the enemy's stopped digit onto *your* reel instead of parrying |
| III | **Rewrite** | Free Ink each fight (rewrite one reel digit) |
| IV | **Factor** | Split one strike into two reel digits (56 → 7 and 8) |
| V | **Loop** | Replay last round's reel once per fight |
| Finale | **Divide by Zero** | Ultimate: NIL's digit becomes wild on every wheel for a round |

The Ledger Tree has 7 branches (one per memory digit) with 3–4 nodes each. Example nodes: *Remainder +1* (reel gains a 4th tube permanently, late), *Audit Eye* (see the enemy's next wheel), *Compound Remainder* (+Mult equal to the number of Settled enemies this act).

---

## 7. Hero progression
- **Levels** (shared XP): +10 tens per level, so digits never change. Cap 30.
- **Bond arcs:** 4 Teahouse scenes per hero → second passive, Link Art upgrades, and true-ending flags.
- **Awakening** (Act IV): choose one of two class branches per hero. This is the Cyberpunk-style "build identity" moment.
- **Gear:** one *Charm* slot per hero (hero-specific talismans, e.g. Vesper's *Marked Deck*).

---

## 8. Minimal UI, still

| Screen | In-world object | Interaction |
|---|---|---|
| Combat | Diorama + region-styled reel (neon sign, stone stele, golden abacus, ghost ledger, rose window, slot machine, Basilica clock) | Tap heroes, tap to stop |
| Map | Unrolled scroll in the region's art style | Tap a node |
| Market | A stall with wares on the table | Tap to buy; drag a face onto a wheel |
| Teahouse | A table with tea cups; heroes sit around it | Drag heroes into the 2 seats beside NIL; constellation lines show bonds |
| Talismans | Pinned to the reel frame, left to right | Drag to reorder |
| Lucky-number choice | The Naming terminal | Ten Nixie tubes |

The only screen-space HUD is cinematic: letterbox bars, cut-ins, pattern titles, and a single coin counter on the map.

---

## 9. Jam slice scope (what ships Nov 13)
Full detail and schedule in `PRODUCTION_PLAN.md` §3.

**"Chapter 0–I: The Remainder and the Fourth Gate"**: the intro cinematic, the Prologue (Remainder Wards, 3 nodes + Varro) and Act I (Sì Shan, ~6 nodes + Bai Si), then an ending cinematic teasing Bāfā Harbor and Thale.

| System | In the jam slice |
|---|---|
| Core verb, reel, patterns, parry | ✅ all |
| Heroes | NIL + Vesper + Ling (+ Bai Si as a post-boss join and teaser) |
| Bonds / Link Arts | Complements + Neighbours; 2 Link Arts (Vesper + NIL Twins/Complement depending on digit; Ling's Void) |
| Ultimates | ✅ each hero |
| Fu Talismans | 12, 3 slots |
| Wheel crafting | Remove + Gold/Jade/Glass at one Shrine |
| NIL verbs | Splice + Carry |
| Bosses | Varro, Bai Si (both with unique rules) |
| Not in jam | Economy beyond coins-on-map, Oracle sticks, Ink, Awakenings, Acts II–V |

---

## 10. Build & tech summary
Unity 6 LTS · URP · WebGL 2 (WebGPU optional) · Unity 2D Animation (PSB rigs) + Cinemachine 3 + Timeline + PrimeTween · VideoPlayer for cinematic clips from StreamingAssets · pure C# rules core with EditMode tests · ScriptableObject data for heroes, wheels, faces, talismans, enemies, bosses and maps. Details in `PRODUCTION_PLAN.md` §5.
