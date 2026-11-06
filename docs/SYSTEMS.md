# ZERO-SUM: OMEN — Systems Design (luck mechanics, fantasy mechanics, kits, ultimates, charms)

The full rules behind [`GDD.md`](GDD.md). Numbers live in [`TUNING.md`](TUNING.md) (jam) and [`ECONOMY_PROGRESSION.md`](ECONOMY_PROGRESSION.md) (full game). Everything here obeys GDD §0: **one verb** (stop the number), everything else changes what that verb can do.

---

## 1. The luck model in one picture

```
 Hap (the god)             → Hap's Favour, Whispers, Open Hand shrines        (luck turns; coincidences)
 The land                  → Land Law (superstition as a rule)                (curses, blessings, interest, karma, sieve, loop)
 Your party                → lucky digits → bonds, Link Arts                  (who you bring)
 Your wheels               → faces: width = odds, enhancements                (what can land)
 Your tap                  → the stopped digit                                (skill)
 The reel                  → pattern × Mult                                   (the payoff)
 Your charms, gems, sticks → modify every layer above                         (the build)
```
Every layer is visible on screen: the sigil on the reel frame (Hap), the Land Law icon, the constellation lines (bonds), face widths, the reel, the charms pinned to the frame.

## 2. Luck mechanics

### 2.1 Fate Wheels and faces
- A wheel is a vertical strip of faces; **a face's height is its odds**. Starter wheels have **8 faces**: each hero omits two digits (below).
- The ones digit spins; the tens are fixed (hero level + gear). *Tens are safe, ones are fate.*
- Spin speed per hero (Slow 380, Medium 470, Fast 620 px/s at 1080p); assist mode −30%.

| Hero | Starter faces (omitted) | Widths |
|---|---|---|
| NIL | all but the two digits farthest from your number (e.g. digit 7 omits 2 and 1) | your digit ×2 |
| Vesper | omits 4, 9 | 7 ×2 |
| Maeve | omits 4, 8 | 3 ×2; 1 Horseshoe face |
| Hina | omits 4, 0 | 9 ×2; bounces |
| Ba Jinling | omits 4, 1 | 8 ×2; 2 Gold faces |
| Bai Si | omits 9, 0 | 4 ×3 |
| Shunya | omits 4, 9 | 0 ×3 |
| Prima | only 2, 3, 5, 7, 0 (5 faces, by design) | equal |
| Fibi | omits 4, 6 | her current digit ×2 (moves every round) |
| Varro | omits 4, 9 | 1 ×3 |
| Kyūsuke | omits 4, 9 | 5 ×2 |
| Liu Shun | omits 4, 7 | 6 ×2; Jade faces |

### 2.2 Reel patterns (GDD §1.3, priority §1.5)
Overwrite (×21 for every digit) → Reaper's Toll (×4, 44% of every Balance with a 4 in its Omen) → Jackpot (×digit, min ×2) → Cascade (×3, extra round) → Zero-Sum (×2, cancel enemy action) → Pair (×2) → Bust (×1). **Unlockable patterns:** Prime Trio (all three prime, ×5; Prime Party bond), Fibonacci Run (1-1-2, 2-3-5, 3-5-8: counts as Cascade with Fibi or the Golden Ratio charm), Four-tube patterns (NIL's *Remainder Release*, the Ledger Tree's *Remainder +1*): Two Pair ×3, Four of a Kind ×digit², Long Cascade ×5; Five-tube (Fibi's *Spiral Deal*): Full House ×6, Five of a Kind ×digit³.

### 2.3 Pattern Sight
When the third striker's wheel appears, faces that would complete a pattern shimmer in that pattern's colour (Pair silver, Zero-Sum cyan, Cascade blue, Jackpot gold, Overwrite white-gold). It teaches patterns without text and makes the last tap a decision. Accessibility: each shimmer also carries a shape (dot, ring, chevron, star).

