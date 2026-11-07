# Generative AI and provenance record

Updated 7 November 2026. AI authors/processes production under user direction (D02). **No shipped Unity build in the evidence record.** This records sources/changes, not shipping approval. [Jam overview](https://itch.io/jam/official-unity-game-jam-2026) requires submission-page AI-use disclosure for prizes.

## 1. Submission statement contract

Retire the claim that 'everything else' was manual. Fill the following from the actual final manifest:

> AI tools authored/revised design and story text/software and created or processed these shipped art/animation/audio groups: {actual tools/models/assets}. The user directed and selected work. Processing: {actual scripts/edits; unknown versions marked unknown}. External credits/licences: {actual list}. Runtime generation: none.

Replace every field/remove irrelevant categories before publication. Concept tool attribution is not automatically final-asset attribution. Never claim human finishing, cultural approval or unsupported model versions.

## 2. Historical source record (6 November baseline)

Prior repository attributions below are retained as claims. Files alone do not verify provider/model/request metadata; original job IDs and source scenes were not supplied. No automatic runtime approval.

| Source | Historical attribution | Evidence/limits |
|---|---|---|
| Original design/prototype | Claude via Claude Code under user direction | Files exist; individual model logs not supplied |
| `art/lookdev/*_blockout.png` | Higgsfield 3D Jutsu/Blender guides | Rasters exist; scenes/scripts missing |
| `art/concepts/*.jpg` | Higgsfield angles / claimed Seedream V5 Pro over layouts | Concepts exist; exact model/request IDs unverified; pass-1 references |
| `art/motion/*.mp4` | Higgsfield video / claimed Seedance 2.5 from stills | Two tests; IDs unverified; landscape intro/portrait reveal, no assembled film |
| `art/base3d/*.png` | Claude-scripted Blender/Workbench in 3D Jutsu | Rasters exist; no tracked source scene/scripts |
| `art/graphics/*.svg`, `figures/*.svg` | AI-authored `tools/graphics.py` / `figures.py` | Reproducible candidates; approximate figures, not rigs/back views |

If legacy concepts are corrected/used, log the derived asset and actual processing. No future promises of manual painting/rigging/editing/composing count as evidence.

## 3. Current changes

| Date | Group | Process | Evidence/status |
|---|---|---|---|
| 2026-11-06 | Refinement reports/inventories | Codex agents, metadata reads, primary web research | Dated review baseline, not runtime implementation |
| 2026-11-07 | Docs/generator/parser/render corrections | Codex agents under adopted decisions | Source edits; actual checks in DOC_AUDIT/PROJECT_STATUS |
| 2026-11-07 | Fresh visual designs (`art/concepts/fresh/*_v4.png`, `*_v5.png`) | Built-in image-generation tool, directed by Codex from current canon/art briefs; v4 style candidates followed by more detailed lore/prop-focused v5 designs | New generated candidates; exact prompts/reference history and hashes in the asset provenance record. No claim of a named model version beyond tool evidence. Not runtime rigs. |
| 2026-11-07 | Scripted lookdev (`tools/build_lookdev.py`, new `art/source/` and `art/renders/lookdev/` outputs when produced) | Codex-authored Blender geometry, source-authored labels, unmirrored RGBA compositing and seven-bore prop | Generation/processing work, distinct from the initial read-only provider checks; validation captured with actual outputs |
| 2026-11-07 | Provider checks | Read-only Higgsfield/Meshy account/capability reads | Access verified; no Higgsfield/Meshy generation/upload/purchase/credit spend in those provider checks |

## 4. Final manifest

Asset ID, source/output paths+SHA256, scope/status, tool/model/version if known, request ID if known, reference hashes, prompt/script/scene, parameters/seed if supported, licence/attribution evidence/date, actual edit chain, runtime export/import settings, acceptance evidence and shipped build ID. Mark missing/unsupported fields explicitly. Preserve required provenance metadata; no secrets/signed URLs.

Before submission reconcile shipped code/text/art/audio, credits/licences and exact package contents. No accidental reference files. A complete log alone proves neither rights, authenticity nor game quality.
