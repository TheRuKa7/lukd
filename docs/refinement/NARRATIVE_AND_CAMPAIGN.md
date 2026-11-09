# ZERO-SUM: OMEN — Narrative and campaign refinement review

> **HISTORICAL SNAPSHOT - 6 November 2026, baseline `3d88239`.** Findings/proposals describe that snapshot, not the current corrected repository. See [adopted decisions](../DECISIONS.md), [current status](../PROJECT_STATUS.md) and [audit resolutions](../DOC_AUDIT.md).
Review date: 6 November 2026 (Asia/Kolkata). Repository baseline: `3d88239dff58db1d313b8d979d6ae98a8f1ceed0`.

**Historical review snapshot.** The body preserves findings/proposals against that source revision; its section references and “current” descriptions are not the present specification. The 7 November corrections are governed by [DECISIONS.md](../DECISIONS.md), current domain documents and [DOC_AUDIT.md](../DOC_AUDIT.md). Many listed defects have now been resolved in source. This report itself is not evidence of implementation, review approval or playtesting.

This is an assessment and a set of **proposals**, not a change to existing canon. No scene has been playtested, no cultural sign-off has occurred, and no Unity campaign implementation was verified in this review. The original source documents remain unchanged.

## 1. Recommendation

Keep the central invention: a world that treats a person's luck as a visible asset; a protagonist made from discarded fractions; and party synergy that eventually changes the world's zero-sum law. NIL's chosen digit returning at the gate and ending is a strong long-range payoff. Hap's dice eyes, the Open Hand, Vesper's ignored coin, Hina's unfinished century and Fibi's first dawn already provide memorable recurring images.

The largest narrative improvement is **causal continuity**, not additional lore. Right now each region has an attractive local story, but much of the campaign follows the same arrival → companion → keeper → Auditor → Seal template. Make each victory change the next region's situation, give the party decisions with visible costs, and resolve the rules below before producing expensive scenes. The jam should demonstrate the opening, one relationship and the central interaction; the campaign should expand only after those work.

**Current production steering:** use existing/free tools first, prioritize the Unity jam and expand afterward. Recommended jam default is a complete 10–15-minute Prologue with NIL, Vesper and Varro; Maeve is optional only after that path works. Hyakki belongs after the jam unless the root production plan's 9 November gate proves it is affordable. The original two-region JAM_SLICE remains repository canon/design intent; this is an explicit scope-change recommendation. Freeze production by the end of 11 November IST, use 12 November for verification, and upload on 13 November ahead of the 14 November 17:30 IST deadline. The narrative plan does not depend on purchasing new generation services.

## 2. Current canon to preserve

| Element | Current source | Preserve because |
|---|---|---|
| NIL is a person, not Hap or a god | WORLD_BIBLE §2A; CHARACTER_BIBLE §1 | The story concerns personhood rather than a chosen deity winning by birthright. |
| The Basilica began centuries before Thale | LORE_LEXICON §3 | Thale inherits an institution and chooses to perpetuate its harm. |
| Eight core companions and three secret recruits | CHARACTER_BIBLE §0, §13 | A varied authored roster already exists; more recruits are not the first missing ingredient. |
| One question for NIL in each act | STORY §0 | An emotional spine connects the mathematical premise to people. |
| Midpoint Remainder reveal; finale revelation of Hap's cage | WORLD_BIBLE §3; STORY §4, §7 | Two different revelations can support a long build if evidence and consequences are separated. |
| Warm noir, brief dialogue, lived customs | NARRATIVE_STYLE §1–2 | The cast should feel like people rather than tour guides or interchangeable quip machines. |
| Companions from different lands create mechanical value together | GDD §2.3; STORY §0 | The central theme can be experienced before it is spoken. |
| Auditors are understandable but accountable | CHARACTER_BIBLE §10 | Motive gives conflict weight; kindness alone must not excuse harm. |

## 3. Canon conflicts and unresolved rules

“Conflict” below means the documents prescribe incompatible behavior. “Unresolved” means an explanation could work but has not yet been specified. Priority P0 means resolve before producing the affected jam scene; P1 means resolve before full-campaign content production.

