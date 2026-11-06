#!/usr/bin/env python3
"""Build the ZERO-SUM: OMEN world & art bible PDF.

Usage:  python3 tools/build_bible.py            (writes build/bible.html, then node renders the PDF)
Needs:  pip install markdown pillow ; Node with playwright (Chromium) for tools/render_pdf.js
"""
import html
import os
import re
import subprocess
import sys

import markdown
from PIL import Image

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BUILD = os.path.join(ROOT, "build")
IMG = os.path.join(BUILD, "img")
OUT_PDF = os.path.join(ROOT, "docs", "ZERO-SUM_OMEN_World_and_Art_Bible.pdf")
os.makedirs(IMG, exist_ok=True)


# ---------------------------------------------------------------- images
def web_image(src_rel, max_side=1500, quality=82):
    """Copy a repo image into build/img as a print-friendly JPEG; return its path relative to build/."""
    src = os.path.join(ROOT, src_rel)
    name = os.path.splitext(os.path.basename(src_rel))[0] + ".jpg"
    dst = os.path.join(IMG, name)
    if not os.path.exists(dst):
        im = Image.open(src).convert("RGB")
        im.thumbnail((max_side, max_side))
        im.save(dst, quality=quality, optimize=True, progressive=True)
    return "img/" + name


def video_still(src_rel, t=0.6):
    src = os.path.join(ROOT, src_rel)
    name = os.path.splitext(os.path.basename(src_rel))[0] + "_still.jpg"
    dst = os.path.join(IMG, name)
    if not os.path.exists(dst):
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", str(t), "-i", src, "-frames:v", "1", "-q:v", "3", dst], check=True)
    return "img/" + name


# ---------------------------------------------------------------- markdown
MD = markdown.Markdown(extensions=["tables", "fenced_code", "sane_lists"])


def md_file(rel, drop_title=True):
    with open(os.path.join(ROOT, rel), encoding="utf-8") as f:
        text = f.read()
    if drop_title:
        text = re.sub(r"\A#\s[^\n]*\n", "", text)
        text = re.sub(r"\A###\s[^\n]*\n", "", text.lstrip())
    # links to other repo files become plain text; external links stay
    text = re.sub(r"\[([^\]]+)\]\((?!https?://)[^)]+\)", r"\1", text)
    MD.reset()
    out = '<section class="doc">' + MD.convert(text) + "</section>"
    # demote headings one level so part titles stay on top
    out = re.sub(r"<(/?)h([1-5])>", lambda m: f"<{m.group(1)}h{int(m.group(2)) + 1}>", out)
    return out


# ---------------------------------------------------------------- design pieces
def swatches(colors, label=None):
    cells = "".join(
        f'<div class="sw"><div class="chip" style="background:{c}"></div><div class="hex">{n}<br>{c}</div></div>'
        for n, c in colors
    )
    head = f'<div class="sw-label">{html.escape(label)}</div>' if label else ""
    return f'<div class="swatches">{head}<div class="sw-row">{cells}</div></div>'


from canon import CHARACTERS, FIGURE_KEYS, LANDS  # noqa: E402  (shared with the art book)
import figures as FIG  # noqa: E402

PASS1_NOTE = "Pass 1 exploration art, in the superseded style. Kept for reference; to be redone under Art Direction v2."


def luminance(hexc):
    h = hexc.lstrip("#")
    r, g, b = (int(h[i:i + 2], 16) / 255 for i in (0, 2, 4))
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def strong_color(colors):
    """First palette colour dark enough to read on cream paper."""
    for _, c in colors:
        if luminance(c) < 0.62:
            return c
    return "#141018"


