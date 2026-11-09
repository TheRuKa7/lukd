# ZERO-SUM: OMEN — World Bible

> **8 November editorial revision:** [Resolved series bible](novel/RESOLVED_SERIES_BIBLE.md) supersedes conflicting older naming, origin wording, character backstories, political outcomes and story-length targets below. Gameplay formulas retain their existing domain authority. This source is being adapted to the49-chapter edition; its historical schedules and game scene numbering are not manga chapter numbering.

> *"Every soul a number. Every number a share. The books must balance."*
> — the Comptroller's catechism, recited at every Dawn Tally

This file is the story source of truth: world, lore, the god of luck, lands, villain, cast, plot and endings. The full scene-by-scene campaign is in [`STORY.md`](STORY.md); each land's acts, encounters and bosses are in [`ACT_DESIGN.md`](ACT_DESIGN.md). Mechanics live in [`GDD.md`](GDD.md); schedule and pipeline in [`PRODUCTION_PLAN.md`](PRODUCTION_PLAN.md).

Updated 7 November 2026. **Specified, not implemented or externally validated.** [DECISIONS.md](DECISIONS.md) resolves cross-document rules. The jam is the 10–15-minute Meridian Prologue in [JAM_SLICE.md](JAM_SLICE.md); other lands, bonds and endings below are the full campaign. [PROJECT_STATUS.md](PROJECT_STATUS.md) records evidence.

---

## 1. The one-paragraph pitch

In **the Tally**, every ordinary living soul carries a floating **Civic Omen** (00–99), its registered share of the world's luck. Luck is conserved under the Basilica: a gain must debit another account or an identified reserve. It wasn't always like this. Every people once had its own idea of fate: spun thread, a ledger of deeds, underworld books, a contract at midnight. Then the capital, **Meridian**, built **the Basilica** and bound those different ledgers into one machine that gives every registered soul one number.

**NIL** wakes in Meridian's slums with no number at all, only a glitching **NaN**. When NIL is made to state a lucky number at a back-alley Naming Rite, the Basilica screams **REMAINDER DETECTED**, and every bounty hunter in the world comes running. To stop the **Final Audit**, which will freeze every fate forever and erase NIL to balance the books, NIL must travel the lands of the Tally, free the ledgers the Basilica stole, gather a party from every culture, and learn the truth: NIL *is* the world's missing luck.

---

## 2. Why numbers matter (the rules of the world)