| Priority / status | Evidence | Player or production consequence | Proposed resolution |
|---|---|---|---|
| P0 conflict: opening timing | FIRST_10_MINUTES rules 1–2 require the first tap by 20 seconds and lucky-number choice in minute one. JAM_SLICE beat 2 makes a ~45-second myth intro mandatory before Rain Alley. JAM_SCRIPT §1 allocates 37 seconds of shots despite the ~45-second label. WORLD_BIBLE §8 describes a ~2:30 opening. | The cold-open hook cannot meet its stated timing if all intros are concatenated. | Make FIRST_10_MINUTES the jam pacing authority. Begin in Rain Alley. Move the myth montage to the rooftop, optional title extras, or later dream fragments; never play two versions of the opening in sequence. |
| P0 conflict: rescue dialogue implies unexplained erasure | JAM_SCRIPT Rain Alley has NIL say “Neither do you, now” to the Collector after raising Ama's number. World rules allow only NIL's NaN exception. | NIL appears to erase a person's Omen before the player understands the stakes; this also undermines the later mercy toward Varro. | Replace that beat with a brief escape instruction, e.g. NIL to Ama and Tobi: “Go. Both of you.” This is proposed replacement copy. |
| P0 unresolved: where Ama's extra six points come from | WORLD_BIBLE §2 conserves luck; the opening moves Ama from 01 to 07. No corresponding debit or transfer is shown. | The first magical act appears to contradict the defining law. | Show a Collector's confiscation jar lose six sparks while Ama gains six. NIL reroutes already confiscated luck; later evidence can show they can access remainders. Do not establish unrestricted creation of luck here. |
| P0 conflict: Hina already having lived a hundred years | CHARACTER_BIBLE §4 locks her at 99 until the finale. JAM_SCRIPT Tamamo counter-ultimate says she has lived a hundred years of nights. | The climactic line contradicts her defining desire. | Proposed line: “Ninety-nine years. Enough nights to know you.” Keep the century incomplete. |
| P0 scope dependency: optional trial teaches a needed verb | JAM_SLICE marks Enma's trial and Carry as Should; campaign ACT_DESIGN treats that trial as the source of Carry. | Cutting the trial can leave a tutorial, boss expectation or character line referring to an unlearned verb. | Jam Carry is either cut with its trial or granted in a short Hina rehearsal before Tamamo. Store a verb-unlocked flag and condition later instructions. |
| P1 conflict: Thale's authorship of the system | LORE_LEXICON §3 dates the cage to TR 702, Thale's birth to approximately TR 948 and discovery to TR 999. WORLD_BIBLE §2A gives him the “I put chance in a box” line; §4 and STORY finale have him claim he replaced the many ledgers. | A centuries-old institution sounds like one living man's invention. | Thale inherited the Basilica; his innovation is Fixed Fate. Rewrite factual claims accordingly, or explicitly stage the existing claims as institutional propaganda that NIL can challenge. |
| P1 conflict: Fixed Fate saves or kills Hap | WORLD_BIBLE §2A says a frozen god is dead; §4 says Thale “would save the world from the Default.” | The antagonist's argument depends on which assertion the writer treats as true. | Record three fields: objective truth, Thale's belief, public doctrine. Objective: freezing postpones visible disorder but destroys chance/Hap. Thale believes stability is rescue. Show one measurable short-term benefit of his system so the dilemma is earned. |
| P1 terminology ambiguity: Default | LORE_LEXICON glossary says Basilica collapse and return of Noise; WORLD_BIBLE §2A says Hap's death and absolute stillness; post-game treats Default as stillness. | Writers may render opposite disasters with the same name. | Keep the common public prediction and the hidden truth, but label both explicitly in the lexicon and spoiler tiers. |
| P1 conflict: Maeve's family chronology | BOND_ARCS and WORLD_BIBLE describe her grandmother's charms failing when the Rounding began; LORE_LEXICON dates that to 300 years ago. Maeve is 20 and no family longevity is specified. | A personal memory inadvertently spans centuries. | Make her grandmother experience a recent local tightening/recalibration of the old system, not its original creation. Preserve the first gear as a historical artifact found later. |
| P1 conflict: Bai Si's fifth lantern | BOND_ARCS scene 3 lights a fifth lantern; CHARACTER_BIBLE §6 says always four lanterns. | Generated sheets, rigs and scenes disagree about silhouette and symbolism. | Keep four physical lanterns. Put the uncounted name inside one of them, or let a fifth reflected flame appear only in water; specify whether that is a deliberate exception. |
| P1 conflict: Hina's Awakening | SYSTEMS §5 makes her turn 100 in Act IV; CHARACTER_BIBLE §4 says never before finale. | A build selection resolves her story ahead of its written payoff. | Rename the branch as accepting herself at 99; it changes control/style rather than literal age. Reserve her birthday for the epilogue. |
| P1 hidden ending lock: optional Maeve | STORY/CHARACTER_BIBLE allow the forge to be missed; STORY ending requires all eight core bonds and their pieces. | A minute-five route can silently deny the ending hours later. | Offer a guaranteed later recruitment and a non-missable final catch-up route for every core companion. The jam may omit Maeve without importing a full-game ending penalty. |
| P1 scheduling gap: late bonds | Fibi joins Act V but needs four scenes, while ACT_DESIGN provides few rest nodes. Prima's fourth bond scene is her story boss rescue. | Bond completion can require arbitrary backtracking or scenes that have already happened. | Tag scenes as story-integrated or optional. Fibi's four stages fit distinct loop investigations, the revelation, and dawn; those main-path scenes count. Prima's rescue counts automatically after prior stages. |
| P1 conflict: earned endings and post-ending bond rewards | Fibi's dawn and Shunya's publication appear as fourth bond rewards; the latter reads like an epilogue event. Positive-Sum requires all bonds complete before the ending. | A reward that happens after the ending cannot be a precondition for choosing that ending. | Complete Shunya's bond when she offers NIL co-authorship and obtains consent; publication is the epilogue payoff. Dawn occurs before the finale, so Fibi can complete there. |
| P1 arithmetic error: Seal alarms | STORY Act V beat 10 says seven alarms. Finale lists six acquired Seals plus NIL's chosen digit. | Gate logic, UI and scene count disagree. | Six Seal alarms; the seventh signal is NIL approaching/using the gate, if a seventh alarm is desired. |
| P1 staging ambiguity: gate lock vs Thale opening it | STORY Act V says Thale opens the Upper Gate, then finale requires seven digits and Ivo opens a service door. | Three different agents seem to remove the same obstacle. | Distinguish the exterior security cordon, ritual Seal lock and interior service passage. Thale recalls guards; NIL satisfies the lock; Ivo bypasses an interior trap. |
| P1 unresolved: Omen, resonance and combat display | WORLD_BIBLE makes Omen a person's luck share. GDD §1.6 normalizes it from 99 to 00 in combat and overlays shared party Balance on NIL's NaN. Characters also have unrelated single resonant digits. | A low-Omen civilian may inexplicably appear as 99, NIL appears numbered, and a lore rule reading an Omen may read the wrong value. | Specify distinct data fields: civic Omen, resonance digit and Audit Balance/readout. Use distinct visual frames and clearly state which rules read which field. Preserve a visible NaN on NIL. |
| P1 ending contradiction for lucky zero | Positive-Sum resolves NIL's NaN into the player's chosen digit; canon requires two-digit Omens and 00 means Settled. | Choosing 0 can make the hopeful ending visually imply NIL has immediately died. | The chosen digit becomes NIL's stable **resonance**, while their civic Omen is a positive two-digit share. For resonance 0, use an explicitly positive value such as 10. Show both meanings, not 00 as a happy health result. |
| P1 unresolved: ending cap and conservation | Balance ending raises every Omen by one despite a 99 maximum; Positive-Sum changes conservation itself. | A major rule breaks in the final images without explanation. | Balance raises eligible Omens to a maximum of 99 and deposits excess in reserves. Seed evidence for Positive-Sum's alternative earlier: differing ledgers describe possibilities, not merely coins in a finite pool. Make the final change an earned repair supported by the equation and artifacts. |
| P1 policy conflict: cultural representation | WORLD_BIBLE says revered figures are never enemies while Rahu/Ketu are named bosses and also acknowledged as venerated bodies; CULTURAL_CONSULTATION flags this exact open question. | “Respectful” labeling alone does not resolve the stated policy. | Make the final choice explicit before Act III production: a non-hostile celestial alignment trial, or invented Basilica eclipse constructs as combatants while revered figures remain outside enemy roles. Do not claim AI research supplies cultural sign-off. |
| P1 pacing conflict | ACT_DESIGN/GDD say 25–35 minutes per act, STORY headers total 315 minutes (~5h15), while the stated journey is 6–8h. | Writers and asset producers lack a common scene budget. | Use one budget: a main path around 5h15 plus 45–105 minutes of bonds, optional quests and navigation as an initial 6–7h hypothesis; verify by playtest rather than assuming written estimates. |
| P1 presentation conflict: universal disintegration vs spared cast | BESTIARY rule 4 says enemies round down into digits and blow away. The same file gives Varro, Tamamo, Jin Chan, the House and Thale surviving aftermaths. | A reusable death effect could erase an actor immediately before their mercy/reconciliation scene. | Separate machine/Noiseling disintegration, mortal defeat, spirit withdrawal and keeper completion outcomes. Defeated named actors remain staged for their aftermath unless a scene explicitly requires disappearance. |
| P1 unresolved: finale recalls absent or unreachable companions | BESTIARY Thale Phase 3 says each companion returns when NIL lands their digit; SYSTEMS starter wheels omit digits, Fibi's digit changes, and some recruits are optional or post-game only. | The finale could promise a reunion that the player's roster cannot produce, or require an unavailable face. | Return recruited core cast automatically through a scripted recall sequence; digit taps accelerate/shape presentation rather than gate required callbacks. Explicitly map Fibi's echo to her current or canonical recall digit. Optional guests receive optional variants. |

