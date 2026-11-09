#!/usr/bin/env python3
"""Build the complete ZERO-SUM: OMEN artbook as auditable, offline HTML.

No PDF is created by this program. Render book.html with tools/render_pdf.js
after the PDF-operation marker and inspect the resulting page images.
"""
from __future__ import annotations

import argparse
from collections import Counter
from dataclasses import dataclass
from datetime import date
import hashlib
import html
import importlib.util
import json
import math
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys

from PIL import Image, ImageColor

ROOT = Path(__file__).resolve().parents[1]
VIEWS = ("front", "left", "right", "back")
LANDS = (
    ("meridian", "Meridian Undercity", "Prologue", "#FF7A2C"),
    ("hyakki", "Hyakki", "Act I", "#E34234"),
    ("river", "The River Empire", "Act II", "#00A86B"),
    ("sunyapura", "Shunyapura", "Act III", "#F4A300"),
    ("kroton", "Kroton Nova", "Act IV", "#1F6FB2"),
    ("crossroads", "The Crossroads Territory", "Act V", "#B7410E"),
    ("basilica", "The Basilica", "Finale", "#B5A642"),
)
SOURCE_DOCS = (
    "docs/DECISIONS.md", "docs/PROJECT_STATUS.md", "docs/ART_DIRECTION.md",
    "docs/ART_SPEC.md", "docs/WORLD_BIBLE.md", "docs/WORLD_ENCYCLOPEDIA.md",
    "docs/WORLD_OPERATIONS.md", "docs/LORE_LEXICON.md", "docs/LOCATIONS.md",
    "docs/CHARACTER_BIBLE.md", "docs/BOND_ARCS.md", "docs/STORY.md",
    "docs/SYSTEMS.md", "docs/NARRATIVE_STYLE.md", "docs/MANGA_DIRECTION.md",
    "docs/ARTBOOK_PRODUCTION.md", "docs/AI_DISCLOSURE.md",
    "docs/manga/MANGAKA_WORKFLOW.md", "docs/manga/README.md",
    "docs/manga/SERIES_PRODUCTION_BRIEF.md", "docs/manga/OPENING_SCRIPT_01_03.md",
    "docs/manga/CHAPTER_TREATMENT_04_22.md", "docs/manga/SERIES_REVEAL_LEDGER.md",
)
E = html.escape


def plain(value):
    if value is None:
        return "Not specified"
    if isinstance(value, dict):
        return "; ".join(f"{str(k).replace('_', ' ')}: {plain(v)}" for k, v in value.items())
    if isinstance(value, (list, tuple)):
        return "; ".join(plain(v) for v in value)
    text = str(value).strip()
    text = re.sub(r"\[([^]]+)\]\([^)]+\)", r"\1", text)
    return re.sub(r"[*`_]", "", text)


def inline(value):
    text = E(str(value))
    text = re.sub(r"\[([^]]+)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"`([^`]+)`", r"<code>\1</code>", text)
    text = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<em>\1</em>", text)
    return text


def cells(line):
    return [v.replace("\\|", "|").strip() for v in re.split(r"(?<!\\)\|", line.strip().strip("|"))]


@dataclass
class Block:
    markup: str
    weight: int
    heading: str = ""


def markdown_blocks(text):
    """Convert sources to short editorial blocks, never eight-column mini-tables."""
    lines = text.splitlines()
    result = []
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if not line or re.fullmatch(r"[-*_]{3,}", line):
            i += 1
            continue
        if line.startswith("# "):
            i += 1
            continue
        if line.startswith("##"):
            title = re.sub(r"^#+\s*", "", line)
            result.append(Block(f'<h3>{inline(title)}</h3>', 170, plain(title)))
            i += 1
            continue
        if line.startswith("```"):
            rows = []
            i += 1
            while i < len(lines) and not lines[i].strip().startswith("```"):
                rows.append(lines[i])
                i += 1
            # Long source examples are wrapped paragraphs, not cropped code images.
            code = "\n".join(rows)
            result.append(Block(f'<pre>{E(code)}</pre>', len(code) + 140))
            i += 1
            continue
        if line.startswith("|") and i + 1 < len(lines) and re.search(r"\|\s*:?-{2,}", lines[i + 1]):
            headers = cells(line)
            i += 2
            while i < len(lines) and lines[i].strip().startswith("|"):
                row = cells(lines[i])
                row += [""] * max(0, len(headers) - len(row))
                if any(row):
                    title = row[0] or headers[0]
                    detail = "".join(f'<div><dt>{inline(k)}</dt><dd>{inline(v)}</dd></div>'
                                     for k, v in zip(headers[1:], row[1:]) if v.strip())
                    markup = f'<article class="entry"><h4>{inline(title)}</h4><dl>{detail}</dl></article>'
                    # A labelled field consumes a line even when its value is short.
                    result.append(Block(markup, sum(len(v) for v in row) + 120 + 125 * len(row)))
                i += 1
            continue
        if re.match(r"^(?:[-*]|\d+\.)\s", line):
            item = re.sub(r"^(?:[-*]|\d+\.)\s+", "", line)
            result.append(Block(f'<p class="bullet">{inline(item)}</p>', len(item) + 35))
            i += 1
            continue
        paragraph = [line]
        i += 1
        while i < len(lines):
            nxt = lines[i].strip()
            if not nxt or nxt.startswith(("#", "|", "```")) or re.match(r"^(?:[-*]|\d+\.)\s", nxt):
                break
            paragraph.append(nxt)
            i += 1
        prose = " ".join(paragraph)
        # Split long paragraphs on sentences; keep every sentence.
        sentences = re.split(r"(?<=[.!?])\s+(?=[A-Z])", prose)
        chunk = ""
        for sentence in sentences:
            if chunk and len(chunk) + len(sentence) > 1100:
                result.append(Block(f'<p>{inline(chunk)}</p>', len(chunk) + 30))
                chunk = sentence
            else:
                chunk += (" " if chunk else "") + sentence
        if chunk:
            result.append(Block(f'<p>{inline(chunk)}</p>', len(chunk) + 30))
    return result


