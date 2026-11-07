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
import canon as C

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BUILD = os.path.join(ROOT, "build")
IMG = os.path.join(BUILD, "img")
OUT_PDF = os.path.join(ROOT, "docs", "ZERO-SUM_OMEN_World_and_Art_Bible.pdf")


# ---------------------------------------------------------------- images
def web_image(src_rel, max_side=1500, quality=82):
    return C.derivative_image(src_rel, BUILD, max_side=max_side, quality=quality)


def video_still(src_rel, t=0.6):
    return C.derivative_video_still(src_rel, BUILD, t=t)


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

PASS1_NOTE = "Historical pass-1 concept, not accepted runtime art. Retained as reference; current direction is Art Direction v3."


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
            f'<figure class="char-art"><img src="{web_image(art)}" alt="{html.escape(name)} concept art"><figcaption>{"Fresh v4 design candidate; visual/lookdev approval does not establish a runtime rig." if "/fresh/" in art else PASS1_NOTE}</figcaption></figure>'
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
            figs += f'<p class="note">{PASS1_NOTE} Future Hyakki plates are composition references; no runtime acceptance or source scene is supplied.</p>'
        if keys:
            figs += "".join(f'<figure class="plate half"><img src="{web_image(k, 1200)}" alt=""></figure>' for k in keys)
            figs += '<p class="note">Historical raster base and colour key; source scene/scripts missing at baseline. AI-directed production is specified in ARTBOOK_PRODUCTION.</p>'
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
        (video_still("art/motion/nil_reveal.mp4"), "NIL reveal (5 s, portrait). Historical generation test; not a current landscape cinematic."),
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


ART_STATUS = '<p class="note">Runtime asset acceptance is recorded in ASSET_LIST/PROJECT_STATUS. Concepts and design figures are candidates; no external job status or finished rig is inferred from them.</p>'



