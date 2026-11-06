# ZERO-SUM: OMEN — Game Design Document

> *"Every number in this world is spinning. You're the only one who can stop them."*

An anime 2.5D party RPG across lands inspired by **Japanese, Chinese, Indian, Greek and American** myth and folklore. Every number spins like a slot reel, and you **tap to stop it**. Travel with NIL and two of eight companions, build Balatro-style synergies between heroes, charms and wheel faces, and break the Seals on the road to the Comptroller.

- Story, world and characters: [`WORLD_BIBLE.md`](WORLD_BIBLE.md)
- Phases, schedule, art/animation pipeline: [`PRODUCTION_PLAN.md`](PRODUCTION_PLAN.md)
- Higgsfield prompt pack: [`../art/HIGGSFIELD_PROMPTS.md`](../art/HIGGSFIELD_PROMPTS.md)
- Feel prototype (core verb only): [`../prototype/index.html`](../prototype/index.html)

---

## 0. Pillars (in priority order)

1. **Anime spectacle drives the game.** Cut-ins, camera, animation and motion graphics *are* the feedback. Every system pays out in something you watch.
2. **One verb, deep consequences.** Stop the number. Everything else (who acts, what's on your wheels, which charms you carry, who's in your party) changes *what that one action can do*.
3. **Complexity is earned, one land at a time.** Each land's culture contributes the system it is famous for (§5). The game starts with one wheel and ends with a team-synergy engine.
4. **Diegetic first.** Every combatant's Omen floats over its head and doubles as its health readout (§1.6); the reel is an in-world object styled per land; menus are in-world objects.
5. **The theme is the math, and the math is multicultural.** Lucky numbers and superstitions from every land drive story, mechanics and team-building. Theme counts double in jam judging.

---

## 1. Core combat (the Audit)

### 1.1 One round
1. **Your three strikes.** Tap a hero (or press 1/2/3) to choose who strikes next. Their **Fate Wheel** appears overhead: tens fixed, the ones digit spinning. **Tap to stop.** The hero attacks (cut-in, dash, hit-stop), and the stopped digit tears off the damage number and slams into the **reel** (3 tubes).
   - Party of 1: NIL strikes 3 times. Party of 2: choose an order, and one hero strikes twice. Party of 3: each strikes once.
2. **The reel resolves** into a pattern that multiplies the round (§1.3), with a full-screen cinematic.
3. **The enemy strikes.** Its wheel spins over it. Stop on **0** to parry, on your lucky digit to reflect; anything else hurts.

### 1.2 The number (chips × mult, made visible)
```
Strike value  = Tens (hero level + gear) + Digit stopped + face bonus
Round damage  = (Σ strike values + flat bonuses)  ×  Mult
Mult          = Pattern mult (+ gem levels)  + additive mult (charms, faces)  then  × each ×Mult charm
```
Strikes land as small white numbers; then the pattern title slams in and a **× Mult** counts up into one huge gold number. That gives a small payoff every 3 seconds and a big one every round.

**Design rule: tens are safe, ones are fate.** Anything that adds to the tens never changes the digit you stopped.

### 1.3 Reel patterns
| Pattern | Example | Base mult | Extra | Cinematic |
|---|---|---|---|---|
| Bust | 2-9-5 | ×1 | — | Tubes flicker out |
| Pair | 7-1-7 | ×2 | — | Small flourish |
| Zero-Sum | 3-3-4 (sums to 10/20) | ×2 | Enemy's next action cancelled | Mirror wipe, ledger chime |
| Cascade | 3-4-5, 9-8-7 | ×3 | Extra round (the enemy waits) | Time-slow bands |
| Jackpot | 7-7-7 | ×digit (min ×2) | — | Squad panels slash down, screen crack |
| **Omen Overwrite** | your digit ×3 | ×3·digit | Charges every ultimate | Gold everything; bells ring your number of times |
| Reaper's Toll | 4-4-4 | ×4 | Every Omen containing a 4 loses 44% of its Balance, **yours included** | Four bells toll, red wash |

### 1.4 Defence
The enemy's wheel shows its odds by cell size. **0 → Parry** (no damage, counter flash); **your digit → Fortune** (reflect); otherwise take tens + digit. Some enemies (the Prime Synod) have no 0 on their wheel, so the party must win the race instead.

