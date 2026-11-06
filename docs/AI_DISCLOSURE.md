# Generative AI disclosure log

The Official Unity Game Jam 2026 allows generative AI **only if it is disclosed on the submission page, including how it was used.** Not disclosing disqualifies the entry from prizes. Log every AI-assisted asset that ships, as you make it, and paste the summary into the itch page.

## Summary for the submission page (fill in before submitting)
> Draft, update before submitting: Generative AI was used in this project as follows. Claude (Anthropic) helped draft the design documents, world bible and browser prototype under the team's direction, and wrote the code for our vector graphics and 3D layout scenes. Higgsfield (Seedream, Seedance) generated concept art and cinematic tests from our own 3D layouts; shipped art is painted over by the team. [List any AI art, audio or video that ships, from the log below.]
> Everything else (final art, animation rigs, motion graphics, editing, music arrangement, final writing) was made by the team.

## Log
| Date | Asset | Tool / model | How it was used | Human edits after generation |
|---|---|---|---|---|
| 2026-11-06 | Design docs, prototype code | Claude (Anthropic) via Claude Code | Drafted design documents and the browser prototype with the team | Reviewed and directed by the team |
| 2026-11-06 | `art/lookdev/*_blockout.png` | Higgsfield 3D Jutsu (Blender scene) | Simple 3D layout renders used as composition guides | — (not shipped) |
| 2026-11-06 | `art/concepts/*.jpg` (character key art and environment concepts) | Higgsfield 3D Jutsu "angles" (Seedream V5 Pro), image generated over our own 3D layout renders, from prompts in `art/HIGGSFIELD_PROMPTS.md` | Concept and key art for NIL, Vesper, Maeve, Hina, Tamamo, Varro, Thale; Meridian and Hyakki environments | Concepts only so far; shipped versions will be painted over, layered and rigged by the team |
| 2026-11-06 | `art/motion/*.mp4` (intro shot, NIL reveal) | Higgsfield 3D Jutsu video (Seedance 2.5), animated from our generated key art as the start frame | Cinematic pipeline tests for the intro and character reveals | Tests only; final cutscenes will be edited, graded, scored and subtitled by the team |
| 2026-11-06 | `art/base3d/*.png` (Wards, Moon Pier, line-up clay bases and colour keys) | Blender scenes built by Claude (scripted bpy) in Higgsfield 3D Jutsu, Workbench renders. No image model | Stage-1 3D bases and flat colour keys for the register-A paint passes | Not shipped; reference for painting |
| 2026-11-06 | `art/graphics/*.svg` (faction emblems, Omen displays, charm icons) | Hand-written SVG code by Claude (`tools/graphics.py`). No image model | Graphic identity for the art book and UI icon drafts | Drafts; to be redrawn or refined by the team before shipping |
| | | | | |
| 2026-11-06 | `art/graphics/figures/*.svg` (flat model-sheet figures for 16 characters and 4 eras), `art/graphics/reel_*.svg` | Hand-written SVG code by Claude (`tools/figures.py`, `tools/graphics.py`). No image model | Silhouette and colour designs for the art book, the bible and UI drafts | Drafts; to be redrawn by the team |