def character_pages():
    out = []
    for fkey, (name, role, digit, land, shape, colors, art, locks) in zip(FIGURE_KEYS, CHARACTERS):
        sig = strong_color(colors)
        art_html = (
            f'<figure class="char-art"><img src="{web_image(art)}" alt="{html.escape(name)} concept art"><figcaption>{PASS1_NOTE}</figcaption></figure>'
            if art else
            f'<div class="char-art pending" style="border-color:{sig}"><div class="pending-label">Key art pending</div>'
            f'<p>Generate with the character suffix in Art Direction §6 and the description in the Character Bible.</p></div>'
        )
        lock_items = "".join(f"<li>{html.escape(l)}</li>" for l in locks)
        out.append(f"""
<section class="char-page">
  <div class="char-head" style="border-color:{sig}">
    <div><div class="eyebrow">{html.escape(role)}</div><h3 class="char-name">{html.escape(name)}</h3></div>
    <div class="digit" style="color:{sig}">{html.escape(digit)}</div>
  </div>
  <div class="char-body">
    {art_html}
    <div class="char-side">
      <div class="meta-row"><span>From</span><b>{html.escape(land)}</b></div>
      <div class="shape-box"><div class="fig-col">{FIG.figure(fkey)}</div><div class="fig-ink">{FIG.figure(fkey, "ink")}</div><div class="meta-small">Design figure and its silhouette (tools/figures.py). Shape language: {html.escape(shape.replace("_", " + "))}</div></div>
      {swatches(colors, "Palette")}
      <div class="locks"><div class="sw-label">Canon locks</div><ul>{lock_items}</ul></div>
    </div>
  </div>
</section>""")
    return "\n".join(out)


def land_pages():
    out = []
    for name, sub, colors, arts in LANDS:
        figs = "".join(
            f'<figure class="plate"><img src="{web_image(a)}" alt="{html.escape(name)} concept"></figure>' for a in arts
        )
        keys = {"Meridian Undercity": ["art/base3d/wards_base_clay.png", "art/base3d/wards_colorkey_v1.png"],
                "Hyakki": ["art/base3d/hyakki_pier_base_v1.png", "art/base3d/hyakki_pier_colorkey_v1.png"]}.get(name, [])
        if arts:
            figs += f'<p class="note">{PASS1_NOTE} The Hyakki pier deck plate is the usable layout for the battle stage.</p>'
        if keys:
            figs += "".join(f'<figure class="plate half"><img src="{web_image(k, 1200)}" alt=""></figure>' for k in keys)
            figs += '<p class="note">3D base (clay) and flat colour key for the v2 paint pass (Art Book Production Guide §4).</p>'
        else:
            figs = '<div class="pending wide"><div class="pending-label">Environment art pending</div><p>Establishing shot and battle stage to be generated with the background suffix in Art Direction §6, using this land\'s palette and the Locations Guide.</p></div>'
        out.append(f"""
<section class="land-page">
  <div class="eyebrow">{html.escape(sub)}</div>
  <h3 class="land-name">{html.escape(name)}</h3>
  {swatches(colors, "Colour script")}
  {figs}
</section>""")
    return "\n".join(out)


def part(num, title, intro):
    return f"""<section class="part"><div class="part-num">Part {num}</div><h1>{html.escape(title)}</h1><p class="part-intro">{html.escape(intro)}</p><div class="tally"><s>||||</s> <s>||||</s> <s>||||</s> ||</div></section>"""


def motion_and_layouts():
    stills = [
        (video_still("art/motion/intro_meridian_dawn.mp4"), "Intro shot 5 (8 s): the Basilica's searchlight sweeps the Undercity at dawn. Seedance 2.5 test."),
        (video_still("art/motion/nil_reveal.mp4"), "NIL reveal (5 s, vertical). Seedance 2.5 test; inherits the \"Nan\" typo from pass 1."),
    ]
    layouts = [
        (web_image("art/lookdev/pose_blockout.png", 900), "Standing pose layout"),
        (web_image("art/lookdev/dynamic_pose_blockout.png", 900), "Action pose layout (v2)"),
        (web_image("art/lookdev/street_blockout.png", 900), "Establishing-shot layout"),
        (web_image("art/lookdev/stage_blockout.png", 900), "Battle-stage layout"),
    ]
    s = "".join(f'<figure class="plate half"><img src="{p}" alt=""><figcaption>{html.escape(c)}</figcaption></figure>' for p, c in stills)
    l = "".join(f'<figure class="plate quarter"><img src="{p}" alt=""><figcaption>{html.escape(c)}</figcaption></figure>' for p, c in layouts)
    return f'<h2>Motion tests</h2><div class="grid2">{s}</div><h2>3D layouts used to keep framing consistent</h2><div class="grid4">{l}</div>'