Additional small fixes: the script uses “bucks” where the currency is fen (keep as intentional slang or change consistently); Varro's cast overview presents 61 under a “Digit” column while the recruit resonance is 1 (label 61 as Omen); Fibi's “only person who remembers” needs to become “only local who remembers” once the party retains loop knowledge. Define whether 1,597 means completed loops or the current numbered loop, and whether outside time advances.

## 4. Build the long story through evidence, consequence and payoff

Do not repeatedly announce that NIL is special. Track a small number of mysteries and resolve one layer at a time. Proposed evidence plan:

| Thread | Seed | Complication | Proof / reversal | Payoff |
|---|---|---|---|---|
| Whose luck is NIL using? | Ama's rescue reroutes a visible confiscated share. NIL hears unfamiliar remembered words. | Enma has no page for NIL, but an old wish appears in the decoder. | The Ten Courts have many fractional mismatches; Śūnyapura reconstructs their common account. | NIL chooses how to return what was taken, with the party preserving their personhood. |
| Is order actually mercy? | Collectors prevent a dangerous accident for a high-Omen person while threatening Ama. | A region's freed Seal improves one community but briefly destabilizes trade/weather. | Thale provides evidence that his emergency measures reduced some harms, alongside evidence he hid costs. | The final argument concerns a demonstrated tradeoff, not an obviously false claim versus friendship. |
| What is Hap? | Coin on its edge; warmth in an Open Hand; first unexplained dream. | The same dice-eye motif appears in incompatible local art traditions. | Midpoint reveals NIL's source account, but not the cage's occupant. Act V's dream gives a partial inside view. | The Basilica eye and Open Hand imagery become one mechanical and visual truth. |
| Can luck be shared without stealing? | A modest Link Art does more than two isolated attacks, without lore commentary. | Shunya finds regional equations that cannot all be represented in the Basilica's single unit. | Prima defends “composites”; Fibi accepts a future nobody can guarantee. | The equation, thread, records and contract allow translation between ledgers; the Open Hand outcome is technically and emotionally prepared. |
| Vesper's ignored coin | She flips without looking, teaching NIL that tells reveal choices. | A witness or marked card in Act II challenges her selective version of the rigged hand. | In Act V she gives Fibi the rules and accepts a fair loss; helping becomes a choice, not a successful cheat. | Her final Link Art line echoes a promise NIL has seen her keep. |
| Varro and Livia | Window, named relationship and one concrete need in the prologue. | A dated “pending” form in Act II contradicts the promise. | The party obtains a reliable route to Livia rather than a vague condition flag. | Varro chooses to help before receiving assurance that his own debt will be forgiven. |
| The House's protection | Early casino receipt or Vesper memory mentions a price paid for a saved dawn. | Penny's counting and Fibi's knowledge show repeated outcomes, but different details survive. | The contract explicitly links the fatal dawn to its own maintenance. | Breaking it saves Fibi because the player discovered its terms; the grandfather accepts uncertainty. |

