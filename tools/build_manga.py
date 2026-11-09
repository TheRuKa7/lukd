"""Build the separately lettered, offline manga reader. Does not generate art or PDFs.

python tools/build_manga.py --check
python tools/build_manga.py --output-dir build/manga --render-pages
The optional Node renderer writes PNGs, panel crops and a game manifest; PDF
rendering is a separate artifact operation performed by the project integrator.
"""
from __future__ import annotations

import argparse
import hashlib
import html
import json
import math
from pathlib import Path
import re
import os
import shutil
import subprocess
import sys
from PIL import Image, ImageFont
from urllib.parse import quote

ROOT = Path(__file__).resolve().parents[1]
CHAPTER = ROOT / "art/manga/chapter_01"
FONT_CANDIDATES = {
    "dialogue": [ROOT / "art/fonts/BarlowSemiCondensed-Bold.ttf"],
    "display": [ROOT / "art/fonts/BebasNeue-Regular.ttf"],
}
FONT_LICENSES = [ROOT / "art/fonts/BarlowSemiCondensed-OFL.txt", ROOT / "art/fonts/BebasNeue-OFL.txt"]


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def digest(path: Path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def rectangle(box):
    return len(box) == 4 and all(isinstance(v, (int, float)) and math.isfinite(v) for v in box) and box[0] >= 0 and box[1] >= 0 and box[2] > 0 and box[3] > 0 and box[0] + box[2] <= 1.00001 and box[1] + box[3] <= 1.00001


def contains(outer, inner, epsilon=.0001):
    return inner[0] >= outer[0] - epsilon and inner[1] >= outer[1] - epsilon and inner[0] + inner[2] <= outer[0] + outer[2] + epsilon and inner[1] + inner[3] <= outer[1] + outer[3] + epsilon


def overlaps(a, b):
    return min(a[0] + a[2], b[0] + b[2]) - max(a[0], b[0]) > .001 and min(a[1] + a[3], b[1] + b[3]) - max(a[1], b[1]) > .001


def load_font(role, size):
    for path in FONT_CANDIDATES[role]:
        if path.exists():
            return ImageFont.truetype(str(path), size), path
    raise RuntimeError("No measured lettering font found for " + role + "; install a condensed bold font and add its exact path to FONT_CANDIDATES.")


def wrap(copy, font, max_width):
    result, current = [], ""
    for word in copy.split():
        test = (current + " " + word).strip()
        if font.getlength(test) <= max_width:
            current = test
        else:
            if current:
                result.append(current)
            if font.getlength(word) > max_width:
                return None
            current = word
    if current:
        result.append(current)
    return result


def fit_entry(entry, page_size, tokens):
    width, height = page_size
    x, y, w, h = [n * s for n, s in zip(entry["box"], [width, height, width, height])]
    copy = entry["text"]
    for key, value in tokens.items():
        copy = copy.replace("{{" + key + "}}", str(value))
    kind = entry["kind"]
    if kind in {"title", "subtitle"}:
        start, floor, padding = (154 if kind == "title" else 178), 72, 12
    elif kind == "imprint":
        start, floor, padding = 46, 42, 12
    elif kind == "sfx":
        start, floor, padding = 84, 42, 7
    elif kind == "ui":
        start, floor, padding = 46, 42, 15
    elif kind == "label":
        start, floor, padding = 50, 42, 4
    elif kind == "digit":
        start, floor, padding = 104, 70, 4
    else:
        start, floor, padding = 50, 42, 16
    role = "display" if kind in {"title", "subtitle", "sfx", "digit"} else "dialogue"
    for size in range(start, floor - 1, -1):
        font, path = load_font(role, size)
        # Mixed-case world identifiers such as NaN must remain exact.
        display_copy = copy if entry.get("preserve_case") else re.sub(r"\bNAN\b", "NaN", copy.upper())
        lines = wrap(display_copy, font, w - padding * 2)
        if lines and len(lines) <= entry["max_lines"] and len(lines) * size * 1.08 <= h - padding * 2:
            return dict(id=entry["id"], size=size, font=str(path), role=role, lines=lines, box=[x, y, w, h], normalized_box=entry["box"], padding=padding, copy=copy, line_height=size * 1.08)
    raise ValueError(f"Lettering does not fit {entry['id']}: {copy!r}; enlarge its explicit box, do not silently shrink below the reading floor.")


def validate(manifest, dialogue, require_art=True):
    errors, warnings, sources, fits = [], [], [], []
    page_ids = [p["id"] for p in manifest["pages"]]
    if len(set(page_ids)) != len(page_ids): errors.append("Duplicate page IDs")
    if len(page_ids) != manifest["page_count"] or len(page_ids) != 20: errors.append("Chapter must contain exactly20 authored pages")
    if manifest.get("reading_direction") != "ltr": errors.append("Unexpected reading direction")
    panel_map, entries = {}, {}
    for page in manifest["pages"]:
        if page["reading_order"] != [p["id"] for p in page["panels"]]: errors.append(page["id"] + ": incorrect reading order")
        for p in page["panels"]:
            if p["id"] in panel_map: errors.append("Duplicate panel " + p["id"])
            panel_map[p["id"]] = p
            if not rectangle(p["rect"]): errors.append("Invalid panel rect " + p["id"])
        for i, a in enumerate(page["panels"]):
            for b in page["panels"][i + 1:]:
                if overlaps(a["rect"], b["rect"]): errors.append("Overlapping panels " + a["id"] + "/" + b["id"])
        image = ROOT / page["clean_art"]
        if not image.exists():
            if require_art: errors.append("Missing clean art: " + page["clean_art"])
            continue
        try:
            with Image.open(image) as im:
                im.verify()
            with Image.open(image) as im:
                if abs(im.width / im.height - 2 / 3) > .01: errors.append(f"Wrong portrait aspect for {page['id']}: {im.size}; revise composition before delivery")
                sources.append(dict(page_id=page["id"], path=page["clean_art"], sha256=digest(image), pixels=list(im.size), mode=im.mode))
                if im.width < 1536: warnings.append(f"{page['id']}: source width{im.width}px; exported1536px is a resample, not newly drawn detail")
        except Exception as exc:
            errors.append(str(image) + ": " + str(exc))
    for entry in dialogue["entries"]:
        if entry["id"] in entries: errors.append("Duplicate dialogue " + entry["id"])
        entries[entry["id"]] = entry
        if entry["page_id"] not in page_ids: errors.append("Unknown page for " + entry["id"])
        if entry["panel_id"] not in panel_map: errors.append("Unknown panel for " + entry["id"]); continue
        if not rectangle(entry["box"]) or not contains(panel_map[entry["panel_id"]]["rect"], entry["box"]): errors.append("Lettering box outside panel: " + entry["id"])
        if len(entry["text"]) > dialogue["max_characters_per_balloon"]: errors.append("Copy exceeds limit: " + entry["id"])
        try: fits.append(fit_entry(entry, manifest["page_size_px"], {"resonance": manifest["print_route"]["resonance"]}))
        except Exception as exc: errors.append(str(exc))
    for p in panel_map.values():
        for did in p["dialogue_ids"]:
            if did not in entries: errors.append(p["id"] + ": absent dialogue " + did)
        es = [entries[d] for d in p["dialogue_ids"] if d in entries]
        for i, a in enumerate(es):
            for b in es[i + 1:]:
                if overlaps(a["box"], b["box"]): errors.append("Overlapping lettering boxes " + a["id"] + "/" + b["id"])
    report = dict(chapter_id=manifest["chapter_id"], pages=len(page_ids), panels=len(panel_map), lettering_entries=len(entries), found_clean_images=len(sources), errors=errors, warnings=warnings, image_sources=sources, lettering_fits=fits, evidence_scope="Schema, files and measured lettering only; sequence art and actual speaker-tail placement require visual review.")
    return report


def lettering_svg(entry, fit, page_size, layer="all"):
    esc = html.escape
    x, y, w, h = fit["box"]
    kind = entry["kind"]
    shape, tails = [], []
    ink = "#17151a"
    if kind == "speech":
        if entry.get("tail_anchor"):
            tx, ty = [n * s for n, s in zip(entry["tail_anchor"], page_size)]
            dx, dy = tx - (x + w / 2), ty - (y + h / 2)
            # Attach to the nearest side; an upper or side speaker must not
            # receive a tail that crosses the entire balloon.
            if not (x <= tx <= x + w and y <= ty <= y + h):
                if abs(dx) / w > abs(dy) / h:
                    edge = x + w - 3 if dx > 0 else x + 3
                    base = min(max(ty, y + .22 * h), y + .78 * h)
                    points = [(edge, base - 14), (tx, ty), (edge, base + 14)]
                else:
                    edge = y + h - 3 if dy > 0 else y + 3
                    base = min(max(tx, x + .18 * w), x + .82 * w)
                    points = [(base - 16, edge), (tx, ty), (base + 16, edge)]
                # The anchor identifies the speaker direction, not a demand to
                # draw a spear across the artwork all the way to their face.
                bx, by = (points[0][0] + points[2][0]) / 2, (points[0][1] + points[2][1]) / 2
                length = math.hypot(tx - bx, ty - by)
                if length > 120:
                    points[1] = (bx + (tx - bx) * 120 / length, by + (ty - by) * 120 / length)
                tails.append('<path d="M' + ' L'.join(f'{px:.2f},{py:.2f}' for px, py in points) + f' Z" fill="#fffdf7" stroke="{ink}" stroke-width="4"/>')
        shape.append(f'<rect x="{x:.2f}" y="{y:.2f}" width="{w:.2f}" height="{h:.2f}" rx="{min(38,h*.3):.2f}" fill="#fffdf7" stroke="{ink}" stroke-width="4"/>')
    elif kind in {"caption", "imprint"}:
        shape.append(f'<rect x="{x:.2f}" y="{y:.2f}" width="{w:.2f}" height="{h:.2f}" rx="3" fill="#f2e8d5" fill-opacity=".96" stroke="{ink}" stroke-width="3"/>')
        shape.append(f'<rect x="{x:.2f}" y="{y:.2f}" width="7" height="{h:.2f}" fill="#d67235"/>')
    elif kind == "ui":
        shape.append(f'<rect x="{x:.2f}" y="{y:.2f}" width="{w:.2f}" height="{h:.2f}" rx="5" fill="#17151a" fill-opacity=".94" stroke="#e4c29a" stroke-width="2"/>')
    fill = "#fff5de" if kind in {"title", "subtitle", "ui", "label", "digit"} else ink
    outline = ' paint-order="stroke fill" stroke="#fff9ed" stroke-width="9" stroke-linejoin="round"' if kind == "sfx" else (' paint-order="stroke fill" stroke="#17151a" stroke-width="10"' if kind in {"title", "subtitle"} else (' paint-order="stroke fill" stroke="#17151a" stroke-width="4"' if kind in {"label", "digit"} else ''))
    family = "ZSO Display" if fit["role"] == "display" else "ZSO Dialogue"
    weight = 400 if fit["role"] == "display" else 700
    start_y = y + h / 2 - (len(fit["lines"]) - 1) * fit["line_height"] / 2 + fit["size"] * .34
    spans = ''.join(f'<tspan x="{x+w/2:.2f}" y="{start_y+i*fit["line_height"]:.2f}">{esc(line)}</tspan>' for i, line in enumerate(fit["lines"]))
    bounds = esc(json.dumps(fit["box"]))
    shape.append(f'<text data-letter-id="{entry["id"]}" data-bounds="{bounds}" text-anchor="middle" font-family="{family}" font-weight="{weight}" font-size="{fit["size"]}" fill="{fill}"{outline}>{spans}</text>')
    content = tails if layer == "tails" else (shape if layer == "main" else tails + shape)
    return '<g class="letter-entry" data-id="' + entry["id"] + '">' + ''.join(content) + '</g>'


def build(manifest, dialogue, report, output):
    output.mkdir(parents=True, exist_ok=True)
    font_dir = output / "fonts"
    font_dir.mkdir(exist_ok=True)
    fonts = [paths[0] for paths in FONT_CANDIDATES.values()]
    for source in fonts + FONT_LICENSES + [ROOT / "art/fonts/sources.json"]:
        if not source.exists(): raise FileNotFoundError("Required redistributable font/license missing: " + str(source))
        shutil.copyfile(source, font_dir / source.name)
    font_css = '@font-face{font-family:"ZSO Dialogue";src:url("fonts/BarlowSemiCondensed-Bold.ttf") format("truetype");font-weight:700;font-style:normal;font-display:block;}@font-face{font-family:"ZSO Display";src:url("fonts/BebasNeue-Regular.ttf") format("truetype");font-weight:400;font-style:normal;font-display:block;}'
    css_path = ROOT / "tools/manga.css"
    inputs = [CHAPTER / "pages.json", CHAPTER / "dialogue.json", Path(__file__), css_path] + fonts + FONT_LICENSES + [ROOT / "art/fonts/sources.json"]
    source_sha = hashlib.sha256(''.join(digest(p) for p in inputs).encode()).hexdigest()
    fits = {f["id"]: f for f in report["lettering_fits"]}
    parts = []
    pw, ph = manifest["page_size_px"]
    for page in manifest["pages"]:
        page_entries = [e for e in dialogue["entries"] if e["page_id"] == page["id"]]
        overlays = ''.join(lettering_svg(e, fits[e["id"]], [pw, ph], "tails") for e in page_entries) + ''.join(lettering_svg(e, fits[e["id"]], [pw, ph], "main") for e in page_entries)
        svg = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {pw} {ph}" role="img" aria-label="Separately typed page lettering"><style>{font_css}</style>{overlays}</svg>'
        (output / (page["id"] + '.lettering.svg')).write_text(svg, encoding="utf-8")
        transcript = ' '.join(e["speaker"] + ': ' + e["text"].replace('{{resonance}}', str(manifest["print_route"]["resonance"])) for e in dialogue["entries"] if e["page_id"] == page["id"])
        clean = (ROOT / page["clean_art"]).resolve()
        clean_relative = quote(os.path.relpath(clean, output).replace(os.sep, '/'), safe='/')
        parts.append(f'<section class="manga-page page{" current" if page["number"] == 1 else ""}" id="{page["id"]}" data-number="{page["number"]}" data-clean-path="{html.escape(str(clean))}" aria-label="Page{page["number"]}: {html.escape(page["title"])}"><img class="clean-art" src="{clean_relative}" alt="{html.escape(page["title"])}"/>{svg}<div class="accessible-transcript">{html.escape(transcript)}</div></section>')
    data = dict(manifest=manifest, dialogue=dialogue, source_sha256=source_sha)
    data_json = json.dumps(data, ensure_ascii=False).replace('<', '\\u003c')
    options = ''.join(f'<option value="{p["number"]}">{p["number"]:02d} - {html.escape(p["title"])}</option>' for p in manifest["pages"])
    transcript = ''.join(f'<h3>Page{p["number"]:02d} - {html.escape(p["title"])}</h3><p>' + '<br/>'.join(html.escape(e["speaker"] + ': ' + e["text"].replace('{{resonance}}', str(manifest["print_route"]["resonance"]))) for e in dialogue["entries"] if e["page_id"] == p["id"]) + '</p>' for p in manifest["pages"])
    content = f'''<!doctype html><html lang="en"><head><meta charset="utf-8"/><meta name="viewport" content="width=device-width,initial-scale=1"/><meta name="source-sha256" content="{source_sha}"/><title>ZERO-SUM: OMEN - The Remainder</title><style>{css_path.read_text(encoding="utf-8")}</style></head><body>
<nav class="reader-bar" aria-label="Reader controls"><button id="previous">Previous</button><select id="page-select" aria-label="Page">{options}</select><button id="next">Next</button><button id="transcript-toggle" aria-expanded="false">Transcript</button></nav>
<p class="edition-note">Reference edition: resonance7 / Horseshoe. A read-only illustrated story, not a replay or gameplay controller.</p>
<main>{''.join(parts)}</main><section id="transcript" class="transcript" hidden><h2>Chapter01 transcript</h2>{transcript}</section>
<script id="manga-data" type="application/json">{data_json}</script><script>
const pages=[...document.querySelectorAll('.manga-page')], selector=document.getElementById('page-select');let index=0;
function show(n){{index=Math.max(0,Math.min(pages.length-1,n));pages.forEach((p,i)=>p.classList.toggle('current',i===index));selector.value=index+1;document.getElementById('previous').disabled=index===0;document.getElementById('next').disabled=index===pages.length-1;try{{localStorage.setItem('zso_manga_ch01_reader_page',String(index));}}catch(e){{}}}}
document.getElementById('previous').onclick=()=>show(index-1);document.getElementById('next').onclick=()=>show(index+1);selector.onchange=()=>show(Number(selector.value)-1);
document.addEventListener('keydown',e=>{{if(e.target.matches('select,input,textarea'))return;if(e.key==='ArrowRight')show(index+1);if(e.key==='ArrowLeft')show(index-1);}});
document.getElementById('transcript-toggle').onclick=e=>{{const t=document.getElementById('transcript');t.hidden=!t.hidden;e.currentTarget.setAttribute('aria-expanded',String(!t.hidden));}};
try{{show(Number(localStorage.getItem('zso_manga_ch01_reader_page')||0));}}catch(e){{show(0);}}
window.mangaReader={{show,getIndex:()=>index}};
</script></body></html>'''
    html_path = output / "chapter_01.html"
    html_path.write_text(content, encoding="utf-8")
    provenance = dict(chapter_id=manifest["chapter_id"], source_sha256=source_sha, input_files=[dict(path=str(p.relative_to(ROOT)), sha256=digest(p)) for p in inputs], image_sources=report["image_sources"], fonts=[dict(path=str(p.relative_to(ROOT)), sha256=digest(p), redistributed_as='fonts/' + p.name) for p in fonts], font_licenses=[dict(path=str(p.relative_to(ROOT)), sha256=digest(p)) for p in FONT_LICENSES], lettering_min_px=min(f["size"] for f in report["lettering_fits"]), page_count=len(manifest["pages"]), note="Build metadata and lettering fit; no artistic or Unity acceptance implied.")
    (output / "provenance.json").write_text(json.dumps(provenance, ensure_ascii=False, indent=2) + '\n', encoding="utf-8")
    (output / "validation.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding="utf-8")
    return html_path


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--check', action='store_true', help='Read-only input/file/lettering validation; no outputs')
    ap.add_argument('--schema-only', action='store_true', help='Permit absent art while validating script/layout; never produces a deliverable')
    ap.add_argument('--output-dir', default='build/manga')
    ap.add_argument('--render-pages', action='store_true')
    ap.add_argument('--game-dir', default='art/manga/chapter_01')
    ap.add_argument('--render-width', type=int, default=2336, help='Lettered page width; default matches the current native source width')
    ap.add_argument('--node', default=shutil.which('node') or 'node')
    args = ap.parse_args()
    manifest, dialogue = read_json(CHAPTER / 'pages.json'), read_json(CHAPTER / 'dialogue.json')
    report = validate(manifest, dialogue, require_art=not args.schema_only)
    summary = {k: report[k] for k in ['chapter_id', 'pages', 'panels', 'lettering_entries', 'found_clean_images', 'errors', 'warnings', 'evidence_scope']}
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    if report['errors']: return 1
    if args.check or args.schema_only: return 0
    path = build(manifest, dialogue, report, (ROOT / args.output_dir).resolve())
    print('HTML:', path)
    if args.render_pages:
        subprocess.run([args.node, str(ROOT / 'tools/render_manga.js'), str(path), str((ROOT / args.game_dir).resolve()), '--width', str(args.render_width)], check=True)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
