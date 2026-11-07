# ZERO-SUM: OMEN — Lore Lexicon, Timeline and World Rules

Use this file to keep every word, date and rule consistent across writing, art, UI and marketing.

Updated 7 November 2026 under [DECISIONS.md](DECISIONS.md). Specified canon, not an implemented Codex. Distinguish objective truth, public doctrine and character belief; a voiced belief is not automatically a world rule. Jam scope is the Meridian Prologue only.

---

## 1. Glossary

| Term | Meaning | Usage notes |
|---|---|---|
| **Hap** | The Tally's one god of luck: the will inside chance. Caged in the Basilica since TR 702 | "Hap" (never "the Hap"). It/its, or whatever the speaker's culture prefers. Invented for this world |
| **The Open Hand** | Hap's symbol (an open palm holding a die); also the outlawed faith that still leaves offerings to Hap | Shrines are called "Open Hands" |
| **The Even Hand engine** | The Basilica's heart, which closed around Hap and divides it into Omens every dawn | Only Thale and the Ledger-priests know the name |
| **Hap's Favour / Hap's Whisper** | Gameplay: luck turning after bad luck; coincidence events on the map | In dialogue: "Hap's watching" |
| **The Tally** | The known world: Meridian plus the ring of lands around it | "Across the Tally"; never "the world map" in dialogue |
| **Civic Omen** | Registered personal luck/status 00–99 outside an Audit; floats over a soul; NIL instead shows NaN | Always two digits: Civic 07. A civic value is not normalized combat health. |
| **Audit Omen** | Separately framed 99–00 normalized readout of a staked Balance | Positive Balance: ceil(99×Balance/MaxBalance), clamp 01–99; zero→00. Combat rules read this unless explicitly marked civic. |
| **Omen** | Contextual shorthand after Civic/Audit distinction is taught | Never silently switch meaning in a rule; label both in authoring data and UI. |
| **Balance** | Integer luck staked in an Audit; damage exhausts the stake | MaxBalance>0, 0≤Balance≤MaxBalance; party shares a stake, displayed beside NIL's NaN, not instead of it. |
| **NaN** | NIL's non-number glitch | Written exactly "NaN"; characters pronounce it "nan" |
| **The Basilica** | The brass clockwork cathedral-engine in Meridian that computes every Omen | "The Basilica" (capitalised). Never "the machine" in formal speech. |
| **The Ledger** | The merged record of every Omen held by the Basilica | Distinct from the older, local ledgers (Enma's ledger, the Book of Life and Death, Chitragupta's records, the Moirai's thread, the Black Book) |
| **Dawn Tally** | The daily recomputation of every Omen at sunrise; a beam sweeps the city | Clocks in Meridian strike 0 at dawn |
| **The Rounding** | The dropping of every soul's fractional luck at each Dawn Tally | Secret until Act II/III |
| **The Remainder** | The accumulated rounded-off luck, embodied as NIL | Basilica alerts: "REMAINDER DETECTED" |
| **The Deficit** | Decline in circulating luck as rounded fractions accumulate in an unlisted account and Hap starves | Total remains conserved across accounts/reserves before Positive-Sum. First measuredTR 962. |
| **The Default** | Objective: extinguished chance/Hap's death, absolute stillness | Public doctrine incorrectly predicts Basilica collapse/return ofNoise; mark that claim as doctrine, not a second objective definition. |
| **Noise / Noise storm** | Patches of pure chance where numbers scramble; where Noiselings come from | Visual: static, scrambled digits, glitch colour |
| **Noiseling** | Small glitch creature made of scrambled digits | Common enemy |
| **Civic settlement** | Civic 00 leaves a person exposed to lethal misfortune within days; a separate story event | May be reversed by a legitimate transfer before death. Funerals called “settlings” do not make every combat a funeral. |
| **Audit settlement** | Balance 0 exhausts the stake and ends combat | Does not automatically change Civic Omen or kill/disintegrate a person; named bosses survive where the scene requires. |
| **Audit** | A duel of fates; combat | "Audit him" = fight him |
| **Auditor** | Someone who can summon and stop a Fate Wheel; also the title of the six Seal-holders | Capitalise as a title ("the Auditor of Hyakki") |
| **Fate Wheel** | The spinning strip of digits summoned in an Audit (descended from Fortune's wheel, *Rota Fortunae*) | Players say "wheel" |
| **The reel** | The three slots where stopped digits land; styled per land | Never "slot machine" in dialogue |
| **Naming Rite** | The ceremony at age seven where a child states their lucky number to the Basilica | In the intro, NIL performs it at a black-market terminal |
| **Lucky number / resonance digit** | Digit 0–9 used for personal channeling and mathematical bonds; NIL chooses it, Fibi's changes by combat round | Distinct from both Omen readouts and Balance. Resonance 0 is not Civic 00. |
| **Seal / Seal Digit** | The lock binding each land's ledger into the Basilica; the gate needs 7 digits | Seven digits: 1, 9, 8, 0, 2, 7 + the player's number |
| **Final Audit** | Thale's plan: settle the Remainder, then Fixed Fate | — |
| **Fixed Fate** | Freezing every Omen forever | Thale calls it "mercy" |
| **Keepers** | Revered guardians of the old ledgers (Enma, Judge Cui, Chitragupta, the Moirai) | Never "bosses" in text |
| **Luck-in** | A single point of Omen sold for food or favours | Slum slang |
| **Fen** | Small coins used across the Tally | "Eight fen for a bowl of noodles" |
| **Overwrite** | Landing your own lucky digit three times | Gameplay and in-world slang for a miracle |
| **Confiscation reserve / luck jar** | An identified account holding luck transferred from citizens | Opening debits six units from the jar and credits Ama 01→07 atomically; not newly created luck. |
| **Eclipse Engines “Rahu” and “Ketu”** | Invented Basilica occluder disc and surveyor rail, named by operators after celestial references | Brass machines with visible stamps/cables; not the revered figures, bodies, avatars or divine enemies. |
| **Narrative bond stage** | Authored relationship state 0–4 per companion | Distinct from mathematical Complement/Twin/Neighbour and from an Awakening branch. |

## 2. Idioms and slang
- "Hap deals, people choose": the oldest proverb; said before any big decision.
- "Hap's watching": said at a coincidence; also a gambler's excuse to keep playing.
- "Rounded down": cheated, or killed.
- "In the black": safe, lucky. "In the red": in debt, unlucky.
- "Lucky as a ninety-nine": very lucky (Meridian); in Hyakki it's an insult, since 9 means suffering.
- "Don't count your fen at the table."
- "May your Omen never round": goodbye or blessing.
- "Settle down!" is a grim joke in Meridian.
- Swearing: "Default take you", "Noise and ruin".

## 3. Timeline (Tally Reckoning, TR)

| Year | Event |
|---|---|
| Before TR | **The Noise**: fortune moves like weather |
| Ancient (many centuries) | **The Many Ledgers**: each land develops its own accounting with fate (the Moirai's thread, Chitragupta's records, the Book of Life and Death, Enma's ledger, the Black Book of the Crossroads) |
| ~1,000 years before TR | Zero formalised in Śūnyapura |
| TR 0 | Meridian founded as a trading city at the centre of the Tally |
| TR 380–690 | **The Binding**: Meridian's actuaries copy, buy or seize each land's ledger |
| TR 702 | **The Basilica** completed; **the Final Binding** cages Hap in the Even Hand engine; first Dawn Tally; the Rounding begins. Worship of Hap is outlawed in Meridian |
| TR 760→ | **Ledgerism**: the Basilica's brass-and-steel style spreads through Meridian's offices and uniforms |
| TR 850→ | **Charmpunk**: immigrant quarters fill Meridian; every culture's charms worn at once on the street |
| TR 960 | A Noise storm destroys Lucan Thale's street; he is 12. **Remainder** style begins in the Undercity as Omens fall |
| TR 962 | The Deficit is first measured by Śūnyapura's observatory |
| TR 985 | Thale becomes Comptroller |
| TR 990 | Tightened rounding allocations stop Maeve's grandmother's charms; her family migrates. This is not the original creation of the Rounding |
| TR 990→ | **Gilded Fortune**: the 99 s and Exchange magnates flaunt gold leaf, jade and gardens |
| TR 999 | Thale proves the Rounding and finds Hap; drafts the Final Audit; begins regional pact renewals and authorizes the surveyors' eclipse-control office |
| TR 999 | The House buys a local protection loop. Fibi later completes 1,596 repeats before the party's current iteration 1,597; outside time advances only the anchored night |
| TR 1001 | Varro becomes a Collector and later takes the Undercity Auditor office/Seal 1; he did not sign its original TR 999 pact |
| TR 1002 (present) | NIL wakes; the Naming Rite; REMAINDER DETECTED. The game begins. |

The present year is **TR 1002**, deliberately just past the round 1000.

## 4. Factions

| Faction | Seat | Wants | Symbol |
|---|---|---|---|
| **The Open Hand** (outlawed faith of Hap) | Everywhere, quietly | To free Hap; second chances for everyone | An open palm holding a die |
| **The Basilica** (Comptroller, clerks, Ledger-priests) | Meridian | Order, the Final Audit | A brass gear around the Basilica's eye (which reads as a 0) |
| **The Collectors** | Meridian | Debts paid; bounties | A hound skull over a ledger seal |
| **The Charm Bazaar guilds** | Meridian | Trade, survival, folk luck | A ring of mixed charms |
| **The Yokai Courts** | Hyakki | To keep existing | Nine foxfire flames |
| **The Luck Exchange** | Bāfā Harbor | Profit | The three-legged toad with a coin |
| **The Ten Courts** (keepers) | Under the River Empire | The true count of the dead | The Judge's brush |
| **The Observatory** | Śūnyapura | Truth by measurement | An astrolabe around a 0 |
| **The Pythagorean Synod** | Kroton Nova | Purity of number | The tetractys (ten dots) inside a sieve ring |
| **The House** | Lucky Strike, Crossroads | The night never ending | The ouroboros around 89 |

## 5. World rules (canon locks)
1. Civic Omens are two digits and visible, except unregistered NIL's NaN. Audit Omens are a separate normalized frame. Machine trial/boss stakes do not imply a Civic soul.
1a. Hap never speaks in daylight and never appears as an enemy. It appears only in dreams, coincidences and the finale.
2. Only Auditors can stop their own wheel. Most people can't.
3. Luck is conserved across people/reserves/the hidden account under the Basilica. Ordinary damage/score does not create Civic luck. Positive-Sum changes how plural ledgers share possibilities, after earlier proof, not retroactively.
4. Audit defeat is stake exhaustion. Civic settlement is the separate dangerous state described above; neither automatically disintegrates a named person.
5. Keepers cannot be killed and are never framed as evil.
6. The Basilica's light is always Nixie amber; steel numbers belong only to the Basilica's officials.
7. Charms work by their declared SYSTEMS payload everywhere; no undocumented home-region multiplier. A local set or Land Law interaction applies only when explicitly named and previewed.
8. No guns of modern military style: weapons are revolvers, blades, staves, hammers, fans, shields and instruments.
9. Technology is retro-futurist brass and Nixie, with no screens except Basilica terminals and Exchange boards.

## 6. Naming conventions
| Land | Rules | Examples |
|---|---|---|
| Meridian | Mixed origins; surnames that are words or numbers | Vesper Sette, Varro Kade, Maeve Triskel |
| Hyakki | Japanese-style given names; spirits named by number or object | Hina, Tamamo |
| River Empire | Chinese-style names with meaningful characters, especially numbers | Ba Jinling (eight golden bells), Bai Si (white four) |
| Śūnyapura | Sanskrit-derived words for concepts and numbers | Shunya (zero), Purna (fullness) |
| Kroton Nova | Greek-style, Latin numerals for rank | Prima, Archon Seventeen |
| Crossroads | Americana nicknames, Italian-American and Irish-American surnames | Fibi Leone, "Mr. Eighty-Nine" |

AI source-check every non-English name/script and record the source, date and uncertainty. This is not native-speaker approval. If external review actually occurs, record its evidence accurately; under AI-only production no human finishing step is assumed. Remove or fictionalize sensitive unverified imagery (CULTURAL_CONSULTATION).

## 7. Truth and knowledge tiers

| Fact | Objective canon | What can be said before its reveal |
|---|---|---|
| Basilica age | BindingTR 380–690; cageTR 702 | Public myth may omit coercion, but Thale never literally built it |
| Thale | Born~TR 948; childhood stormTR 960; inherited officeTR 985; found cageTR 999 | Claims of institutional greatness are his belief/propaganda, not autobiographical authorship |
| Rounding | Available luck moves to an unlisted conserved account | Prologue shows confiscation; Act I a missing page; Act II fractional discrepancies; Act III proves NIL's account |
| Hap | Caged in the engine; NIL is its lost change, a separate person | Dreams/coincidences suggest a speaker; Act III identifies account, Act V glimpses inside eye, finale exposes cage |
| Default | Absolute stillness when chance dies | Public warnings about returning Noise are doctrine; Thale mistakes freezing for rescue |
| Positive-Sum | Different regional records encode compatible possibilities, translated by the collective proof | Link cooperation and mismatched records seed the equation before the finale; no pre-finale ordinary attack creates luck |

Final Civic values: Balance ending transfers from NIL's recorded reserve, capped 99 with excess recorded; Positive-Sum gives NIL positive Civic 10 for resonance 0, otherwise chosen 01–09. Resonance remains the player's choice. Fibi's retained memories initially concern local routines; the party was not present on previous iterations. End-condition flags and catch-up rules are canonical in STORY §9.