ART_STATUS = """
<h2>Art status (end of Nov 6)</h2>
<table>
<thead><tr><th>Asset</th><th>Status</th><th>Next step</th></tr></thead>
<tbody>
<tr><td>Art Direction v2 style frames (NIL action, Meridian dawn, Hyakki pier, battle frame)</td><td>6 paint passes stuck in Higgsfield "submission unknown"</td><td>Check credits; reconcile; then paint over the 3D bases</td></tr>
<tr><td>3D bases and colour keys</td><td>Done: Remainder Wards, Moon Pier, line-up base</td><td>Paint pass (register A)</td></tr>
<tr><td>Design figures for all 16 characters + 4 Meridian eras</td><td>Done (vector stand-ins, art book and model pages)</td><td>Replace with key art and turnarounds</td></tr>
<tr><td>Graphic identity: emblems, Omen displays, charm icons, reel objects</td><td>Done (art/graphics/)</td><td>Refine by hand; reuse as UI icons</td></tr>
<tr><td>Character key art, v2 style (16 characters)</td><td>Pending</td><td>Generate after the style frames are approved</td></tr>
<tr><td>Environment establishing + battle stage per land (7 lands)</td><td>Meridian and Hyakki explored in pass 1; colour scripts for all</td><td>Redo in v2; then the five remaining lands</td></tr>
<tr><td>Enemy sheets (Meridian, Hyakki)</td><td>Pending</td><td>3-pose sprites per enemy</td></tr>
<tr><td>Intro cinematic shots</td><td>2 test shots done</td><td>Storyboard stills, then video</td></tr>
<tr><td>Turnarounds and attack key poses for jam heroes</td><td>Pending</td><td>Needed for rigs</td></tr>
</tbody></table>
"""


