# ZERO-SUM: OMEN — Comparative design research

**Research date: 6 November 2026.** Sources below are official developer/publisher pages. These are documented feature comparisons, not hands-on playtest findings. Proposed applications and experiments are our inferences. No recommendation assumes that a reference game's scope or production budget is reproducible with AI alone.

## 1. Reference matrix

| Reference and verified feature | Useful principle for OMEN | Concrete experiment | What to avoid importing |
|---|---|---|---|
| **Balatro:** poker-hand scoring, restricted boss rounds, ordered build choices through Jokers | Make build logic readable and each boss disrupt a clear habit | Use three charms: reliable base, pattern-dependent gain, risky multiplier; ask the player to predict which helps against Varro | Copying card/Joker presentation or adding dozens of items before the first choices work |
| **Clair Obscur: Expedition 33:** reactive turn-based attacks/defence, character builds, boss-specific counters | Preparation and execution can both matter; reactive systems need readable feedback | Show the next enemy rule before choosing strike order; test predictable safe defence against a smaller Fortune opportunity | Matching its numbered-world/death premise or assuming parry depth can substitute for varied strategy |
| **Sea of Stars:** timed hits, multi-character combos and damage-type locks | A tiny input vocabulary can support meaningful enemy interruption and teamwork | One Varro turn offers a visible trade-off between pattern damage and jar recovery | Adding traversal/co-op because the reference has them |
| **Octopath Traveler II:** eight protagonists with distinct motives, 2D/3D visual composition, Path Actions and Break/Boost | Characters should affect interactions beyond battle; the image needs deliberate depth | Let Vesper and Hina change one authored event differently; test a fixed-camera layered stage in motion | Pixel art/HD-2D imitation when OMEN already chooses inked anime characters |
| **Hades:** repeated attempts reveal story, permanent progression and returning character interactions | Remembering the player's history makes repetition part of the story | After a Varro loss, use one changed Vesper line and keep the tutorial skipped; test whether the response feels relevant | Thousands of reactive lines or full voiceover before a flag/event scheduler works |
| **Eiyuden Chronicle: Hundred Heroes:** recruitable characters with stories, a growing hub, party combos | Recruitment should visibly change the journey and enable relationships | A recruit adds a party decision, a camp scene and one return interaction; measure content burden | A hundred-person roster or mandatory obscure recruit checks |
| **Into the Breach:** enemy attacks are telegraphed | Transparency enables strategy even under severe constraints | Give Varro's next jar action a clear preview and ask players to plan their third strike | Removing all uncertainty from a game whose fantasy is shaping luck |

Sources: [Balatro official FAQ](https://www.playbalatro.com/faq), [Expedition 33 gameplay breakdown](https://www.expedition33.com/post/your-first-look-at-gameplay-from-clair-obscur-expedition-33), [Sea of Stars official site](https://seaofstarsgame.co/), [Octopath Traveler II publisher store](https://eu.store.square-enix-games.com/octopath-traveler-ii), [Hades developer FAQ](https://www.supergiantgames.com/blog/hades-faq/), [Eiyuden publisher launch overview](https://505games.com/?p=66804), [Into the Breach developer overview](https://www.subsetgames.com/itb.html). The last page's indexed official description was available; a direct fetch returned 403 during this review.

## 2. Distinctive position

The most defensible pitch uses features already central to OMEN: **a numberless outsider, visible luck as social power, timing to shape a reel, and companion relationships expressed through number theory**. The game should distinguish itself through the personal lucky-digit choice, an economy of luck/debt, and releasing Hap through shared agency.

Expedition 33 is particularly important as a comparison because its official premise also combines a number-driven world, threatened lives, an authored party and reactive turn-based combat. This is a design-positioning observation, not a finding of copying. Avoid marketing OMEN mainly as “an RPG where numbers decide who dies.” Show the Audit, Favour, relationships and lucky-number choice in the first minute. [Expedition 33 official overview](https://www.expedition33.com/overview)

## 3. Art direction experiments

Keep OMEN's current art bible as the direction. References should answer narrow craft questions rather than become prompt shortcuts.

1. **Stage composition:** render the same Meridian encounter with a flat painted backdrop, three depth planes, and a full 3D blockout. Compare readability, camera motion, generation consistency, download and iteration cost. Choose the cheapest composition that satisfies the shot.
2. **Character treatment:** compare current glossy concepts against a controlled two-tone ink treatment at actual gameplay size, under the same lighting and effects. Lock one treatment before generating poses.
3. **Regional variation:** vary materials, motifs, palette and architecture while preserving lens, actor proportions, line behavior, shading, UI grammar and typography. The party should remain visually unified when characters cross regions.
4. **Impact rather than duration:** compare a 0.5s in-engine payoff, a 1.5s cut-in and a 4s film across ten repeated triggers. Measure waiting and information loss, not just which first viewing looks expensive.
5. **Character identity:** inspect turnaround/pose/video consistency on signature props, costume asymmetry and silhouette. Automated image similarity cannot alone certify the correct number of chambers, tails or lanterns.

These are proposed controlled comparisons, not completed studies.

## 4. Gameplay and story experiments before scale

| Question | Test | Useful evidence |
|---|---|---|
| Does the stop feel like agency? | Same encounter with honest face timing, Pattern Sight, then Favour; compare per input level | Player can name the target, perceive the accepted digit and explain a changed outcome |
| Are all lucky numbers viable early? | Same seed family, legal wheels and policy for each digit at each recruitment checkpoint | Win/round/Overwrite distributions, no unavailable-counter lock |
| Do companions change thinking? | First test NIL alone, then NIL/Vesper with one explained relationship | Player changes order or build for an articulated reason |
| Does the first reveal create interest? | Interactive Rain Alley versus current long opening | Time to first action, quits, recall of Ama/NIL and desire to continue |
| Does a quiet beat help? | Boss defeat into immediate teaser versus a short rooftop exchange first | Recall of the relationship and anticipation of the next place |
| Are setbacks tolerable? | Act restart versus encounter retry under story assist | Time lost, abandon/retry choice and perceived fairness |

Use small, fresh-player sessions to find obvious confusion; do not describe five testers as statistically proving market demand. Automated agents can exercise paths and gather timing, but their responses are not substitutes for player preference.

## 5. Research boundaries

This review researched official descriptions and current tool documentation. It did not watch and annotate every game's campaign, perform user research, verify a final release price, select paid subscriptions, or determine trademark/copyright clearance. More research is useful when it resolves a production decision. It should not delay the first Unity Web build.

Tool-specific primary sources and availability limits are recorded in [ART_AND_AI_PIPELINE.md](ART_AND_AI_PIPELINE.md); Unity technical sources are recorded in [ENGINEERING_AND_GAMEPLAY.md](ENGINEERING_AND_GAMEPLAY.md).
