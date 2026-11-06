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


SHAPES = {
    "rect_circle": '<rect x="38" y="20" width="44" height="90" rx="2"/><path d="M60 4 a14 14 0 1 1 -12 7" fill="none" stroke-width="5"/>',
    "triangles": '<polygon points="60,8 100,70 20,70"/><polygon points="40,70 80,70 60,112"/>',
    "circles": '<circle cx="60" cy="40" r="24"/><path d="M28 112 a32 32 0 0 1 64 0" fill="none" stroke-width="10"/>',
    "dome": '<path d="M14 58 a46 46 0 0 1 92 0 z"/><rect x="58" y="58" width="4" height="40"/><circle cx="60" cy="104" r="10"/>',
    "fan": '<path d="M60 108 L10 40 A70 70 0 0 1 110 40 Z"/>',
    "vertical": '<rect x="44" y="6" width="32" height="108"/><rect x="30" y="20" width="60" height="10"/>',
    "astrolabe": '<circle cx="60" cy="60" r="44" fill="none" stroke-width="10"/><circle cx="60" cy="60" r="8"/><line x1="16" y1="60" x2="104" y2="60" stroke-width="5"/>',
    "shield": '<circle cx="60" cy="58" r="44"/><circle cx="60" cy="58" r="30" fill="#F2E8D5"/>',
    "spiral": '<path d="M60 60 m0 0 a6 6 0 0 1 12 0 a12 12 0 0 1 -24 0 a20 20 0 0 1 40 0 a30 30 0 0 1 -60 0 a42 42 0 0 1 84 0" fill="none" stroke-width="6"/>',
    "block": '<rect x="20" y="20" width="80" height="84"/>',
    "crescent": '<path d="M90 20 a44 44 0 1 0 0 80 a34 34 0 1 1 0 -80z"/>',
    "sphere": '<circle cx="60" cy="62" r="46"/>',
    "column": '<rect x="48" y="4" width="24" height="112"/><rect x="36" y="4" width="48" height="8"/><rect x="36" y="108" width="48" height="8"/>',
    "ouroboros": '<circle cx="60" cy="60" r="44" fill="none" stroke-width="10"/><circle cx="60" cy="60" r="20" fill="none" stroke-width="6"/>',
    "arch": '<path d="M20 116 V50 a40 40 0 0 1 80 0 V116 h-16 V52 a24 24 0 0 0 -48 0 V116z"/>',
    "eclipse": '<circle cx="54" cy="60" r="38"/><circle cx="72" cy="56" r="34" fill="#F2E8D5"/>',
}


def shape_svg(key, color):
    return (
        f'<svg class="shape" viewBox="0 0 120 120" fill="{color}" stroke="{color}" xmlns="http://www.w3.org/2000/svg">'
        f"{SHAPES[key]}</svg>"
    )


