# ZERO-SUM: OMEN — Bond Arcs, Key Scenes and the Dialogue Database (Gate B6)

Every companion has a **4-scene bond arc** at Teahouse/Campfire nodes. Completing all four gives a second passive, a Link Art upgrade and the true-ending flag (with their ledger piece). Campaign scenes are in [`STORY.md`](STORY.md); jam lines in [`JAM_SCRIPT.md`](JAM_SCRIPT.md).

---

## 1. Bond arcs

| Hero | Scene 1 | Scene 2 | Scene 3 | Scene 4 (payoff) | Reward |
|---|---|---|---|---|---|
| **Vesper** | Teaches NIL to read tells ("Everyone has one. Yours is you don't blink.") | Admits the rigged hand that Settled a child in Lucky Strike | Faces the House's table again (Act V) | Deals Fibi an honest hand; stops flipping the coin | *Honest Hand*: her Pairs pay ×3; ledger piece: the House's marked deck |
| **Maeve** | Forges NIL a charm that does nothing ("It's for luck. Not *magic* luck. Friend luck.") | Her grandmother's charms stopped working the day of the Rounding | Finds a Basilica gear in a Kroton scrapheap: the first one ever cast | Forges the horseshoe that can hold a Seal open | *Forge-Mother's Mark*; ledger piece: the first-gear horseshoe |
| **Hina** | Counts NIL's wishes ("Zero. That's sad. Hina will lend you some.") | Afraid of turning 100 and not being real | Ofuku tells her the shrine kept her because people loved her, not because she was old | Decides she's already real; paints NIL a daruma eye | *Already Real*: 9s give ×1.9 Mult; ledger piece: Enma's torn page |
| **Ba Jinling** | Charges NIL interest on a cup of tea, then pays it back double | Shows NIL the debts she buys and burns in secret | Her father's laugh; she almost forgives him | Reopens the Exchange at 0% for anyone under 8 fen | *Bank of Bells* upgrade; ledger piece: her father's true account book |
| **Bai Si** | Counts lanterns; says almost nothing | The first soul he ever executed (he remembers the number) | NIL shows him a remainder he missed; he lights a fifth lantern for the first time | Smiles (first time, Act IV or later) | *True Count*; ledger piece: the true count of the dead |
| **Shunya** | Explains zero with a cup of chai ("Empty isn't nothing. It's room for chai.") | Her teacher's catalogue has a gap she never told him about | After the reveal: sits with NIL in silence on the observatory steps | Publishes "On the Remainder" with NIL as co-author | *Śūnya* bond for any digit; ledger piece: the Remainder equation |
| **Prima** | Recites primes to calm down; trips | Admits she always felt like the Synod's mistake | Lachesis's thread; she and Shunya argue whether 1 is prime | Catches the Archon, her teacher, as he falls | *Even Prime* upgrade; ledger piece: Lachesis's thread |
| **Fibi** | Finishes NIL's sentences (she's heard them 1,596 times) | Shows NIL the motel room where she's spent every 3 a.m. | Learns the loop is to keep her alive; is furious | Watches her first sunrise; doesn't know what to say; says "One." | *1,597*: freeze her digit once per fight; ledger piece: the Black Book's last page |
| **Varro** *(secret)* | Shares a meal; doesn't take the mask off | Livia's letter | Takes the mask off for good | Opens a dog shelter with Livia | *Free Man* |
| **Kyūsuke** *(secret)* | Sells NIL every cucumber | Fills NIL's dish "for luck" | Bows to a Basilica clerk; the clerk bows back | Goes home with a full cart and a story | *River God's Friend* |
| **Liu Shun** *(secret)* | Teaches mahjong; cheats; denies it | Her husband's lucky 6, carved on her tile purse | Loses to NIL on purpose (she says) | Teaches Tobi mahjong in the epilogue | *Heavenly Hand* |

**Complement pairs** get one extra duo scene each (e.g. Vesper + Maeve: "Third time lucky, seven times lucky: who's luckier?").

## 2. Hap's Dreams (one per act)
| After | Hap's face | Question | NIL's answer (player can't change it) |
|---|---|---|---|
| Prologue | A street fortune-teller | "Pick a number. Any number." | (the player's number) |
| Act I | An old paper lantern | "Do you think you're real?" | Silence |
| Act II | A smiling money toad | "Everyone owes me something. You're the only one I owe." | "Owe me what?" |
| Act III | A monsoon cloud full of stars | "You're the change I never got back." | "Are you real?" |
| Act IV | A cracked marble statue | "Which of your friends is worth the least?" | "Wrong question." |
| Act V | A laughing slot machine | "Tomorrow is the only bet I always take." | "Then bet on us." |

## 3. Dialogue database (format)

Every line lives in one table (Unity Localization string table + a metadata sheet `story/lines.csv`):

| Field | Example |
|---|---|
| id | `p01_alley_010` (act_scene_line) |
| speaker | `VESPER` |
| text_en | Need a hand? Seven bucks. |
| emotion | smug |
| trigger | `scene:p01_alley` / `bark:pattern:jackpot` / `bond:vesper:2` |
| conditions | `party_has:hina`, `lucky:7`, `flag:livia_saved` |
| voice | `vo_vesper_p01_010` (or none) |
| max_chars | 90 (enforced by a check) |
| notes | "Tone: dry, warm" |
| review | `jp_ok` / `zh_ok` / `hi_ok` / `el_ok` (cultural sign-off where relevant) |

**Barks:** each hero has 3–5 per category (strike, hurt, pattern, ultimate, bond-partner banter, lucky-number reaction for all 10 digits).
**Lucky-number reactions:** every companion has one line for each digit the player might choose (e.g. Hina on 4: "Brave. Or silly. Hina likes both.").
