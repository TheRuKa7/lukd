# ZERO-SUM: OMEN

Entry for the [Official Unity Game Jam 2026](https://itch.io/jam/official-unity-game-jam-2026). Theme: **Lucky Number**.

In a world where every soul's luck floats above its head as a number, a nameless wanderer with no number at all tells the city its lucky number, and becomes the most wanted person alive. An anime 2.5D party RPG through lands inspired by Japanese, Chinese, Indian, Greek and American myth and folklore, where every number spins and you **tap to stop it**, and where the god of luck, **Hap**, waits in a cage at the heart of the capital.

Hard deadline: **Sat 14 Nov 2026, 12:00 UTC.** A WebGL build is required.

## Start here
| | |
|---|---|
| [`docs/ZERO-SUM_OMEN_World_and_Art_Bible.pdf`](docs/ZERO-SUM_OMEN_World_and_Art_Bible.pdf) | **Everything in one designed PDF.** Rebuild with `python3 tools/build_bible.py` |
| [`docs/ZERO-SUM_OMEN_Artbook_Draft.pdf`](docs/ZERO-SUM_OMEN_Artbook_Draft.pdf) | **Art book v1.0** (~130 pages): fixed art spec; the world (Hap, logic of luck, schools of power, history, politics, jobs, stores, 11 faction style pages); every land as a 3D blockout from above, in 2.5D and from the battle camera; all 56 character models front/left/right/back. Rebuild with `python3 tools/build_artbook.py` |
| [`docs/PREPRODUCTION_DOCS.md`](docs/PREPRODUCTION_DOCS.md) | Which docs exist, what each must answer, and what is still to verify in production |
| [`prototype/index.html`](prototype/index.html) | Browser prototype of the core verb: tap/Space to stop a number; tap a hero or press 1/2/3 |

## World and story
| Doc | What's in it |
|---|---|
| [`WORLD_BIBLE.md`](docs/WORLD_BIBLE.md) | The world, **Hap the god of luck** (§2A), why numbers matter, luck and superstition by region, history, the villain, the lands, the cast, endings, cultural care |
| [`STORY.md`](docs/STORY.md) | The whole campaign scene by scene: Prologue, five acts, Hap's Dreams, finale, four endings, post-game |
| [`ACT_DESIGN.md`](docs/ACT_DESIGN.md) | Every land: its story, Land Law, act map, encounters, keeper trial, boss, side quests, Hap's Whispers |
| [`BESTIARY.md`](docs/BESTIARY.md) | Every enemy, elite, keeper and boss: wheels, rules, phases, telegraphs, ultimates |
| [`CHARACTER_BIBLE.md`](docs/CHARACTER_BIBLE.md) | Every character's look, voice, arc and canon locks; secret recruits; side characters by region; Hap's depiction rules |
| [`BOND_ARCS.md`](docs/BOND_ARCS.md) | 4-scene bond arcs for 11 companions, Hap's Dreams, the dialogue database format |
| [`WORLD_ENCYCLOPEDIA.md`](docs/WORLD_ENCYCLOPEDIA.md) | How the world works: the logic of luck, the six schools of power and how people use them, factions and their styles, jobs, money, law, transport, stores, politics, full timeline |
| [`LORE_LEXICON.md`](docs/LORE_LEXICON.md) | Glossary, idioms, timeline, factions, world rules, naming |
| [`LOCATIONS.md`](docs/LOCATIONS.md) | One page per land: districts, locations, little things, sound |
| [`NARRATIVE_STYLE.md`](docs/NARRATIVE_STYLE.md) | Tone, voice, formatting, UI copy |

## Gameplay
| Doc | What's in it |
|---|---|
| [`GDD.md`](docs/GDD.md) | Combat, scoring, party and synergy, build systems, acts and bosses, complexity ladder, NIL's growth, jam scope |
| [`SYSTEMS.md`](docs/SYSTEMS.md) | Luck mechanics (Pattern Sight, Hap's Favour, Land Laws, curses, Whispers), fantasy mechanics, every kit and ultimate, Awakenings, Link Arts, 63 charms, interaction matrix |
| [`TUNING.md`](docs/TUNING.md) + [`tuning/jam_tuning.csv`](tuning/jam_tuning.csv) | Jam numbers and targets, backed by `tools/sim_patterns.py` |
| [`ECONOMY_PROGRESSION.md`](docs/ECONOMY_PROGRESSION.md) | Full-game Balance curve, fen economy, progression layers, unlock cadence |
| [`GAME_FEEL.md`](docs/GAME_FEEL.md) | The tap frame by frame; the payoff ladder; speed rules |
| [`FIRST_10_MINUTES.md`](docs/FIRST_10_MINUTES.md) | Second-by-second opening and teaching rules |
| [`UX_SPEC.md`](docs/UX_SPEC.md) | Every menu and screen as an in-world object; combat layout; settings |
| [`PLAYER_EXPERIENCE.md`](docs/PLAYER_EXPERIENCE.md) | The loops, why it's moreish (and the lines we don't cross), the emotional arc |

## Art
| Doc | What's in it |
|---|---|
| [`ART_SPEC.md`](docs/ART_SPEC.md) | **Fixed art spec**: scale, proportions, turnaround standard, line/shading/colour numbers, faction costume keys, cameras, battle stage, light per land, 3D pipeline, QC |
| [`ART_DIRECTION.md`](docs/ART_DIRECTION.md) | "Painted world, inked people"; colour scripts; QC; prompt grammar; the four eras of luck |
| [`ARTBOOK_PRODUCTION.md`](docs/ARTBOOK_PRODUCTION.md) | How to reach art-book quality: the 3D base → paint → overpaint pipeline, spread list, first 12 images |
| [`ASSET_LIST.md`](docs/ASSET_LIST.md) | Every jam asset with specs, owners and due days |
| [`art/cast/`](art/cast/) · [`art/envs/`](art/envs/) | **3D blockouts**: 56 character models (front/left/right/back renders + `zso_cast_blockout.blend`, from `tools/cast.py` via `tools/render_cast.py`) and 7 lands (top/2.5D/front renders + `zso_envs_blockout.blend`, `tools/build_envs.py`). Needs `pip install bpy==5.2.3` |
| [`art/graphics/`](art/graphics/) · [`art/base3d/`](art/base3d/) | Vector identity kit and design figures; 3D bases and colour keys |
| [`art/HIGGSFIELD_PROMPTS.md`](art/HIGGSFIELD_PROMPTS.md) | Prompt pack |

## Production
| Doc | What's in it |
|---|---|
| [`PRODUCTION_PLAN.md`](docs/PRODUCTION_PLAN.md) | Phases, day-by-day jam plan, pipeline, risks |
| [`JAM_SLICE.md`](docs/JAM_SLICE.md) | The locked slice with must/should/could and cut dates |
| [`JAM_SCRIPT.md`](docs/JAM_SCRIPT.md) | Every line in the slice, with boards |
| [`AUDIO.md`](docs/AUDIO.md) | Music per land, SFX vocabulary, mix rules |
| [`TECH_DESIGN.md`](docs/TECH_DESIGN.md) | Architecture, data, determinism, WebGL budgets, build, save |
| [`PLAYTEST.md`](docs/PLAYTEST.md) · [`QUALITY_BAR.md`](docs/QUALITY_BAR.md) · [`QA_TEST_PLAN.md`](docs/QA_TEST_PLAN.md) | How we find the fun, define done, and ship clean |
| [`CULTURAL_CONSULTATION.md`](docs/CULTURAL_CONSULTATION.md) · [`LOCALISATION.md`](docs/LOCALISATION.md) · [`ACCESSIBILITY.md`](docs/ACCESSIBILITY.md) | Care for every player and culture |
| [`TELEMETRY.md`](docs/TELEMETRY.md) · [`MARKET_POSITIONING.md`](docs/MARKET_POSITIONING.md) · [`MARKETING_PLAN.md`](docs/MARKETING_PLAN.md) | After the jam |
| [`LEGAL_IP_AI.md`](docs/LEGAL_IP_AI.md) · [`AI_DISCLOSURE.md`](docs/AI_DISCLOSURE.md) · [`TEAM_HANDBOOK.md`](docs/TEAM_HANDBOOK.md) | Rules, disclosure, how we work |
