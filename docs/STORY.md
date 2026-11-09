# ZERO-SUM: OMEN — The Story, Start to End

> **8 November editorial revision:** [Resolved series bible](novel/RESOLVED_SERIES_BIBLE.md) supersedes conflicting older naming, origin wording, character backstories, political outcomes and story-length targets below. Gameplay formulas retain their existing domain authority. This source is being adapted to the49-chapter edition; its historical schedules and game scene numbering are not manga chapter numbering.

The full campaign outline: Prologue, five acts, six dream epilogues, finale and four endings. World rules are in [`WORLD_BIBLE.md`](WORLD_BIBLE.md), people in [`CHARACTER_BIBLE.md`](CHARACTER_BIBLE.md), encounters in [`ACT_DESIGN.md`](ACT_DESIGN.md), and bond scheduling in [`BOND_ARCS.md`](BOND_ARCS.md). Updated 7 November 2026 under [DECISIONS.md](DECISIONS.md). These are **specified scenes and state contracts**, not finished dialogue assets or an implemented campaign.

**Scope and budget.** The campaign critical path is 35/45/50/50/45/50/40 minutes = **315 minutes**, plus 45–105 minutes optional bonds/quests/navigation: a **6–7-hour hypothesis**, unmeasured. Required bond stages may be integrated into these critical-path scenes; optional versions provide extra depth. The jam is a separate 10–15-minute Prologue adaptation defined only by JAM_SLICE/JAM_SCRIPT/FIRST_10_MINUTES, with NIL and Vesper, three encounters and rooftop/results; it does not include the extra campaign route, dream, ultimate system or later lands.

---

## 0. The shape of it

**Logline.** A nameless wanderer with no number, who turns out to be the last free piece of the caged god of luck, crosses five lands to stop a kind man from freezing fate forever.

**Theme.** *Luck shared isn't zero-sum.* Every act shows a land whose idea of luck the Basilica flattened, a person who suffers for it, and a companion who learns, with NIL, that people are worth more together than apart. The game's synergy system is the theme made playable.

**NIL's question per act** (the spine of the story):

| Act | Land | NIL asks | NIL learns | Companion who answers |
|---|---|---|---|---|
| Prologue | Meridian | "Why don't I have a number?" | That a number decides everything here | Vesper |
| I | Hyakki | "What makes something real?" | Being believed in; being chosen | Hina |
| II | River Empire | "Who owns luck?" | Luck is debt to some and gift to others | Ba Jinling, Bai Si |
| III | Śūnyapura | "What am I?" | NIL is the Remainder: what everyone lost | Shunya |
| IV | Kroton Nova | "Are some numbers worth less?" | No. "Indivisible" means people | Prima |
| V | Crossroads | "Can you outrun the dawn?" | No; you have to let tomorrow come | Fibi, Vesper |
| Finale | The Basilica | "What do I give back?" | The player decides | Everyone, and Hap |

**Three movements.**
1. **Hunted (Prologue–Act II):** NIL runs, learns the world's rules and gathers friends. Stakes: survival.
2. **Remainder (Act III–IV):** NIL learns what they are; the hunt becomes a choice. Stakes: identity.
3. **Zero-Sum (Act V–Finale):** NIL chooses to walk into the Basilica. Stakes: the god of luck and everyone's tomorrow.

**Thale's thread.** Short scenes show care and its withheld cost: feeding pigeons, authorizing relief but withholding release, visiting his family's street. He inherited the centuries-old system and discovered Hap in TR 999. His new idea is Fixed Fate. His competence reduces accidents on selected routes by debiting reserves and poorer districts; Act II evidence exposes that transfer. Compassion does not erase responsibility.

---

## 1. Prologue: "NaN" (Meridian Undercity) · ~35 min

**Setup.** TR 1002. Dawn in the Remainder Wards. The Dawn Tally beam sweeps the slums; every Omen ticks.

