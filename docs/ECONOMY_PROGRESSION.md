# ZERO-SUM: OMEN — Economy and Progression

Updated 7 November 2026 IST. [DECISIONS.md](DECISIONS.md) D 06 is adopted policy. Full-game numbers below are **hypotheses**, not a validated economy. Jam has one free charm choice, no fen/shop/crafting/act reset.

## 1. Persistent and transient layers

| Layer | Progression | Carryover |
|---|---|---|
|Party level |Shared XP, +10 fixed strike base/level, cap 30 |Permanent; level 2 at jam Varro |
|Roster |Eight core+three secret companions+NIL |Unlock journal; required recruits get catch-up route |
|NIL verbs/tree |Story milestones/memory IDs |Permanent; each ability separately gated |
|Narrative bonds |Four authored stages/companion |Permanent stage flags; not mathematical resonance bonds |
|Awakening |Act IV branch, respec at shrines |Chosen branch saved |
|Wheel modifications |Validated face removals/enhancements |Keep across acts |
|Gem levels |Authored pattern upgrades |Keep across acts |
|Party charms |Owned IDs; slots 3→6 |Select 3 active at act transition, stash all other owned charms; later camps may re-equip to unlocked slots |
|Personal gear |One authored item/hero |Separate from party slots and set counts |
|Fen |Node rewards and bounded interest |floor (fen/2) per act |
|Karma |Defence/Zero-Sum resource after unlock |floor (0.75×Karma) per act |

Choosing ferry keeps is an equipment choice, not permanent deletion. No gem/face reset is implied by shorthand “mini-run.” Endless mode is a separate future mode with explicit per-run reset and no campaign save mutation.

## 2. Power curve and validation requirements

| Segment |Small/Big/Boss Balance |Expected level |
|---|---|---|
|Prologue |300/500/1200 |1–2 |
|Hyakki |1500/2500/6000 |3–4 |
|River |8000/14000/35000 |6–8 |
|Śūnyapura |50000/90000/200000 |10–12 |
|Kroton |300000/600000/1500000 |14–17 |
|Crossroads |2500000/5000000/12000000 |19–22 |
|Finale |99,999,999 totalphasepool hypothesis |24–26 |

At level 25, three bases near 250 do not by themselves prove that Mult 3000 defeats a 99,999,999 pool in ten rounds:750×3000≈2.25 million/round before mechanics. A full fight/phase model is required. No “synergy build must pass, plain build must fail” result is claimed. Test legal parties including NIL, all chosen digits, ordinary/strong/poor offers, actual passives, defence and encounter retry. Treat Hina/wilds/extra turns, permanent face changes and next-round boosts as priority outliers.

## 3. Future fen budget

Candidate first-act rewards: Small 8, Big 15, Elite 25, Boss 40. Prices: common 6, rare 12, legendary 25; remove 5, duplicate 8, enhance 8, gem 10, stick 4; reroll 3+reroll index. Gate F-ECON must fix node availability, payout order and per-node limits before activation. Candidate interest=floor (held Fen/5), cap 5, once after a rewarded combat node; upgrades may change explicit caps but never pay on UI reopen, retry or wall-clock ticks.

The old 45 fen “rare OR two enhancements” example was false:12+8+8=28. Do not imply scarcity from it. Example budget trace at 20 fen: rare 12 leaves 8, two enhancements 16 leaves 4, both cost 28 and are unavailable together. This is illustrative arithmetic, not a measured route. Before enabling markets, enumerate every guaranteed/optional faucet and sink in the act and expose the opportunity cost of the actual offer.

Inflation candidate is×1.5 per later act for reward and base-price schedules, floor once per transaction. Keep price/reward tables explicit to avoid ambiguous “+50%per act” compounding. Market reroll price resets only on a new market ID; offers/deductions are transactional. Gold-face and charm income cannot retrigger their own source. Wagers require visible stakes and a safe decline; no real-money gambling or purchases are required.

## 4. Save, defeat and idempotence

Campaign defeat restores **complete act-start gameplay snapshot**: active/equipped/owned/stashed items, face modifications, gems, fen, Karma, levels/XP, tree spending, active party and RNG state. Permanent narrative/unlock journal evidence is reconciled idempotently by unique event/reward IDs. A story unlock may remain known without paying the same memory/XP/fen reward twice. Reconciliation must define each retained event's gameplay consequence; no generic “keep all rewards” exception.

A snapshot is versioned, immutable and checksummed. Retry does not regenerate offers, earn repeated entry rewards or duplicate recruits. Provide a safe restart/catch-up route after migration failure. Jam instead restores its encounter checkpoint, selected charm and full stake; no act boundary economy exists.

## 5. Difficulty and accessibility

Jam assist baseline slows wheels×0.7; any enemy-Balance reduction must be separately specified, visible and tested before being offered. Full-game Story Mode may reduce enemy stake and retry a round without loss, but uses a distinct save/mode flag; it cannot corrupt normal-mode achievements. Future Omen Levels 1–8 require explicit per-level data and testing. Removing Hap's Hand at a top challenge tier is opt-in challenge design, not an accessible default.

## 6. Unlock cadence and campaign time

Critical path 315 minutes:35/45/50/50/45/50/40 by segment. Optional content 45–105 minutes gives 6–7 hours as a hypothesis. Jam 10–15 minutes is separate. Measure learn/test/combine beats, rest scenes and optional-character interruptions; do not promise a universal new mechanic every 15 minutes. Each new companion/region must prove its F-KIT/content/save gates before another is mass-produced.

## 7. Balance-check findings and gates

Health: **CONCERNS — specified curve without fight/economy validation**. Corrected defects: invalid affordability example, unclear act resets, illegal non-NIL comps and duplicated baseline upgrades. Remaining production evidence: XP/reward node table, full fight simulator, legal-party win/round distributions, market budget trace, player difficulty and carryover UX. No parameter is declared balanced from a pattern-only Monte Carlo model. Current reproducible checks are TUNING §4 and tests/; no full-game balance certificate exists.
