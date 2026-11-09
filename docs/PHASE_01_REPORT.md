# Phase1 — production baseline

8 November 2026. Scope: establish an accurate, reproducible starting point and resolve contradictory project entry points. The [ten-phase plan](TEN_PHASE_PLAN.md) assigns scene-level and literary development to subsequent phases; completing this baseline is not completing the story.

## Corrections performed

- Root README now describes the story-first priority and treats the jam schedule as historical.
- Manga README now states the current49-chapter/1,078-page edition directly, without presenting the obsolete22-chapter edition as current immediately below a warning. Its former contents are preserved in [the historical policy](manga/README_22_CHAPTER_HISTORICAL.md).
- The old22-chapter contract remains explicitly historical for its validator; [current-edition validation](../tools/check_novel_plan.py) checks the49 ordered chapters, seven groups and six acquired Seals.
- The resolved series bible remains the current editorial authority. Older reference compilations and exploratory prose are identified as snapshots/drafts rather than accepted current manuscript.
- A machine-readable inventory records all49 chapters, the three existing prose drafts, the seven context dossiers' actual line counts,91 selected source boards and the reviewed94-page concept collection's file hash. No native service state or accepted manga output is inferred from local planning files.
- The phase tracker assigns explicit statuses and deliverables. Partial prose, incomplete contexts and existing concepts are not marked as completed phases.
- Native workflow and the presentation architecture's TR-VIEW-018 registry/ADR/traceability row now state49 chapters ×22 story pages and volume-by-volume acceptance. Historical treatments and clean diagnostic inputs have explicit superseded banners. The current-edition evidence heading retains the architecture link and read-only game-reader constraints.

## Completion gate

Run `python tools/project_checkpoint.py`, `python tools/check_novel_plan.py`, `python tools/check_docs.py` and `git diff --check`. The inventory command fails on missing/changed selected artwork, changed reviewed PDF, wrong current scope or incomplete chapter numbering. The other commands check the outline's structure, links/data contracts and whitespace. Actual command outcomes are recorded below after execution.

## Remaining work assigned forward

The complete49-chapter scene ledger, full character/faction trajectories, completed prose, seven6,000-line substantive contexts, current manga page scripts, accepted native exports and Unity game are not complete. These are assigned to Phases2–10 rather than hidden as baseline exceptions. Current three prose chapters require further whole-series editorial review.

Printed reference books other than the94-page concept collection remain older source snapshots. No re-rendering, external generation, subscription purchase, publishing or GitHub push is part of Phase1. Existing working-tree changes are preserved.

See [inventory](phase_01_inventory.json) for observed counts and hashes and [phase tracker](production_state.json) for execution status.

## Executed results and verdict

**PASS — Phase1 complete for its declared baseline scope.**

- Inventory:49 ordered chapter slots, seven volumes, three prose drafts,91 selected source boards. Every selected image's actual hash matches its selected-output manifest. The reviewed94-page concept collection hash matches its QA record.
- Context lines by volume:505,362,391,418,422,451,459. None is declared a completed6,000-line context.
- Current plan validator:PASS,49 chapters,1,078 target pages,154 per volume; Seals1/9/8/0/2/7 in order.
- Documentation/data validator:PASS,99 Markdown files and729 local links; historical22-chapter counters remain explicitly historical. A missing architecture anchor found during reconciliation was repaired before the final pass.
- Whitespace diff check:PASS; Git reports only line-ending normalization notices for existing edited files, not whitespace errors.

No creative-completeness, semantic perfection, accepted manga, playtest or Unity-build claim follows from these checks. Phase2 is the next dependency: a complete49-chapter scene and knowledge ledger.
