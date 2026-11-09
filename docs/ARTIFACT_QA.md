# Printed artifact QA

8 November 2026. PDF inspection followed by a companion Bible artwork refresh within the existing authoring workflow. The result covers the printed reference books; it does not approve a Unity build, finished runtime assets or completed Mangaka chapters.

## Final files and verdict

| Artifact | Verified final file | Verdict |
|---|---|---|
| [Complete artbook](../output/pdf/ZERO-SUM_OMEN_Complete_Artbook.pdf) | 440 A4 landscape pages; 97,934,535 bytes; SHA256 `36250391ce240390b75a6d0c48d4ebc5939e245cb35363678e8291686e1ef1fd` | Printed reference layout passes the inspected coverage. All 440 pages were rasterized; the full prior contact review is supplemented by inspection of the changed final workflow/disclosure/index pages. |
| [World/design bible](../output/pdf/ZERO-SUM_OMEN_World_and_Design_Bible.pdf) | 177 A4 portrait pages; 22,057,327 bytes; SHA256 `77958b1ad89b1b66aa5edce35c07ed8fd2fc9107d62a11c85a105060e9e53238` | Printed layout passes. All 177 pages were rasterized; the full prior contact review is supplemented by changed final status/workflow/disclosure checks. All 16 indexed character profiles and seven regional profiles contain current illustrated boards; no artwork placeholders remain. |

Both final PDFs have zero empty-text pages and zero Unicode replacement characters in pypdf extraction. Their sparse pages are designed dividers or section endings. Both structural render reports record zero missing images, failed requests or overflow warnings. These automated checks support, but do not replace, the visual review.

## Visual coverage

The initial artbook layout received 24 full-size inspections at approximately 1800 pixels: 23, 30, 55, 65, 103, 106, 115, 116, 117, 124, 125, 126, 129, 133, 135, 138, 139, 173, 191, 212, 350, 351, 422 and 440. This covered dark hero plates, the seven-bore prop, power contracts, occupations, factions, painted environment boards, actual environment camera drafts, four-view characters, dense dossiers, shared keeper groups, the Vetala pose distinction, current manga rules and the source index. All seven regional environment groups were also inspected in the contact overview.

The final artbook edition was re-rasterized and all 440 pages reviewed again at contact scale after image recompression and content fixes. Changed pages 135, 138 and 139 were rechecked at full size. The Bible cover was inspected at full size; its NaN stamp preserves the lowercase a. After the companion artwork remap and workflow synchronization, all 177 pages were re-rasterized and contact-reviewed. New artwork occupies pages 61–67 and 72–87. Full-size checks covered environment pages 61, 64 and 67, character pages 72, 75, 76, 78, 81, 84 and 87, the complete Far Lands paragraph on 70 and disclosure table on 177. An independent reviewer checked Hina, Shunya, boss Varro, Thale and the date table. No missing embedded image, overlapping text or page-edge clipping was observed in this coverage. Print JPEGs remain legible at the inspected size; source PNGs were not changed.

The companion now resolves its 23 boards through the same request/output catalog as the complete artbook. Each selection requires a unique matching request, an existing output and an exact recorded SHA256. Profile swatches also come from the current character catalog; this removes NIL's legacy cyan costume swatch in favour of Brass. Missing or stale selected output fails the build instead of printing a placeholder. The final companion includes the current MANGAKA_WORKFLOW source. Replacing older multi-page Meridian/Hyakki studies removed three pages; the updated workflow added one, changing the previous 179-page edition to 177 pages without removing the source-derived design chapters.

The final frozen-source synchronization includes the current PROJECT_STATUS and AI_DISCLOSURE. Artbook pages 422–423, 435–436 and 440 were checked full-size by an independent reviewer; Bible page 6 and its workflow/disclosure pages were checked again. A workflow-only pagination budget keeps the artbook's official references on page 423, and a 20 mm first column keeps the Bible's complete status table and final reference paragraph together on page 6. Both reference-only spill pages were removed without changing source prose, type size or artwork. No extra blank page, missing image, clipping or overlap was observed in the changed pages. Final automated integrity checks cover all 617 book pages.

The complete artbook's source list and fingerprint set now explicitly include all six manga authority files: MANGAKA_WORKFLOW, manga/README, SERIES_PRODUCTION_BRIEF, OPENING_SCRIPT_01_03, CHAPTER_TREATMENT_04_22 and SERIES_REVEAL_LEDGER. Their recorded hashes, plus the frozen PROJECT_STATUS and AI_DISCLOSURE hashes, match the actual source files. The current disclosure reports the native diagnostic's zero story pages and UI-reported zero credits; transient analysis states are not presented as comic completion. Original images and the existing print JPEG settings remain unchanged.

The artbook contains 91 illustrated cast/environment boards alongside separately labelled Blender drafts. Four-view illustrated proposals and actual camera output are distinguished. The upright Vetala illustration is explicitly a costume proposal; its separate hanging-pose draft does not falsely establish illustrated motion coverage. The rejected old coloured manga pages are not presented as an accepted chapter.

## Resolved findings and retained limits

