# Generative AI and provenance record

Updated 8 November 2026. AI authors/processes production under user direction (D02). **No shipped Unity build in the evidence record.** This records sources/changes, not shipping approval. [Jam overview](https://itch.io/jam/official-unity-game-jam-2026) requires submission-page AI-use disclosure for prizes.

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
| 2026-11-08 | Full illustrated cast/environment pass | Higgsfield `gpt_image_2_6`, high quality, requested4k/3:2, reference-guided by actual Blender views and the matching v5 identity studies | 84 distinct cast design sheets cover91 indexed records; seven region sheets. Native delivered3504x2336 pixels. Request/output/job/hash manifests in `art/catalog/`; illustrated proposals, not camera renders or accepted runtime assets. Focused continuity revisions retained separately. |
| 2026-11-08 | Superseded colour manga studies | Higgsfield `gpt_image_2_6`, high quality, requested4k/2:3;20 original page jobs plus focused continuity corrections | Native delivered2336x3504 pixels. Clean originals, lettering/display JSON/SVG, job IDs and hashes remain in `art/manga/chapter_01/` as production-history evidence. The user rejected this20-page adaptation; successful jobs/render checks do not make it the accepted manga. Earlier built-in studies are also historical. |
| 2026-11-08 | Expanded geometry and print/game processing | AI-authored local Blender recipes and offline Python/Chromium builders | 29 encounter studies,116 true camera outputs; seven environment/84 distinct cast view sets overall. Book JPEGs and game JPEGs are explicitly sized derivatives; native originals remain unchanged. |
| 2026-11-08 | Mangaka-native series planning | AI-authored production brief,90 opening-page instructions,114 five-page blocks for chapters04–22, reveal ledger and local32-page manuscript PDF; actual Mangaka studio workflow inspected |22 x30 B&W story-page target. This is a plan/manuscript, not generated native chapters. Current policy and source hierarchy are [manga/README](manga/README.md); native series/chapter export evidence remains separate. |
| 2026-11-08 | Native Mangaka input diagnosis | Full manuscript and a separate clean Chapter01 PDF uploaded to the actual Mangaka studio. The smaller input extracted one chapter; NIL's existing concept sheet was uploaded and its native description corrected. Analysis reversals and alias accumulation were observed | UI reported0 credits spent during the diagnostic. No native story pages or new cast images were generated. Exact input hashes, project IDs, observed states and later corrections are in [the recovery record](manga/MANGAKA_RECOVERY.md). A transient analyzed screen is not proof of stable production. |
| 2026-11-08 | Font dependencies | Unmodified Barlow Semi Condensed and Bebas Neue from official Google Fonts repository | SIL Open Font License1.1 text, source URLs and SHA256 are bundled under `art/fonts/`; no Windows font files are redistributed in the game package. |

The user explicitly selected Higgsfield after the initial free/local-first exploration. Existing account credits pay for these image jobs; no plan, credit pack or trial was purchased/activated by the agent. Requested model resolution is distinct from actual pixel dimensions. Generation metadata does not establish artistic, cultural, legal or runtime acceptance.

The reconciled production log records127 submissions:126 completed and one provider-blocked request. The selected illustrated artbook concept pass uses91 cast/environment boards. The20 selected colour manga images belonged to the now-rejected study edition; they and its successful revisions remain historical. No native Mangaka chapter is established by these ordinary-image job counts. Observed use was535.5 existing credits, including the continuity passes. Per-request quoted cost was4.25; rejected-job accounting is reconciled through the observed total rather than guessed from submission count. The local log contains job IDs/statuses without credentials, signed URLs or account balances.

One proposed inverted Vetala illustration was rejected by the provider. It was not repeatedly resubmitted. A different, upright neutral costume study is used alongside the independently rendered Blender pose reference; it does not claim illustrated motion coverage. Preserve the rejected job status in the production log and exclude the wrong earlier traveller/effigy design from the selected book plates.

The revised user instruction requires Mangaka-native B&W story pages. Ordinary image generation is now limited to separately indexed colour covers/backs/inserts and supplementary illustration, outside660 story pages. Do not grey-convert or reuse the rejected page recipe as the new comic. The earlier image spend remains recorded even though the user rejected the manga result; technical completion and creative acceptance are distinct.

## 4. Final manifest

Asset ID, source/output paths+SHA256, scope/status, tool/model/version if known, request ID if known, reference hashes, prompt/script/scene, parameters/seed if supported, licence/attribution evidence/date, actual edit chain, runtime export/import settings, acceptance evidence and shipped build ID. Mark missing/unsupported fields explicitly. Preserve required provenance metadata; no secrets/signed URLs.

Before submission reconcile shipped code/text/art/audio, credits/licences and exact package contents. No accidental reference files. A complete log alone proves neither rights, authenticity nor game quality.
