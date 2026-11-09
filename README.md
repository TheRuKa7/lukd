# ZERO-SUM: OMEN

Originally conceived for the Official Unity Game Jam 2026 theme, Lucky Number. The current project follows a story-first production order.

In a world where every soul's luck floats above its head as a number, a nameless wanderer with no number at all tells the city its lucky number, and becomes the most wanted person alive. An anime 2.5D party RPG through lands inspired by Japanese, Chinese, Indian, Greek and American myth and folklore, where every number spins and you **tap to stop it**, and where the god of luck, **Hap**, waits in a cage at the heart of the capital.

**Current priority:** complete and revise *The Remainder*, a125,000-word prose master, then adapt49 chapters into seven manga volumes (1,078 story pages). Existing prose chapters are drafts. Unity implementation follows the story and manga gates; no Unity game build has been verified. The old jam timetable is historical.

Start with the [pre-production plan](docs/PREPRODUCTION_PLAN.md) and the [9 November critique](docs/CRITIQUE_2026-11-09.md), then the earlier [ten-phase plan](docs/TEN_PHASE_PLAN.md), [resolved series bible](docs/novel/RESOLVED_SERIES_BIBLE.md), [current manga policy](docs/manga/README.md) and [project evidence](docs/PROJECT_STATUS.md).

## Start here
| | |
|---|---|
| [Concept collection](output/pdf/ZERO-SUM_OMEN_Concept_Collection.pdf) |94 pages:84 existing cast/outfit/encounter boards and7 regional boards, with scope, current-story guidance and provenance. |
| [Complete world and artbook](output/pdf/ZERO-SUM_OMEN_Complete_Artbook.pdf) | Historical full-reference snapshot:91 detailed cast/environment boards,91 indexed cast records,84 distinct actual four-view sets and seven regions. Design proposals and first-draft3D evidence remain distinct. Build with `python tools/build_full_artbook.py` |
| [World and design bible](output/pdf/ZERO-SUM_OMEN_World_and_Design_Bible.pdf) | Historical design compilation; Markdown remains authoritative. Build with `python tools/build_bible.py` |
| [Mangaka series production manuscript](output/production/OMEN_Mangaka_22_Chapter_Manuscript.pdf) |Superseded32-document-page manuscript planning22 B&W chapters x30 story pages;90 numbered opening instructions and114 later five-page blocks. This is not a completed660-page comic. [Current production policy](docs/manga/README.md) |
| [Mangaka input diagnosis](docs/manga/MANGAKA_RECOVERY.md) | Actual stopped-analysis evidence and preserved input hashes. [Clean Chapter01 input](output/production/OMEN_Chapter_01_Story_Only_v2.pdf) and [lean22-chapter story digest](output/production/OMEN_22_Chapter_Story_Digest.pdf) separate native story input from the long editorial reference. |
| [`docs/PREPRODUCTION_DOCS.md`](docs/PREPRODUCTION_DOCS.md) | Which docs exist, what each must answer, and what is still to verify in production |
| [`prototype/index.html`](prototype/index.html) | Browser combat sandbox, not the Unity jam campaign: tap/Space to stop; choose a hero by pointer or number |

The older135-page artbook and158-page bible under `docs/` are retained historical presentations from upstream commit4856ec5. The earlier20-page colour manga is a user-rejected study. Native Mangaka analysis, production and export must have separate evidence; completed ordinary image jobs do not establish an accepted comic.

## World and story
| Doc | What's in it |
|---|---|
| [`WORLD_BIBLE.md`](docs/WORLD_BIBLE.md) | The world, **Hap the god of luck** (§2A), why numbers matter, luck and superstition by region, history, the villain, the lands, the cast, endings, cultural care |
| [`STORY.md`](docs/STORY.md) | The whole campaign scene by scene: Prologue, five acts, Hap's Dreams, finale, four endings, post-game |
| [`ACT_DESIGN.md`](docs/ACT_DESIGN.md) | Every land: its story, Land Law, act map, encounters, keeper trial, boss, side quests, Hap's Whispers |
| [`BESTIARY.md`](docs/BESTIARY.md) | Every enemy, elite, keeper and boss: wheels, rules, phases, telegraphs, ultimates |
| [`CHARACTER_BIBLE.md`](docs/CHARACTER_BIBLE.md) | Every character's look, voice, arc and canon locks; eight core and three secret companions; Hap's depiction rules |
| [`BOND_ARCS.md`](docs/BOND_ARCS.md) | 4-scene bond arcs for 11 companions, Hap's Dreams, the dialogue database format |
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
| [`ART_DIRECTION.md`](docs/ART_DIRECTION.md) | "Painted world, inked people"; colour scripts; QC; prompt grammar; the four eras of luck |
| [`ARTBOOK_PRODUCTION.md`](docs/ARTBOOK_PRODUCTION.md) | AI-only asset production, reproducible source scenes, correction/export gates and book layout |
| [`ASSET_LIST.md`](docs/ASSET_LIST.md) | Every jam asset with specs, owners and due days |
| [`art/graphics/`](art/graphics/) · [`art/base3d/`](art/base3d/) | Vector identity kit and design figures; 3D bases and colour keys |
| [`art/HIGGSFIELD_PROMPTS.md`](art/HIGGSFIELD_PROMPTS.md) | Prompt pack |

## Production
| Doc | What's in it |
|---|---|
| [`PRODUCTION_PLAN.md`](docs/PRODUCTION_PLAN.md) | Phases, day-by-day jam plan, pipeline, risks |
| [`JAM_SLICE.md`](docs/JAM_SLICE.md) | Current Prologue-only jam scope, exact required beats, charm contracts and extension gate |
| [`JAM_SCRIPT.md`](docs/JAM_SCRIPT.md) | Every line in the slice, with boards |
| [`AUDIO.md`](docs/AUDIO.md) | Music per land, SFX vocabulary, mix rules |
| [`TECH_DESIGN.md`](docs/TECH_DESIGN.md) | Architecture, data, determinism, WebGL budgets, build, save |
| [`PLAYTEST.md`](docs/PLAYTEST.md) · [`QUALITY_BAR.md`](docs/QUALITY_BAR.md) · [`QA_TEST_PLAN.md`](docs/QA_TEST_PLAN.md) | How we find the fun, define done, and ship clean |
| [`CULTURAL_CONSULTATION.md`](docs/CULTURAL_CONSULTATION.md) · [`LOCALISATION.md`](docs/LOCALISATION.md) · [`ACCESSIBILITY.md`](docs/ACCESSIBILITY.md) | Care for every player and culture |
| [`TELEMETRY.md`](docs/TELEMETRY.md) · [`MARKET_POSITIONING.md`](docs/MARKET_POSITIONING.md) · [`MARKETING_PLAN.md`](docs/MARKETING_PLAN.md) | After the jam |
| [`LEGAL_IP_AI.md`](docs/LEGAL_IP_AI.md) · [`AI_DISCLOSURE.md`](docs/AI_DISCLOSURE.md) · [`TEAM_HANDBOOK.md`](docs/TEAM_HANDBOOK.md) | Rules, disclosure, how we work |

## Audit and validation

- [Current audit and remaining production gates](docs/DOC_AUDIT.md)
- [Architecture and requirements traceability](docs/architecture/traceability.md)
- [Historical refinement review, 6 November](docs/refinement/README.md)

Run the documentation and reference-rule checks listed in the audit before accepting cross-document changes. PDF builds must record their date/source fingerprint; concept art is not an accepted runtime rig or gameplay screenshot.