| Finding | Final observed result |
|---|---|
| Basilica location text inherited Meridian neighbourhood details | Fixed. Artbook 135 now describes the Upper Gate, Ivo's passage, archives, nave, Even Hand and Thale's workroom, with institution-specific daily life and conflict. |
| Bible page containing only the final Far Lands line | Fixed. The expansion paragraph is together on final page 70 with meaningful preceding Basilica content. |
| AI disclosure DATE heading and dates broken vertically | Fixed. Final pages 176–177 show a readable horizontal date column. |
| Repeated NIL canon locks and decoder prop | Fixed. Final artbook 138–139 retain the specifications without the reported duplicate list entries. |
| Bible cover visibly reading NAN although source said NaN | Fixed. Final cover uses a case-preserving body font for the stamp and visibly reads NaN. |
| Meridian isometric draft crops the upper Basilica tower | Retained as a source-camera scope limit on the district-massing draft, not a PDF clipping defect or a complete skyline reference. |
| Companion Bible still shows art placeholders | Fixed. All 16 indexed character profiles and all seven regional profiles now use current complete illustrations. Older portrait/region selections and placeholder fallbacks are replaced; selected source files remain unchanged. |
| Companion NIL swatches disagree with the current costume catalog | Fixed. Profile palettes now resolve from the current character catalog; NIL uses Ink, Nixie, Bone and Brass. |
| Final workflow/status updates create reference-only spill pages | Fixed. The artbook workflow uses a targeted page-weight budget; the Bible status table has an adequate Area column. References remain attached to their complete preceding sections. |

Simple faction/camera geometry remains labelled first draft. This review does not certify every small hand, prop count, numeric glyph or cultural detail. Production modeling, rigging, animation, readability in combat and runtime acceptance retain their separate gates.

## Manga status and evidence

The manga target is 22 chapters of 30 black-and-white story pages, totaling 660 story pages. Neither these reference PDFs nor the rejected twenty image-generated studies establish that deliverable. Completed native Mangaka exports, reconciled chapter/page counts and a story/acting review are still required.

### Current authoring inputs

These PDFs contain text instructions and story treatments, not illustrated comic pages. They were rebuilt after the explicit Baker-to-Tobi-to-NIL bun handoff and the revised Chapter 1 alias/spoiler wording were adopted.

| Input | Verified final file | Inspection |
|---|---|---|
| [Current complete production manuscript](../output/production/OMEN_Mangaka_22_Chapter_Manuscript.pdf) | 32 pages; 385,483 bytes; SHA256 `e7a82d9eb9b8e0695b77bd71eefe408be5262166be27ca55ddaffa987b0287a5` | All 32 pages rasterized and contact-reviewed; dense pages 8, 17, 28 and 30 inspected full-size. PDF page 8 includes the bun handoff and pocketing before the alarm. |
| [Revised Chapter 1 story-only input](../output/production/OMEN_Chapter_01_Story_Only_v2.pdf) | 2 pages; 73,913 bytes; SHA256 `96653db943f50d8ac214c8d04a03a3bd031c90e8dd755aa574f79b109e914e45` | Both pages inspected full-size. A small typography adjustment from 11 to 10.5 points retains all 30 beats and the continuity note without a paragraph-only third page. |
| [Lean 22-chapter story digest](../output/production/OMEN_22_Chapter_Story_Digest.pdf) | 4 pages; 110,096 bytes; SHA256 `ce591b905744995a840bfb5331a67ff7bb41727816ab5e2fbc8b99a28cff366a` | All four pages inspected full-size. All 22 chapter headings, ordered story summaries and the ending remain present. |

All three inputs have zero empty-text pages, Unicode replacement characters, missing images, failed requests or reported layout warnings. No clipped prose, overlapping elements or broken table rows were observed in the visual coverage. The full manuscript's dense ledgers repeat their table headers correctly. These checks establish readable authoring inputs; they do not establish successful Mangaka analysis, generated chapter counts or native comic exports.

The exact initial 32-page upload is preserved as [the historical manuscript PDF](../output/production/archive/OMEN_Mangaka_22_Chapter_Manuscript_initial_upload_20261108.pdf), SHA256 `b2061a4535bab6e8b09847a38b212b7fea726b5a2a2c25d82a4c9a2347fc740d`. The [original three-page Chapter 1 diagnostic PDF](../output/production/OMEN_Chapter_01_Story_Only.pdf) remains unchanged, SHA256 `7c8b33a87ecea3da82f155b6f77ea4750acd6670b058ec1fc0d612f00a86ab1c`.

Reproduction evidence is saved under `output/production/source-manifests/`: each current input has its PDF hash/size/page count, exact UTF-8 source snapshots and hashes, builder/renderer hashes and font hashes. Historical manifests retain the original upload hashes separately; no claim is made that revised source text matches those historical uploads. The combined preservation record is [historical_uploads.json](../output/production/source-manifests/historical_uploads.json).

Temporary rasters, contact sheets and text audits are under `build/pdf-qa/`. Final book text audits are in `bible-frozen/text-audit.json` and `artbook-frozen/text-audit.json`; manuscript/input checks remain in their separate authoring-input folders. Inspection used Poppler rasterization and pypdf text/page integrity. Source/build manifests remain authoritative for provenance.
