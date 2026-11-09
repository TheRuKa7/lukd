# Current manga edition and source hierarchy

> **Superseded on 8 November 2026:** The user has changed the edition to seven volumes of seven chapters, with 22 story pages per chapter (1,078 total), and requires the full prose novel before volume-by-volume manga generation. See [SEVEN_VOLUME_NOVEL_PLAN](SEVEN_VOLUME_NOVEL_PLAN.md). The 22-chapter material and machine-readable contract below are retained as historical draft evidence; they are not the current production target. The complete novel and its revised continuity ledger still need to be written and reviewed.

Updated8November2026 under the user’s revised request. **The accepted production route is Mangaka-native black-and-white manga:22 chapters,30 story pages each,660 story pages.** The prior20-page colour-image adaptation is user-rejected study material. Completed ordinary image jobs, a local reader or an exported study PDF do not make those pages the accepted comic.

## Current edition and evidence

The production manuscript is prepared as [a PDF](../../output/production/OMEN_Mangaka_22_Chapter_Manuscript.pdf). Its32 document pages contain a production brief,90 numbered opening-page instructions,114 later five-page blocks and the reveal ledger. **Those32 manuscript pages are not comic pages.** They do not establish that Mangaka has produced or exported any chapter. Native chapter generation, export counts, visual acceptance and game integration require their own actual evidence.

The target is English left-to-right B&W story pages. Covers, backs, selected colour inserts and supplementary lore are separate exports outside660 story pages. Ordinary image generation may produce those separately indexed colour supplements; it must not generate the story pages, grey-convert the rejected studies or substitute a generic image batch for Mangaka.

## Authority and reading order

1. The user’s latest instruction and [MANGAKA_WORKFLOW](MANGAKA_WORKFLOW.md) control production/tool policy and acceptance. A product setting such as Medium is approximate; counted native exports must satisfy the authored30-page chapter boundary.
2. [SERIES_PRODUCTION_BRIEF](SERIES_PRODUCTION_BRIEF.md) defines the edition’s dramatic promise, B&W language, character continuity and fixed print route: resonance7/Horseshoe, early Maeve, Livia saved, Positive-Sum.
3. [OPENING_SCRIPT_01_03](OPENING_SCRIPT_01_03.md) controls the first90 numbered story pages. [CHAPTER_TREATMENT_04_22](CHAPTER_TREATMENT_04_22.md) controls the remaining19 chapters through six five-page blocks each. Mangaka may refine performance/panelling without changing cause, consent or reveal timing.
4. [SERIES_REVEAL_LEDGER](SERIES_REVEAL_LEDGER.md) controls all22 titles, midpoint11/12,32 core relationship stages, eight protected proofs, chronology and causal region transitions. Resolve treatment conflicts against the ledger and the underlying fictional canon before generation.
5. [OPENING_EDITORIAL_REVIEW](OPENING_EDITORIAL_REVIEW.md) is review guidance, not another chapter or a competing script. [MANGA_DIRECTION](../MANGA_DIRECTION.md) retains enduring drawing/action/accessibility/game-adapter constraints; obsolete20-page dimensions, grids and panel coordinates are historical only.

[STORY](../STORY.md), [BOND_ARCS](../BOND_ARCS.md), [DECISIONS](../DECISIONS.md), [CHARACTER_BIBLE](../CHARACTER_BIBLE.md) and [WORLD_BIBLE](../WORLD_BIBLE.md) govern fictional facts and game branches. The printed route does not replace the player’s digit0–9, optional recruits/rescues or four ending choices. The user’s revised manga production policy supersedes an older document’s ordinary-image pipeline.

## Machine-readable planning boundary

This contract is **plan validation only**. It is not an export manifest or a claim of provider completion. Native Mangaka IDs, output formats/counts, source resolution and chapter acceptance must be recorded after actual UI/export evidence exists.

<!-- series-plan-contract -->
```json
{
  "edition_id": "omen_mangaka_series_v1",
  "evidence_scope": "plan_only",
  "production_tool": "Mangaka",
  "story_art": "black_and_white",
  "reading_direction": "ltr",
  "chapter_count": 22,
  "story_pages_per_chapter": 30,
  "story_page_target": 660,
  "ordinary_image_generation_for_story_pages": false
}
```

`python tools/check_docs.py` validates22 consistent chapter titles, the opening’s30 numbered pages per chapter, the later chapters’ six five-page blocks, eight canonical proof IDs and32 relationship-stage cells. It separately reports the old study files with `legacy_manga_study_*` counters. Neither result proves new Mangaka chapters exist. The32-page manuscript’s document pagination is a third, separate measure.

## Production gate

For the current stopped-analysis investigation, input truncation finding and controlled Chapter01 test, see [MANGAKA_RECOVERY](MANGAKA_RECOVERY.md). The full manuscript remains an editorial reference; the clean input sources are provider-facing derivatives, not replacements for the reveal ledger or an exported comic.

Review/analyse the prepared story, then review recurring Cast & World identities before chapter production. Inspect chapter01’s emotional hook, geography, acting, dialogue, page turns and export count before scaling to later chapters. Preserve the actual native series/chapter IDs and export/edit history. A completed job is a candidate, not quality sign-off. No automatic public publication, subscription change or credit purchase is authorized by this plan.

For game reuse, validate what the native export actually supports. Clean/lettered separation, panel crops, transcript/localization data and a read-only reader remain adaptation requirements; no unsupported native layer export is assumed. Reader bookmarks must stay separate from campaign saves, and any future live adapter must stop for real choices/combat. The legacy20-page JSON/crops demonstrate only the superseded study’s processing.