Every reveal should have at least two earlier observable clues, a plausible incomplete explanation, and a consequence that changes what the player does next. Optional lore may deepen a reveal; it must not contain the only evidence required to understand the main plot.

Use the Seal memory flashes already promised in WORLD_BIBLE §6. Each should show one ordinary person's lost possibility, not a second exposition lecture: an unopened shop, a delayed apology, a ferry that did not arrive. Repeat one face or object later as a resident whose life has changed. This makes “everyone's remainders” legible as people.

### Proposed causal bridge between regions

1. Breaking Varro's Seal marks NIL's route; Meridian exports pursuit to Hyakki.
2. Releasing Hyakki's ledger shifts a commercial obligation to the Luck Exchange; Jinling has a reason to seek NIL beyond the bounty.
3. Jinling's burned accounts expose the same fractional deficit in living and dead records; that evidence directs the journey to the observatory.
4. The midpoint proof forces Thale to accelerate the Sieve, making Act IV a consequence of what NIL learned rather than the next stamp on the route.
5. A contract recovered in Kroton links the original engine's finance to the House; Vesper must choose whether to disclose her history before the party follows it.
6. The Crossroads contract supplies the legal/mechanical weakness that makes the Basilica approach possible. The final journey is a commitment, not a teleport to a boss room.

