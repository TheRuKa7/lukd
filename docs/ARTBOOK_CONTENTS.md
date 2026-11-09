# Complete artbook build and coverage

The complete world/artbook is a separate, HTML-first production volume built by `tools/build_full_artbook.py`. It does not overwrite the historical draft by default. Its design is A4 landscape, ledger cream/ink/Nixie orange, with fixed page templates, large fresh-concept studies, material closeups, readable source-derived text and a full four-view catalog.

## Contents

1. Fixed visual language: current art direction, exact production specification and fresh NIL/Vesper/Varro design studies with useful-detail crops.
2. World: the encyclopedia, operations, power logic, history, vocabulary and adopted rules.
3. Factions: goals, authority, materials, tools, uniforms and individuals.
4. Seven lands: 2.5D, top and front drafts plus spatial/daily-life notes.
5. Full character catalog: one four-view sheet and one detailed dossier per catalog entry, covering outfits, core/secret recruits, bosses, keepers, named NPCs and job/faction archetypes. Missing views remain visibly labelled and reported, never silently claimed complete.
6. Campaign and voice: story structure, consequences, writing and comedy.
7. Manga: page/panel grammar and a four-page preview of the separate complete, portrait-format lettered chapter when present.
8. Production: source/provenance, AI use, character and source indexes.

## Commands

```powershell
python tools/build_full_artbook.py --check
python tools/build_full_artbook.py --check --require-complete-views
python tools/build_full_artbook.py --output-dir build/full-artbook
```

The first command is read-only. The strict coverage flag fails if a required catalog view or source model is absent. Normal HTML generation retains visible specification-only panels and a missing-asset report so work is not lost.

Outputs are `book.html`, `full_artbook.css` and `build-manifest.json` in the selected output directory. The manifest records source revision/fingerprint, all image fingerprints, page titles/folios, character index and missing coverage. The file is a source snapshot; the final PDF requires a separate marker, offline Chromium rendering, structural layout audit and visual page inspection.

```powershell
node tools/render_pdf.js build/full-artbook/book.html output/pdf/ZERO-SUM_OMEN_Complete_Artbook.pdf landscape
```

Run the PDF skill's artifact-operation marker immediately before first PDF authoring; do not interpret this example as a completed render. `window.__artbookAudit` in the loaded HTML records every missing image and overflowing `[data-overflow-check]` region. A successful HTML build is not visual acceptance.

## Evidence labels

Fresh concept illustrations are visual-development candidates. Imported 3D character/environment blockouts are first drafts; they do not establish final anatomy, faces, hands, cultural representation, topology, rigging or gameplay. Current decisions and character canon supersede obsolete details in an older model. Record rejected/obsolete imagery rather than quietly reusing it as a new approved reference.

The current manga is a Mangaka-native22-chapter B&W production targeting30 story pages each. Its rejected20-page colour predecessor is excluded from the current artbook. Native outputs and supported export layers must be verified before game adaptation; a book page or look-development composition is not a Unity gameplay screenshot.

## Complete camera evidence and illustration queue

`tools/render_encounters.py` supplies the additional 29 editable encounter studies and 116 real camera views. The catalog currently has 91 records, linked to 84 distinct four-view sets; five named keepers are also indexed within shared compound groups. Noise Storm and the Default are contextual environmental studies, not invented anatomical embodiments. The Default study contains still grey volumes and negative space, with no wheel. The replacement Rahu/Ketu are two fictional mechanical eclipse instruments. Camera evidence establishes spatial drafts, not final detailed manga construction or game-ready models.

```powershell
& 'C:/Program Files/Blender Foundation/Blender 5.2/blender.exe' --background --python tools/render_encounters.py -- --height 768 --samples 32 --update-catalog
python tools/prepare_higgs_artbook.py
```

The second command composes one actual four-camera reference per unique set and seven three-camera environment references into `build/higgs_artbook_refs`. It creates detailed, original-design requests in `art/catalog/higgsfield_artbook_requests.json`, with stable request IDs and source/image SHA-256 fingerprints. It does not upload, submit a generation, use credits, or approve an illustration. The queue preserves exact asymmetries, factions, work, power costs and contextual/non-anatomical limits; generated lettering is prohibited. Provider outputs must pass identity, construction and camera checks before the artbook treats them as current illustrated concepts.

When request outputs exist, the book adds each unique illustrated board once on its own spread, before the separately labelled actual-camera sheets. These are visual-development candidates, without automatic count, rig or runtime acceptance. The book preserves the original PNGs and creates content-hash-keyed 2400px/quality90 JPEG print derivatives under the output directory's `print-assets/`; `build-manifest.json` records both hashes, dimensions and sizes. Only the illustrated boards use these derivatives. Changing an original naturally creates a new derivative rather than silently reusing an obsolete print image.