def chapters(text):
    chunks = re.split(r"(?m)^##\s+", text)
    out = []
    for chunk in chunks[1:]:
        title, _, body = chunk.partition("\n")
        out.append((plain(title), body))
    return out


def read_doc(rel):
    path = ROOT / rel
    return path.read_text(encoding="utf-8-sig") if path.exists() else ""


def load_catalog():
    path = ROOT / "art/catalog/characters.json"
    if path.exists():
        data = json.loads(path.read_text(encoding="utf-8-sig"))
        return data.get("entries", data if isinstance(data, list) else [])
    source = ROOT / "tools/cast.py"
    if not source.exists():
        return []
    spec = importlib.util.spec_from_file_location("fullbook_cast", source)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    result = []
    for c in mod.CAST:
        look = c.get("look", {})
        result.append(dict(
            id=c["key"], name=c["name"], group=c["group"], role=c["role"],
            region=c.get("land", ""), height_m=c.get("h"), outfit=c.get("outfit", ""),
            age="See Character Bible", pronouns="See Character Bible", silhouette=c.get("body", look.get("body", "human")),
            palette=[dict(name=n, hex=v) for n, v in c.get("palette", [])],
            appearance=dict(costume=c.get("spec", "Source-model construction; current Character Bible governs final design.")),
            props=[p[0] for p in look.get("props", [])], canon_locks=c.get("locks", []),
            power=dict(status="Full-game specification; consult SYSTEMS for exact contracts."),
            design_rationale="First-draft volume, costume and scale reference; not a final face, hand, rig or runtime asset.",
            source_documents=["docs/CHARACTER_BIBLE.md", "tools/cast.py"],
            view_paths={v:f'art/cast/views/{c["key"]}_{v}.png' for v in VIEWS},
            source3d_path="art/cast/zso_cast_blockout.blend",
            provenance=dict(status="Imported first-draft blockout", render_status="Not final production art")))
    return result