CHARACTERS = [
    # name, role, digit, land, shape, colours, art (repo path or None), locks
    ("NIL", "Protagonist · the Remainder", "Player's choice", "Meridian Undercity", "rect_circle",
     [("Nixie orange", "#FF7A2C"), ("Ink black", "#141018"), ("Bone white", "#EDE6DA"), ("Rim cyan", "#00E5FF")],
     "art/concepts/nil_keyart.jpg",
     ["Decoder on the RIGHT wrist", "One orange streak in white hair", "Halo reads exactly \"NaN\"", "Coat's left tail is longer", "Amber eyes"]),
    ("Vesper Sette", "Gunslinger · companion", "7", "Meridian / Crossroads", "triangles",
     [("Crimson", "#E5243B"), ("Black", "#141018"), ("Brass", "#B5A642"), ("Shirt white", "#F4F1EA")],
     "art/concepts/vesper_keyart.jpg",
     ["Exactly 7 chambers", "Scar on the lip", "Braid over the LEFT shoulder", "Crimson + black + brass only"]),
    ("Maeve Triskel", "Charm-smith · companion", "3", "Meridian, Celtic quarter", "circles",
     [("Copper", "#D9822B"), ("Clover", "#3BB273"), ("Leather", "#6B4226"), ("Red hair", "#C0392B")],
     "art/concepts/maeve_keyart.jpg",
     ["Exactly 3 braids", "Triskele on the hammer", "Clover pin on the collar"]),
    ("Hina of the Ninety-Nine", "Tsukumogami · companion", "9", "Hyakki", "dome",
     [("Vermilion", "#E34234"), ("Indigo", "#26428B"), ("Paper", "#F2E6C9"), ("Gold", "#F2B33D")],
     "art/concepts/hina_keyart.jpg",
     ["The umbrella has ONE eye and a tongue", "Kimono numbers stop at 99", "Never reaches 100 before the finale"]),
    ("Ba Jinling", "Financier · companion", "8", "River Empire", "fan",
     [("Jade", "#00A86B"), ("Gold", "#F4C430"), ("Lacquer red", "#B22222"), ("Violet eyes", "#5D3A7A")],
     None, ["Exactly 8 bells", "Abacus-rib fan", "Jade + gold palette"]),
    ("Bai Si", "Executioner · companion", "4", "River Empire (Ten Courts)", "vertical",
     [("Mourning white", "#F4F1EA"), ("Ink", "#1B1B1B"), ("Talisman yellow", "#E8C547"), ("Lantern", "#F2B33D")],
     None, ["Always 4 lanterns, 4 talismans", "White robes only", "Never smiles before Act IV"]),
    ("Shunya", "Astronomer · companion", "0", "Śūnyapura", "astrolabe",
     [("Indigo", "#3F3D99"), ("Saffron", "#F4A300"), ("Brass", "#B5893B"), ("Mirror silver", "#C9CED6")],
     None, ["The brass astrolabe", "Mirror-work embroidery", "\"Zero isn't nothing.\""]),
    ("Prima of Kroton", "Paladin · companion", "2", "Kroton Nova", "shield",
     [("Aegean blue", "#1F6FB2"), ("White gold", "#E9DDB3"), ("Chalk", "#F4F1EA"), ("Glass blue", "#6FB7E9")],
     None, ["Sieve shield", "2-3-5-7 halo", "Short hair"]),
    ("Fibi Leone", "Dealer · companion", "Fibonacci", "Crossroads", "spiral",
     [("Gold", "#F2B33D"), ("Midnight", "#1D1A3A"), ("Card white", "#F4F1EA"), ("Neon pink", "#FF2E88")],
     None, ["1,597 nights", "Spiral irises", "Her digit changes every round"]),
    ("Varro Kade", "Prologue boss → ally", "61", "Meridian", "block",
     [("Rust", "#B7410E"), ("Gunmetal", "#4A4E54"), ("Debt-jar glow", "#FF7A2C"), ("Mask bone", "#E3DCCB")],
     "art/concepts/varro_keyart.jpg", ["Hound-skull mask", "Glass debt jars", "\"61\" in red"]),
    ("Tamamo", "Act I boss", "Nine tails", "Hyakki", "crescent",
     [("Violet", "#8E44AD"), ("Gold", "#F4C430"), ("Foxfire cyan", "#7FDBFF"), ("White", "#F4F1EA")],
     "art/concepts/tamamo_keyart.jpg", ["Nine tails, each tipped with a digit", "Foxfire is cold cyan-violet", "Modest court robes (paint-over)"]),
    ("Chancellor Jin Chan", "Act II boss", "88", "River Empire", "sphere",
     [("Gold", "#D4AF37"), ("Toad green", "#6B8E23"), ("Red", "#B22222")], None,
     ["Three-legged toad throne", "Coins spill from his mouth"]),
    ("Rahu & Ketu", "Act III boss", "Eclipse", "Śūnyapura", "eclipse",
     [("Eclipse purple", "#4B2A6B"), ("Corona gold", "#F4A300"), ("Night", "#141018")], None,
     ["Awe-inspiring, never grotesque", "Two bodies, one fight", "Cultural review required"]),
    ("Archon Seventeen", "Act IV boss", "17", "Kroton Nova", "column",
     [("Bronze", "#8C6A3F"), ("Chalk", "#F4F1EA"), ("Sieve white", "#DDE6EE")], None,
     ["Bronze laurel", "Sieve staff", "Cold \"17\""]),
    ("The House", "Act V boss", "89", "Crossroads", "ouroboros",
     [("Ivory", "#F4F1EA"), ("Casino red", "#C0392B"), ("Gold", "#D4AF37")], None,
     ["White suit", "Ouroboros tattoo", "Backwards pocket watch"]),
    ("Comptroller Lucan Thale", "Final antagonist", "50 (steel)", "Meridian", "arch",
     [("Steel white", "#E8E6E1"), ("Brass", "#B5A642"), ("Nixie", "#FF7A2C"), ("Steel", "#8E9196")],
     "art/concepts/thale_keyart.jpg", ["Gear monocle", "Steel, never glowing, \"50\"", "Never shouts"]),
]