def build_html():
    css_path = os.path.join(ROOT, "tools", "bible.css")
    with open(css_path, encoding="utf-8") as f:
        css = f.read()
    body = []
    body.append("""
<section class="cover">
  <div class="cover-top">OFFICIAL UNITY GAME JAM 2026 · THEME: LUCKY NUMBER</div>
  <div class="cover-title">ZERO&#8209;SUM:<br><span>OMEN</span></div>
  <div class="cover-sub">The World &amp; Art Bible</div>
  <div class="cover-nan">NaN</div>
  <div class="cover-bottom">World · Lore · Lands · Characters · Art Direction · Gameplay · Production<br>Version 2 · TR 1002 · Living document: the Markdown files in <code>docs/</code> are the source of truth.</div>
</section>
<section class="toc">
  <h1>Contents</h1>
  <ol>
    <li><b>The game in one page</b></li>
    <li><b>The world</b>: why numbers matter, history, the villain, the lands, the cast, plot and endings</li>
    <li><b>Lore lexicon</b>: glossary, idioms, timeline, factions, world rules, naming</li>
    <li><b>The lands</b>: colour scripts, concept plates, locations guide</li>
    <li><b>Characters</b>: model pages (silhouette, palette, canon locks) and the character bible</li>
    <li><b>Art direction</b>: painted world, inked people; lessons from the Cyberpunk 2077 art book</li>
    <li><b>Gameplay</b>: the game design document</li>
    <li><b>Production</b>: plan, art status, prompt pack</li>
    <li><b>Appendix</b>: narrative style guide, AI disclosure</li>
  </ol>
  <p class="note">How to use this bible: when two documents disagree, the order of authority is Art Direction (for visuals) → Character Bible (for characters) → World Bible (for story) → GDD (for mechanics).</p>
</section>
""")
    body.append(part("I", "The game in one page", "What we are making and why it will feel like nothing else."))
    body.append("""
<div class="onepage">
<p class="lede">In a world where every soul's luck floats above its head as a number, a nameless wanderer with no number at all tells the city its lucky number, and becomes the most wanted person alive.</p>
<div class="grid2 text">
<div><h3>The fantasy</h3><p>You are NIL, the world's missing luck in human form. Every number in the Tally spins like a slot reel, and you are the only one who can stop them. Travel lands inspired by Japanese, Chinese, Indian, Greek and American myth, gather a party of eight, and break the seals of the machine that flattened every culture's idea of luck into one zero-sum number.</p></div>
<div><h3>The play</h3><p>One verb: tap to stop the number. Three heroes strike, their digits drop into the reel, and patterns pay out as full-screen anime cinematics. Depth comes from team synergy (heroes whose lucky digits add to 10, run in sequence, or are all prime), charms from every culture, and wheels you reshape like a deck.</p></div>
<div><h3>The look</h3><p><b>Painted world, inked people.</b> Hand-painted, sunlit, lived-in lands in the spirit of Studio Ghibli's backgrounds; graphic, neon-edged characters and fights in the spirit of <i>Cyberpunk: Edgerunners</i>.</p></div>
<div><h3>The theme</h3><p>A world that believes luck is zero-sum learns, from a party drawn from every culture, that luck shared isn't.</p></div>
</div></div>""")
    body.append(part("II", "The world", "Why numbers matter, where they came from, and who wants to freeze them forever."))
    body.append(md_file("docs/WORLD_BIBLE.md"))
    body.append(part("III", "Lore lexicon", "Every word, date and rule, kept consistent."))
    body.append(md_file("docs/LORE_LEXICON.md"))
    body.append(part("IV", "The lands", "Seven places, seven palettes. Travelling between them should feel like changing countries."))
    body.append(land_pages())
    body.append(md_file("docs/LOCATIONS.md"))
    body.append(part("V", "Characters", "Model pages first, then the full character bible."))
    body.append(character_pages())
    body.append(md_file("docs/CHARACTER_BIBLE.md"))
    body.append(part("VI", "Art direction", "Painted world, inked people."))
    body.append(md_file("docs/ART_DIRECTION.md"))
    body.append(motion_and_layouts())
    body.append(part("VII", "Gameplay", "One verb, deep consequences."))
    body.append(md_file("docs/GDD.md"))
    body.append(part("VIII", "Production", "From jam slice to full game."))
    body.append(md_file("docs/PRODUCTION_PLAN.md"))
    body.append(ART_STATUS)
    body.append(md_file("art/HIGGSFIELD_PROMPTS.md"))
    body.append(part("IX", "Appendix", "Writing rules and disclosures."))
    body.append(md_file("docs/NARRATIVE_STYLE.md"))
    body.append(md_file("docs/AI_DISCLOSURE.md"))

    fonts = ("https://fonts.googleapis.com/css2?family=Big+Shoulders+Display:wght@700;900"
             "&family=Barlow+Semi+Condensed:ital,wght@0,400;0,500;0,700;1,400"
             "&family=JetBrains+Mono:wght@400;600"
             "&family=Noto+Sans+JP:wght@400;700&family=Noto+Sans+SC:wght@400;700"
             "&family=Noto+Sans+Devanagari:wght@400;700&display=swap")
    doc = f"""<!doctype html><html lang="en"><head><meta charset="utf-8">
<title>ZERO-SUM: OMEN — World & Art Bible</title>
<link rel="stylesheet" href="{fonts}">
<style>{css}</style></head><body>{''.join(body)}</body></html>"""
    path = os.path.join(BUILD, "bible.html")
    with open(path, "w", encoding="utf-8") as f:
        f.write(doc)
    return path


if __name__ == "__main__":
    html_path = build_html()
    print("HTML:", html_path)
    r = subprocess.run(["node", os.path.join(ROOT, "tools", "render_pdf.js"), html_path, OUT_PDF])
    sys.exit(r.returncode)