These are proposed connectors, not established events. They reuse existing artifacts and characters to avoid adding an unbounded second cast.

## 5. Regions should differ in decisions, not just surface style

| Region | Dominant human conflict | Play pattern to emphasize | A meaningful local decision | Later visible echo |
|---|---|---|---|---|
| Meridian | Survival under readable social rank | A chase and protection sequence; few choices while the player learns | Help a specific person at a visible cost to escape time/resources | Ama or Tobi describes the consequence at a later checkpoint. |
| Hyakki | Belonging versus being preserved unchanged | Disguise, procession and interpreting unreliable appearances | Preserve a comforting public story or tell an uncomfortable truth with Hina | A parade participant changes costume, greeting or allegiance. |
| River Empire | Ownership, debt and accountable repair | Negotiate above; inspect records below | Which debt record to investigate first, with transparent costs and both eventually recoverable | A recurring merchant or orphan benefits; Jinling's new policy has an actual case. |
| Śūnyapura | Consent to knowledge about a person | Observation, measured experiments, descent and a pause after proof | NIL decides who may see the equation about them | Shunya changes her wording and later asks permission to publish. |
| Kroton Nova | Purity versus solidarity | Vertical spaces, rescue and cooperation across castes | Rescue effort versus access to evidence; avoid making children a point-scoring punishment | The undercity builds part of the final coalition. |
| Crossroads | Protection becoming captivity | Repeated investigation with new retained knowledge | Which promise can be broken honestly and who accepts the uncertainty | Dawn scene reflects the player's discovered evidence and chosen trust. |
| Basilica | Choosing institutions, not only defeating a man | A synthesis of learned verbs followed by a deliberate ending decision | Which earned future NIL endorses | Epilogue demonstrates winners, obligations and remaining problems. |

For each region, author a working day, a dissenting local opinion and one joke unrelated to the national-number motif. Do not make every resident a spokesperson for the same belief. Keep culture, political institution and individual opinion distinct. Avoid treating all traditional ledgers as a hierarchy under Hap; the existing bible explicitly says they are not secretly Hap.

## 6. Recruitment, unlocks and custom characters

### Authored roster first

