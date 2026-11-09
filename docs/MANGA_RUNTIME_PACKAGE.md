# Portable Chapter 01 asset package

`tools/package_manga.py` creates a local reader and lightweight asset handoff. It never imports Unity, implements live game events, modifies native artwork, or creates a PDF.

Run only after the final lettering export is complete and its `export_report.json` hashes match the lettered PNGs:

```powershell
python tools/package_manga.py --check
python tools/package_manga.py
```

The output is `output/game/ZERO-SUM_OMEN_Chapter_01.zip`. Extract it fully and open its `index.html`; the reader uses relative files and does not need a server or connection.

The complete package includes:

- 20 clean and 20 separately lettered page JPEGs, maximum long side 1200px.
- 80 clean and 80 lettered panel JPEGs, maximum long side 1024px, loaded only on request.
- Page/panel manifest, normalized regions, exact dialogue IDs, transcript, image dimensions, byte sizes and SHA-256 hashes.
- Editable SVG lettering overlays, dialogue/page sources, bundled unmodified open fonts and their OFL texts/source fingerprints.
- A portable reader with keyboard navigation, page selection, clean/lettered and page/panel modes, a transcript, and a reader-only bookmark.

JPEG quality defaults to 86; 85 is also allowed. Native PNGs remain unchanged in `art/manga/chapter_01`. The default complete ZIP and uncompressed delivered assets must each stay within 50 decimal MB. The command reports actual sizes and refuses to silently omit pages if the budget fails. Rebuild with a smaller `--panel-max` or `--page-max` when necessary; final acceptance still includes reading-size review.

The fixed print route is an authored resonance-7/Horseshoe example. Navigation never grants rewards, damages an enemy, chooses resonance or charms, releases a Seal, or changes a campaign checkpoint. The manifest preserves all live choice/combat pause/resume boundaries as future adapter requirements. A Unity adapter must omit printed reference combat results and resume only after actual completed gameplay. No Unity project or implemented game reader is claimed by this package.

The package manifest hashes every delivered file except itself, and records source PNG hashes separately from derived JPEG hashes. SVG files are lettering overlays rather than complete art pages. A font's OFL applies to that font, not to the story or illustrations.
