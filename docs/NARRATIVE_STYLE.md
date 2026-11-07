# ZERO-SUM: OMEN — Narrative Style Guide

How the game sounds. Use it for dialogue, item text, UI copy and marketing.

Updated 7 November 2026 under [DECISIONS.md](DECISIONS.md). Specified editorial contract. JAM_SCRIPT is the exact required jam copy; STORY/BOND_ARCS contain future campaign scene contracts, not completed localization rows. AI authors drafts and revisions; the user directs choices. Actual review/test evidence is recorded separately.

## 1. Tone
- **Warm noir.** The world is unfair and the jokes are dry, but people are kind to each other. Think rainy city detective story told by someone who still believes in strangers.
- **Wonder before cynicism.** Every land should feel like a place you'd want to visit, even when it's in danger.
- **Stakes are personal.** Big ideas (fate, luck, conservation) always land through one person's number.
- **Age rating target:** Teen. Peril, death off-screen ("settling"), no gore, no sexual content, mild language.

## 2. Voice rules
1. **Short lines.** Most dialogue lines are under 15 words. Cut adjectives first.
2. **One number habit per character** (Character Bible §12). Don't overuse it: once per scene at most.
3. **Dialogue sounds like speech; rules stay precise.** In conversation say “your number's rising”; in item/UI rules say “50% wider” when it changes a decision. Never hide a mechanical cost behind vague flavour.
4. **NIL speaks least.** Their silences are written in, as beats.
5. **No exposition dumps.** Lore arrives through objects, jokes and choices, three sentences at most at a time.
6. **Villains get the best arguments.** Thale's lines should make players hesitate.
7. **Cultures are lived, not explained.** Characters mention their customs casually and never stop to define them for the player; the Codex does that.

## 3. Formatting
- Speaker names in caps in scripts: `VESPER:`
- Omens written as two digits: "Omen 07".
- Label Civic Omen and Audit Omen distinctly in stage directions/data. Resonance is a digit 0–9. NIL's NaN remains visible alongside combat readouts; resonance 0 is never equated with healthy Civic 00.
- Lore terms capitalised per the Lexicon (the Basilica, the Ledger, the Rounding).
- Non-English terms in italics on first use in the Codex only, never in dialogue.

## 4. Sample scene (intro, after the Naming Rite)
> *The terminal sparks. Every tube on the wall flips to orange.*
> **BROTHER NOUGHT:** The machine knows you're missing.
> **NIL:** I thought it didn't know me.
> *Outside, every screen in the city reads REMAINDER DETECTED.*
> **BROTHER NOUGHT:** It does now. Run.

This is campaign voice reference only; use JAM_SCRIPT's fixed shorter Naming lines in the jam. The player chose a valid digit; the error is an unregistered account, not the fiction declaring 0–9 “not a number.”

## 4A. Humour (v3: witty, never winking)
The world is unfair and the stakes are real; the jokes are how the characters survive it. Inspired by the deadpan deflation of *One Punch Man* and the banter of heist films, never by meta-jokes.

**Joke engines (use these, in this order of frequency):**
1. **NIL's deadpan precision** against everyone else's drama. *VARRO: "Final notice!" / NIL: "You've said that three times. It's not final."*
2. **Number habits colliding** (Character Bible §12): Jinling prices a rescue at 8% compounding; Prima counts primes mid-panic; Maeve insists the third attempt will work (it's the fourth).
3. **Bureaucracy of fate:** the Basilica is a cosmic DMV. Forms, stamps, queue numbers, "please hold while your luck is processed."
4. **Running gags** that pay off: Gus's "credit" (finally called in, in Act V); Niko's missing goat (found in the Moirai's cave); Maeve's one-hat disguise (works every time, to everyone's horror); Kyūsuke's cucumber stock (sold out at the finale).
5. **Understatement after spectacle:** the bigger the Jackpot, the smaller the line after it. *(777 detonates; the screen settles.) NIL: "…Huh."*

**Rules:**
- **Big beat, then the joke.** Never undercut a reveal, a death, a keeper, or Hap's dreams.
- **Characters are funny to each other**, not to the audience. Nobody breaks the fourth wall.
- **Punch up.** Jokes target power (the Basilica, the House, the rich 99s), never the poor, the Settled, or a culture.
- **One gag per fight round, max**; barks stay under 8 words.
- **Every comic character has one moment played completely straight** (Maeve's grandmother's charms; Fibi's 1,597th dawn).

## 4B. Fight dialogue
- **Pre-fight (Versus card):** one line each, trash talk with character. *VESPER: "Seven chambers, Varro. You've got one face." / VARRO: "And one bounty."*
- **Mid-fight barks** react to *what just happened on the reel* (a Bust, a Pair, a Jackpot, a parry). 3–5 per hero per category; never repeat the same bark twice in a row.
- **Phase changes:** the boss gets the best line in the fight, and it reveals their motive (Villains get the best arguments, §2.6).
- **Finishers:** short and personal. Never a pun on death.
- **After the fight:** a breath. One quiet exchange, or one gag, then move on.

## 5. UI and item copy
- Item names are concrete and short: "Beckoning Cat", "Door God", "Rabbit's Foot".
- Item text = rule, then flavour in one line: "+1 fen per strike ending in your digit. *It waves twice for regulars.*"
- Pattern banners in caps: JACKPOT, OMEN OVERWRITE, ZERO-SUM.
- Errors and confirmations speak plainly: "Not enough fen." / "Charm equipped."

## 6. Cultural care in writing
- AI source-check names, scripts and customs against primary regional material; record uncertainties and avoid claims of native expertise. External review is named only if it actually occurred. No required human writing/finishing step is implied; remove or fictionalize unsupported sensitive imagery.
- Keepers speak with dignity; no comic relief at their expense.
- No accents rendered phonetically in text.

## 7. Continuity and delivery checks

- Attribute public doctrine and Thale's beliefs as beliefs. He inherited the Basilica and developed Fixed Fate; he did not build the cage three centuries before his birth. Default objectively means extinguished chance, while returning Noise is the public prediction.
- Hina remains 99 until the true-ending epilogue one year later; BaiSi keeps four physical lanterns; Vesper has seven chambers and left braid; NIL decoder is right-wrist. Preserve names/pronouns/identity under cosmetic variants.
- The Act III enemy names label invented Basilica machines, not revered Rahu/Ketu as enemy avatars. Keeper completion is a satisfied trial, not killing a god. Named Audit defeats leave people alive where their aftermath needs them.
- Each scene specifies its participant/knowledge prerequisites, emotional change, choice and atomic outcome. Main-path clues support required reveals; optional lore enriches interpretation. A later line cannot assume a skipped optional recruit scene.
- Maximum 90 characters per subtitle row is the initial import limit, measured on final localized text; wrap into two lines at actual display width. Split a longer authored speech into multiple stable IDs. A validator and visual check are required production work, not checks already passed.
- Skip is available from first view and commits the same result; pause at choices. Endings are selected deliberately with consequences/confirmation/cancel, never assigned by a mistimed final tap. Required core bond stages and pieces remain recoverable before commitment.
- Exact system math comes from SYSTEMS; do not restate outdated film prompts as runtime rules. UI uses “fen,” not an unexplained second currency. Jam humour creates a story debt, not a new loan subsystem.