| Companion | Current entry | Proposed unlock guarantee and story function |
|---|---|---|
| Vesper | Prologue rescue | Mandatory; she teaches choosing someone to rely on. First trust scene belongs on the main path. |
| Maeve | Optional forge defense | Early optional entry; later guaranteed caravan/forge encounter if missed. Her contribution cannot silently lock the final repair. |
| Hina | Act I parade | Mandatory; first relationship in which NIL protects someone else's definition of being real. |
| Jinling | Act II guest, permanent after father | Keep guest-to-permanent distinction in UI and save data. Her final choice visibly changes the Exchange. |
| Bai Si | Act II Judge's trial | Mandatory after his record discrepancy is proven; his loyalty is to accurate memory rather than NIL's power. |
| Shunya | Act III observatory | Mandatory; explicitly seek NIL's consent in the reveal's aftermath. |
| Prima | Act IV defection | Escort is not recruitment. Unlock after the school rescue; integrate the teacher rescue into her bond progression. |
| Fibi | Act V loop | Mandatory; supply four bond stages within the loop investigation and dawn rather than requiring four generic camp visits. |
| Kyūsuke | Act I cucumber quest | Optional side recruit. Leave a post-act contact/catch-up route; signal the quest as a recruit opportunity without revealing every reward. |
| Liu Shun | Act II mahjong quest | Optional. Let alternative resolution succeed for players who do not understand mahjong; the joke should not hide recruitment behind unrelated mastery. |
| Varro | Act V guest; full recruit after ending/NG+ | Preserve the distinction. Base-campaign balance cannot assume a permanent digit-1 Twin is available earlier. Revisit the claim that every chosen number has equivalent partner access throughout the campaign. |

Use stable recruit states: `unmet`, `met`, `guest`, `quest_available`, `recruitable`, `recruited`, `temporarily_unavailable`. Each requires an entry event, visible journal hint, catch-up route and save migration behavior. Never silently remove an equipped character during a story scene.

“Custom characters” has two different scopes. The existing roster already supplies distinct authored recruitable characters. A player character creator or free-form generated recruit is **not currently specified**. Recommended first release: authored companions, unlockable outfits and selectable kit branches, with NIL's identity and pronouns preserved. Do not add runtime generation or API-dependent dialogue to the jam.

If player-made mercenaries become a later feature, use bounded templates: cosmetic silhouette presets, approved palettes/parts, one allowed resonance digit and a balanced existing kit. Keep them out of core ledger-piece requirements and do not let them impersonate key cast or invent canon. Commissioning their optional introduction through an offline AI authoring pipeline is more controllable than generating lore during play. This is a future proposal requiring its own UI, writing, animation, save and balance budget.

## 7. Bonds and synergies should reward attention without forcing grind

Keep four stages per core companion, but separate the **relationship scene**, **mechanical upgrade** and **ending evidence**. They need not all unlock at the same instant. Recommended stages are: a shared task; a specific disagreement; a costly choice; a changed habit. Avoid four successive confessions in front of an unchanged campfire.

Concrete existing payoffs to keep: Vesper finally looks at or puts away the coin; Maeve asks a question instead of offering a charm; Hina claims she is real before her birthday; Jinling acknowledges generosity publicly; Bai Si remembers an individual rather than correcting an aggregate; Shunya asks before publishing; Prima catches the person who taught her the harmful rule; Fibi allows a sentence she cannot finish in advance.

The main path should make the ending's necessary commitments achievable. Optional bonds can deepen the result and improve Link Arts. Give a readable pre-finale journal checklist for unresolved promises and a last opportunity to finish them. Do not label character affection as a hidden numerical score.

Existing scope: 32 core bond scenes, or 44 for all 11 companions, before duo scenes and barks. CHARACTER_BIBLE's “every pair per act” banter promise grows to 55 companion pairs at full roster. GDD also promises dedicated cinematics for Complement and Neighbour pairs. Limit production deliberately: one authored spotlight duo per act, a small set of context-sensitive barks, and reusable Link Art staging with unique effects only for the most important pairs. Not every mathematical pairing requires a new rendered movie.

Resolve the promise that **every** chosen digit has a Complement: under literal sum-to-10, 0 has no digit-10 partner. Shunya's wild bond is an exception, not arithmetic equality. Present that exception plainly and verify when each partner becomes available. A permanent narrative choice in minute one should not be an undisclosed difficulty selector.

## 8. Proposed jam opening and onboarding revision

FIRST_10_MINUTES is the best existing pacing reference. Preserve its interactive rescue and personal lucky-number choice. Suggested edit order:

