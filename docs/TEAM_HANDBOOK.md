# ZERO-SUM: OMEN — Agent Production Handbook

Updated 7 November 2026. DECISIONS resolves conflicts; PROJECT_STATUS records evidence. Meridian Prologue; AI-only development, existing/free tools first.

## 1. Ownership

| Area | Responsible role | Sources/output |
|---|---|---|
| Vision/scope | User director + integrator agent | DECISIONS/JAM_SLICE/GDD |
| Rules/data/sequencing | Gameplay agent | SYSTEMS/TECH_DESIGN/BESTIARY, typed data/fixtures |
| UI/build/save | Integrator | UX/accessibility, actual hosted-build evidence |
| Character/motion | Character agent | CHARACTER_BIBLE/ART_DIRECTION/ASSET_LIST; scene/scripts and pose captures |
| Environment/VFX | Environment agent | LOCATIONS/art contracts; camera/layers/variants |
| Story/audio | Narrative/audio agents | STORY/JAM_SCRIPT/AUDIO, exact IDs/reproducible sources |
| Source/rights/cultural checks | Research/reviewer agent | Cultural/rights/disclosure records, explicit uncertainty |

Parallel tasks own disjoint files. One integrator owns shared schemas/scene wiring. Each task declares files, inputs/rule IDs, artifact, acceptance and rollback. Read diffs before edits; never overwrite another agent's work. Review actual source/runtime capture, not completion assertions.

## 2. Rhythm and evidence

Record files/checks/blockers/next gate each session. Use specified/implemented/verified/not in scope. Build/playtest targets are work to attempt/record, not achievements. No hosted build/study claimed without build ID/URL/results. Scope swaps obey JAM_SLICE, not art wishlists. Feature freeze 10 November; content lock end 11 November; verify 12 November; submit 13 November; hard deadline 14 November 17:30 IST.

## 3. Repository/tools

Markdown canonical; PDFs derived snapshots. `canon.py` indexes selected facts but cannot guarantee books never disagree. A parse failure or duplicated fact must be corrected and generated text checked. Typed tuning is data, not executable formulas.

Target `game/`, installed Unity 6000.4.11f1+Web module for viability. No tracked project/build assumed. Baseline default branch is `ccr-05a281dd-krqvi8`, not an assumed green `main`. Verify branch/remote; use short `codex/` branches. Review/CI is a quality process until checks actually exist. Do not rewrite history; choose binary storage before large production assets accumulate.

Local Blender/SVG, AI-authored Unity C#, deterministic motion and synthetic audio are defaults. Higgsfield/Meshy reads now succeed; per-operation eligibility/cost/rights need evidence. Balance is not authorization to spend. A docs-only pass does not authorize subscriptions/trials/uploads/generation. The later explicit request for fresh designs authorizes the recorded built-in image/Blender work; it does not authorize provider purchases or paid jobs. Reconcile uncertain IDs; no duplicate charged work. No secrets/live provider dependency in build.

## 4. Production

Contract→canon references→AI-authored layout→procedural or authorized generated candidate→AI correction→scripted poses/layers/rig/export→engine→review→player validation→provenance. No human finishing handoff. Simplify/re-render/reject failures. Exact labels/digits are runtime/code-native. A flattened picture is not a rig; a raster base is not saved Blender source. External feedback may guide direction without outsourcing production; AI cannot certify enjoyment/cultural approval.

## 5. Book builds

Validate: `python tools/build_bible.py --check`, `python tools/build_artbook.py --check` (no output). Preview: `--html-only --output-dir build/review-bible` or `build/review-artbook`. PDF: omit html-only; optionally `--node PATH`. Choose an output directory to preserve reviewed books. Input manifests/content-keyed caches and offline renderer; local/system fonts. See ARTBOOK_PRODUCTION for dependencies. Regenerate only after source integration, then record snapshot and visual checks; stale books are historical.