1. **Interactive cold open.** No myth film precedes input. The optional 44-second origin montage (WORLD_BIBLE §8) is offered after the rooftop or in the Codex, never concatenated ahead of the rescue.
2. **Rain Alley 9.** Ama's **Civic Omen** drops to 01. Her son Tobi stares. A confiscation jar holds six units. NIL, NaN visible, stops the rescue wheel at 07: the jar visibly loses six and Ama gains six. A Collector: “That one has no number.” NIL to the family: “Go. Both of you.” The Collector keeps their own Omen. Set `ama_rescued` once.
3. **Chase** through the Wards: charms of every culture over every door. NIL ducks into a black-market shrine.
4. **Brother Nought's Naming shrine.** "Every soul needs a number, child." **The player states their lucky number** (0–9; each digit shows what it means across the Tally). The terminal overloads; across the city every screen reads **REMAINDER DETECTED**; the Basilica's eye opens. Brother Nought, quietly: "Hap's watching." (First mention of Hap. Players won't know it yet.)
5. **First Audit** vs Debt Hounds, alone. Tutorial: stop the wheel, the reel, Pair, Jackpot (scripted), Parry.
6. **Vesper Sette** drops from a fire escape: “Need a hand? Seven fen.” She joins before the second Audit; both heroes act, one twice. Choosing order and reading Pattern Sight supplies the next decision.
7. **The Charm Bazaar.** Gus offers a first charm without a currency/debt subsystem. The campaign later offers his optional account quest. **Campaign-only route:** defend Maeve's forge and recruit her early. If missed, her caravan catches the party at Hyakki's Teahouse, and the pre-finale camp guarantees recruitment/catch-up (CHARACTER_BIBLE §16). Missing a route never destroys her proof piece.
8. **Livia's window.** NIL glimpses a sick girl with Omen 06 in an upstairs window guarded by Collectors. (Payoff in Act V.)
9. **The drain gates.** **Varro Kade, the Ledgerhound**, corners them. His Civic 61 is distinct from normalized Audit Omen. The Debt Jar is visibly explained (BESTIARY/SYSTEMS). A full-campaign ultimate tutorial may introduce Vesper's Requiem after the basic rules are understood; the jam uses only an optional scripted defeat flourish with no charge mechanic.
10. **Varro spared.** He growls that he needs the bounty for his sister and limps away.
11. **The world-map reveal.** Varro's defeated Audit releases Seal 1 without killing him. Vesper explains six acquired Seals plus NIL's resonance open the ritual gate. The map shows Meridian and the five outer lands; it is a future journey, not six unlocked playable regions in the jam. A confiscation receipt directs the party toward the Hyakki toll ledger.
12. **Thale scene.** In the Basilica nave, the Comptroller reads the alert, closes his eyes and says, almost tenderly: "There you are."

**Campaign Hap's Dream 0: “The Pick.”** NIL dreams of a vast figure with dice eyes and a street fortune-teller's face. “Pick a number. Any number. …Oh, that one. Interesting.” It laughs; NIL wakes. This repeats the chosen resonance, never resets it, and is not required jam content.

---

## 2. Act I: "The Night Parade" (Hyakki) · ~45 min

**What's wrong here.** Yokai fade when people stop believing in them. Tamamo, the Nine-Tailed Auditor, made a pact with Thale: deliver the Remainder and Fixed Fate will freeze every yokai into permanence. A Ledgerist toll gate now taxes the shrine road.

1. **Arrival by ferry** with Tetsu the ferryman, under a Hokusai-style wave. Tetsu was a Collector once; he won't say why he left.
2. **The Moon Pier.** Lantern ghosts attack; the torii's three lanterns become the reel (land reel object).
3. **The Night Parade** crosses the red bridge; the party hides inside it, disguised as yokai. If Maeve joined early her disguise is just a hat; otherwise Vesper improvises a paper mask. Stage variants use roster flags.
4. **Hina** jumps out of a shrine's umbrella stand and attaches herself to NIL: "You smell like a hundred wishes." She is 99, one year short of becoming a "real" spirit. **Hina joins.** Party of 3 unlocks; bonds and Link Arts (*Midnight Parade* with Vesper).
5. **Ofuku's shrine of the Seven Lucky Gods.** Charms and charm sets. Ofuku paints one daruma eye a day "for whoever needs it".
6. **The kappa river.** Side quest: **Kyūsuke** the tired kappa (secret recruit, digit 5).
7. **Shi and Ku** is demonstrated safely: a 4 curses the striker's next strike, a 9 curses the next party defence; Hina's active-party protection makes 9 s safe (SYSTEMS owns exact effects). A non-Hina counter remains available; no forced active composition.
8. **Enma's gate** (keeper trial). Enma judges whether the living may pass the shrine of the dead: a trial fight with no hatred. Afterwards Enma opens his ledger: NIL's page is **missing**. "You are not written here. You are not written anywhere." NIL learns **Carry** (strikes over 50 carry +1 to the next hero's digit; Hina taught NIL to count past a hundred).
9. **The Kitsune twins Ao and Aka** guard the foxfire palace (elite).
10. **Tamamo** in her foxfire palace. Boss: nine tails, illusion faces, 9 s curse you unless Hina is in the party.
11. **Tamamo's question.** Defeated, she asks NIL: “What is a yokai worth without belief?” NIL: “What's anyone worth without a number?” Hina says she is already real, still 99. Tamamo blesses her and withdraws; no death effect. **Seal 9.** Hina keeps Enma's torn page. Releasing the toll ledger shifts an obligation to the Luck Exchange: Jinling now has a reason to seek the party.
12. **Thale scene.** He visits Hyakki's ledgers in the Basilica archive and leaves a cucumber on Enma's shelf. (A clerk asks why. "Superstition," he says, and smiles.)

**Hap's Dream I: "Real."** Hap wears the face of an old paper lantern. "She thinks she isn't real yet. Do *you* think you're real?" NIL doesn't answer.

---

## 3. Act II: "Eight Bells and the Book of the Dead" (River Empire) · ~50 min

**What's wrong here.** Chancellor Jin Chan's Luck Exchange trades Omens like shares; luck compounds for the rich and debt compounds for everyone else. Below the river, the Ten Courts' count of the dead has always been short.

1. **Bāfā Harbor at the Lantern Festival.** Live Omen price boards; dragon boats; Little Lantern (Xiao Deng), an orphan messenger, steals NIL's charm and returns it with a note: "Someone wants to buy you."
2. **Ba Jinling's pawnshop.** Jinling buys the party's bounty and hides them: "Everyone's in debt, darling. I just keep better books." **Jinling joins** as a guest.
3. **Granny Liu Shun's mahjong table.** Optional recruit 6: learn one tile rule or help retrieve her purse. Neither route requires defeating her at mahjong; she never loses a played hand on screen.
4. **Markets and wheel crafting** unlock at the Exchange's back alleys; **oracle sticks** at the temple.
5. **The river's end.** The party rides a Debt Junk off the edge of the world into the **Ten Courts** (ink-wash art). Crossing Naihe Bridge; Meng Po's pavilion of forgetting (the party refuses the soup).
6. **Ox-Head and Horse-Face's trial**: the wardens must both be bested in the same round. Afterwards they bow.
7. **Bai Si**, the executioner who counts the dead, blocks the Hall of the Book. NIL's decoder shows him three hundred years of rounding: his count was always short. He kneels, and follows the party to the Hall.
8. **Judge Cui's trial.** The Judge tests whether NIL may hold the Brush that writes in the Book of Life and Death. NIL learns **Rewrite** (free Ink each fight). Satisfied that the count can be corrected, **Bai Si joins**.
9. **Return to the harbor.** The Exchange blocks Civic Omen transfers to force the party out. Jinling copies her father's true book into a protected archive, then burns enforcement copies in public; the ending proof is never burned. The archive exposes the same fractional mismatch in living and dead accounts and who pays for Thale's protected routes. That evidence directs the party to Śūnyapura.
10. **Chancellor Jin Chan** in his coin palace. Boss: interest, the Jackpot tax, swallowing a hero.
11. **Father and daughter.** Bankrupt, Jin Chan laughs until he cries: "You were always better at books than I was." Jinling takes over the Exchange and forgives every debt under 8 fen. **Jinling joins** fully. **Seal 8.**
12. **Thale scene.** He authorizes Livia's exemption but withholds its release, filing it “pending.” Jinling obtains the dated authorization and an unpaid-release order. Varro was promised a completed exemption, not merely a signature. Ivo's initials on an archive correction seed his eventual defection.

**Interlude: the Open Hand.** Brother Nought finds the party in Bāfā's temple of oracle sticks. He shows them an open stone hand with a die in its palm and tells them about **Hap**, the god of luck that Meridian outlawed. "Every land had a way to talk to Hap. The Basilica took all of them." He doesn't know where Hap went. NIL feels the die in the stone hand is warm.

**Hap's Dream II: "Owed."** Hap wears the face of a smiling money toad. "Everyone owes me something. You're the only one I owe." It won't explain.

---

## 4. Act III: "Śūnya" (Śūnyapura) · ~50 min · the midpoint

**What's wrong here.** Basilica surveyors are suppressing the observatory's measurements. Two invented, visibly mechanical eclipse engines nicknamed “Rahu” and “Ketu” occlude the plateau. They are not the revered celestial figures, their bodies or avatars. Brass operator stamps and a surveyor control ledger establish who built and commands them.

1. **Monsoon arrival.** Rain on stone; a city built around giant sundials and astrolabes.
2. **Baital the Vetāla** riddles the party from a banyan tree (riddle encounters; the answer is always a digit).
3. **Shunya** at the observatory with Acharya Vidya Rao. She sees the party's mismatched records: “The books are short by one soul. Exactly one. Hello.” It is a hypothesis about an unlisted living account, not a claim that NIL's worth equals a health number. **Shunya joins.** Karma and gems unlock. She asks NIL's consent before testing the decoder.
4. **The Stepwell of a Thousand Steps** with Meera the diver (dungeon; she seeks her drowned brother's karma record).
5. **Chitragupta's Hall** (keeper trial): palm-leaf records to the horizon. Chitragupta reads NIL's page aloud. It is blank. Then the ink appears, written in every soul's handwriting at once: one tiny fraction from every life in the Tally.
6. **The reveal.** Shunya joins the missing record, fractional signatures and NIL's memories: three centuries of remainders became one person. **NIL is the Remainder.** NIL learns **Place Value**. “Then whose luck am I?” “Everyone's. But you are yours.” She shows that the regional records encode different possibilities, not identical coins; this seeds the final translation equation. A silent observatory rest lets NIL respond before the next fight.
7. **The eclipse engines.** The occluder disc and articulated rail synchronize their suppressors. Balance their machine stakes using the telegraphed linked-body rule (BESTIARY). Ordinary attacks destroy only machinery; the celestial figures remain beyond the combat frame.
8. **Open sky.** Both engines shut down. The natural eclipse passes; Vidya Rao writes “NIL. Remainder. Brightness: varies.” **Seal 0.** NIL accepts a protected copy of the equation, not public ownership of their identity.
9. **Thale scene.** Thale learns the Remainder now knows. He orders the Sieve of Kroton Nova "accelerated", then goes home and cooks dinner for one.

**Hap's Dream III: “Change.”** Hap wears the face of a monsoon cloud full of stars. “You're the change I never got back.” NIL now asks directly whether Hap is real: “Are you real?” Hap: “Ask me in the Basilica.” Earlier questions in other dreams remain canon.

---

## 5. Act IV: "Indivisible" (Kroton Nova) · ~45 min

**What's wrong here.** Kroton Nova is a white island city built as a giant sieve; the Pythagorean Synod has decided that citizens whose Omens are composite are impure, and the Sieve drops them into the undercity. Archon Seventeen calls it purification; Thale calls it "acceleration".

1. **Noon arrival** on the Sieve terraces; goats; evil-eye beads; Niko the goat-herd falls through a hole (running gag).
2. **Prima of Kroton**, the Synod's "even prime" novice, escorts the party as prisoners. **Awakenings** are explained at the Agora of Primes.
3. **The undercity of the fallen.** Mother Kallisto leads the "composite" people in shanties built from Basilica scrap.
4. **Prima defects** when the Sieve drops a school; she holds the children on her shield over the drop. **Prima joins.** "If the Sieve drops children, the Sieve is wrong."
5. **The Moirai's cave** (three keeper trials: Clotho spins a wheel you must stop in sequence; Lachesis measures the party's bonds; Atropos asks what NIL would cut). Lachesis gives Prima a strand of thread. NIL learns **Factor**.
6. **The Archon's temple.** **Archon Seventeen** boss: he strikes digits off your wheels like the Sieve of Eratosthenes; composite strikes are halved.
7. **The fall.** The damaged Sieve mechanism gives way beneath the Archon; Prima catches him. His Civic 17 has not changed because his Audit stake fell. The Sieve stops; Kallisto's people climb the terraces. **Seal 2.** A first-generation gear and financing contract connect Maeve's horseshoe and the Crossroads. Vesper discloses her history before the party follows that lead.
8. **Thale scene.** Thale stands in his family's empty street on the anniversary of the storm. It's raining. He doesn't open his umbrella.

**Hap's Dream IV: "Worth."** Hap wears the face of a cracked marble statue with a living smile. "Which of your friends is worth the least?" NIL: "Wrong question." Hap laughs so hard the stars shake.

---

## 6. Act V: "1,597 Nights" (the Crossroads Territory) · ~50 min

**What's wrong here.** The House financed decades of Basilica maintenance; the institution itself predates him. In TR999 he commissioned protection for Fibi; its fatal-loop trigger activates on story Day28 inTR1002, when she is18. The party arrives on iteration 1,597 after 1,596 completed repeats. Outside time advances one night; local memories reset except Fibi's and, after entry, the party's, anchored by NIL's unregistered account. Only authorized loop objects persist; ordinary rewards cannot be farmed by resetting scenes.

1. **The midnight crossroads.** One streetlamp; the Stranger (keeper) with the black book offers NIL a deal. NIL learns **Deal** (once per fight, take a Crossroads Deal). The Stranger never cheats.
2. **Lucky Strike.** Casino neon; Route 7 motels; the same drunk falls off the same stool every night. **Loops** begin: every few scenes the night resets; the party keeps what it learned.
3. **Fibi Leone** predicts the bartender's speech and the third step that breaks every iteration. NIL says something new; she cannot finish it. **Fibi joins** during her 1,597th night. Her four bond stages are integrated into the investigation, contract discovery and dawn (BOND_ARCS).
4. **Penny** on the railway: the ghost girl with 1,596 lucky pennies (Ghost Train quest).
5. **Varro returns.** The authorization was signed but never released. The party presents the Act II order and arranges Livia's transfer to Brother Nought through Gus's courier route. A new letter introduces this option even if the prologue window was missed. Completing `livia_saved` adds Varro as a guest for the remaining act; full recruitment is post-ending/NG+. Declining never blocks a main ending.
6. **Sheriff Dolores Vance** helps solve the loop: the night resets whenever Fibi's heart stops at dawn.
7. **Vesper's honest hand.** Vesper confronts the rigged hand that civically Settled a child years ago. She deals Fibi a game with open rules and accepts a fair loss. The recovered contract proves its “maintenance” clause drains Fibi at dawn; protection itself became the threat. Fibi consents to cancelling it; the House must relinquish control.
8. **The House.** Boss: rewinds time every 3 rounds; copies your last pattern; offers a mid-fight deal.
9. **Dawn.** After the fight the House and Fibi cancel the fatal clause using its recovered terms. Fibi lives because that drain ends, not because a winning attack creates luck. He says goodbye, leaves Lucky Strike alive and relinquishes the casino. Fibi's first sunrise completes her fourth stage and supplies the Black Book's last page. **Seal 7.**
10. **Thale scene.** Six acquired Seal alarms are lit. Thale recalls the exterior guards: “Let them come home.” He does not bypass the ritual Seal lock or the interior service trap.

**Hap's Dream V: "Tomorrow."** Hap wears the face of a jackpot slot machine, laughing. "Tomorrow is the only bet I always take." It shows NIL the Basilica's eye from the inside, and the eye is Hap's.

---

## 7. Finale: "Zero-Sum" (Meridian & the Basilica) · ~40 min

1. **The Upper Gate.** Six Seal Digits glow (1, 9, 8, 0, 2, 7). The seventh socket waits. **The player's lucky number**, chosen in minute one, is the last key. (If the player chose a digit already used, the socket asks for it a second time, and the gate shows both.)
2. **Clerk Ivo Marr**, whose corrected archive notes the party saw in Act II, opens an interior service passage around a trap after the ritual gate opens. “Somebody should file a complaint.”
3. **The nave.** Every land's original ledger hangs on the walls: thread, palm leaves, the Book and the Brush, Enma's ledger, the black book. Ledger-priests chant the catechism.
4. **The Even Hand engine.** The party sees the truth: the Basilica's heart is a closed brass fist around a god. **Hap is in the cage**, starved and counting itself.
5. **Thale.** “Thread, karma, contracts: every account left someone behind. I inherited the arithmetic. I will end the loss.” He argues from real protected-route evidence; the party confronts the hidden debit and Hap's starving cage. Fixed Fate ends chance, not just the storms. He asks NIL to come home to the Ledger.
6. **Phase 1, Regression to the Mean:** every wheel compresses toward 5.
7. **Phase 2, Fixed Fate:** the wheels stop spinning; a puzzle fight where you arrange digits instead of stopping them.
8. **Phase 3, Zero:** NIL begins alone. Recruited core companions return as scripted recalls at phase milestones, active or reserve; no absent wheel digit gates a required callback. Optional guests receive optional variants. The final guided ritual uses legal explicit choices; choosing 0 permits the optional 0-0-0 secret configuration. It is not dependent on random damage or an inaccessible starter face.
9. **Thale falls to one knee,** Omen still frozen at 50. "Then tell me what you'd do with it."
10. **The Open Hand (no fight).** Hap's wheel displays available ending faces with readable consequences and missing prerequisites. The player chooses a face, can cancel, then confirms the final tap; no timing skill assigns an unwanted ending. A pre-commitment save allows return to the camp catch-up. Eligibility is defined in §9.

### Endings
| Ending | Condition | What happens | Final image |
|---|---|---|---|
| **Balance** | Finale complete; chosen and confirmed | NIL's Remainder account becomes a recorded reserve funding one Civic Omen unit per eligible registered soul, capped at 99; excess stays in reserve. The present Deficit closes; Hap remains caged | The party at a grave with no number; Tobi leaves a folded paper die |
| **Overflow** | Always available | NIL breaks the Basilica. Hap bursts free all at once; every Omen becomes NaN; the Noise returns; each land goes back to its old ways, for better and worse. NIL fades into the storm | A Noise storm over Meridian, and in it, a NaN that winks |
| **Positive-Sum** (true) | Eight core narrative stage-4 flags and eight protected proof pieces; chosen and confirmed | The already-seeded equation lets distinct ledgers share possibilities. The fist opens into an **Open Hand**; Hap deals freely through multiple ledgers, and Thale lives to see it | NIL receives chosen stable resonance and positive Civic Omen (10 if resonance 0, otherwise 01–09). Tobi performs a new Rite as a renewing participant, not a child belatedly reaching seven |
| **Divide by Zero** (secret) | Resonance 0; deliberate final ritual 0-0-0; chosen and confirmed | The Basilica crashes; accessible styled error card and debug credits; Hap laughs. It never overrides another selected ending | `REMAINDER: 0. HAP: FREE.` |

### Epilogue cards (true ending)
Vesper deals honest games · Maeve's charms work again · **one year later**, Hina turns 100 and throws a festival (she remained 99 throughout the campaign and all Awakening choices) · Jinling's Exchange lends at 0% · Bai Si's count is finally right · Shunya publishes the work NIL already consented to co-author · Prima teaches · Fibi sees a second sunrise · if Livia was saved, Varro and Livia open their shelter · Thale tends pigeons. Post-ending images are payoffs, never prerequisite flags.

---

## 8. After the story

- **New Game+ "The Second Hand":** carry charms and bonds; Thale is your companion for one act (a what-if).
- **The Endless Ledger** (roguelike post-game): every land shuffled, Omen Levels 1–8, the Daily Omen seed. Its final boss is **the Default** (the world without luck, a creature of pure stillness), the only boss that is "nothing" rather than someone.
- **Hap's Gallery:** every face Hap wore, unlocked by dreams, side quests and coincidences.

These post-game modes are future scope, not jam promises. Thale's NG+ guest appearance is a what-if variant, not a thirteenth persistent roster member or a reversal of an ending's canon.

## 9. Scene, recruit and ending state contract

Use stable IDs below in future content imports. This is the interface specification; `story/` tables, localization rows, full scripts and runtime validators remain production work. Each scene entry has prerequisites, participants/availability, choice, outcome flags, reward IDs, checkpoint and fallback; no guessed runtime field is evidence of implementation.

| Required campaign milestone | Prerequisite | Idempotent outcome and dependency |
|---|---|---|
| `p_rescue` | New game | `ama_rescued`; debit jar 6, credit Ama 6 in the same event |
| `p_naming` | `ama_rescued` | `resonance_chosen`, chosen digit 0–9, `remainder_detected`; confirm once |
| `p_vesper` | Solo tutorial complete | `recruit.vesper = recruited`; two-hero tutorial becomes available |
| `p_varro_mercy` | Varro Audit won | `varro_spared`, `seal.1`; mercy is the authored main-path act, not an unimplemented kill branch |
| `a1_hina` / `a1_enma` / `a1_tamamo` | Seal 1 and ferry arrival | Hina recruited; Carry unlocked by Enma; then `seal.9` and `piece.enma_page`; missed Maeve route offered at Teahouse |
| `a2_guest` / `a2_judge` / `a2_exchange` | Seal 9, transferred toll obligation | Jinling guest; Bai Si recruited and Rewrite unlocked; then Jinling permanent, `seal.8`, protected `piece.true_accounts` and `piece.dead_count` |
| `a3_remainder` / `a3_engines` | Seal 8 and records | Shunya recruited; consent before examination; `remainder_known`, Place Value, `piece.remainder_equation`; then engines disabled and `seal.0` |
| `a4_prima` / `a4_moirai` / `a4_archon` | Seal 0 and Thale's acceleration | Prima recruited, Factor/Awakenings unlocked; rescue resolution supplies `piece.lachesis_thread`, `seal.2`, first gear accessible to Maeve |
| `a5_fibi` / `a5_contract` / `a5_dawn` | Seal 2 and financing evidence | Fibi recruited; fatal clause proved and consensually cancelled; `seal.7`, `piece.black_book_page`, Fibi stage 4; Vesper receives `piece.marked_deck` |
| `f_camp` | All six acquired Seals | Guaranteed Maeve recruitment if missed; core stage catch-up, `piece.first_gear_horseshoe`; review ending checklist, then create pre-commitment save |
| `f_gate` / `f_service` | Six Seals + chosen resonance | Ritual gate accepts repeated digit in separate socket; Ivo opens only the interior service route |
| `f_finale` | Gate/camp and completed boss phases | `finale_complete`; recalls selected from roster, optional `finale_zero_triple`; no battle RNG chooses the ending |

Core companion IDs: `vesper`, `maeve`, `hina`, `jinling`, `bai_si`, `shunya`, `prima`, `fibi`. Each has `bond.<id>.stage` 0–4. The eight proof-piece IDs are those listed above; story-important pieces are protected journal records, cannot be sold, consumed by crafting or lost in an act retry. If a physical original changes hands, the protected proof remains. All core characters are permanently available after recruitment except explicitly staged guest transitions; reserve participation counts.

**Catch-up:** at `f_camp`, every missing core recruit/stage/piece appears as a named journal objective and conversation. A missed past event uses an archive/letter recap plus a present-day decision with that character, not time travel or duplicate rewards. A declined conversation stays available. Completing a piece/stage uses its stable event ID once, then reconciles journal evidence after rollback. Skip applies the same final state as watch. A scene interrupted before its atomic completion commits no partial reward; replay either resumes or safely repeats presentation.

**Ending predicates (evaluated after `finale_complete`):**

- `ending.balance.available = true`; `ending.overflow.available = true`.
- `ending.positive_sum.available = all eight core stage values == 4 AND all eight piece flags`.
- `ending.divide_zero.available = chosen_resonance == 0 AND finale_zero_triple`.
- The optional final ritual has a visible “Set 0–0–0: unlock Divide by Zero” action only for chosen zero, with cancel/undo. It is an authored puzzle exception with explicit faces, not a normal wheel or a random last-hit requirement. It does not alter availability of Balance, Overflow or an already earned Positive-Sum.
- Ending confirmation stores one `ending_selected` value. The wheel describes consequences; the player may return to `f_camp` before confirming. No secret recruit, purchasable item, post-ending image or timing-perfect input is required. Claiming a locked ending opens its journal checklist rather than discarding the save.

**Reveal ledger:** prologue confiscation and alien memory → Enma's missing page → Ten Courts' fractional mismatch → midpoint Remainder proof → differing ledgers' compatible possibilities → financing contract/cage clue → exposed Hap → collective translation. Main-path scenes contain each essential clue; optional lore adds perspective. The midpoint changes NIL's verb and their consent relationship with Shunya. The ending changes an institution because the party assembled evidence, not because an ordinary pre-finale attack created luck.

**Verification gate:** traverse watch/skip, ten resonances, missed Maeve, declined-and-returned bonds, Fibi's four pre-finale stages, optional Varro absent/present, duplicate scene callbacks, save/reload and each ending. Check both eligibility and final images, especially resonance 0 versus Civic 00. These tests and player comprehension studies are specified work, not recorded passes.