### 2.4 Hap's Favour (luck turns)
- **Warm** (after 1 Bust; one die on the Open Hand sigil lights): next round all wheels −20% speed; faces matching a digit already on the reel are ×1.5 wide.
- **Hap's Hand** (after 2 Busts in a row; both dice light): the next round **cannot Bust**. If it would, Hap's hand flicks a die across the reel and it becomes a Pair (a small cinematic, never hidden).
- **Cools** after any pattern. Some charms and Whispers warm it on purpose.
- **Why:** the fantasy "my luck turned", and no player ever suffers three Busts in a row. Measured with `python3 tools/sim_patterns.py --favour` (jam party, 8-face wheels, 8-round fights):

| Player | Fights with 3+ Busts in a row | Bust rate |
|---|---|---|
| Random tapper | 52% → **0%** | 56% → 46% |
| Average (25% aim) | 25% → **0%** | 40% → 35% |
| Skilled (50% aim) | 6% → **0%** | 23% → 21% |

### 2.5 Land Laws (each land's superstition as a rule)
| Land | Law | Effect | Counter in the same land |
|---|---|---|---|
| Meridian | Debt | Every 3rd round, −5% party Balance unless the round scored a pattern | Vesper's Lucky Seven; any pattern |
| Hyakki | Shi and Ku | 4 curses the striker (−10% next strike); 9 curses your next parry; 7 and 8 bless (+1 Mult) | Hina (9s safe, +9 Mult); Ofuda ward |
| River Empire | Interest | 10% of each round's Mult carries to the next; resets on Bust; enemies too | Jinling's Compound; streak play |
| Śūnyapura | Karma | Parries and Zero-Sums bank Karma; Busts vs cursed enemies cost it | Shunya; 108 Beads |
| Kroton Nova | Indivisibility | Prime strikes pierce; composite strikes deal half; every 3 rounds the Sieve removes one composite face from each wheel | Prima; Factor |
| Crossroads | The House | Wagers before fights; every 3 rounds the fight loops (reel and enemy Balance reset; your build persists) | Fibi; Deals |
| Basilica | Fixed Fate | Wheels −5% speed and lose their least-used face each round | Outrun it |

### 2.6 Curses and blessings
- **Curses** (from Land Laws, enemies, Deals): shown as a small black ribbon on the hero's wheel. Lemon and Seven Chillies cancels one per fight; Ofuda cancels the first; Karma can buy one off.
- **Blessings** (from Shrines, Whispers, keepers): a gold ribbon. Lasts one fight unless stated.
- **Unlucky numbers by land** (13 in Meridian and the Crossroads, 17 in Kroton Nova, 4 and 9 in Hyakki, 4 in the River Empire) appear as enemy weak points: hitting an enemy whose Omen shows its land's unlucky number deals +13%.

### 2.7 Hap's Whispers (coincidence events)
Map nodes with a single choice, always about luck, always in the land's idiom (lists per land in [`ACT_DESIGN.md`](ACT_DESIGN.md)). Rules: one choice, two lines of text at most, no traps without a visible price, at least one Whisper per act is pure good luck (a gift from Hap).

