# Canon: what is true, and where it is written

Pre-production phase 1, 9 November 2026. This folder is the single entry point for canon. When two documents disagree, the higher row wins and the lower one gets corrected or marked historical.

## Authority order

| Rank | Source | Owns |
|---|---|---|
| 1 | [Resolved series bible](../docs/novel/RESOLVED_SERIES_BIBLE.md) | Cosmology, the luck rules, adopted story decisions, names |
| 2 | [Scene ledger](../docs/novel/SCENE_LEDGER.md) and [continuity](../docs/novel/PHASE_02_CONTINUITY.md) | What happens in each of the 49 chapters, when, and who holds what |
| 3 | The novel manuscript ([index](../docs/novel/README.md)) | How it happens, voice and detail |
| 4 | **This registry** ([REGISTRY.md](REGISTRY.md), [characters.json](characters.json), [items.json](items.json), [places.json](places.json)) | Who exists, their class and tier, first appearance, design status, game role. Generated from ranks 1–3 and the art catalog |
| 5 | [Character dossiers](../docs/novel/CHARACTER_DOSSIERS.md), [societies](../docs/novel/SOCIETIES_AND_RELATIONSHIPS.md) | Motives, voices, relationships |
| 6 | Art catalog and concept boards (`art/catalog`, `art/concepts/complete`) | Appearance, palette, locks; proposals until phase 4 approves them |
| 7 | Game documents (GDD, SYSTEMS, STORY, ACT_DESIGN, BESTIARY, CHARACTER_BIBLE, jam docs) | **Adaptation proposals.** Rewritten in phase 6 against ranks 1–6 |

Rebuild the registry with `python tools/build_canon_registry.py`; `--check` fails if it is out of date. The build also fails if any name in the scene ledger has no record.

## Classes and tiers

Every character has one **class** (their role in the story) and one **tier** (how much production effort they get). The tier table lives in the [pre-production plan](../docs/PREPRODUCTION_PLAN.md#character-tiers-used-by-phases-1-4-6-7-and-10).

| Class | Game role | Tier |
|---|---|---|
| protagonist | playable | A |
| core companion | recruitable | A |
| final antagonist | final boss | A |
| boss | boss (Varro is A: he is the most-seen antagonist and a later ally) | B |
| recurring hunter | recurring enemy (Collector Captain, the field pursuer the critique asks for) | B |
| secret recruit | optional recruit (game only) | B |
| deity | story presence (Hap) | B |
| keeper | trial giver | C |
| story NPC | NPC (Livia, Nought, Ivo, Mara and Gus are B) | C |
| faction archetype, enemy archetype, background, record only | templates and enemies | D |

Current totals: 11 tier-A identities, 14 tier-B, 26 tier-C and 40 tier-D, plus four Nil outfits.

**Ten records still need a design** (phase 4): Mara Vale, Baker, Wen (as testimony and a work knot, not a portrait), the cart resident, Clotho, Lachesis and Atropos as individuals, Ox-Head and Horse-Face as individuals, and the composite knight.

## Reconciling the game with the novel

| Topic | Novel (canon) | Game documents today | Resolution |
|---|---|---|---|
| Structure | 7 volumes, 49 chapters | Prologue, Acts I–V, finale | Same spine: Prologue = Volume 1 (Meridian), Act I = 2 (Hyakki), II = 3 (River), III = 4 (Śūnyapura), IV = 5 (Kroton Nova), V = 6 (Crossroads), finale = 7 (Basilica) |
| Ending | One ending: Positive-Sum, through witnessed, revocable mandates | Four endings (Balance, Overflow, Positive-Sum, Divide by Zero) | Positive-Sum is canon. Other endings are **open for phase 6/7**: keep as game branches or cut |
| Secret recruits | Kyūsuke and Liu Shun do not appear | Optional recruits | Game-only; keep or cut in phase 6. Varro's recruitment must follow the novel's restitution framing |
| Rahu and Ketu | Chapter 27 stages an operator-built eclipse engine, keeping surveyors' acts separate from revered figures | Act III boss "Rahu & Ketu, the Eclipse" | The game boss follows the novel's staging and needs cultural review |
| Vesper's secret | Rigged hand that harmed Mara Vale, aged nine; she survived; no forgiveness required | Older drafts differ | Novel wins (already corrected in CHARACTER_BIBLE) |
| Names | Chosen name "Nil"; NIL is the decoder's field value | NIL used throughout | Story text: Nil after chapter 4. UI and data IDs may keep `nil` |
| Hap | The cage is revealed only in chapter 45 | Hap's Dreams and Whispers | No early cage imagery in either medium |
| Powers | Carry (ch 11), Rewrite (ch 19), Deal (ch 36), with Place Value and Factor still to place | Several verbs from GDD §6 | Phase 6 maps the game's growth onto the novel's order |
| Jam build | — | Uses older jam-script lines (for example "Ama Okoro") | Historical jam track; not canon and not a phase 10 input |

## Superseded material

These remain in the repository as dated history and must not be used as current sources: the 22-chapter manga plan and its PDFs (`docs/manga/README_22_CHAPTER_HISTORICAL.md`, `output/production/OMEN_Mangaka_22_Chapter_Manuscript.pdf`), the colour manga study in `art/manga/chapter_01`, the older art books under `docs/` (historical snapshots), the jam-scope sections of GDD and PRODUCTION_PLAN, and the [refinement review of 6 November](../docs/refinement/README.md). Each already carries a historical banner or is listed here.

## Repository rules

- Text files under `docs/`, `tools/`, `canon/`, `tests/` and the compiled `output/` Markdown and JSON use LF line endings everywhere (`.gitattributes`), so byte-exact build checks pass on any OS.
- Large art goes through Git LFS: manga page images, concept boards, renders, `.blend` sources and print PDFs (see `.gitattributes`). The existing art backlog of about 2.4 GB has **not** been uploaded yet, because LFS storage and bandwidth count against the GitHub account's quota.