LANDS = [
    ("Meridian Undercity", "Prologue · cosmopolitan capital · cyber-noir painted city",
     [("Wet slate", "#2E3A4B"), ("Window amber", "#E8A04B"), ("Moss", "#5E7D4A"), ("Nixie", "#FF7A2C"), ("Neon yellow", "#F5E400"), ("Neon magenta", "#FF2E88"), ("Neon cyan", "#00E5FF")],
     ["art/concepts/env_meridian_establishing.jpg", "art/concepts/env_meridian_battle_alley.jpg"]),
    ("Hyakki", "Act I · Japanese folklore · ukiyo-e + painted night",
     [("Indigo", "#1B2440"), ("Ink blue", "#2E4A7A"), ("Paper", "#F2E6C9"), ("Vermilion", "#E34234"), ("Lantern gold", "#F2B33D"), ("Firefly", "#9BD15A")],
     ["art/concepts/env_hyakki_establishing.jpg", "art/concepts/env_hyakki_battle_deck.jpg", "art/concepts/env_hyakki_battle_mock.jpg"]),
    ("The River Empire", "Act II · Chinese folk religion · gongbi gold + ink-wash underworld",
     [("Jade", "#00A86B"), ("Ochre", "#C8963E"), ("Red lacquer", "#B22222"), ("Gold leaf", "#D4AF37"), ("Rice paper", "#E9E2D0"), ("Ink green", "#3A4A3F")], []),
    ("Śūnyapura", "Act III · Indian myth & mathematics · miniature painting + monsoon light",
     [("Sandstone", "#D8A86B"), ("Peacock", "#1E7B6F"), ("Saffron", "#F4A300"), ("Indigo", "#3F3D99"), ("Brass", "#B5893B"), ("Eclipse", "#4B2A6B")], []),
    ("Kroton Nova", "Act IV · Greek myth · marble, mosaic, Aegean noon",
     [("Chalk", "#F4F1EA"), ("Aegean", "#1F6FB2"), ("Olive", "#7A8B4A"), ("Bronze", "#8C6A3F"), ("Sky", "#D6E6F2")], []),
    ("The Crossroads Territory", "Act V · American folklore · desert sunset + casino neon",
     [("Rust", "#B7410E"), ("Sage", "#9CAF88"), ("Dusk violet", "#5B3E73"), ("Sunset", "#F28C28"), ("Midnight", "#1D1A3A"), ("Neon pink", "#FF2E88")], []),
    ("The Basilica", "Finale · the machine · brass and steel",
     [("Brass", "#B5A642"), ("Steel", "#8E9196"), ("Steel white", "#E8E6E1"), ("Nixie", "#FF7A2C"), ("Ink", "#141018")], []),
]

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
    for name, role, digit, land, shape, colors, art, locks in CHARACTERS:
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
      <div class="shape-box">{shape_svg(shape, sig)}<div class="meta-small">Silhouette shape</div></div>
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
        if arts:
            figs += f'<p class="note">{PASS1_NOTE} The Hyakki pier deck plate is the usable layout for the battle stage.</p>'
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
<h2>Art status</h2>
<table>
<thead><tr><th>Asset</th><th>Status</th><th>Next step</th></tr></thead>
<tbody>
<tr><td>Art Direction v2 style frames (NIL action, Meridian dawn, Hyakki pier, battle frame)</td><td>Submitted; Higgsfield reports "submission unknown"</td><td>Reconcile with Higgsfield, then regenerate</td></tr>
<tr><td>Character key art, v2 style (16 characters)</td><td>Pending</td><td>Generate after the style frames are approved</td></tr>
<tr><td>Meridian era comparison sheet (person / charm / Omen display × 4 eras)</td><td>Pending</td><td>First Meridian concept task</td></tr>
<tr><td>Environment establishing + battle stage per land (7 lands)</td><td>Meridian and Hyakki explored in pass 1</td><td>Redo in v2; then the five remaining lands</td></tr>
<tr><td>Enemy sheets (Meridian, Hyakki)</td><td>Pending</td><td>3-pose sprites per enemy</td></tr>
<tr><td>Intro cinematic shots</td><td>1 test shot done</td><td>Storyboard stills, then video</td></tr>
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
  <div class="cover-bottom">World · Lore · Lands · Characters · Art Direction · Gameplay · Production<br>Version 1 · TR 1002 · Living document: the Markdown files in <code>docs/</code> are the source of truth.</div>
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