### 2.8 Open Hand shrines
Rest nodes with a stone hand and a die. Choose one: **re-deal** one Market or reward offer; **pray** (start the next fight with Favour warm); **offer** fen (every 99 fen offered across the game unlocks one of Hap's faces in the gallery and a small permanent blessing).

### 2.9 Omen and Balance
Every combatant has a **Balance** (luck at stake); the Omen over its head shows the share left, 99 → 00 (GDD §1.6). The party shares one Balance. Rules that "read an Omen" read the two-digit display.

## 3. Fantasy mechanics (one per land, all built on the same verb)

| Land | Mechanic | What it does |
|---|---|---|
| Hyakki | **Tsukumogami faces** | A face stopped 100 times wakes up with a small soul: a random extra effect (e.g. +1 fen, a free re-spin once per fight). Faces can only wake once. Hina's kit interacts with this (her 99 → 100 arc) |
| River Empire | **Ink** (Judge Cui's Brush) | Rewrite one reel digit after it lands. NIL gets one free per fight from Act II (Rewrite); more from charms and sticks |
| River Empire | **Oracle sticks** (求签) | Shake the cylinder; a stick falls with a one-shot effect and a two-line fortune poem. 24 sticks; rarity by fortune (great luck → great misfortune, and misfortune sticks are powerful with a price) |
| Śūnyapura | **Karma** | Banked from parries and Zero-Sums; spend 1 to re-spin a wheel, 3 to block a lethal hit; carries between acts |
| Śūnyapura | **Navaratna gems** | Nine planetary gems, each permanently levels one pattern (below) |
| Śūnyapura | **Place Value** (NIL) | Move a stopped digit into the tens of the next strike (×10 its weight) |
| Kroton Nova | **Awakenings** (the Moirai's thread) | Each hero chooses one of two branches (§5) |
| Kroton Nova | **Factor** (NIL) | Split one strike into two reel digits (56 → 7 and 8) |
| Crossroads | **Deals** | A powerful boon with a lasting price (list below) |
| Crossroads | **Wagers** | Bet fen or Balance before a fight; win ×2 fen or a rare reward; lose the stake |
| Crossroads | **Loops** | The fight rewinds; your build persists |
| Basilica | **Divide by Zero** (NIL's final verb) | NIL's digit is wild on every wheel for one round |

### Navaratna gems
| Gem | Planet | Levels |
|---|---|---|
| Ruby (*Manik*) | Sun | Jackpot +1 level (+×1 base) |
| Pearl (*Moti*) | Moon | Pair (+×0.5) |
| Red coral (*Moonga*) | Mars | Reaper's Toll (spares one hero per level) |
| Emerald (*Panna*) | Mercury | Cascade (+×0.5, extra round chance) |
| Yellow sapphire (*Pukhraj*) | Jupiter | Omen Overwrite (+×1) |
| Diamond (*Heera*) | Venus | Link Arts (+15% each) |
| Blue sapphire (*Neelam*) | Saturn | Zero-Sum (cancels two enemy actions at level 3) |
| Hessonite (*Gomed*) | Rahu | Bust (+tens on a Bust) |
| Cat's eye (*Lehsunia*) | Ketu | Hap's Favour (warms after 1 Bust at level 2) |

### Crossroads Deals (sample of 12; each is "boon / price")
+2 charm slots / Omen display capped at 77 · Every Jackpot ×2 / Pairs pay ×1 · Free re-spin every round / enemies' wheels +20% speed · Start every fight with Favour hot / Shrines closed for the act · All Gold faces ×2 fen / Markets cost +50% · +1 reel tube / lose one hero's ultimate · Karma never decays / Karma can't block lethal hits · Overwrite charges ultimates twice / Busts curse the striker · See enemy wheels' next digit / your Pattern Sight is off · One free Wager win per act / Wagers can't be refused · Your digit ×3 wide / your digit's Jackpot pays ×1 · Revive once per act / the House takes 10% of all fen.

## 4. Hero kits, ultimates and secret recruits

| Hero | Digit | Passive | Ultimate (3–5 s cinematic) | Charge |
|---|---|---|---|---|
| **NIL** | yours | Grows by act: Splice · Carry · Rewrite · Place Value · Factor · Deal · Divide by Zero | ***Remainder Release***: the reel gains a 4th tube this round, filled by whatever NIL taps on a free wheel | Your digit lands 3 times, or an Overwrite |
| **Vesper Sette** | 7 | *Lucky Seven*: each 7 on the reel adds +7 to every strike this round | ***Seven-Chamber Requiem***: 7 auto-stopping mini-wheels; each 7 doubles the shot | Her 7 lands 3× |
| **Maeve Triskel** | 3 | *Third Time Lucky*: the round's 3rd strike counts double if Maeve made it; upgrades charms at forges | ***Triskele***: three spinning horseshoes each land a free 3 (a Jackpot of 3s, or Twins with NIL 3) | 3 lands 3× |
| **Hina** | 9 | *Ninety-Nine*: 9s don't curse her party; each 9 gives +9 Mult while her Omen is 99 or below | ***Hundred-Year Night***: her umbrella opens its eye; for one round every wheel shows only the party's lucky digits | 9 lands 3× |
| **Ba Jinling** | 8 | *Compound*: +0.8 Mult per consecutive patterned round | ***Eight Bells***: ×1.1 Mult per bell (×2.14) and +8 fen each | 8 lands 3× |
| **Bai Si** | 4 | *Fourfold*: every 4th strike of a fight marks the enemy (×1.44 damage taken) | ***Four Lanterns Out***: a Reaper's Toll that spares the party | 4 lands 3× |
| **Shunya** | 0 | *Pūrṇa*: 0s on the reel are wild for every pattern | ***Place Value***: move any reel digit into the tens of every strike next round | 0 lands 3× |
| **Prima** | 2 | *Indivisible*: prime strikes pierce; +1 Mult per prime on the reel | ***Sieve of Light***: shatter every composite number on screen (shields, armour) | a prime lands 3× |
| **Fibi Leone** | Fib. | *Golden Ratio*: Cascades ×1.618; Fibonacci triples count as Cascade; her digit advances each round | ***Spiral Deal***: the reel extends to 5 tubes this round | her current digit lands 3× |
| *Varro Kade* | 1 | *First and Only*: strikes first; on a Bust his digit fills the empty slots | ***Debt Collector***: steal the enemy's last reel digit into a jar, then smash it for ×6 | 1 lands 3× |
| *Kyūsuke* | 5 | *Bow*: once per fight, a 5 right after his bow makes the enemy skip a strike | ***Cucumber Tide***: every 5 on the reel heals the party 5% of Balance | 5 lands 3× |
| *Liu Shun* | 6 | *Six-Six Smooth*: two 6s make the rest of the round land in order (a free Cascade) | ***Thirteen Orphans***: the reel becomes 13 mahjong tiles for one round; any pair pays ×13 | 6 lands 3× |

## 5. Awakenings (Act IV: two branches per hero)

| Hero | Branch A | Branch B |
|---|---|---|
| NIL | ***The Remainder***: Divide by Zero charges 2× faster | ***The Open Hand***: Hap's Favour warms after 1 Bust for the whole party |
| Vesper | ***Dead Man's Hand***: crits (×3) on aces-and-eights (1 then 8 in a round) | ***Blackjack***: if the round's strikes total 21 (or 210…), ×21 |
| Maeve | ***Forge-Mother***: every charm gets +1 level at forges | ***Triskelion***: every third round is a guaranteed pattern |
| Hina | ***Hundred Years***: she turns 100: +100 tens, loses the 9 immunity | ***Kasa-obake***: stays a trickster: her wheel bounces into your best face once per round |
| Ba Jinling | ***Bank of Bells***: interest on fen (1 per 4 held, uncapped) | ***Golden Fan***: abacus beads hit every enemy for 8% of the round |
| Bai Si | ***True Count***: the 4th-strike mark is permanent | ***Mourning White***: Reaper's Toll heals the party instead of hurting it |
| Shunya | ***Śūnya***: 0s count as any digit for bonds too | ***Astrolabe***: she sees and shows every enemy wheel's next digit |
| Prima | ***Even Prime***: 2 counts as prime *and* composite (best of both) | ***Aegis***: the shield blocks the first two strikes each fight |
| Fibi | ***1,597***: her digit can be frozen for one round | ***Golden Spiral***: Cascades extend to 4 tubes |
| Varro / Kyūsuke / Liu Shun | ***Bailiff*** / ***Full Dish*** / ***Heavenly Hand*** | ***Free Man*** / ***River God's Friend*** / ***Mahjong Queen*** |

## 6. Bonds and Link Arts

Bonds (GDD §2.3): Complements (sum to 10), Neighbours (consecutive), Twins (same digit), Prime Party, Powers of Two, Śūnya, Old World / New World.

| Link Art | Pair | Bond | Effect | Look |
|---|---|---|---|---|
| ***Lucky Strike*** | Vesper + Maeve | Complement 7+3 | Ricochet ×7 hits | Burning horseshoe shot in mid-air |
| ***Golden Sieve*** | Ba + Prima | Complement 8+2 | Pierces all armour; +8 fen per hit | Coins pour through the sieve shield as spears |
| ***Ninety-Nine and One*** | Hina + Varro / Fibi on 1 | Complement 9+1 | The enemy's Omen display is forced to 01 for a round (×9 damage) | A hundred umbrellas open at once |
| ***Six Lanterns, Four Lanterns*** | Bai Si + Liu Shun | Complement 4+6 | Reaper's Toll that heals the party | Mahjong tiles burn like lanterns |
| ***Lucky Eight*** | Vesper + Ba | Neighbours 7-8 | Next 2 rounds' Pairs count as Jackpots | Gunshots ring eight bells |
| ***Lantern Fan*** | Ba + Hina | Neighbours 8-9 | Fan blows the enemy's wheel one face | A gold fan scatters paper lanterns |
| ***Spark and Shield*** | Prima + Maeve | Neighbours 2-3 | Shield bash + forge sparks: guaranteed Cascade | Hammer on shield |
| ***Third Lantern*** | Maeve + Bai Si | Neighbours 3-4 | Removes the enemy's next 3 faces | A horseshoe cuts a talisman |
| ***Midnight Parade*** | Hina + Vesper | Old/New World | Every wheel shows the party's digits for a round | Ukiyo-e yokai stampede through a saloon door |
| ***Zero Count*** | Bai Si + Shunya | Śūnya | Lanterns go out; the sundial shadow cuts the enemy (×10 to the last digit) | Shadow of the observatory gnomon |
| ***Golden Ratio Deal*** | Fibi + Shunya | Śūnya | Spiral of cards; a 5-tube reel with 0 wild | φ drawn in light |
| ***Prime Directive*** | Prima + Vesper + Maeve | Prime Party (2-3-7) | Prime Trio guaranteed | Three columns, three shots |
| ***Powers of Two*** | Prima + Bai Si + Ba | Powers of Two (2-4-8) | Doubles the next round's Mult, twice | Binary lanterns |
| ***Twins*** | NIL + anyone with NIL's digit | Twins | Shared ultimate gauge; that Jackpot ×2 | Mirror split-screen |

## 7. Charms of the World (63: nine per set, seven sets)

Holding 3 from one set: set bonus I; 5: set bonus II. Slots grow 3 → 6.

| Set | Charms (rule in short) | Set bonus I / II |
|---|---|---|
| **Meridian** (street luck) | Four-Leaf Clover (1 in 4: duplicate a digit) · Thirteenth Floor (×13 if the round total ends in 13) · Black Cat (first Bust → Pair) · Lucky 77 Jacket (+7 tens per 7) · Nixie Pendant (your digit +1 width) · Bazaar Ribbon (+1 charm slot, −10% damage) · Collector's Badge (+20% vs Collectors) · Naming Token (your digit's Pair ×3) · Gus's Receipt (Markets −15%) | +1 Mult per different culture held / charms trigger twice on Overwrite |
| **Hyakki** (shrine luck) | Beckoning Cat (+1 fen per strike ending in your digit) · Daruma (land your digit 3× → ×2 Mult for the fight) · Ofuda (first enemy strike parried) · Ebisu (+fen on Pairs) · Daikokuten (+tens on 8s) · Bishamonten (+parry window) · Benzaiten (Link Arts +20%) · Jurōjin & Fukurokuju (heal 3% per 7) · Hotei (Busts give +3 fen) | 7s are blessed twice / all Seven Lucky Gods: every 7 is a Jackpot by itself |
| **River Empire** (prosperity) | Red Envelope (+8 fen on a Jackpot) · Door God (parries strike back) · Peach-Wood Sword (×2 vs ghosts and Noiselings) · Money Toad (interest +1) · Jade Bi Disc (Jade faces +2 Mult) · Firecracker String (first round ×2) · Lucky Knot (Pairs heal 2%) · Dragon Boat Oar (Cascades +1 extra round chance) · Joss Paper (on Settle, +88 fen) | Interest doubled / every 8 on the reel is gold (+3 fen) |
| **Śūnyapura** (auspicious) | Lemon and Seven Chillies (cancel one curse per fight; +7 tens per 7) · 108 Beads (every 108th point counts double) · Rangoli Chalk (first Zero-Sum each fight ×3) · Peacock Feather (Favour warms 1 Bust sooner) · Brass Diya (+1 Karma per Pair) · Kolam Thread (Neighbours bonds active for any two digits) · Shankha Shell (enemies' wheels −10% speed) · Navagraha Ring (+1 gem slot) · Palm-Leaf Page (see the boss rule early) | Karma ×2 / 0 is wild for bonds |
| **Kroton Nova** (proportion) | Evil-Eye Bead (see the enemy's next digit) · Fortuna's Wheel (once per fight, re-roll the reel) · Owl Coin (+1 Mult per prime strike) · Olive Wreath (+10% Balance) · Golden Ratio (Fibonacci triples count as Cascade) · Tetractys Token (if strikes sum to 10, ×10) · Amphora (store a digit for later) · Laurel of Seven (×7 on 7-7-x) · Thread of Lachesis (one Atropos-style cut per act: remove an enemy face) | Primes pierce / perfect numbers (6, 28) on the round total pay ×6 |
| **Crossroads** (deals) | Horseshoe (your digit's cells 50% wider) · Rabbit's Foot (one free re-spin per fight) · Lucky Penny (+1 fen per 1) · Seven-Come-Eleven Dice (×7 if the round totals 7 or 11) · Pumpkin Lantern (×2 vs the headless) · Silver Dollar (Wager wins +50%) · Route 7 Sign (+7% speed on enemy wheels, +7 Mult) · Dead Man's Card (1-8 in a round: ×8) · Last Train Ticket (loop rounds keep the reel) | Deals' prices halved / one free Deal per act |
| **The Open Hand** (Hap; legendary, from shrines and Whispers) | Hap's Die (once per fight, set any reel digit) · Open Palm (Favour never cools below warm) · Shooting Star (once per act, re-deal a whole Market) · Coin on Its Edge (a Bust has 1 in 10 to become an Overwrite) · Rainbow at Night (+1 Mult per different digit on the reel) · Lucky Stranger (a random companion's passive each fight) · The Long Shot (Jackpots of 0 or 1 pay ×20) · Second Chance (revive once per run) · Hap's Laugh (on Overwrite, every charm triggers again) | Hap's Whispers appear twice as often / the finale's Fixed Fate is halved |

## 8. Other build systems
- **Wheel crafting** (River Empire Markets): Remove · Duplicate · Enhance (Gold +3 fen · Jade +4 Mult · Glass ×2 strike, 1 in 4 shatters · Iron +20 tens while not stopped · Lantern slows the wheel passing it · Ink wild · Horseshoe lands as your digit 1 in 4 · Cursed +50 tens, curses the striker · Foxfire shows as another digit to enemies).
- **The Ledger Tree** (from Act III): 7 branches (one per Seal), 3–4 nodes each, bought with memory digits from Seals and side quests. Capstones: *Remainder +1* (permanent 4th tube), *Audit Eye*, *Compound Remainder*, *Open Hand*.
- **Levels:** shared XP; +10 tens per level; cap 30. Digits never change.
- **Gear:** one personal charm slot per hero.

## 9. Interaction matrix (what combos, what breaks)

| | Charms | Wheel crafting | Gems | Karma | Deals | Link Arts | Hap's Favour |
|---|---|---|---|---|---|---|---|
| **Charms** | sets | Horseshoe + wide faces ⇒ reliable Overwrites | pattern charms × gem levels | Diya feeds Karma | Crossroads set halves prices | Benzaiten +20% | Open Hand set |
| **Wheel crafting** | | removing faces raises odds | | | +1 tube Deal | | Favour widens matching faces |
| **Gems** | | | | Cat's eye ⇒ Favour | | Diamond | |
| **Karma** | | | | | Karma Deal | | |
| **Deals** | | | | | | | "Favour hot" Deal |

**Watch list (likely to break the game, test first):** removing faces to 3 per wheel (guaranteed Jackpots: cap minimum faces at 4) · Hap's Laugh + Overwrite loops (cap at one re-trigger) · Tetractys Token + Factor (allow, but cap ×10 once per round) · Liu Shun's Thirteen Orphans with Twins (cap ×13 once per fight).