### 1.5 Wheels show the odds
A wheel is a strip of **faces**, and a face's height is its odds. Players read probability by looking.

**Pattern priority.** A reel matches the first pattern in this order: Omen Overwrite → Reaper's Toll → Jackpot → Cascade → Zero-Sum → Pair → Bust. So 4-4-4 is an Overwrite for a player whose digit is 4, and a Reaper's Toll for everyone else. (Same order as `evaluate()` in the prototype.)

### 1.6 Omen and Balance (how a two-digit number can be a health bar)
An Omen is always two digits, 00–99 (World Bible §2). In an Audit, each side stakes a **Balance**: the luck it puts on the table. Damage drains the Balance, and the Omen over the combatant's head shows the share that's left, from 99 down to 00. At 00 the combatant is Settled.
- Enemy Balances grow exponentially by act (§4.2), so damage numbers get huge while the number over every head stays a readable two-digit Omen.
- The party shares one Balance (300 in the Prologue), shown as the party's Omen over NIL's NaN.
- Rules that read an Omen (Reaper's Toll, Hina's *Ninety-Nine*, "13" charms) read the displayed two-digit value; rules that deal damage hit the Balance.

---

## 2. The party

**NIL plus 2 of 8 companions.** Swap at a Teahouse / Campfire node or before a boss.

### 2.1 What every hero has
Fate Wheel (speed + faces) · base tens · a passive · an **ultimate** (charged when their digit lands three times or by an Overwrite) · a synergy digit · an **Awakening** (Act IV, one of two class branches) · a **bond arc** (4 scenes).

### 2.2 Roster kits
| Hero | Digit | Land | Wheel | Passive | Ultimate |
|---|---|---|---|---|---|
| **NIL** | yours | — | Medium; your digit double-wide; **Splice** (tens *and* ones wheels) | Grows by act (§6) | *Remainder Release*: the reel gains a 4th tube this round |
| Vesper Sette | 7 | Meridian / Crossroads | Fast | *Lucky Seven*: each 7 on the reel adds +7 to every strike this round | *Seven-Chamber Requiem*: 7 rapid auto-stopping mini-wheels; each 7 doubles the shot |
| Maeve Triskel | 3 | Meridian (Celtic quarter) | Medium; has **Horseshoe** faces | *Third Time Lucky*: the round's 3rd strike counts double if Maeve made it; she upgrades charms at forge nodes | *Triskele*: three spinning horseshoes each land a free 3 on the reel (an instant Jackpot of 3s, or a Twins pattern with NIL 3) |
| Hina of the Ninety-Nine | 9 | Hyakki | Bouncy: it reverses direction at random | *Ninety-Nine*: 9s don't curse her party; each 9 landed gives +9 Mult while her Omen is 99 or below… which it always is | *Hundred-Year Night*: her umbrella opens with one eye; for one round every wheel shows only the party's lucky digits |
| Ba Jinling | 8 | River Empire | Slow; 8 double-wide; Gold faces | *Compound*: +0.8 Mult per consecutive patterned round | *Eight Bells*: ×1.1 Mult per bell (×2.14) and +8 fen each |
| Bai Si | 4 | River Empire | Medium; 4 triple-wide | *Fourfold*: every 4th strike of a fight marks the enemy (×1.44 damage taken) | *Four Lanterns Out*: Reaper's Toll that spares the party |
| Shunya | 0 | Śūnyapura | Slow; 0 triple-wide | *Pūrṇa (fullness)*: 0s on the reel are wild for every pattern | *Place Value*: move any reel digit into the tens of every strike next round (×10 its weight) |
| Prima of Kroton | 2 | Kroton Nova | Only 2-3-5-7 plus one 0 | *Indivisible*: prime strikes pierce armour; +1 Mult per prime on the reel | *Sieve of Light*: shatter every composite number on screen (enemy shields and armour) |
| Fibi Leone | Fibonacci | Crossroads | Her lucky digit **advances every round** (1, 1, 2, 3, 5, 8, 3, 1…) | *Golden Ratio*: Cascades give ×1.618; Fibonacci triples count as Cascade | *Spiral Deal*: the reel extends to 5 tubes this round (Full House, Five-Run…) |