1. **0:00–0:20:** Start unlocks audio; Rain Alley; Ama 01; first tap reroutes six visible sparks from the jar to her Omen. Subtitles carry the beat if audio is off.
2. **0:20–1:00:** Short chase; Naming terminal; choose a digit; REMAINDER DETECTED. Do not require a cultural-tooltip tour before selection; the player can inspect one-line meanings voluntarily.
3. **1:00–3:00:** First safe Audit: stop, observe the reel, receive an explicitly scripted tutorial Jackpot, attempt one forgiving defense. Do not imply the scripted success is a reliable natural probability.
4. **3:00–5:00:** Vesper's short entrance; striker choice; one opportunity to notice Pattern Sight. Introduce Cascade and Zero-Sum as results when they occur, not another compulsory text lesson.
5. **5:00–8:00:** One charm choice, a brief optional Maeve event if implemented, a concrete hint of Livia. No additional mythology montage.
6. **8:00–12:00 target:** Varro's jar is demonstrated, then one ultimate payoff, mercy and rooftop map. The current ten-minute claim must be measured; do not speed-read the relationship beats solely to meet it.

For the recommended Prologue-only jam, resolve the local question: NIL chooses to spare Varro, Vesper chooses to keep helping, and the rooftop shows a possible future. Use a short Hina silhouette/ferry invitation only if an existing approved asset is ready; do not present unbuilt recruitment or regions as playable content. The complete first session must work without that teaser.

If Hyakki passes the production gate, or when it is built after the jam, its arc should focus on Hina wanting to remain able to change and Tamamo offering permanence as safety. It needs one quiet exchange before the fight and a short release after it. Preserve the line connecting being real to being chosen. End with an actual local resolution and a future invitation; a long teaser for unbuilt lands should not dominate the payoff.

Five novice players understanding the basic rules is an existing release criterion, not a completed result. A useful narrative test asks, without prompting: “Why are you hunted?”, “What does Hina fear?”, “Why does Tamamo oppose you?” and “What did you choose that mattered?” These reveal comprehension more reliably than asking whether the lore is interesting.

## 9. Cutscenes: spend on moments the player has earned

Use three tiers, all driven by authored scene IDs and skippable without losing state changes:

| Tier | Use | Initial budget hypothesis |
|---|---|---|
| In-engine acting and dialogue | Most travel, negotiation, short bonds and responsive scene variants | Short exchanges; every region reuses a small location kit and poses. |
| Layered illustration / motion comic | Memory flashes, dream questions, map reveals and quieter emotional beats | Often 5–20 seconds; pan, focus and restrained effects from locked key art. |
| Bespoke cinematic | One or two milestone reveals per major production phase; selected ultimate showcase | Establish duration in animatics before rendering. The jam can ship with still-motion versions. |

For a full-game first pass, budget roughly 12–18 minutes of authored cinematic sequences across the campaign, excluding interactive dialogue and repeated attack effects. This is a proposal to test, not a promise of finished footage. Longer scenes must earn time through a change in relationship or player objective. The midpoint needs silence and a response from NIL, not another montage explaining the equation twice.

Every shot record should specify actor identity, costume/version, prop side, visible Omen/resonance, camera, action, emotional change, exact duration, subtitle ID, audio cue, skip behavior and reduced-motion substitute. Reuse the same locked reference frames. Put precise text, Omens, cards, bells and number-dependent effects in compositing or Unity so generated footage cannot change game meaning.

Skipping must apply the same recruitment, quest, Seal and bond flags as watching. Pausing/resuming or a failed video must not soft-lock a scene. Give important ending choices a deliberate selection and confirmation; retain the final “stop Hap's wheel” motif as presentation without accidentally assigning a tragic ending from a mistimed tap. Assist, keyboard and reduced-motion options must support that choice.

## 10. AI-only development needs a controlled authoring system

AI can draft the campaign, synthesize assets and implement its state machine, but the repository needs a small canon database and deterministic validators to prevent drift. Recommended offline workflow:

1. Extract canonical entities into versioned data: identity, pronouns, age, appearance locks, resonance, civic Omen rules, recruit point, knowledge tier and source reference.
2. Give each scene a contract: prerequisites, participants, location/time, objective, incoming knowledge, one emotional turn, choices, state effects and word/asset budget.
3. Generate a draft against only the relevant canon subset. Run an independent continuity pass against the whole entity/flag graph, then a voice pass against NARRATIVE_STYLE.
4. Build a cheap animatic with temporary voices and subtitles. Review silhouette, comprehension, pacing and state transitions before spending on final video or animation.
5. Export approved text into localization tables and a dialogue manifest. Keep IDs stable even when wording changes. No runtime service is needed to play the authored campaign.
6. Test every scene's prerequisite and exit state, all skip paths, missable recruit recovery, save/reload boundaries and ending eligibility. Validate that an optional branch cannot strand the main plot.

AI researchers can collect primary sources, compare depictions and record uncertainty. They cannot truthfully mark the empty cultural review log as signed or claim native lived experience. The user's strict AI-development constraint should be documented in the production plan: existing requirements for paid cultural reviewers and disabled-player tests remain unmet unless the production policy is deliberately changed. A practical fully AI-authored direction can reduce dependence on real sacred figures by using invented keepers and eclipse machinery; this would be a canon proposal, not an authenticity certification.

### Proposed narrative data files

The following are recommendations; they were not generated as campaign content in this review:

- `story/characters.json`: stable identities, visual/voice locks, digit and availability.
- `story/facts.json`: `fact_id`, objective/public/believed truth, spoiler tier, first allowable scene, source.
- `story/scenes.json`: scene graph, costs, prerequisites, choices, state effects and fallback variant.
- `story/lines.csv`: the line schema already specified in BOND_ARCS, with fixed IDs and length constraints.
- `story/recruits.json`: all recruit routes, guest transitions, catch-up route and exclusions.
- `story/payoffs.csv`: seed scene, reinforcing clue, reveal scene, consequence and verification status.
- `story/endings.json`: explicit eligibility predicates and readable journal conditions.
- `story/shots.csv`: animatic/asset contracts, references, duration and accessibility substitute.

Validators should check references and state reachability rather than asserting that a story is emotionally good. An AI critique can flag repetition and voice drift; actual player response remains unmeasured until people play.

## 11. Order of work and completion evidence

1. Resolve P0 opening, conservation and Hina lines; choose a single jam scene order.
2. Resolve civic Omen/resonance/Balance terminology with combat design before final UI, scripts or cutscenes.
3. Implement the jam story as a small scene graph with short still-motion scenes and tested skip/resume behavior.
4. Capture one complete playable journey to the rooftop; measure time and comprehension. Build the Hina/Tamamo loop after the jam unless the 9 November gate supports including it.
5. Make one representative full-game chapter outline with prerequisite flags and realistic budgets; validate the recruitment/bond schedule before writing all dialogue.
6. Lock the reveal/payoff ledger and campaign causal bridges; draft and stage one region at a time.
7. Add optional recruits and customization only after their catch-up, kit, animation and save costs are affordable.

Completion evidence: a scene graph with no unreachable required ending condition; all ten lucky-digit choices represented correctly; the Maeve-missed route recoverable; all four Fibi stages available before the finale; skip/watch outcomes identical; no age/prop/Seal contradictions; subtitles and reduced-motion scenes complete; a playtest report distinguishes observed player understanding from design intent.

## 12. Files read

Narrative primary sources: `docs/WORLD_BIBLE.md`, `docs/STORY.md`, `docs/ACT_DESIGN.md`, `docs/CHARACTER_BIBLE.md`, `docs/BOND_ARCS.md`, `docs/LORE_LEXICON.md`, `docs/LOCATIONS.md`, `docs/NARRATIVE_STYLE.md`, `docs/JAM_SCRIPT.md`, `docs/FIRST_10_MINUTES.md`.

Related sources: `README.md`, `docs/GDD.md`, `docs/SYSTEMS.md`, `docs/JAM_SLICE.md`, `docs/BESTIARY.md`, `docs/ECONOMY_PROGRESSION.md`, `docs/PLAYER_EXPERIENCE.md`, `docs/CULTURAL_CONSULTATION.md`, `docs/LOCALISATION.md`, `docs/UX_SPEC.md`, `docs/ACCESSIBILITY.md`.

This report relies on the repository's text as design intent. It does not assert that the PDF derivatives, visual assets, prototype or runtime implement these narrative requirements; those are separate audit surfaces.
