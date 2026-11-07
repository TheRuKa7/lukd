# ZERO-SUM: OMEN — Bond Arcs, Key Scenes and the Dialogue Database (Gate B 6)

Updated 7 November 2026 under [DECISIONS.md](DECISIONS.md). **Specified campaign content, not implemented dialogue or tested relationship pacing.** Each companion has **four narrative stages**, through story-integrated scenes or optional conversations. Narrative state is separate from mathematical resonance bonds and Act IV Awakenings. Completion grants the named bond reward once through SYSTEMS' content payload plus the protected proof flag where relevant. STORY §9 owns ending predicates/catch-up. The jam has no bond system; Vesper's rescue and mercy remain ordinary story beats.

---

## 1. Bond arcs

| Hero | Scene 1 | Scene 2 | Scene 3 | Scene 4 (payoff) | Reward |
|---|---|---|---|---|---|
| **Vesper** | Teaches NIL to read tells ("Everyone has one. Yours is you don't blink.") | Admits the rigged hand that Settled a child in Lucky Strike | Faces the House's table again (Act V) | Deals Fibi an honest hand; stops flipping the coin | *Honest Hand*: her Pairs pay ×3; ledger piece: the House's marked deck |
| **Maeve** | Forges a charm that does nothing (“Friend luck.”) | Her grandmother's charms stopped during the TR 990 tightening of the centuries-old Rounding | Finds a first-generation Basilica gear in Kroton's archive scrap | Asks what NIL needs, then forges the horseshoe to hold a Seal open | *Forge-Mother's Mark*; `piece.first_gear_horseshoe` |
| **Hina** | Counts NIL's wishes (“Hina will lend you some.”) | Afraid of turning 100 and still not feeling real | Ofuku says the shrine kept her because people loved her | Decides she is already real at 99; paints NIL a daruma eye | *Already Real*; `piece.enma_page`; no age change |
| **Ba Jinling** | Charges NIL interest on a cup of tea, then pays it back double | Shows NIL the debts she buys and burns in secret | Her father's laugh; she almost forgives him | Reopens the Exchange at 0% for anyone under 8 fen | *Bank of Bells* upgrade; ledger piece: her father's true account book |
| **Bai Si** | Counts four lanterns; says little | Remembers the first civically Settled soul he counted | NIL names a missed remainder; he writes that name inside one of his four existing lanterns | Smiles for the first time in Act IV, remembering an individual rather than a total | *Remembered Name*; `piece.dead_count`; always four physical lanterns |
| **Shunya** | Explains zero with chai (“It's room for chai.”) | Admits the catalogue gap before requesting NIL's consent to examine it | After the reveal sits silently with NIL, without trying to solve their feelings | Offers co-authorship; asks what may be published; NIL chooses consent and receives a protected copy | *Careful Proof*; `piece.remainder_equation`; publication is epilogue only, not a gate |
| **Prima** | Recites primes to calm down; trips | Admits she always felt like the Synod's mistake | Lachesis's thread; she and Shunya argue whether 1 is prime | Catches the Archon, her teacher, as he falls | *Even Prime* upgrade; ledger piece: Lachesis's thread |
| **Fibi** | Predicts local routines, then hears NIL say something new in iteration 1,597 | Shows the motel 3a.m. she remembers from 1,596 completed repeats | Reads the contract, learns its drain causes the fatal dawn and consents to cancelling it | Watches her first new sunrise; cannot finish her own next sentence; says “One.” | *First Tomorrow*; `piece.black_book_page`; four stages before finale |
| **Varro** *(secret)* | Shares a meal, mask still on, before truth is proved | Reads Livia's letter and withheld release order | Removes mask for good when he chooses to help in Act V | Post-ending recruit accepts the shelter's first stray with Livia | *Free Man*; never a main-ending prerequisite |
| **Kyūsuke** *(secret)* | Sells NIL every cucumber | Fills NIL's dish "for luck" | Bows to a Basilica clerk; the clerk bows back | Goes home with a full cart and a story | *River God's Friend* |
| **Liu Shun** *(secret)* | Teaches one tile rule and claims she won the party | Shows her husband's lucky 6 carved on her purse | Sets a cooperative puzzle for NIL; they solve it together, no played loss | Promises to teach Tobi, letting the next generation choose its own lucky number | *Heavenly Hand*; epilogue lesson is payoff, not prerequisite |

**Reward separation:** names in this table identify story reward events (`bond_reward.<hero>`), not automatic selections of similarly named Awakening branches or a second grant of a base passive. Exact mechanical payloads live in SYSTEMS/content data and require balance checks before an expansion build enables them. Shunya's base pattern-wild and later Awakening bond-wild are not unlocked by this narrative scene. Hina stays 99. This table does not invent an extra multiplicative 9 passive beside the declared kit.

**Duo budget:** one spotlight duo plus four short roster-conditioned exchanges per act, with an absent-character fallback. An extra Complement exchange can be that spotlight; it is optional enrichment, not another required ending counter. Zero has no ordinary Complement. No requirement to produce a unique film for every companion pair.

### Stage schedule and recovery

| Core companion | Stage 1 | Stage 2 | Stage 3 | Stage 4 before commitment |
|---|---|---|---|---|
| Vesper | Prologue rooftop/campaign road rest | River marked-card evidence | Act V honest-hand preparation | Honest game in front of the House |
| Maeve | Forge or Hyakki caravan recruit | Hyakki/River rest; recent tightening memory | Kroton first-gear archive | Forge at Kroton exit or final camp |
| Hina | Parade/rest | Enma approach | Ofuku's message at next rest | Tamamo aftermath or present-day camp conversation |
| Jinling | Pawnshop tea | Burned-debt evidence | Father's defeat aftermath | Signed 0% policy and protected true book at River exit |
| Bai Si | Hall approach | Ten Courts true-count record | Śūnyapura equation reveals a named remainder | Act IV undercity memory/rest; first smile |
| Shunya | Observatory tea | Before Hall examination, consent | Silent steps after reveal | Śūnyapura exit or final camp co-author decision |
| Prima | Escort introduces personality, recorded when she recruits | Undercity doubt before defection | Lachesis trial | Archon rescue aftermath |
| Fibi | Act V arrival investigation | Motel investigation | Contract proof before boss | Dawn after cancellation, before Basilica |

STORY-integrated scenes advance their stage only when earlier stages are present; if a prior optional version was skipped, final-camp catch-up supplies the missing present conversation and resolves the next stage in order. A history recap never pretends the character made a decision they declined. Every missing core stage remains available at the final camp until the player confirms an ending. Reserve characters count; no repetitive combat, friendship currency or four generic camp visits are required. Eight core arcs total 32 stages; secret arcs add 12, outside jam scope.

Proof pieces are protected narrative records with stable IDs (STORY §9). Leaving a region, burning an enforcement copy, cutting a charm in a trial, act rollback or changing equipment cannot delete them. Stage/reward event IDs apply once; skip/watch agree; reload and replay do not grant duplicate stats or currency.

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

The target import is one Unity Localization string table plus `story/lines.csv` metadata. These runtime files are not supplied by this Markdown. Required schema:

| Field | Example |
|---|---|
| id | `p01_alley_010` (act_scene_line) |
| speaker | `VESPER` |
| text_en | Need a hand? Seven fen. |
| emotion | smug |
| trigger | `scene:p01_alley` / `bark:pattern:jackpot` / `bond:vesper:2` |
| conditions | `party_has:hina`, `lucky:7`, `flag:livia_saved` |
| voice | `vo_vesper_p01_010` (or none) |
| max_chars | 90 (validator must enforce before content import; no check is claimed to exist yet) |
| notes | "Tone: dry, warm" |
| review | `unverified` / `source_checked` / `external_review_recorded`; source check never equals native/cultural approval |

Additional scene metadata: `scene_id`, ordered prerequisites, participant states, stage transition, proof/reward ID, choice labels, skip outcome, checkpoint and fallback. Cite actual reviewer evidence if an external review is recorded; never generate a false approval flag. End-condition validators consume stable flags, not translated dialogue strings.

**Bark budget:** jam uses only JAM_SCRIPT's triggered lines, with no charged-ultimate category. Campaign initial pass has two strikes, two hurt, one pattern and one relationship bark per companion; avoid repeats in the same round. Extra variation and ten digit reactions per hero are optional authored content after the core scenes work. Any written reaction treats the digit as personal resonance, never as intrinsic moral worth or a promised difficulty tier.