def build_html():
    css_path = os.path.join(ROOT, "tools", "bible.css")
    with open(css_path, encoding="utf-8") as f:
        css = f.read()
    os.makedirs(IMG, exist_ok=True)
    body = []
    body.append("""
<section class="cover">
  <div class="cover-top">OFFICIAL UNITY GAME JAM 2026 · THEME: LUCKY NUMBER</div>
  <div class="cover-title">ZERO&#8209;SUM:<br><span>OMEN</span></div>
  <div class="cover-sub">The World &amp; Art Bible</div>
  <div class="cover-nan">NaN</div>
  <div class="cover-bottom">Required jam: Meridian Prologue · NIL/Vesper/Varro/Debt Hound · AI-only/free-first<br>Full campaign content is future specification · Specification snapshot · 7 November 2026 · TR 1002 · the Markdown files in <code>docs/</code> are the source of truth.</div>
</section>
<section class="toc">
  <h1>Contents</h1>
  <ol>
    <li><b>The game in one page</b></li>
    <li><b>The world</b>: why numbers matter, Hap the god of luck, history, the villain, the lands, the cast, endings</li>
    <li><b>The story</b>: the whole campaign, act design for every land, the bestiary, bond arcs</li>
    <li><b>Lore lexicon</b>: glossary, idioms, timeline, factions, world rules, naming</li>
    <li><b>The lands</b>: colour scripts, concept plates, locations guide</li>
    <li><b>Characters</b>: model pages and the character bible, side characters, secret recruits</li>
    <li><b>Art direction</b>: painted world, inked people; original shape, palette and production contracts</li>
    <li><b>Gameplay</b>: GDD, systems, tuning, economy, game feel, first ten minutes, UX, player experience</li>
    <li><b>Production</b>: plan, pre-production docs, jam slice, assets, audio, script, tech, playtests, quality, QA</li>
    <li><b>Care, launch and policy</b>: cultures, localisation, accessibility, telemetry, market, marketing, legal, team</li>
    <li><b>Appendix</b>: narrative style guide, AI disclosure</li>
  </ol>
  <p class="note">How to use this bible: DECISIONS resolves conflicts; JAM_SLICE controls required content; PROJECT_STATUS distinguishes specification from implementation. Domain documents provide details.</p>
</section>
""")
    body.append(md_file("docs/DECISIONS.md", drop_title=False))
    body.append(md_file("docs/PROJECT_STATUS.md", drop_title=False))
    body.append(part("I", "The game in one page", "What we are making and why it will feel like nothing else."))
    body.append("""
<div class="onepage">
<p class="lede">In a world where every soul's luck floats above its head as a number, a nameless wanderer with no number at all tells the city its lucky number, and becomes the most wanted person alive.</p>
<div class="grid2 text">
<div><h3>The fantasy</h3><p>You are NIL, the world's missing luck in human form. Every number in the Tally spins like a slot reel, and you are the only one who can stop them. Travel lands inspired by Japanese, Chinese, Indian, Greek and American myth, recruit eight core companions plus three secrets across the full game/postgame, take NIL and up to two companions into an Audit, and break the seals of the machine that flattened every culture's idea of luck into one zero-sum number.</p></div>
<div><h3>The play</h3><p>One verb: tap to stop the number. Three strikes fill the reel; a solo or two-person party repeats legal actors. Settle damage once; concise in-engine effects explain the pattern. Depth comes from team synergy (heroes whose lucky digits add to 10, run in sequence, or are all prime), charms from every culture, and wheels you reshape like a deck.</p></div>
<div><h3>The look</h3><p><b>Painted world, inked people.</b> Matte, lived-in painted lands with graphic two-tone cel characters, coloured contours and deliberate neon accents.</p></div>
<div><h3>The theme</h3><p>A world that believes luck is zero-sum learns, from a party drawn from every culture, that luck shared isn't.</p></div>
</div></div>""")
    body.append(part("II", "The world", "Why numbers matter, the god of luck, and who wants to freeze fate forever."))
    body.append(md_file("docs/WORLD_BIBLE.md"))
    body.append(part("III", "The story", "From a NaN in the rain to the Open Hand: every act, every boss, every bond."))
    for f in ["STORY", "ACT_DESIGN", "BESTIARY", "BOND_ARCS"]:
        body.append(md_file(f"docs/{f}.md"))
    body.append(part("IV", "Lore lexicon", "Every word, date and rule, kept consistent."))
    body.append(md_file("docs/LORE_LEXICON.md"))
    body.append(part("V", "The lands", "Seven places, seven palettes. Travelling between them should feel like changing countries."))
    body.append(land_pages())
    body.append(md_file("docs/LOCATIONS.md"))
    body.append(part("VI", "Characters", "Model pages first, then the full character bible."))
    body.append(character_pages())
    body.append(md_file("docs/CHARACTER_BIBLE.md"))
    body.append(part("VII", "Art direction", "Painted world, inked people."))
    body.append(md_file("docs/ART_DIRECTION.md"))
    body.append(md_file("docs/ARTBOOK_PRODUCTION.md"))
    body.append(motion_and_layouts())
    for rel in ("art/renders/lookdev/omen_battle_v5.png", "art/renders/lookdev/meridian_empty_v5.png", "art/renders/lookdev/meridian_clay_v5.png"):
        if os.path.isfile(os.path.join(ROOT, rel)):
            body.append(f'<figure class="plate"><img src="{web_image(rel)}" alt="Lookdev render"><figcaption>Fresh reproducible lookdev render — not a Unity game screenshot or verified runtime asset.</figcaption></figure>')
    body.append(part("VIII", "Gameplay", "One verb, deep consequences."))
    for f in ["GDD", "SYSTEMS", "TUNING", "ECONOMY_PROGRESSION", "GAME_FEEL", "FIRST_10_MINUTES", "UX_SPEC", "PLAYER_EXPERIENCE"]:
        body.append(md_file(f"docs/{f}.md"))
    body.append(part("IX", "Production", "From jam slice to full game."))
    body.append(md_file("docs/PRODUCTION_PLAN.md"))
    body.append(ART_STATUS)
    for f in ["PREPRODUCTION_DOCS", "JAM_SLICE", "ASSET_LIST", "AUDIO", "JAM_SCRIPT", "TECH_DESIGN", "PLAYTEST", "QUALITY_BAR", "QA_TEST_PLAN"]:
        body.append(md_file(f"docs/{f}.md"))
    body.append(md_file("art/HIGGSFIELD_PROMPTS.md"))
    body.append(part("X", "Care, launch and policy", "Cultures, players, data, the market and the rules."))
    for f in ["CULTURAL_CONSULTATION", "LOCALISATION", "ACCESSIBILITY", "TELEMETRY", "MARKET_POSITIONING", "MARKETING_PLAN", "LEGAL_IP_AI", "TEAM_HANDBOOK"]:
        body.append(md_file(f"docs/{f}.md"))
    body.append(part("XI", "Appendix", "Writing rules and disclosures."))
    body.append(md_file("docs/NARRATIVE_STYLE.md"))
    body.append(md_file("docs/AI_DISCLOSURE.md"))

    snapshot = C.write_manifest(BUILD, "bible")
    doc = f"""<!doctype html><html lang="en"><head><meta charset="utf-8">
<title>ZERO-SUM: OMEN — World & Art Bible</title>
<meta name="source-sha256" content="{snapshot}">
<style>{css}</style></head><body>{''.join(body)}</body></html>"""
    path = os.path.join(BUILD, "bible.html")
    with open(path, "w", encoding="utf-8") as f:
        f.write(doc)
    return path


if __name__ == "__main__":
    args = C.build_options("bible", "ZERO-SUM_OMEN_World_and_Art_Bible.pdf")
    print(C.validate_sources())
    if args.check:
        sys.exit(0)
    BUILD = str(args.build_dir)
    IMG = os.path.join(BUILD, "img")
    OUT_PDF = str(args.pdf_path)
    html_path = build_html()
    print("HTML:", html_path)
    if args.html_only:
        sys.exit(0)
    r = subprocess.run([args.node, os.path.join(ROOT, "tools", "render_pdf.js"), html_path, OUT_PDF])
    sys.exit(r.returncode)