| # | Law | In the world | In the game |
|---|---|---|---|
| 1 | **Civic and Audit Omens differ** | The two-digit Civic Omen is personal luck/status; NIL's unregistered identity is NaN. | The separately framed **Audit Omen** normalizes staked **Balance** from 99 to 00. It is not the Civic Omen. NIL's NaN stays visible beside the party's shared Audit readout. |
| 2 | **The Zero-Sum Law** | Total luck is constant across people, reserves and the hidden Remainder. Fortune can be traded, taxed, inherited or stolen; interest debits an account. | Damage exhausts a stake; provisional strike numbers are not new Civic luck. Zero-Sum (three digits summing to 10 or 20) cancels the next enemy action. |
| 3 | **Resonance (your lucky number)** | At seven, every child performs the **Naming Rite** and states their lucky number. That digit is how the Basilica reads you and how you channel luck. | Each hero has a resonant digit. Their wheel favours it, and landing it charges their ultimate. The player chooses NIL's. |
| 4 | **Settlement** | **Civic settlement** at Civic 00 leaves someone vulnerable to lethal misfortune within days; it is a separate story event. | **Audit settlement** means Balance 0 and combat defeat, not automatic death or a Civic reset. Named people survive for their aftermath; constructs/Noise alone may disintegrate. |
| 5 | **Audits** | When fates collide, Omens contest. Trained **Auditors** summon a **Fate Wheel** (the old *Rota Fortunae*, Fortune's wheel, now made of digits) and strike with the digits they stop. | The core verb: every number spins, and you stop it. Combat is called an Audit. |

**Daily life details to show, not tell.** Lifts skip floors 4, 9 and 13. Weddings crowd onto the 8th. Gamblers kiss sevens. Beggars sell "luck-ins" (a point of Omen for a meal). Children compare Omens in the schoolyard. Shopkeepers hang a lemon with seven green chillies over the door, or a horseshoe, or a blue evil-eye bead, or a beckoning cat, depending on the street.

**Readout contract.** Resonance is a separate digit 0–9, never a health/status value. Positive Balance shows `ceil(99 × Balance / MaxBalance)`, clamped 01–99; zero Balance shows 00. MaxBalance is positive. Unless explicitly marked civic, combat rules read Audit Omen. A Collector's confiscation jar is a reserve account: the opening visibly debits six units from it as Ama rises Civic 01→07. NIL neither creates luck nor erases the Collector's number.

### Lucky and unlucky numbers across the Tally (the jam theme, built into the setting)
| Number | Where it's lucky / unlucky | Why (real-world belief the land is inspired by) |
|---|---|---|
| 0 | Śūnyapura (India-inspired) | Zero as a number was formalised in India; *śūnya* means void and also the place that holds everything |
| 2 | Kroton Nova (Greece-inspired) | The only even prime; Pythagoreans treated numbers as divine |
| 3 | Celtic quarter of Meridian | Triads, the triskele; "third time lucky" |
| 4 | Hyakki (Japan-inspired) and the River Empire (China-inspired), unlucky | 四 sounds like 死, death, in both Japanese (*shi*) and Chinese (*sì*/*sǐ*) |
| 7 | Meridian, Hyakki, the Crossroads | Western lucky seven; Japan's Seven Lucky Gods; "seven come eleven" at the dice table |
| 8 | The River Empire, Hyakki | 八 *bā* rhymes with 发 *fā* (to prosper); in Japan 八 widens like a fan (*suehirogari*) |
| 9 | Hyakki unlucky; River Empire lucky | Japanese *ku* echoes 苦 (suffering); Chinese *jiǔ* echoes 久 (long-lasting) |
| 13 | Meridian, the Crossroads, unlucky | Western triskaidekaphobia |
| 17 | Kroton Nova, unlucky | In Italian tradition XVII rearranges to VIXI, "I have lived" (i.e. I am dead) |
| 99 / 100 | Hyakki | Japanese folklore: objects that reach 100 years gain a soul (*tsukumogami*) |
| 108 | Śūnyapura | Sacred count of prayer beads |

---

## 2A. Hap, the god of luck who governs the Tally

> *"Hap deals. People choose."* — the oldest proverb in the Tally, said in every language

**Hap** is the Tally's one god of luck: not a god *of* a land, but the will inside chance itself. The name is the old word that still hides in *happen*, *happy*, *perhaps* and *mishap*. Hap is invented for this world; it is not any real religion's deity.

| | |
|---|---|
| **What Hap is** | Luck with a heart. Playful, generous, unfair, never cruel on purpose. Hap loves surprise more than anything: the long shot, the second chance, the stranger who turns out to be family. |
| **How Hap governs** | Hap never commands. It **deals**: every morning, before the Basilica, Hap scattered luck across the world like seed, unevenly, and let people decide what to grow. Every land built its own way of talking to Hap: thread, karma, books of the dead, a contract at midnight. Those ways are the **many ledgers**. |
| **How Hap appears** | Never the same face twice. To each land it shows the face that land's stories expect, drawn in that land's art style; in the game it appears as a figure of overlapping faces under a turning wheel of stars, with **two dice for eyes** and every digit 0–9 orbiting its head like a halo. Its voice is the sound of dice in a cupped hand. |
| **Symbol** | **The Open Hand**: an open palm with a die resting in it. Shrines to Hap are just that: a hand carved in stone, a die, and somewhere to sit. |
| **Signs of Hap** | Coincidences. A coin landing on its edge, a stranger with your birthday, a rainbow at night. People say "Hap's watching" and buy a ticket. |
| **Hap and the land gods** | Every land keeps its own revered figures (the Seven Lucky Gods' shrine in Hyakki, the keepers of the old ledgers, Fortuna's wheel in Kroton Nova, Lady Luck at the Crossroads card tables). In this world they are how each culture *talks about* luck; the game never claims they are secretly Hap, and never makes them villains (§10). |

**What happened to Hap (the truth, revealed across the game):**
1. **The Binding** (TR 380–690) took the ledgers: the ways people spoke to Hap.
2. **The Final Binding** (TR 702): the Basilica's heart, the **Even Hand engine**, closed around Hap itself. The Basilica's great amber eye is **Hap's eye, caged**. Since then Hap no longer deals; it is **counted**. Every Dawn Tally divides the caged god into whole-number shares: the Omens.
3. **The Rounding** shaves the fractions off Hap every morning. Three hundred years of shavings pooled into one account, and the account woke up: **NIL is the part of Hap that refused to be counted.** NIL is not Hap, and not a god; NIL is a person made of the god's lost change, and the last free piece of luck in the world.
4. **The Deficit** is Hap starving in the cage. **Noise storms** are its seizures. **The Default** that the theologians fear is not "the Noise returns"; it is **Hap's death**, after which nothing would ever happen by chance again: no surprises, no second chances, no luck at all.
5. **Thale** inherited the Basilica, discovered the cage in TR 999 and developed **Fixed Fate**. He believes continuing its emergency allocations is mercy: “I inherited the box. I can make it safe.” His Final Audit would absorb NIL and freeze chance completely. His belief is wrong: ending all chance kills Hap rather than curing the Default.

**Hap in the game:** before the finale, Hap speaks only in dreams. At each campaign segment's end NIL dreams of a dice-starred void where Hap appears with the face of the land just visited and asks one question (STORY; BOND_ARCS §2). Hap can speak openly when its cage is exposed in the finale. In play it appears through **Favour**, **Whispers** and **Open Hand shrines** (SYSTEMS). The jam ends at the rooftop; a dream is not required.

## 3. History (the myth told in the intro)

1. **The Noise.** Before numbers, fortune moved like weather: Hap dealt freely, and nobody kept accounts. Floods and fortunes fell where they fell.
2. **The Many Ledgers.** Every people learned to keep accounts with fate in its own way:
   - In **Kroton Nova**, three sisters, the **Moirai**, spin, measure and cut the thread of every life.
   - In **Śūnyapura**, the scribe **Chitragupta** records every soul's deeds for the lord of death, and the land's mathematicians gave the world **zero**.
   - In **the River Empire**, the underworld's Ten Courts keep the **Book of Life and Death** (生死簿), and a Judge holds the brush that writes in it.
   - In **Hyakki**, the King of Hell, **Enma**, keeps a ledger of the dead, and objects that live a hundred years wake up with souls.
   - In **the Crossroads Territory**, a stranger waits where two roads meet at midnight with a black book, and anyone can sign a deal for luck.

   None of these ledgers agreed. Luck meant karma in one land, thread in another, a contract in a third. The world was messy, plural and alive.
3. **The Basilica.** Meridian, a young trading capital at the centre of the Tally, sent actuaries to every land. Over three centuries they **copied, bought or seized each ledger** and bound them into one brass engine, **the Basilica**, which recomputes one Omen for every soul at sunrise (**the Dawn Tally**). One number for everyone; one law for luck. In TR 702 the engine's heart closed around **Hap itself** (§2A); since then the god of luck is not worshipped in Meridian, it is *counted*. Meridian became the capital of the world because it holds the merged Ledger.
4. **The Rounding.** Every Dawn Tally drops fractional luck from the visible accounts into an unlisted account. The total remains conserved, but circulating luck declines. The process began in TR 702; its cumulative consequence went unrecognized until the observatory measured the Deficit and Thale later found the cause.
5. **The Deficit (now).** The observatory first measured declining available luck in TR 962, forty years ago. Noise storms are spasms of the starving caged Hap, not luck being newly created. **Objective truth:** the Default is extinguished chance and absolute stillness. **Public doctrine:** the Basilica warns that collapse will return the Noise. These are different claims, not two contradictory objective definitions.

**The secret (midpoint reveal, Act III, in Śūnyapura, the land that invented zero):** the rounded-down fractions didn't vanish. Three centuries of everyone's lost remainders pooled into a hidden account, and that account became a person. **NIL is the Remainder**, the world's missing luck, embodied. NIL has no Omen because NIL isn't *in* the Ledger. NIL *is what the Ledger owes.*

**The final secret (Finale, inside the Basilica):** the remainders were shaved from **Hap**. NIL is the last free piece of the god of luck. Settling NIL would complete the count, and Fixed Fate would freeze Hap forever.

---

## 4. The villain: Comptroller Lucan Thale

| | |
|---|---|
| **Role** | Comptroller of Meridian, master of the Basilica |
| **Look** | Tall, ageless; immaculate white-and-brass vestments shaped like a clockwork cathedral; a monocle with a turning gear; his Omen frozen at **50** (the perfect median), rendered in steel, not light |
| **Voice** | Calm, kind, exhausted. Narrates the intro myth. |
| **Backstory** | Born in Meridian's slums. At twelve, a Noise storm took his family and his street in one minute, by pure chance. He became the greatest actuary in history to make sure chance never decides anything again. |
| **His plan: the Final Audit** | 1) Capture the Remainder (NIL) and settle it back into the Ledger, closing the Deficit. 2) Freeze every Omen forever ("Fixed Fate"): no luck, no loss, no Noise. |
| **The real benefit he defends** | His emergency allocations have reduced accidents on protected routes by transferring luck from reserves and less protected districts; the cost is disclosed in Act II records. He believes permanent control will prevent the Default. |
| **Why he's wrong** | He perpetuates an inherited flattening of regional ledgers, hides who pays for safety, and would erase NIL and kill chance by freezing Hap. |
| **Line** | *“Thread, karma, contracts: every account left someone behind. I inherited the arithmetic. I will end the loss.”* |

**How he hunts NIL: the Auditors and the Seals.** Six **Auditor offices** control ledger locks: local pact-holders, Varro's Undercity office, and the surveyors' paired eclipse-engine control office. Each holds one Seal Digit. Pacts began in TR 999; Varro inherited his office and its Seal in TR 1001. Thale promises protected allocations under Fixed Fate. Breaking a Seal ends its monopoly/control channel; local ledgers regain agency while physical originals remain in the Basilica archive until the finale. The ritual Upper Gate needs six acquired digits plus NIL's chosen resonance in its seventh socket; duplicate digits still occupy different keyed sockets.

**Why the party fights:**
1. NIL is hunted: every Auditor wants the bounty.
2. The gate needs the Seal Digits.
3. Each land suffers under its Auditor's deal, and breaking a Seal returns that land's own idea of luck to its people.
4. Each companion comes from one land and has a personal stake there.
5. If the Final Audit happens, NIL is erased and fate is frozen.

---

## 5. The lands: a journey across the world's mythologies

The Tally is a ring of lands around Meridian's plateau. The upper city is sealed, so to go up, you must go around.

| Act | Land | Inspired by | Art style | Ledger held there | Law of the land | Auditor (boss) | Seal |
|---|---|---|---|---|---|---|---|
| **Prologue** | **Meridian Undercity** (the Remainder Wards) | A cosmopolitan modern capital | Anime cyber-noir: rain, neon, Nixie signage | The Basilica itself | *Debt*: everyone owes luck | **Varro Kade, the Ledgerhound** | 1 |
| **I** | **Hyakki (百鬼), the Isles of a Hundred Demons** | Japanese folklore | *Ukiyo-e* woodblock prints + anime: flat colour, bold outlines, Hokusai waves, torii, lantern light | **Enma's Ledger** of the dead | *The Rule of Shi and Ku*: 4 and 9 are cursed; 7 is blessed | **Tamamo, the Nine-Tailed Auditor** | 9 |
| **II** | **The River Empire**: Bāfā Harbor (八发港) above, the Ten Courts (十殿) below | Chinese folk religion and festival culture | Ink-wash (水墨) for the underworld; *gongbi* (工笔) fine line and gold leaf + neon for the harbor | **The Book of Life and Death** and the Judge's Brush | *The Rule of Interest*: luck compounds | **Chancellor Jin Chan (金蟾), the Golden Toad** | 8 |
| **III** | **Śūnyapura, the City Where Zero Was Born** | Indian mythology, astronomy and mathematics | Indian miniature painting and Pattachitra outlines + anime; monsoon light; giant stone observatory instruments; geometric stepwells | **Chitragupta's Ledger** of deeds (karma) | *The Rule of Karma*: every action is recorded and returns | **Eclipse Engines “Rahu” and “Ketu”** (invented Basilica constructs) | 0 |
| **IV** | **Kroton Nova, the Sieve of the Aegean** | Greek mythology and Pythagorean number mysticism | White marble, Aegean blue, mosaic and red-figure-pottery motifs + anime | **The Thread of the Moirai** | *The Rule of Indivisibility*: only primes pass | **Archon Seventeen** of the Pythagorean Synod | 2 |
| **V** | **The Crossroads Territory** | American folklore: frontier tall tales, the blues crossroads legend, immigrant charms, desert neon | Americana: desert sunsets, Route-66 motels, pulp-poster lettering, art-deco casino neon | **The Black Book of the Crossroads** | *The Rule of the House*: the night loops, and every deal has a price | **The House (Octavian Nine, "Mr. Eighty-Nine")** | 7 |
| **Finale** | **Meridian & the Basilica** | — | Brass clockwork cathedral, monochrome + Nixie amber; every land's art style appears on its wall | All of them | *Fixed Fate* | **Comptroller Lucan Thale** | *yours* |

**Gods are not the villains.** Revered figures (including Rahu/Ketu) are not enemy targets. Keepers pose nonlethal trials. The Act III targets are invented, visibly bolted brass eclipse engines named “Rahu” and “Ketu” by Basilica surveyors; they are not the celestial beings, their bodies, avatars or disguised forms. Their control seal is the Act III Auditor's lock. Destroying machinery releases the sky's ordinary eclipse rather than defeating a deity. Other Auditors are mortals or fictionalized folklore tricksters accountable for their choices.

### Luck and superstition by region (what each land believes, and how it plays)
| Land | What luck means here | Lucky | Unlucky | Everyday customs | Becomes in play |
|---|---|---|---|---|---|
| **Meridian** | A number you own, rent or owe | 7, 77, 99 | 13 (floors skipped), 00 | Charms of every culture on one door; kissing sevens; selling "luck-ins" | *Debt*: the Collectors' interest; Charmpunk shops sell every set |
| **Hyakki** | A relationship with spirits; old things wake up | 7 (Seven Lucky Gods), 8 (*suehirogari*, widening fan) | 4 (*shi*, death), 9 (*ku*, suffering) | Daruma eyes, omamori, beckoning cats, throwing salt, no room 4 | Shi/Ku: 4 curses striker's next strike; 9 curses next party defence; SYSTEMS owns exact values. Faces awaken after 100 stops |
| **River Empire** | Prosperity that compounds; harmony between the living and the dead | 8 (*fā*, prosper), 6 (*liù*, smooth), 9 (*jiǔ*, lasting) | 4 (*sǐ*) | Red envelopes, the money toad, oracle sticks, burning joss paper for ancestors | *Rule of Interest*: Mult compounds; ancestors' gifts at shrine nodes |
| **Śūnyapura** | Deeds and their return (karma), auspicious timing | 0 (the place that holds everything), 108, 9 (*navagraha*) | Inauspicious hours during the eclipse | Lemon and seven chillies, rangoli, the nine gems, auspicious hours | *Rule of Karma*: parries and Zero-Sums bank Karma; every action returns |
| **Kroton Nova** | Purity and proportion; the thread the Moirai spin | Primes, 2 (the even prime), the golden ratio | 17 (VIXI), composites (in the Synod's eyes) | Evil-eye beads, spitting three times, Fortuna's wheel | *Rule of Indivisibility*: composite strikes weaken; primes pierce |
| **The Crossroads** | A deal: luck is bought, borrowed and owed | 7, 11, 21 | 13, the dead man's hand (aces and eights) | Horseshoes open end up, rabbit's foot, lucky penny, never count money at the table | *Rule of the House*: the night loops; Deals and Wagers |
| **The Basilica** | Arithmetic; luck abolished | 50 (the median) | Remainders, NaN | Clocks strike 0 at dawn; children perform the Naming Rite at seven | *Fixed Fate*: wheels slow and freeze; the finale takes luck away |

### Land notes (enemies, set pieces, superstitions)

**Meridian Undercity** (Prologue)
- Enemies: Debt Hounds (cyber-dogs), Collectors (armoured bailiffs), Noiselings (glitch sprites).
- Set piece: the Dawn Tally beam sweeping the slums. Its immigrant quarters mix every land's charms on one street.
- Superstition: "Don't let a collector read your number twice."

**Hyakki** (Act I, Japan-inspired)
- Enemies: *Kasa-obake* (one-eyed hopping umbrella spirits), *Chōchin-obake* (lantern ghosts), *Kappa* (river imps who lose their strength if they bow), *Oni* enforcers.
- Set piece: the **Hyakki Yagyō**, the Night Parade of One Hundred Demons, crossing a red bridge under a full moon; a shrine of the **Seven Lucky Gods**.
- Superstitions: no room 4 or 9; daruma dolls get one eye painted when you make a wish and the other when it comes true; the beckoning cat (*maneki-neko*).

**The River Empire** (Act II, China-inspired)
- Bāfā Harbor enemies: Abacus Golems, Debt Junks (armed river boats), Golden Koi spirits (multiply when hit).
- Ten Courts: Ox-Head & Horse-Face (牛头马面) are the Courts' wardens and appear as a **trial**, never as villains (they are satisfied only if both are bested in the same round); enemies are Hungry Ghosts (they eat your fen), Jiangshi and Basilica auditors posted below.
- Set pieces: the Lantern Festival over the Luck Exchange; crossing Naihe Bridge past Meng Po's pavilion of forgetting.
- Superstitions: 8 for prosperity; red envelopes; the three-legged money toad; burning joss paper for the dead.

**Śūnyapura** (Act III, India-inspired)
- Enemies: Vetālas (riddling corpse-spirits from the *Vikram and Betaal* tales, who ask a question before they fight), Brass Yantra Guardians (animated observatory instruments), Monsoon Nāgas (serpent spirits of the stepwells).
- Set pieces: a city-sized open-air observatory of stone sundials and astrolabes; a vast geometric stepwell descending into the dark; the Hall of Chitragupta with palm-leaf records to the horizon.
- Superstitions: a lemon and seven green chillies at the door (*nimbu-mirchi*) against the evil eye; 108 prayer beads; the nine planetary gems (*navaratna*).

**Kroton Nova** (Act IV, Greece-inspired)
- Enemies: Bronze Automata (Talos-like), Harpies, Composite Knights (the Synod's armoured guard), Sirens who sing numbers.
- Set pieces: a white island city built as a giant stone sieve, where citizens whose Omens are composite fall through the holes; the cave where the three Moirai spin.
- Superstitions: the blue evil-eye bead (*mati*); spitting three times against bad luck; Fortuna's wheel; unlucky 17 among the Italian-descended merchants.

**The Crossroads Territory** (Act V, America-inspired)
- Enemies: the Headless Horseman of the hollow, Card-Sharp Automata, Tumbleweed Golems, a Ghost Train whose cars are Loop Echoes of your party.
- Set pieces: a desert crossroads at midnight under one streetlamp; the casino boomtown of Lucky Strike where the same night repeats; a dust storm made of playing cards.
- Superstitions: horseshoes over doors (open end up), rabbit's foot, lucky penny, four-leaf clover, "seven come eleven", never count your money at the table.

### The Far Lands (expansion plan, not the main game)
Uncommitted research directions, outside the jam and first campaign. No content or release date is promised. Each needs source research, explicit cultural-risk review and the same production gates; AI checks cannot be represented as native expertise:
- **Norse North**: the three Norns at the Well of Urðr; nine worlds; runes.
- **Kemet** (Egypt): the Weighing of the Heart against Ma'at's feather; 42 assessors.
- **The Long Count** (Maya): the other civilisation that invented zero; a base-20 calendar.
- **Anansi's Coast** (West Africa, Akan folklore): the spider who bought all the world's stories from the sky god.
- **The House of Wisdom** (Islamic Golden Age): al-Khwārizmī, whose name gave us "algorithm"; the *hamsa*.

---

## 6. The cast

### NIL, the protagonist (the Remainder)
| | |
|---|---|
| **Digit** | The player's choice (0–9) |
| **Look** | ~19, androgynous; silver-white hair with one Nixie-orange streak; amber eyes; a broken holographic **NaN** where an Omen should be; long asymmetric black actuary's coat with brass ledger clasps; a cracked brass **decoder** fused into the right wrist that leaks orange light and floating digits |
| **Personality** | Quiet, observant, dry humour; counts things when anxious; fascinated by other people's numbers because they don't have one |
| **Wants → Needs** | Wants a number and a normal life. Needs to accept being what everyone lost, and choose what to give back. |
| **Arc** | Prologue: hunted nobody → I: learns the Basilica cheats even the dead → II: learns luck is power and debt → III: **learns they are the Remainder** → IV: rejects the idea that some numbers are worth less → V: refuses to loop or hide → Finale: decides the world's future |
| **Growth (the most important in the game)** | Each Seal returns a **memory digit**: NIL's fragments are other people's stolen remainders, so each flashback is someone else's lost moment of luck, in the art style of that land. NIL gains a new verb per act (GDD §6). |

### The roster (8 companions; NIL + 2 in the party)
| Hero | Digit | From | Recruited | Class | One-line |
|---|---|---|---|---|---|
| **Vesper Sette** | 7 | Meridian (raised in the Crossroads casinos) | Prologue | Gunslinger | Ex-croupier who rigged games for the House, until a rigged hand Settled a child |
| **Maeve Triskel** | 3 | Meridian's Celtic immigrant quarter | Prologue (optional) | Charm-smith | Blacksmith's daughter who forges horseshoes and clovers into weapons |
| **Hina of the Ninety-Nine (九十九 雛)** | 9 | Hyakki | Act I | Tsukumogami trickster | An old paper umbrella that woke up with a soul, one year short of a hundred |
| **Ba Jinling (八金铃)** | 8 | River Empire | Act II | Financier | Loan shark who secretly forgives the debts she buys; the Golden Toad's daughter |
| **Bai Si (白四)** | 4 | River Empire (Ten Courts) | Act II | Executioner | The underworld's headsman, who keeps count so no dead soul is lost |
| **Shunya (शून्य)** | 0 | Śūnyapura | Act III | Astronomer | Young mathematician at the great observatory who proves what NIL is |
| **Prima of Kroton** | 2 | Kroton Nova | Act IV | Paladin | The Synod's "even prime" novice, the odd one out |
| **Fibi Leone** | Fibonacci | The Crossroads | Act V | Dealer | Card prodigy in the repeating night; initially the only local retaining full memories |

Eight core companions and three secret companions plus NIL make 12 authored playable characters across campaign/postgame. Each companion has four **narrative bond stages**, some integrated into story scenes (BOND_ARCS). These are distinct from mathematical resonance bonds and the Act IV Awakening choice. Core bond completion supplies an additional passive/Link Art upgrade and the ending proof; every required core stage has a catch-up route before commitment. Secret recruits never gate the central resolution.

#### Vesper Sette (7)
- **Look:** tall, crooked grin, scar across the lip; black hair with a crimson underlayer in a long braid; crimson long coat over a croupier's waistcoat; wide-brim hat with cards in the band; a revolver with a **seven-chamber cylinder** engraved 1–7.
- **Personality:** dry bravado, gambler's charm, guilt hidden behind jokes. Flips a coin before every decision and ignores the result.
- **Backstory:** dealt for the House in Lucky Strike. Ran when a hand she rigged Settled a twelve-year-old.
- **Bond arc:** teaches NIL to read tells → admits the rigged hand → faces the House → deals an honest hand.
- **Ledger piece:** the House's marked deck, proof the Crossroads deals were rigged.

#### Maeve Triskel (3)
- **Look:** freckled, red hair in three braids; leather apron over work clothes; **horseshoe-knuckle gauntlets**; a four-leaf-clover pin; a triskele (triple spiral) burned into her forge hammer.
- **Personality:** loud, warm, stubborn, superstitious about everything and proud of it.
- **Backstory:** her family fled a recent tightening of the old Rounding system in TR 990. Her grandmother's charms stopped working then; neither woman witnessed the system's creation in TR 702. Maeve makes new ones.
- **Role:** upgrades charms at the forge (crafting tie-in); comic warmth for the party.
- **Ledger piece:** a horseshoe forged from the first Basilica gear, which can hold one Seal open.

#### Hina of the Ninety-Nine (九十九 雛, 9)
- **Look:** small girl-shaped spirit; a **red-and-white paper umbrella** she rides and fights with (sometimes it opens a single eye and sticks out its tongue, like a *kasa-obake*); short black bob; furisode kimono patterned with numbers 1–99; geta sandals.
- **Personality:** mischievous, ancient and childish at once; obsessed with turning 100.
- **Backstory:** a 99-year-old umbrella left at Enma's shrine. In Japanese folklore objects that reach 100 years gain a soul (*tsukumogami*). Hina woke up early, at 99, because she was soaked in a century of other people's wishes. The Basilica's Fixed Fate would freeze her at 99 forever: never quite real.
- **Bond arc:** NIL helps her decide she's already real.
- **Ledger piece:** a torn page of Enma's ledger stuck in her umbrella ribs.

#### Ba Jinling (八金铃, 8)
- **Look:** modern jade-and-gold qipao; eight tiny golden bells in her hair ornaments and anklets; a **folding fan whose ribs are abacus rods**; smoky violet eyes; red lips.
- **Personality:** theatrical, sly, mercenary on the surface, enormous heart.
- **Backstory:** Chancellor Jin Chan's daughter. She left the Luck Exchange when she learned how his fortune was built.
- **Ledger piece:** her father's true account book, the proof of the Exchange's fraud.

#### Bai Si (白四, 4)
- **Look:** very tall, pale; long white hair bound with black funeral ribbon; white mourning robes (white is the mourning colour in Chinese tradition) inked with 四; a huge guandao-style blade hung with four paper talismans; joss paper swirls around him.
- **Personality:** stoic, formal, honour-bound, unexpectedly tender with children.
- **Backstory:** the Ten Courts' executioner, who counts every Settled soul so none is forgotten.
- **Turn:** NIL's decoder shows him three centuries of rounding: his count has always been short. He joins after Judge Cui's trial.
- **Ledger piece:** the true count of the dead.

#### Shunya (शून्य, 0)
- **Look:** young woman astronomer; dark hair in a long braid with brass astrolabe pins; indigo-and-saffron layered clothing with mirror-work; a **brass astrolabe** she spins like a weapon; palm-leaf manuscripts tied at her hip; ink-stained fingers.
- **Personality:** brilliant, impatient, joyful about ideas, kind to people who are slow.
- **Backstory:** works at the great observatory where her ancestors formalised zero. She calls 0 "the place that holds everything", not "nothing". She has been tracking the Deficit for years and found that it equals a *person's worth* of luck.
- **Role:** delivers the midpoint reveal to NIL with gentleness and maths.
- **Ledger piece:** the proof: the Remainder equation.

#### Prima of Kroton (2)
- **Look:** short blonde hair, blue eyes; white-and-gold armour with Greek-key borders; a **giant shield shaped like a sieve**, set with blue glass; a halo of floating glyphs 2-3-5-7.
- **Personality:** earnest, loud, honest to a fault; comic relief who becomes the moral backbone.
- **Backstory:** the Synod calls 2 "the even prime", the odd one out. She has always felt like a mistake in a holy system.
- **Bond arc:** discovers the Sieve is a culling machine; must face her mentor, Archon Seventeen.
- **Ledger piece:** a strand of the Moirai's thread, given to her by Lachesis.

#### Fibi Leone (Fibonacci)
- **Look:** 18; golden hair in spiral curls; spiral-patterned irises; tailored croupier tailcoat with headset; glowing cards that flow around her in a golden spiral.
- **Personality:** fast-talking, anxious, brilliant; laughs at bad moments.
- **Backstory:** dealer at the House, the only local initially retaining full memories. The party arrives during the 1,597th iteration, after 1,596 completed repeats. The pact began in TR 999; outside time advances only one night while local time repeats. NIL's unregistered account anchors the party's new memories; Fibi has never met this party on earlier iterations and predicts familiar local routines, not NIL's new sentences.
- **Twist:** Octavian Nine, her grandfather, believes the loop prevents a fatal dawn. His maintenance contract actually drains her at dawn; cancelling that clause, not simply winning damage, allows her to live.
- **Ledger piece:** the last page of the Black Book: her grandfather's own deal.

### The Auditors (bosses) and the keepers (trials)
| Boss | Land | Look | Motive | Fight (the rule) | After defeat |
|---|---|---|---|---|---|
| **Varro Kade, the Ledgerhound** | Meridian | Hulking bailiff, hound-skull mask, debt jars on his belt | Wants the bounty to buy his sister's exemption | **Debt Jar:** a stored last-slot token, visible debt and defence recovery; exact replacement/restoration in BESTIARY/SYSTEMS | Spared; returns in Act V |
| **Tamamo, the Nine-Tailed Auditor** | Hyakki | A nine-tailed fox in courtly layered robes; foxfire (*kitsunebi*) floating around her; each tail tipped with a glowing digit | Yokai fade when people stop believing in them; Thale promised Fixed Fate would make yokai permanent | **Nine Tails:** each tail has its own small Balance; foxfire **illusion faces** appear on your wheels (they show one digit and land as another); landing a 9 hurts you (*ku*) unless Hina is in the party | Retreats into legend; leaves Hina a tail-blessing |
| **Chancellor Jin Chan, the Golden Toad** | River Empire | Enormous jovial lord robed in gold coins on a three-legged toad throne | His bank will hold the world's frozen luck | **Interest:** his Balance grows every round; he taxes your Jackpots; phase 2 he swallows a hero (land a Pair to free them) | Bankrupted; Jinling takes over the Exchange |
| **Eclipse Engines “Rahu” and “Ketu”** | Śūnyapura | Invented brass occluder disc and articulated surveyor rail; visible bolts, operator stamps and broken cables, no sacred bodily imagery | Execute the Basilica surveyors' order to suppress inconvenient measurements | **The Eclipse:** two linked machine Balances; telegraphed occlusion and equalization (BESTIARY) | Machinery shuts down; natural celestial figures remain revered and untouched |
| **Archon Seventeen** | Kroton Nova | Gaunt, beautiful, terrifying; a laurel of bronze and a sieve-shaped staff; his Omen is 17 | Faith: the Final Audit is purification; only the indivisible deserve to remain | **The Sieve:** each round he strikes digits off *your* wheels (multiples of 2, then 3, then 5…, like the Sieve of Eratosthenes); composite strikes are halved | Falls through his own sieve; Prima saves him |
| **The House, Mr. Eighty-Nine** | Crossroads | Elegant old croupier in a white suit, ouroboros tattoo, backwards pocket watch; met in Lucky Strike, distinct from the Stranger | Loops the night to protect his granddaughter; financed recent Basilica operations, not the centuries-old construction | **The Loop:** enemy Balance and the reel reset on marked loop boundaries; build, Karma and Mult persist (SYSTEMS) | Cancels the fatal contract, relinquishes control and leaves town alive |
| **Comptroller Lucan Thale** | Meridian | see §4 | Fixed Fate | **Three phases:** Regression to the Mean (wheels compress toward 5) → Fixed Fate (wheels stop spinning: a puzzle) → Zero (NIL alone; all companions return as Link Arts) | Depends on ending |

**Keepers (trials, not villains):** Enma in Hyakki (judges whether NIL may pass the shrine) · Judge Cui in the Ten Courts (tests NIL for the Brush) · Chitragupta in Śūnyapura (reads NIL's empty page) · the Moirai in Kroton Nova (Clotho, Lachesis and Atropos each pose one challenge) · the Stranger at the Crossroads (offers the deal). These are elite "trial" fights with special rules and no hatred.

---

## 7. Plot beats by act

**Prologue: "NaN"** (Meridian Undercity)
1. *Interactive cold open* (§8). Dawn Tally; NIL transfers six confiscated units to Ama; Naming/lucky digit; REMAINDER DETECTED. No mandatory myth film precedes input.
2. Tutorial Audit vs Debt Hounds, alone.
3. Vesper saves NIL (“Need a hand? Seven fen.”). In the full campaign only, Maeve's forge is an early optional route with guaranteed later recruitment.
4. Varro corners them at the drain gates. Boss. Spared.
5. **World-map reveal:** Vesper explains the seven Seals; six lands light up on the map in six art styles. Seal 1.

**Act I: "The Night Parade"** (Hyakki)
1. Arrival by ferry under a Hokusai wave. The Night Parade crosses the bridge, and the party hides inside it.
2. **Hina** jumps out of a shrine's umbrella stand and attaches herself to NIL ("You smell like a hundred wishes").
3. Shrine of the Seven Lucky Gods (charms); kappa river crossing; **Enma's trial** at the gate of the dead.
4. **Tamamo** in her fox-fire palace. Boss.
5. Tamamo, defeated, asks NIL what a yokai is worth without belief. Seal 9.
6. *Epilogue:* Thale in the Basilica: "The Remainder is learning to count."

**Act II: "Eight Bells and the Book of the Dead"** (River Empire): the Lantern Festival and the Luck Exchange; Ba Jinling buys the party's bounty and hides them; descent through the river's end into the Ten Courts; **Judge Cui's trial** grants the Brush; **Bai Si** joins; return to face **Jin Chan**; father and daughter. Seal 8.

**Act III: “Śūnya”** (Śūnyapura): monsoon arrival; Vetāla riddles; **Shunya** at the observatory; **Chitragupta's Hall**, where NIL's page is blank; **the reveal: NIL is the Remainder**; the invented **Eclipse Engines “Rahu” and “Ketu”** obstruct the sky. Seal 0.

**Act IV: "Indivisible"** (Kroton Nova): Prima defects when the Sieve drops a school; **the Moirai's cave** (three trials); **Archon Seventeen**. Seal 2.

**Act V: "1,597 Nights"** (Crossroads Territory): the midnight crossroads deal; the same night repeating; **Fibi** remembers; Varro returns to help; Vesper's honest hand; **the House** lets dawn come. Seal 7.

**Finale: "Zero-Sum"** (Meridian): the gate takes six digits and the seventh is **the player's lucky number**. Inside the Basilica, the walls show every land's original ledger. Thale's three phases. The choice.

---

## 8. Opening and myth montage

The jam and full campaign share the **interactive cold open**: Start/audio unlock → Rain Alley rescue by 20 seconds → Naming choice by 60 seconds → detection → solo Audit. FIRST_10_MINUTES and JAM_SCRIPT supply exact jam timing and lines. Story text pauses for reading; these are onboarding targets for a normally advancing first session, not a forced countdown or a measured result.

| Beat | Required presentation | State meaning |
|---|---|---|
| Dawn and Ama | Civic 03→02→01; a Collector jar visibly holds six confiscated units | Show a personal threat, not a lore lecture |
| First stop | Explicit scripted tutorial stops at 07; six units leave the jar and reach Ama | Transfer conserves luck; Collector retains their number; NaN remains over NIL |
| Naming | Ten digit buttons, one optional meaning line on focus, clear confirm | Set resonance once; no claim of equal win rates or hidden starting stat bonus |
| Detection | Basilica terminals display REMAINDER DETECTED | The machine recognizes a missing account; it has not explained NIL's origin |

The **44-second Many Ledgers montage** is full-campaign, optional after the rooftop or in the Codex, never a mandatory film before first input: Noise 8 s → five local ledger images 20 s → binding machine 12 s → title 4 s. Thale narrates the institution's public origin myth; later evidence corrects its omissions. It is not required jam footage, and historical Higgsfield prompts are references, not an approved build dependency. Use in-engine or still-motion presentation; video has subtitles, skip and a still fallback. Future longer trailer edits need a separate shot budget.

---

## 9. Endings
| Ending | Condition | What happens |
|---|---|---|
| **Balance** | Deliberately select the always-available return ending | NIL dissolves into the Ledger. The Remainder becomes an identified reserve and funds a one-unit Civic Omen increase per registered soul below 99, capped at 99; any unallocated reserve stays recorded. The present Deficit closes, but Hap remains caged and the institution still needs reform. The party visits a grave with no number. |
| **Overflow** | Break the Basilica | Hap bursts free all at once. Every Omen becomes NaN; the Noise returns and nobody can see anyone's luck: freedom and chaos. Each land returns to its old ways, for better and worse. NIL fades into the storm. |
| **Positive-Sum** (true ending) | Eight core narrative bonds at stage 4 and all eight proof pieces; see STORY §9 for recoverable prerequisites | The party puts its distinct ledger proofs into the engine together. Shunya's translation equation, seeded by differing local records and cooperation, allows possibilities to be shared instead of forced into one finite unit. The fist opens into an **Open Hand**. Thale lives. NIL keeps their personhood, receives a stable resonance equal to the player's choice and a positive Civic Omen: 10 for resonance 0, otherwise the two-digit chosen value 01–09. Zero is never depicted as healthy Civic 00. |
| **Divide by Zero** (secret) | Resonance 0 and the player explicitly arranges the final optional ritual as 0-0-0, then confirms this earned ending | The Basilica crashes, the screen shows a styled error card (with accessible plain-text alternative), and credits roll in debug text with Hap's laugh. It does not randomly replace the selected main ending. |

STORY §9 owns ending predicates and pre-finale catch-up. The ending wheel is a deliberate selection with confirmation and cancel; it is not a timing gamble. Secret recruits, roster availability in the active combat party and post-ending epilogues never supply mandatory flags. Skip/watch commit identical outcomes once.

**The theme in one sentence:** *a world that flattened every culture's idea of luck into one zero-sum number learns, from a party drawn from all of them, that luck shared isn't zero-sum.*

---

## 10. Cultural care
- Each land is **inspired by** a real culture and is not a depiction of a real country. Names are invented or drawn from widely told public folklore.
- **Revered figures are never enemy targets.** Enma, Chitragupta, Judge Cui, the wardens and the Moirai pose dignified, nonlethal trials. Rahu/Ketu remain revered celestial figures. The Act III bosses are explicitly invented Basilica eclipse constructs with operator stamps and machine silhouettes; no sacred head/body imagery is used for those targets.
- **Avoid Indigenous sacred traditions** in the American act (no dreamcatchers, skinwalkers or sacred ceremonies). The Crossroads draws on frontier tall tales, the blues crossroads legend, immigrant superstitions, ghost towns and Sleepy Hollow.
- AI source research must record names/scripts, clothing, context, disagreements and uncertainties against primary regional sources. No native expertise, consultation or community approval is implied. Any external review is recorded only if it actually occurs; no human finishing stage is a production dependency under the AI-only workflow. Unverified sensitive imagery is removed or fictionalized. Localisation beyond jam English is a later production gate, not a completed deliverable.
- The casino is aesthetic only: no real-money mechanics or purchasable randomness.