class Book:
    def __init__(self, output, build_date):
        self.output = output
        self.build_date = build_date
        self.pages = []
        self.assets = {}
        self.missing = []
        self.parts = []
        self.character_pages = []
        self.illustrated_pages = []
        self.print_derivatives = []
        self.illustrated_requests = []
        self.used_illustrations = set()
        request_path = ROOT / 'art/catalog/higgsfield_artbook_requests.json'
        if request_path.is_file():
            self.illustrated_requests = json.loads(request_path.read_text(encoding='utf-8-sig')).get('requests', [])

    def illustrated_board(self, request, title, part, accent):
        """Generated design candidates remain separate from actual Blender cameras."""
        key = request.get('request_id')
        path = request.get('output_target')
        if key in self.used_illustrations or not path or not (ROOT / path).is_file():
            return None
        with Image.open(ROOT / path) as im:
            im.verify()
        self.used_illustrations.add(key)
        self.url('art/catalog/higgsfield_artbook_requests.json')
        caption = ('AI illustrated design candidate / four-view visual proposal. This is a painted/inked concept, not a 3D render. '
                   'The following actual camera drafts, specifications and canon locks remain separate evidence; final anatomy, asymmetry, prop construction and runtime acceptance require their own checks.')
        if request.get('kind') == 'environment_three_view':
            caption = ('AI painted environment concept / matched-view visual proposal. Not an engine screenshot or a camera render. '
                       'Actual Blender plan, 2.5D and front drafts follow separately; matching landmarks, collision, stage clearance and runtime layers require validation.')
        if 'vetala' in request.get('catalog_ids', []):
            caption = ('Neutral upright costume proposal / illustrated concept candidate, not a hanging-pose or motion study. '
                       'The separate actual Blender camera references show the banyan-bound hanging construction. This drawing does not replace those pose references or certify a runtime rig.')
        image = self.print_image(path, 'illustrated-board-image', caption)
        page = self.page(title, part, image, 'illustrated-board', source=str(key)+' / illustrated concept candidate', accent=accent)
        self.illustrated_pages.append(dict(request_id=key, path=path, page=page, status='illustrated concept candidate; not accepted runtime art'))
        return page

    def print_image(self, rel, cls, caption, *, url_only=False):
        """Content-addressed book-only JPEG; source illustration stays untouched."""
        source = ROOT / rel
        self.url(rel)
        source_hash = hashlib.sha256(source.read_bytes()).hexdigest()
        cache = self.output / 'print-assets'
        cache.mkdir(parents=True, exist_ok=True)
        name = source_hash[:24]+'-w2400-q90.jpg'
        target = cache / name
        if not target.is_file():
            with Image.open(source) as original:
                original.thumbnail((2400, 2400), Image.Resampling.LANCZOS)
                if original.mode in ('RGBA','LA') or 'transparency' in original.info:
                    rgba = original.convert('RGBA')
                    picture = Image.new('RGB', rgba.size, ImageColor.getrgb('#F2E8D5'))
                    picture.paste(rgba, mask=rgba.getchannel('A'))
                else:
                    picture = original.convert('RGB')
                picture.save(target, 'JPEG', quality=90, optimize=True, progressive=True)
        with Image.open(target) as im:
            width, height = im.size
        record = dict(source_path=rel, source_sha256=source_hash,
                      print_path='print-assets/'+name, width=width, height=height,
                      bytes=target.stat().st_size, quality=90,
                      sha256=hashlib.sha256(target.read_bytes()).hexdigest())
        self.print_derivatives.append(record)
        if url_only:
            return record['print_path']
        return f'<figure class="{E(cls)}"><img src="{E(record["print_path"])}" alt="{E(caption)}"><figcaption>{E(caption)}</figcaption></figure>'

    def url(self, rel):
        path = ROOT / str(rel)
        if not path.is_file():
            return None
        self.assets[str(rel).replace("\\", "/")] = hashlib.sha256(path.read_bytes()).hexdigest()
        return Path(os.path.relpath(path, self.output)).as_posix()

    def image(self, rel, cls="", caption="", required=False):
        if rel and str(rel).startswith(('art/cast/views/', 'art/envs/')) and (ROOT / rel).is_file():
            return self.print_image(rel, cls, caption)
        url = self.url(rel) if rel else None
        if not url:
            if required:
                self.missing.append(str(rel or "unassigned view"))
            return f'<div class="asset-gap"><b>Specification only</b><span>{E(caption or "This view has no accepted render.")}</span></div>'
        cap = f'<figcaption>{E(caption)}</figcaption>' if caption else ""
        return f'<figure class="{E(cls)}"><img src="{E(url)}" alt="{E(caption)}">{cap}</figure>'

    def page(self, title, part, body, cls="", source="", accent="#FF7A2C"):
        number = len(self.pages) + 1
        fragment = f'''<section class="page {E(cls)}" id="page-{number}" style="--accent:{E(accent)}">
          <header><div class="eyebrow">{E(part)}</div><h2>{E(title)}</h2></header>
          <main class="page-content col-text" data-overflow-check>{body}</main>
          <footer><span>ZERO-SUM: OMEN / {E(part)}</span><span>{E(source)}</span><b>{number:03d}</b></footer>
          </section>'''
        self.pages.append(dict(number=number, title=title, part=part, source=source, html=fragment))
        return number

    def opener(self, number, title, subtitle, image=None):
        self.parts.append(dict(title=title, page=len(self.pages) + 1))
        art = self.image(image, "opener-image") if image else ""
        self.page(title, f"PART {number}", f'{art}<div class="opener-copy"><div class="part-number">{E(number)}</div><h1>{E(title)}</h1><p>{E(subtitle)}</p></div>', "opener dark")

    def document(self, rel, part, title=None, budget=3800, skip_sections=()):
        content = read_doc(rel)
        if not content:
            self.missing.append(rel)
            return
        self.url(rel)
        doc_title = title or plain(content.splitlines()[0].lstrip("# "))
        blocks = markdown_blocks(content)
        if skip_sections:
            filtered = []
            skip = False
            for block in blocks:
                if block.heading:
                    skip = any(s.casefold() in block.heading.casefold() for s in skip_sections)
                if not skip:
                    filtered.append(block)
            blocks = filtered
        page_blocks, weight, sub = [], 0, 1
        for block in blocks:
            if page_blocks and weight + block.weight > budget:
                if page_blocks[-1].heading:
                    carry = page_blocks.pop()
                else:
                    carry = None
                self.page(doc_title if sub == 1 else f"{doc_title} / {sub}", part,
                          '<div class="prose">' + "".join(x.markup for x in page_blocks) + '</div>', source=rel)
                sub += 1
                page_blocks = [carry] if carry else []
                weight = carry.weight if carry else 0
            page_blocks.append(block)
            weight += block.weight
        if page_blocks:
            self.page(doc_title if sub == 1 else f"{doc_title} / {sub}", part,
                      '<div class="prose">' + "".join(x.markup for x in page_blocks) + '</div>', source=rel)

    def fresh_study(self, key, name, rationale, accent):
        rel = next((f"art/concepts/fresh/chr_{key}_{v}.png" for v in ("v5", "v4")
                    if (ROOT / f"art/concepts/fresh/chr_{key}_{v}.png").exists()), None)
        if not rel:
            return
        art = self.image(rel, "fresh-hero", "Fresh concept illustration / visual-development candidate")
        self.page(name, "Fresh design direction", f'<div class="fresh-split"><div class="fresh-copy"><div class="big-index">{E(key.upper())}</div><p class="standfirst">{E(rationale)}</p><p>Detailed ink carries material, wear and mechanism. Broad cloth planes preserve the silhouette. This image is a visual reference, not a completed turntable, layered rig or runtime pose set.</p><div class="status-label">CONCEPT / FRESH PASS</div></div>{art}</div>', "fresh dark", source=rel, accent=accent)
        url = self.url(rel)
        positions = {"nil":[("Decoder / interrupted ring", "28% 28%"), ("Abacus clasps / repaired seam", "53% 42%"), ("Ledger lining / working wear", "52% 70%")],
                     "vesper":[("Dealer tailoring / removed insignia", "42% 36%"), ("Tell-counter / worn cuff", "74% 47%"), ("Bespoke firearm / pocket lining", "37% 58%")],
                     "varro":[("Mask repair / human beneath", "48% 12%"), ("Confiscation vault / release levers", "66% 53%"), ("Ledger armour / protected token", "49% 28%")]}[key]
        panels = "".join(f'<figure class="detail"><div style="background-image:url(\'{E(url)}\');background-position:{pos}"></div><figcaption>{E(label)}</figcaption></figure>' for label, pos in positions)
        self.page(f"{name} / the useful detail", "Fresh design direction", f'<p class="standfirst">A costume is a record of work, allegiance and damage.</p><div class="detail-grid">{panels}</div><div class="detail-notes"><p>Macro crops reveal the construction language of this design. They do not replace mechanical dimensions or validate anatomy, handedness, chamber counts or deformation. Those remain explicit checks against the fixed spec.</p><p>Do not copy a patch onto another character merely to add complexity. Detail earns its place when it identifies a profession, a repaired failure or a choice.</p></div>', source=rel, accent=accent)

    def faction_pages(self):
        text = read_doc("docs/WORLD_ENCYCLOPEDIA.md")
        section = next((body for title, body in chapters(text) if "faction" in title.lower()), "")
        rows = []
        lines = section.splitlines()
        for i, line in enumerate(lines):
            if line.strip().startswith("|") and i + 1 < len(lines) and re.search(r"\|\s*:?-{2,}", lines[i + 1]):
                headers = cells(line)
                j = i + 2
                while j < len(lines) and lines[j].strip().startswith("|"):
                    row = cells(lines[j]); row += [""] * (len(headers) - len(row))
                    rows.append(dict(zip(headers, row)))
                    j += 1
                break
        mapping = [("basilica", "f_ledger_priest", "thale"), ("collector", "f_collector", "varro"),
                   ("bazaar", "f_charmpunk", "maeve"), ("remainder", "f_remainder", "ama"),
                   ("yokai", "hina", "tamamo"), ("exchange", "f_broker", "ba"),
                   ("ten courts", "judge_cui", "bai_si"), ("observatory", "f_pilgrim", "shunya"),
                   ("synod", "f_synod", "prima"), ("house", "f_dealer", "house"),
                   ("open hand", "brother_nought", "stranger")]
        for row in rows:
            name = plain(next(iter(row.values())))
            match = next((m for m in mapping if m[0] in name.lower()), None)
            images = ""
            if match:
                images = self.image(f"art/cast/views/{match[1]}_front.png", "faction-figure", "Uniform / first-draft model") + self.image(f"art/cast/views/{match[2]}_front.png", "faction-figure", "Individual expression / first-draft model")
            facts = "".join(f'<div><dt>{inline(k)}</dt><dd>{inline(v)}</dd></div>' for k, v in list(row.items())[1:] if v)
            self.page(name, "Factions and visual authority", f'<div class="faction-layout"><div><p class="standfirst">Materials signal who controls the count.</p><dl class="spec-facts">{facts}</dl><p class="small-note">Uniforms establish institutions; individuals may dissent. These model studies identify volume and palette, not a finished costume/face/rig.</p></div><div class="faction-pair">{images}</div></div>', source="WORLD_ENCYCLOPEDIA / CHARACTER_BIBLE")

    def lookdev_pages(self):
        for key, title, caption in (
            ("omen_battle_v5", "A frame with a readable intention", "Blender look-development composition. Character planes remain separate from exact labels and the reel; this is a designed render, not gameplay."),
            ("vesper_cylinder_detail_v5", "Seven chambers / one mechanism", "A locally modelled prop study with seven physical through-bores around a solid axle. Geometry makes the count inspectable; the mechanism is a draft, not a complete firearm or animation rig."),
            ("meridian_clay_v5", "The space beneath the paint", "Reproducible geometry, camera and actor staging. The clay view exposes the layout choices behind the composed frame."),
        ):
            rel = f"art/renders/lookdev/{key}.png"
            if (ROOT / rel).is_file():
                self.page(title, "Reproducible design studies", self.image(rel, "showcase-image", caption), "showcase", source="tools/build_lookdev.py / art/source")
        hound = "art/concepts/fresh/enm_debthound_v5.png"
        if (ROOT / hound).is_file():
            self.page("The Debt Hound / work made animal", "Fresh design direction", f'<div class="hound-layout">{self.image(hound, "hound-concept", "Fresh enemy concept / visual-development candidate")}<aside><p class="standfirst">Enforcement has a body language.</p><p>A recognisable hound outline carries brass counting machinery and the material grammar of the Collectors. Its readable wheel anchor belongs to runtime presentation; generated writing is not gameplay data.</p><p>This is an invented construct. Its defeat is mechanical exhaustion, without animal gore. The four-view blockout and runtime pose set must be validated separately.</p></aside></div>', source=hound)

    def region_pages(self):
        location = read_doc("docs/LOCATIONS.md")
        chunks = chapters(location)
        for key, name, act, accent in LANDS:
            request = next((r for r in self.illustrated_requests if r.get('kind')=='environment_three_view' and r.get('region_id')==key), None)
            if request:
                self.illustrated_board(request, name+' / painted world', 'Refined environment concepts', accent)
            token = {"meridian":"Meridian", "hyakki":"Hyakki", "river":"River Empire",
                     "sunyapura":"Śūnyapura", "kroton":"Kroton Nova", "crossroads":"Crossroads",
                     "basilica":"Basilica"}[key]
            source = next((body for title, body in chunks if token.casefold() in title.casefold()), "")
            facts = [re.sub(r"^-\s*", "", x.strip()) for x in source.splitlines() if x.strip().startswith("-")]
            lead = " ".join(plain(x) for x in facts[:2])
            iso_caption = "2.5D Ward district massing / tower continues beyond frame" if key == 'meridian' else "2.5D orthographic / first-draft environment"
            iso = self.image(f"art/envs/{key}_iso.png", "region-hero", iso_caption, required=True)
            self.page(name, f"The lands / {act}", f'<div class="region-layout"><div class="region-copy"><div class="land-id">{E(key.upper())}</div><p class="standfirst">{E(lead)}</p><p>Architectural massing and depth are first-draft references. Painted materials, navigation, collisions, actor placement and camera motion need their own runtime checks.</p><div class="status-label">ENVIRONMENT / DRAFT 01</div></div>{iso}</div>', "region dark", source="LOCATIONS / art/envs", accent=accent)
            views = self.image(f"art/envs/{key}_top.png", "region-view", "TOP / spatial plan", required=True) + self.image(f"art/envs/{key}_front.png", "region-view", "FRONT / battle staging", required=True)
            notes = "".join(f'<p>{inline(x)}</p>' for x in facts[2:])
            self.page(f"{name} / space and daily life", "The lands", f'<div class="environment-views">{views}</div><div class="environment-notes prose">{notes}</div>', "environment-sheet", source="docs/LOCATIONS.md", accent=accent)

    def character(self, c):
        key, name = str(c["id"]), c["name"]
        accent = next((p.get("hex") for p in c.get("palette", []) if isinstance(p, dict) and p.get("hex")), "#FF7A2C")
        request = next((r for r in self.illustrated_requests if key in r.get('catalog_ids', [])), None)
        if request:
            self.illustrated_board(request, request.get('name',name)+' / inked construction', 'Refined illustrated concepts', accent)
        view_paths = c.get("view_paths", {})
        sizes = {}
        for view in VIEWS:
            candidate = view_paths.get(view)
            if candidate and (ROOT / candidate).is_file():
                with Image.open(ROOT / candidate) as im: sizes[view] = im.size
        # One pixel-to-mm scale across the four renders; never fit each view independently.
        k = min(179 / sum(w for w, _ in sizes.values()), 95 / max(h for _, h in sizes.values())) if sizes else 0.1
        view_cards = ""
        for view in VIEWS:
            path = view_paths.get(view)
            if view in sizes:
                width, height = sizes[view]
                url = self.print_image(path, '', '', url_only=True)
                view_cards += f'<div class="turn-view" style="width:{width*k:.3f}mm"><figure class="turn-image"><img src="{E(url)}" style="width:{width*k:.3f}mm;height:{height*k:.3f}mm" alt="{E(name)} {view}"><figcaption>{view.upper()}</figcaption></figure></div>'
            else:
                self.missing.append(f"character:{key}/{view}")
                view_cards += f'<div class="turn-view missing-view">{self.image(path, "turn-image", view.upper())}</div>'
        palette = "".join(f'<div class="palette-swatch"><i style="background:{E(p.get("hex", "#888"))}"></i><span>{E(p.get("name", ""))}<b>{E(p.get("hex", ""))}</b></span></div>' for p in c.get("palette", []) if isinstance(p, dict))
        identity = [("Role", c.get("role")), ("Region", c.get("region")), ("Outfit", c.get("outfit")),
                    ("Height", f'{c.get("height_m")} m' if c.get("height_m") else "Not assigned"),
                    ("Age / pronouns", f'{plain(c.get("age"))} / {plain(c.get("pronouns"))}'), ("Silhouette", c.get("silhouette"))]
        facts = "".join(f'<div><dt>{E(label)}</dt><dd>{E(plain(value))}</dd></div>' for label, value in identity if value)
        locks = "".join(f'<li>{E(plain(x))}</li>' for x in c.get("canon_locks", []))
        provenance = c.get("provenance", {})
        self.character_pages.append(dict(id=key, name=name, page=len(self.pages) + 1))
        self.page(name + (f' / {c["outfit"]}' if c.get("outfit") else ""), str(c.get("group", "Character catalog")),
                  f'<div class="turn-layout"><div class="turn-main"><div class="turn-row">{view_cards}</div><div class="palette">{palette}</div><p class="small-note">FRONT / wearer LEFT / wearer RIGHT / BACK. Actual camera drafts; shared scale within this sheet. Printed scale varies between pages. Recorded heights are design specifications, not verification of these draft dimensions. Current canon governs final production.</p></div><aside><dl class="spec-facts">{facts}</dl><h4>Canon locks</h4><ul class="locks">{locks or "<li>Current Character Bible governs.</li>"}</ul><p class="status-label">{E(plain(provenance.get("status", "Draft model")))}</p></aside></div>', "character-turn", source=key + " / CHARACTER_BIBLE", accent=accent)
        appearance = c.get("appearance", {})
        appearance_fields = [(k, v) for k, v in appearance.items() if v]
        appearance_html = "".join(f'<p class="appearance-line"><strong>{E(k.replace("_", " ").title())}.</strong> {E(plain(v))}</p>' for k, v in appearance_fields)
        props = "".join(f'<li>{E(plain(p))}</li>' for p in c.get("props", []))
        power = c.get("power", {})
        power_html = "".join(f'<div><dt>{E(k.replace("_", " ").title())}</dt><dd>{E(plain(v))}</dd></div>' for k, v in power.items() if v)
        visible_provenance = {k:provenance[k] for k in ("status", "render_scope", "height_status") if k in provenance}
        body = f'<div class="dossier-layout"><div><h3>Construction and all-side specification</h3><div class="dossier-appearance">{appearance_html}</div><h3>Props and work</h3><ul>{props or "<li>No special prop assigned.</li>"}</ul></div><div><h3>Power and use</h3><dl class="spec-facts">{power_html}</dl><h3>Design rationale</h3><p>{E(plain(c.get("design_rationale", "")))}</p><div class="provenance-box"><h4>Evidence and readiness</h4><p>{E(plain(visible_provenance))}</p><p>Sources: {E(plain(c.get("source_documents", [])))}</p><p>3D source: {E(str(c.get("source3d_path", "Not supplied")))}</p></div></div></div>'
        self.page(f"{name} / design dossier", str(c.get("group", "Character catalog")), body, "character-dossier", source=key + " / art/catalog/characters.json", accent=accent)

    def manga_excerpt(self):
        self.page("A story that earns its turns", "Manga and game", '<div class="prose"><h3>Current edition:22 chapters,30 pages each</h3><p>The current target is660 black-and-white story pages through Higgsfield Mangaka. The former20-page colour adaptation was rejected by the user for weak flow, expression, emotion and hook; its panels are excluded from this edition. A completed image job did not establish an accepted comic.</p><h3>Story before pages</h3><p>A new90-page opening script gives NIL a personal want, a costly rescue, voluntary Naming, a failed hope, earned trust with Vesper and a consequential mercy. Nineteen further chapter treatments and a reveal ledger schedule the full story,32 core relationship stages and eight proofs. Native chapter output remains a separate production gate.</p><h3>Reuse with evidence</h3><p>Preserve native Mangaka chapter exports, exact page counts, reading order, cast/world references, transcript and panel metadata where export supports it. A collectible reader is read-only; a live game adapter yields to actual choices and combat. Colour covers, backs, inserts and lore are separate from660 B&amp;W story pages. No runtime integration is implied by a book or manuscript.</p></div>', source="docs/manga/README / MANGAKA_WORKFLOW")

    def write(self):
        self.output.mkdir(parents=True, exist_ok=True)
        css = ROOT / "tools/full_artbook.css"
        shutil.copyfile(css, self.output / "full_artbook.css")
        for path in SOURCE_DOCS:
            if (ROOT / path).is_file(): self.url(path)
        catalog = ROOT / "art/catalog/characters.json"
        if catalog.exists(): self.url("art/catalog/characters.json")
        source_sha = hashlib.sha256(json.dumps(self.assets, sort_keys=True).encode()).hexdigest()
        try:
            revision = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip()
        except (OSError, subprocess.CalledProcessError): revision = "unknown"
        toc = "".join(f'<div><span>{E(p["title"])}</span><b>{p["page"]:03d}</b></div>' for p in self.parts)
        for p in self.pages:
            p["html"] = p["html"].replace("<!--CONTENTS-->", toc)
        audit_js = '''<script>window.addEventListener('load',async()=>{await document.fonts.ready;window.__artbookAudit={pages:document.querySelectorAll('section.page').length,missingImages:[...document.images].filter(i=>!i.complete||!i.naturalWidth).map(i=>i.src),overflow:[...document.querySelectorAll('[data-overflow-check]')].filter(e=>e.scrollHeight>e.clientHeight+2||e.scrollWidth>e.clientWidth+2).map(e=>({page:e.closest('section.page').id,scrollHeight:e.scrollHeight,clientHeight:e.clientHeight,text:e.textContent.slice(0,80)}))};document.documentElement.dataset.layoutAudit=window.__artbookAudit.overflow.length?'fail':'pass';});</script>'''
        body = "".join(p["html"] for p in self.pages)
        doc = f'<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="source-sha256" content="{source_sha}"><meta name="viewport" content="width=device-width,initial-scale=1"><title>ZERO-SUM: OMEN - Complete World and Artbook</title><link rel="stylesheet" href="full_artbook.css"></head><body>{body}{audit_js}</body></html>'
        (self.output / "book.html").write_text(doc, encoding="utf-8")
        manifest = dict(schema_version=1, build_date=self.build_date, source_revision=revision,
                        source_sha256=source_sha, format="A4 landscape / offline HTML",
                        pages=[{k:v for k,v in p.items() if k != "html"} for p in self.pages],
                        character_index=self.character_pages, illustrated_concept_pages=self.illustrated_pages,
                        illustrated_print_derivatives=self.print_derivatives, asset_sha256=self.assets,
                        missing_assets=sorted(set(self.missing)),
                        status="HTML built. PDF rendering and visual QA are separate, unclaimed operations.")
        (self.output / "build-manifest.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        return manifest


def build(output, build_date):
    book = Book(output, build_date)
    env = next((p for p in ("art/concepts/fresh/env_meridian_v5.png", "art/concepts/refined/env_meridian_empty_v3.png", "art/concepts/env_meridian_establishing.jpg") if (ROOT/p).exists()), None)
    bg = book.image(env, "cover-background") if env else ""
    hero = book.image("art/concepts/fresh/chr_nil_v5.png", "cover-hero")
    book.page("ZERO-SUM: OMEN", "World and visual development", f'{bg}<div class="cover-shade"></div><div class="cover-title"><span>WORLD / PEOPLE / POSSIBILITY</span><h1>ZERO-SUM<br><em>OMEN</em></h1><p>The complete world and artbook</p><small>{E(build_date)} / AI-authored visual development</small></div>{hero}', "cover dark")
    book.page("How to read this world", "Colophon", '<div class="colophon-grid"><div><h3>One world. Several kinds of evidence.</h3><p class="standfirst">People are not the number above their heads.</p><p>This volume unites the written world, fixed art direction, factions, environments, full character catalog and a companion manga production. It records authored intent and visible drafts without mistaking either for a shipping game.</p><p>Fresh concepts carry the current design direction. Imported four-view models and regional scenes are first-draft 3D references. Their simple geometry does not validate faces, hands, costumes, cultural representation, animation or gameplay.</p><p>Current adopted decisions supersede historical source-model details. The source corpus and every included image are fingerprinted in the accompanying build manifest.</p></div><div><h3>Contents</h3><nav class="contents"><!--CONTENTS--></nav><div class="provenance-box"><b>Original direction</b><p>Detailed ink, cinematic geography, expressive comedy, tactile luck machinery and matte painted worlds. References inform craft, not copied characters, panels, likenesses or the signature of a named living artist.</p><p>Created through AI-authored writing, code, image generation and local rendering. No manual finishing or external cultural approval is implied.</p></div></div></div>', source="DECISIONS / PROJECT_STATUS")
    book.opener("01", "A fixed visual language", "A silhouette first. A profession second. A life in the details.", env)
    book.document("docs/ART_DIRECTION.md", "The visual language", "Painted world, inked people")
    book.document("docs/ART_SPEC.md", "The visual language", "Fixed production specification")
    for values in (("nil", "NIL / the Remainder", "A salvaged actuary's instrument becomes a coat: interrupted circles, abacus locks and repairs that refuse to erase a person.", "#FF7A2C"),
                   ("vesper", "Vesper Sette", "Dealer tailoring and an altered house uniform make bravado legible as a practiced defence.", "#E5243B"),
                   ("varro", "Varro Kade", "A walking confiscation office: ledger covers become armour, a jar becomes a vault, and a private token survives the uniform.", "#B7410E")):
        book.fresh_study(*values)
    book.lookdev_pages()
    book.opener("02", "The world that counts", "Physics, institutions, work and ordinary life under the Dawn Tally.")
    book.document("docs/WORLD_ENCYCLOPEDIA.md", "World encyclopedia", "The Tally at work", skip_sections=("Factions and their styles", "History and timeline"))
    if (ROOT / "docs/WORLD_OPERATIONS.md").exists():
        book.document("docs/WORLD_OPERATIONS.md", "World operations", "How a day works")
    book.document("docs/LORE_LEXICON.md", "History and vocabulary", "The record beneath the myth")
    book.document("docs/DECISIONS.md", "The logic of power", "The rules that do not change")
    book.opener("03", "Who owns the count?", "Faction materials are visible arguments about power.")
    book.faction_pages()
    book.opener("04", "Seven places to stand", "Plan, depth and battle geography. Every region keeps its own ordinary life.", env)
    book.region_pages()
    book.opener("05", "People before numbers", "Every model, outfit and role: four-view drafts with construction, power and continuity specifications.")
    catalog = load_catalog()
    last_group = None
    for c in catalog:
        group = c.get("group", "Character catalog")
        if group != last_group:
            book.parts.append(dict(title=f"Cast / {group}", page=len(book.pages) + 1))
            last_group = group
        book.character(c)
    book.opener("06", "A story built to return", "Clues become consequences. A repeated image changes meaning.")
    book.document("docs/STORY.md", "Campaign and consequences", "The campaign")
    book.document("docs/NARRATIVE_STYLE.md", "Voice and comedy", "Words, silence and wit")
    book.opener("07", "Ink that can move", "A Mangaka-native series: story, performance and earned reveals before production.")
    if (ROOT / "docs/manga/MANGAKA_WORKFLOW.md").exists(): book.document("docs/manga/MANGAKA_WORKFLOW.md", "Manga direction", "Mangaka production and acceptance", budget=4200)
    book.manga_excerpt()
    book.opener("08", "From reference to build", "Sources, limits, checks and the work that remains.")
    book.document("docs/ARTBOOK_PRODUCTION.md", "Production and provenance", "Reproducible visual production")
    book.document("docs/AI_DISCLOSURE.md", "Production and provenance", "AI use and evidence")
    index_rows = [f'<div><b>{E(c["name"])}</b><span>{E(c["id"])} / {c["page"]:03d}</span></div>' for c in book.character_pages]
    for start in range(0, len(index_rows), 32):
        book.page("Character index", "Reference", '<div class="character-index">' + "".join(index_rows[start:start+32]) + '</div>', source="art/catalog/characters.json")
    sources = '<ul>' + "".join(f'<li>{E(p)}</li>' for p in SOURCE_DOCS if (ROOT/p).exists()) + '</ul>'
    book.page("The source is part of the work", "Source index", f'<div class="prose"><h3>Authoritative Markdown and catalog</h3>{sources}<h3>Rebuild and verification</h3><p>Run python tools/build_full_artbook.py --output-dir build/full-artbook. The HTML and manifest contain page counts, asset fingerprints, missing-view coverage and source revision. Render offline with tools/render_pdf.js after the artifact-operation marker. Inspect page images and the browser layout audit; an HTML build is not a visual approval.</p><h3>What this volume does not certify</h3><p>Not a Unity build, rig certification, rights clearance, cultural sign-off, player study, platform approval or promise that every concept has a game-ready asset. Any missing view is labelled specification-only and remains in the coverage report.</p></div>', source="Build manifest / repository sources")
    return book, book.write()


def validate_catalog(catalog):
    errors, warnings = [], []
    seen = set()
    for entry in catalog:
        key = entry.get("id")
        if not key or key in seen: errors.append(f"Missing/duplicate character id: {key}")
        seen.add(key)
        h = entry.get("height_m")
        if h is not None and (not isinstance(h, (int, float)) or not math.isfinite(h) or h <= 0):
            errors.append(f"Invalid height: {key}")
        for view in VIEWS:
            path = entry.get("view_paths", {}).get(view)
            if not path or not (ROOT / path).is_file(): warnings.append(f"{key}: missing {view}")
            else:
                try:
                    with Image.open(ROOT / path) as im: im.verify()
                except Exception as exc: errors.append(f"{key}/{view}: invalid image: {exc}")
        source = entry.get("source3d_path")
        if source and not (ROOT / source).is_file(): warnings.append(f"{key}: missing 3D source {source}")
    return errors, warnings


def check_layout(output, node="node", previews=""):
    """Browser measurements and optional PNG/JPEG previews; never writes a PDF."""
    script = r'''
const {chromium}=require('playwright');
const fs=require('fs');const path=require('path');const {pathToFileURL}=require('url');
(async()=>{const [folder,requested]=process.argv.slice(1);const launch={};
if(process.env.PLAYWRIGHT_CHROMIUM_EXECUTABLE_PATH)launch.executablePath=process.env.PLAYWRIGHT_CHROMIUM_EXECUTABLE_PATH;
const browser=await chromium.launch(launch);try{const page=await browser.newPage({viewport:{width:1200,height:900}});
const failed=[];await page.route('**/*',async r=>/^https?:/i.test(r.request().url())?r.abort():r.continue());
page.on('requestfailed',r=>failed.push(r.url()));await page.goto(pathToFileURL(path.join(folder,'book.html')).href,{waitUntil:'load',timeout:120000});
await page.emulateMedia({media:'print'});await page.evaluate(()=>document.fonts.ready);
const audit=await page.evaluate(()=>{const regions=[...document.querySelectorAll('[data-overflow-check],section.page>header')];
return{pages:document.querySelectorAll('section.page').length,missingImages:[...document.images].filter(i=>!i.complete||!i.naturalWidth).map(i=>i.getAttribute('src')),
overflow:regions.filter(e=>e.scrollHeight>e.clientHeight+2||e.scrollWidth>e.clientWidth+2).map(e=>({page:e.closest('section.page').id,region:e.tagName,
scrollHeight:e.scrollHeight,clientHeight:e.clientHeight,scrollWidth:e.scrollWidth,clientWidth:e.clientWidth,text:e.textContent.slice(0,100)}))};});
audit.failedRequests=failed;fs.writeFileSync(path.join(folder,'layout-report.json'),JSON.stringify(audit,null,2)+'\n');
if(requested){const ids=requested==='all'?Array.from({length:audit.pages},(_,i)=>i+1):requested.split(',').map(Number);
fs.mkdirSync(path.join(folder,'preview'),{recursive:true});for(const n of ids){if(n<1||n>audit.pages)continue;
await page.locator('#page-'+n).screenshot({path:path.join(folder,'preview',String(n).padStart(3,'0')+'.jpg'),type:'jpeg',quality:82});}}
console.log(JSON.stringify(audit,null,2));if(audit.missingImages.length||audit.overflow.length||failed.length)process.exitCode=1;
}finally{await browser.close();}})().catch(e=>{console.error(e);process.exitCode=1;});'''
    return subprocess.run([node, "-e", script, str(output.resolve()), previews], cwd=ROOT).returncode


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", default="build/full-artbook")
    parser.add_argument("--date", default="2026-11-08", help="Source snapshot date, not execution-host timezone")
    parser.add_argument("--check", action="store_true", help="Read-only source/catalog/image checks; creates no output")
    parser.add_argument("--require-complete-views", action="store_true", help="Treat missing catalog views as a failing coverage gate")
    parser.add_argument("--layout-check", action="store_true", help="Inspect existing HTML in offline Chromium; no PDF")
    parser.add_argument("--node", default="node", help="Node executable for --layout-check")
    parser.add_argument("--preview-pages", default="", help="For --layout-check: comma-separated folios or all")
    args = parser.parse_args()
    output = Path(args.output_dir)
    if not output.is_absolute(): output = ROOT / output
    if args.layout_check:
        return check_layout(output, args.node, args.preview_pages)
    errors, warnings = validate_catalog(load_catalog())
    for rel in ("docs/DECISIONS.md", "docs/ART_DIRECTION.md", "docs/ART_SPEC.md", "docs/WORLD_ENCYCLOPEDIA.md", "docs/CHARACTER_BIBLE.md"):
        if not (ROOT / rel).is_file(): errors.append("Missing source: " + rel)
    if not (ROOT / "art/catalog/characters.json").exists(): warnings.append("Enriched catalog absent; using imported 56-model draft data")
    report = dict(character_entries=len(load_catalog()), errors=errors, missing_view_or_source_warnings=warnings,
                  note="Read-only structural checks; no PDF or visual approval.")
    if args.check:
        print(json.dumps(report, ensure_ascii=False, indent=2))
        return 1 if errors or (warnings and args.require_complete_views) else 0
    if errors:
        print(json.dumps(report, ensure_ascii=False, indent=2)); return 1
    book, manifest = build(output.resolve(), args.date)
    manifest["catalog_validation"] = report
    (output / "build-manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(dict(html=str(output / "book.html"), pages=len(book.pages), character_entries=report["character_entries"], missing_assets=len(manifest["missing_assets"]), catalog_warnings=len(warnings)), indent=2))
    return 1 if args.require_complete_views and (warnings or manifest["missing_assets"]) else 0


if __name__ == "__main__":
    raise SystemExit(main())
