# ZERO-SUM: OMEN — Team, Pipeline and Tools Handbook (Gate B15)

How we work. Short on purpose.

---

## 1. Ownership
| Area | Owner (role) | Source of truth |
|---|---|---|
| Vision, pillars, scope | Director / design lead | GDD, JAM_SLICE |
| Combat, sequencing | Lead dev | TECH_DESIGN, GAME_FEEL |
| UI, map, data, build | Dev 2 | UX_SPEC, TECH_DESIGN |
| Characters, animation | Character artist/animator | CHARACTER_BIBLE, ART_DIRECTION, ASSET_LIST |
| Environments, VFX | Environment/VFX artist | LOCATIONS, ART_DIRECTION |
| Story, cinematics, audio | Writer/cinematics/audio | STORY, JAM_SCRIPT, AUDIO |
| Culture | Design lead + reviewers | CULTURAL_CONSULTATION |

**Order of authority when docs disagree:** Art Direction (visuals) → Character Bible (characters) → World Bible + Story (story) → GDD + Systems (mechanics) → Tuning (numbers).

## 2. Rhythm
- **Daily stand-up (10 min):** yesterday, today, blockers; update ASSET_LIST status; agree any scope swap (JAM_SLICE §4).
- **Daily build** to the private itch page; **daily playtest** (PLAYTEST).
- **Weekly (post-jam):** design review with a playtest video; docs updated in the same PR as the change they describe.

## 3. Repo and tools
- Docs in `docs/` (Markdown is the source; the bible and art book PDFs rebuild with `python3 tools/build_bible.py` and `python3 tools/build_artbook.py`).
- Numbers in `tuning/`; simulation in `tools/sim_patterns.py`.
- Unity project in `game/` (to be created); Git LFS for binary art and audio.
- Branches: `main` always builds; short feature branches; PRs need one review and a passing CI.
- Commit messages say what changed and why; reference the doc section.

## 4. Art pipeline (end to end)
Brief (Art Book Production §5) → 3D base (Blender / 3D Jutsu / Meshy) → colour key → AI paint pass (Higgsfield/FLUX, logged) → **human overpaint** → QC (QUALITY_BAR) → layer split (ASSET_LIST) → engine → playtest.

## 5. Communication
One channel per area plus #builds and #playtests; decisions are written down in the relevant doc within a day, or they didn't happen.