### 2.3 Synergy is number theory (no trait UI)
Bonds come from the **relationships between lucky digits**. The party screen draws constellation lines between digits, and that's the whole interface.

| Bond | Rule | Effect | Example comps (cross-cultural on purpose) |
|---|---|---|---|
| **Complements** | Digits sum to 10 | Zero-Sum becomes ×4 and triggers a **Link Art** | Vesper 7 + Maeve 3 · Ba 8 + Prima 2 · Hina 9 + Fibi (on 1) · Bai Si 4 + NIL 6 |
| **Neighbours** | Consecutive digits | Two-digit runs count as a Cascade | Vesper 7 + Ba 8 · Ba 8 + Hina 9 · Prima 2 + Maeve 3 · Maeve 3 + Bai Si 4 |
| **Twins** | Same digit (NIL chose a companion's digit) | That digit's Jackpot ×2, plus a shared ultimate gauge | NIL 7 + Vesper |
| **Prime Party** | All three digits prime | Every strike pierces; Prime Trio pattern unlocked (×5) | Prima 2 + Maeve 3 + Vesper 7 |
| **Powers of Two** | Digits are 1/2/4/8 | Each pattern doubles next round's mult | Prima 2 + Bai Si 4 + Ba 8 |
| **Śūnya** | Shunya in the party | 0 is wild for every bond above | Shunya + anyone |
| **Old World / New World** | One hero from an "old ledger" land + one from Meridian/Crossroads | Charms from both lands' sets count for each other's set bonuses | Hina + Vesper, Prima + Fibi |

**Why it's deep:** the player picks NIL's number in the opening minute, before knowing any of this, and that quietly decides who completes NIL all game. Pick 3 and Vesper is your Complement; pick 1 and it's Hina; pick 6 and only Bai Si completes you.

### 2.4 Link Arts (duo anime cinematics)
Every Complement and Neighbour pair has a 3–5 s combination attack that blends both heroes' **art styles**:
- **Vesper + Maeve, *Lucky Strike*:** Maeve hurls a burning horseshoe; Vesper shoots it in mid-air into seven ricochets.
- **Ba + Prima, *Golden Sieve*:** coins pour through Prima's shield as golden spears; gongbi gold meets Greek marble.
- **Hina + Vesper, *Midnight Parade*:** ukiyo-e yokai stampede through a Western saloon door.
- **Bai Si + Shunya, *Zero Count*:** lanterns go out one by one and the observatory's sundial shadow cuts the enemy.

These are the trailer moments and the reward for team-building.

---

## 3. Build systems (the Balatro layer), and the land each comes from

| System | Balatro analogue | What it is | Land that teaches it |
|---|---|---|---|
| **Charms of the World** | Jokers | Lucky charms from every culture; slots 3 → 6; ordered left to right | Hyakki (shrine charms, *omamori*) |
| **Wheel crafting** | Deck building + enhancements | Remove, duplicate or enhance faces on each wheel | River Empire (the Luck Exchange) |
| **Oracle sticks** (求签) | Tarot cards | Shake the cylinder and a fortune stick falls: a one-shot effect with a fortune poem | River Empire |
| **Ink** (the Judge's Brush) | Spectral cards | Rewrite one reel digit after it lands | River Empire (Ten Courts) |
| **Karma** | — | A resource banked by parries and Zero-Sums, spent to re-spin or to block a lethal hit | Śūnyapura |
| **Navaratna gems** (the nine planetary gems) | Planet cards | Permanently level up a pattern (Ruby → Jackpot, Pearl → Pair, Emerald → Cascade…) | Śūnyapura |
| **Awakenings** (the Moirai's thread) | — | Each hero picks one of two class branches | Kroton Nova |
| **Crossroads Deals** | Risky vouchers | A powerful boon with a price ("+2 charm slots, but your Omen max is 77") | Crossroads |
| **Wagers** | Stakes | Bet fen or Balance before a fight for bigger rewards | Crossroads |
| **Omen Levels** | Stakes | Difficulty tiers 1–8 | Post-game |

### 3.1 Charms of the World (jam needs 12, full game ~90)
Organised in **sets by land**. Holding several from one set grants a set bonus, so collecting is a build axis.

| Charm | Set | Rule |
|---|---|---|
| Beckoning Cat (*maneki-neko*) | Hyakki | +1 fen per strike ending in your digit |
| Daruma | Hyakki | When you land your digit three times in a fight, paint the second eye: ×2 Mult for the rest of the fight |
| Seven Lucky Gods (7 charms: Ebisu, Daikokuten, Bishamonten, Benzaiten, Fukurokuju, Jurōjin, Hotei) | Hyakki | Each has a small effect; holding all 7 makes every 7 a Jackpot by itself |
| Ofuda ward | Hyakki | The first enemy strike each fight is parried |
| Red Envelope (红包) | River Empire | +8 fen on a Jackpot |
| Door God (门神) | River Empire | Parries also deal the enemy's strike back |
| Peach-Wood Sword (桃木剑) | River Empire | ×2 Mult vs ghosts and Noiselings |
| Lemon and Seven Chillies (*nimbu-mirchi*) | Śūnyapura | Cancels one enemy curse per fight; +7 tens per 7 on the reel |
| 108 Beads | Śūnyapura | Every 108th point of damage in a round counts double (rewards huge numbers) |
| Evil-Eye Bead (*mati*) | Kroton Nova | The enemy's wheel shows its next digit faintly |
| Fortuna's Wheel | Kroton Nova | Once per fight, spin the reel itself: all three digits re-roll |
| Owl Coin | Kroton Nova | +1 Mult per prime strike |
| Horseshoe | Crossroads | Your digit's cells are 50% wider |
| Rabbit's Foot | Crossroads | One free re-spin per fight |
| Lucky Penny | Crossroads | +1 fen when you land a 1 |
| Seven-Come-Eleven Dice | Crossroads | If a round's strikes total 7 or 11 (or 70/110/700…), ×7 Mult |
| Four-Leaf Clover | Meridian (Celtic) | 1-in-4 chance per strike to duplicate its digit on the reel |
| Thirteenth Floor | Meridian | ×13 Mult if the round total ends in 13 |
| Black Cat | Meridian | The first Bust each fight becomes a Pair |

### 3.2 Wheel crafting (faces)
Remove · Duplicate · Enhance: **Gold** (+3 fen) · **Jade** (+4 Mult) · **Glass** (×2 strike; 1-in-4 chance it shatters) · **Iron** (+20 tens while *not* stopped) · **Lantern** (the wheel slows passing it) · **Ink** (wild) · **Horseshoe** (Maeve: lands as your digit 1 time in 4) · **Cursed** (+50 tens, curses the striker). Every enhancement is visible on the wheel itself.

### 3.3 Economy
**Fen** (the Tally's small coins; Lore Lexicon §1) come from fights (with interest: 1 per 5 held, capped), charms and gold faces. They buy charms, sticks, gems, crafting and rerolls at Markets.

---

## 4. Structure: acts, levels and bosses

### 4.1 An act is a map of ~8 nodes ending in a boss
The map is an in-world object in the land's style: a hand-scroll (Hyakki, River Empire), a palm-leaf manuscript (Śūnyapura), a mosaic floor (Kroton Nova), a frontier road map (Crossroads).

| Node | Purpose |
|---|---|
| Small Audit / Big Audit | Fights |
| Elite / **Keeper's Trial** | Hard fight with a special rule; Keepers are revered figures who test you (Enma, Judge Cui, Chitragupta, the Moirai) |
| Market | Charms, sticks, gems, crafting |
| Shrine / Forge | Free charm or face enhancement (Maeve's forge upgrades charms) |
| Teahouse / Campfire | Swap party, bond scenes, rest |
| Story | Cutscene + choice |
| **Boss Audit** | The land's Auditor and its unique rule |

Each act ≈ 25–35 minutes. The full campaign ≈ 6–8 hours.

### 4.2 Difficulty curve (exponential, like Balatro's blinds)
| Act | Small / Big / Boss enemy Balance |
|---|---|
| Prologue (Meridian) | 300 / 500 / 1,200 |
| I (Hyakki) | 1,500 / 2,500 / 6,000 |
| II (River Empire) | 8,000 / 14,000 / 35,000 |
| III (Śūnyapura) | 50k / 90k / 200k |
| IV (Kroton Nova) | 300k / 600k / 1.5M |
| V (Crossroads) | 2.5M / 5M / 12M |
| Finale | 99,999,999 ("the whole Ledger") |

These are Balances, not Omens (§1.6). Linear growth (tens) can't keep up past Act II. Players **must** build multiplier engines. Losing a fight returns you to the act start with the build you had there.

### 4.3 Bosses: each changes the rules
| Boss | Rule | Counter-play it teaches |
|---|---|---|
| Varro, the Ledgerhound | Steals your last reel digit into a debt jar; 3 parries shatter it | Defence matters |
| Tamamo, the Nine-Tailed | 9 tails, each with its own small Balance; foxfire **illusion faces** on your wheels (show one digit, land as another); 9s curse you unless Hina is in the party | Read carefully; the Hina synergy |
| Jin Chan, the Golden Toad | His Balance gains interest each round; taxes your Jackpots; phase 2 swallows a hero (land a Pair to free them) | Burst damage; economy |
| Rahu & Ketu, the Eclipse | Two bodies: Rahu darkens one reel tube each round; Ketu strikes with a blind random wheel; if their Balances drift >10% apart they rejoin and heal | **Balance damage between two targets**: Zero-Sum hits both equally |
| Archon Seventeen | Strikes digits off *your* wheels each round (Sieve of Eratosthenes); composite strikes halved | Wheel crafting; Prima's primes |
| The House | Rewinds time every 3 rounds (your reel and charms persist); copies your last pattern; offers a mid-fight deal | Finish within one loop; read the deal |
| Comptroller Thale | P1 Regression to the Mean · P2 Fixed Fate (wheels don't spin: a puzzle) · P3 Zero (NIL alone; companions return as Link Arts) | Everything |

### 4.4 Variability
Enemy pools per land with distinct wheels (kasa-obake wheels hop; Golden Koi multiply when hit; Vetālas ask a riddle and the answer is a digit; Harpies steal a reel tube; the Headless Horseman's wheel has no top half). Random charm, gem and stick offers; branching maps; Elite modifiers ("Noise storm: all wheels reversed"). Party composition: 28 companion pairs × 10 NIL digits. Post-game **Endless Ledger**: every land shuffled into a true roguelike, Omen Levels 1–8, and a Daily Omen seed.

---

## 5. The complexity ladder (each land teaches what its culture is known for)

| When | New | Taught by |
|---|---|---|
| Prologue, fight 1 | Stop the wheel; reel; Jackpot/Pair/Bust; Parry | NIL alone vs Debt Hounds |
| Prologue, fight 2 | Choose who strikes; hero wheels differ; Cascade, Zero-Sum | Vesper joins |
| Prologue, boss | Ultimates | Vesper's Requiem saves NIL |
| **Act I, Hyakki** | **Charms** (3 slots) and charm sets; curses (4 *shi*, 9 *ku*); Reaper's Toll; **party of 3, bonds, Link Arts** | The Seven Lucky Gods' shrine; Hina joins |
| **Act II, River Empire** | **Fen economy, Markets, wheel crafting, oracle sticks, Ink** | The Luck Exchange; Judge Cui's Brush |
| **Act III, Śūnyapura** | **Karma; Navaratna gems (pattern levels)**; NIL's **Ledger Tree** | Chitragupta's Hall; Shunya |
| **Act IV, Kroton Nova** | **Awakenings**; number properties (prime, perfect 6 and 28, golden ratio) | The Moirai's three trials |
| **Act V, Crossroads** | **Crossroads Deals; Wagers; loops** | The midnight crossroads |
| Finale | Everything, then taken away | Thale freezes your wheels |
| Post-game | Endless Ledger, Omen Levels, Daily Omen | — |

---

## 6. NIL's growth (the most important progression)

| Act | Verb | What it does | Why this land |
|---|---|---|---|
| Prologue | **Splice** | Two wheels (tens and ones) for high-control strikes | NIL's own nature |
| I | **Carry** | A strike over 50 carries +1 to the next hero's digit | Learned from Hina's century of counting |
| II | **Rewrite** | Free Ink each fight (rewrite one reel digit) | The Judge's Brush |
| III | **Place Value** | Move one stopped digit into the tens place of the next strike | India's place-value system |
| IV | **Factor** | Split one strike into two reel digits (56 → 7 and 8) | Greek number theory |
| V | **Deal** | Once per fight, take a Crossroads Deal mid-battle | The black book |
| Finale | **Divide by Zero** | Ultimate: NIL's digit is wild on every wheel for a round | Everything |

The **Ledger Tree** (from Act III) has one branch per Seal (7), with 3–4 nodes each, fed by recovered memory digits. Examples: *Remainder +1* (permanent 4th reel tube, late), *Audit Eye* (see the enemy's next wheel), *Compound Remainder* (+Mult per Settled enemy this act).

---

## 7. Hero progression
- **Levels** (shared XP): +10 tens per level (digits never change). Cap 30.
- **Bond arcs:** 4 scenes per hero → second passive, Link Art upgrade, true-ending flag.
- **Awakening** (Act IV): one of two class branches per hero (e.g. Vesper: *Dead Man's Hand* crits vs *Blackjack* bonus at 21; Hina: *Hundred Years* becomes real vs *Kasa-obake* stays a trickster).
- **Gear:** one personal charm slot per hero.

---

## 8. Minimal UI, still
| Screen | In-world object |
|---|---|
| Combat | Diorama + land-styled reel: neon sign (Meridian) · torii with three hanging lanterns (Hyakki) · golden abacus (River Empire) · observatory sundial dials (Śūnyapura) · three marble columns with mosaic numerals (Kroton Nova) · slot machine (Crossroads) · Basilica clock (Meridian) |
| Map | Scroll / palm-leaf / mosaic / road map, by land |
| Market | A stall with wares on the table |
| Teahouse / Campfire | Heroes sit around; drag two beside NIL; constellation lines show bonds |
| Charms | Pinned to the reel frame, left to right |
| Lucky-number choice | The Naming terminal: ten Nixie tubes |

---

## 9. Jam slice scope (ships Nov 13)
**"Prologue & Act I: The Remainder and the Night Parade"**: the intro cinematic (a five-culture montage), the Prologue (Meridian Undercity, 3 nodes + Varro) and Act I (Hyakki, ~6 nodes + Tamamo), then an ending cinematic teasing the River Empire and Thale.

| System | In the jam slice |
|---|---|
| Core verb, reel, all 7 patterns, parry | ✅ |
| Heroes | NIL + Vesper (7) + Maeve (3) + Hina (9): choose 2 of 3 in Act I |
| Bonds / Link Arts | Complements, Neighbours, Twins; Link Art *Lucky Strike* (Vesper + Maeve) and *Midnight Parade* (Hina + Vesper) |
| Ultimates | ✅ every hero |
| Charms | 12: Hyakki set (beckoning cat, daruma, ofuda, 3 of the Seven Lucky Gods) + Meridian/Crossroads (horseshoe, rabbit's foot, black cat, four-leaf clover, thirteenth floor, seven-come-eleven); 3 slots |
| Wheel crafting | Remove + Gold/Jade/Glass at one Hyakki shrine; Maeve's forge upgrades a charm |
| NIL verbs | Splice + Carry |
| Bosses | Varro, Tamamo (nine tails, foxfire illusions) |
| Keeper's Trial | Enma (optional elite) |
| Not in jam | Economy beyond fen, oracle sticks, Ink, Karma, gems, Awakenings, Acts II–V |

---

## 10. Build & tech summary
Unity 6 LTS · URP · WebGL 2 (WebGPU optional) · Unity 2D Animation (PSB rigs) + Cinemachine 3 + Timeline + PrimeTween · VideoPlayer for cinematic clips from StreamingAssets · pure C# rules core with EditMode tests · ScriptableObject data for heroes, wheels, faces, charms (with set tags), enemies, boss rules and maps. Details in `PRODUCTION_PLAN.md` §5.
