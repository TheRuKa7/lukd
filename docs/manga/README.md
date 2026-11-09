# Current manga production

Current edition: **seven volumes × seven chapters ×22 B&W story pages =1,078 story pages**, English left-to-right. Each volume has154 story pages. Covers, backs and colour inserts are additional.

## Current edition and evidence

The current edition has49 outlined chapters and21 prose drafts;28 chapters remain unwritten. Phase6 is a preliminary review, not a completed whole-novel revision. [Phase7](../PHASE_07_REPORT.md) begins provisional local scripting; no accepted native story-page exports are established. Collectible reading must preserve reading order and spoiler-aware unlocks without committing campaign events; bookmarks remain separate from game saves. A future live cutscene adapter must yield to actual player choices and combat, reconcile saved results, and keep skip/retry idempotent. Historical20-page study exports do not implement this edition's runtime integration. Native output dimensions, layers, transcript extraction and export counts require actual inspection before integration.

## Authority and production order

1. The user's latest instructions control scope.
2. [Resolved series bible](../novel/RESOLVED_SERIES_BIBLE.md) controls current fictional and editorial decisions.
3. [Seven-volume plan](SEVEN_VOLUME_NOVEL_PLAN.md) is the49-chapter scaffold; it is not the complete scene ledger or prose novel.
4. [Ten-phase plan](../TEN_PHASE_PLAN.md) controls production order and exit gates. Finish and revise the prose before native manga generation; produce one volume at a time.
5. [Novel index](../novel/README.md) records actual prose status; [asset inventory](EXISTING_HIGGSFIELD_ASSETS.md) records existing references and missing coverage.

Mangaka generates story pages. Ordinary image generation is limited to separately indexed colour supplements and reference art; rejected colour comic studies are not the new B&W manga. Native approximate length settings do not establish22 story pages. Count the actual exports and exclude cover/closing matter. Keep aliases, identity, source hashes, costs and edits reconciled.

The seven working dossiers now use current canon, scene decisions and available prose; old excerpt-based versions are archived. They contain whole-story author knowledge and do not establish6,000 substantive lines per volume. They are not direct upload scripts. See [their manifest](volumes/manifest.json), the [provisional Volume1 package](scripts/volume_01/README.md) and [recovery evidence](MANGAKA_RECOVERY.md). Raw Markdown line counts, including blank lines, are not meaningful-content acceptance.

## Historical22-chapter evidence

The [earlier production policy](README_22_CHAPTER_HISTORICAL.md), manuscript and22-chapter treatments are retained as superseded evidence. Their titles, page boundaries and bond schedules require remapping; they do not authorize generation of the current edition. The contract below is preserved solely for the historical validator. Current-edition structure is checked by `tools/check_novel_plan.py`.

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
