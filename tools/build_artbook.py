#!/usr/bin/env python3
"""Build the ZERO-SUM: OMEN art book DRAFT (landscape spreads) as a PDF.

Layout grammar follows docs/ARTBOOK_PRODUCTION.md §1 and §6: label tabs, a text column, art bleeding to the edge,
rough colour blocks, stamps and tally-mark overlays. Text facts are read from the Markdown docs through
tools/canon.py, so the book never disagrees with the bibles. Where paintings don't exist yet, the page shows the
designed stand-ins from tools/figures.py and tools/graphics.py and a brief for the painting.
Usage: python3 tools/build_artbook.py
"""
import html
import os
import subprocess
import sys

from PIL import Image

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import canon as C  # noqa: E402
import figures as F  # noqa: E402
import graphics as G  # noqa: E402

ROOT = C.ROOT
BUILD = os.path.join(ROOT, "build", "artbook")
IMG = os.path.join(BUILD, "img")
OUT = os.path.join(ROOT, "docs", "ZERO-SUM_OMEN_Artbook_Draft.pdf")
VERSION = "v0.4"
os.makedirs(IMG, exist_ok=True)

E = html.escape


def img(rel, max_side=1800):
    src = os.path.join(ROOT, rel)
    name = os.path.splitext(os.path.basename(rel))[0] + ".jpg"
    dst = os.path.join(IMG, name)
    if not os.path.exists(dst) or os.path.getmtime(dst) < os.path.getmtime(src):
        im = Image.open(src).convert("RGB")
        im.thumbnail((max_side, max_side))
        im.save(dst, quality=84, optimize=True, progressive=True)
    return "img/" + name


def tab(text):
    return f'<div class="tab">{E(text)}</div>'


def stamp(text, cls=""):
    return f'<div class="stamp {cls}">{E(text)}</div>'


def placeholder_note():
    return stamp("PLACEHOLDER · PASS 1 ART", "ph")


def brief(title, lines, cls=""):
    items = "".join(f"<li>{E(l)}</li>" for l in lines)
    return f'<div class="brief {cls}"><div class="brief-title">ART NEEDED · {E(title)}</div><ul>{items}</ul></div>'


def chips(colors, cls="pal"):
    return f'<div class="{cls}">' + "".join(
        f'<div class="chip" style="background:{c}"><span>{E(n)}<br>{c}</span></div>' for n, c in colors) + "</div>"


def page(inner, cls=""):
    return f'<section class="page {cls}">{inner}</section>'


def folio(n, label):
    return f'<div class="folio">{E(label)} · {n:02d}</div>'


# ---------------------------------------------------------------- data shortcuts
CHAR = {k: c for k, c in zip(C.FIGURE_KEYS, C.CHARACTERS)}  # key -> (name, role, digit, land, shape, colours, art, locks)
HERO_KEYS = C.FIGURE_KEYS[:9]
BOSS_KEYS = C.FIGURE_KEYS[9:]

ERAS = [
    ("charmpunk", "CHARMPUNK", "LUCK OVER SENSE", "#FF2E88", "TR 850→",
     "The street's lingua franca. Every culture's charms worn at once, hand-painted lucky numbers, plastic gold and neon. Charmpunk is loud because luck is a performance: if you can't raise your Omen, you can at least look like you're winning.",
     [("Neon magenta", "#FF2E88"), ("Sign yellow", "#F5E400"), ("Cyan", "#00E5FF"), ("Clover", "#3BB273")], "dice",
     ["Line-up of 6 Bazaar locals in Charmpunk", "Keyframe: the Charm Bazaar at night, every stall a different culture", "Omen display: gaudy holo-halos, fake Omen projectors"]),
    ("remainder", "REMAINDER", "SURVIVAL OVER LUCK", "#8A7F72", "TR 960→",
     "The style of the Undercity, where Omens run low. Scrap brass from old Basilica parts, patched cloth, salvaged Nixie tubes and rope. Durable, ugly, honest. People hide their numbers here out of shame.",
     [("Ash", "#8A7F72"), ("Leather", "#6B4226"), ("Gunmetal", "#4A4E54"), ("Old brass", "#C8963E")], "horseshoe",
     ["Line-up: Remainder Wards residents (mechanic, cook, debt-ridden mother, kids)", "Environment: Rain Alley 9 at dawn", "Omen display: a cracked tube on a cord"]),
    ("ledgerism", "LEDGERISM", "ORDER OVER CHANCE", "#B5A642", "TR 760→",
     "The style of the Basilica and its servants. Brass, steel and white enamel; cathedral arches; clockwork; uniforms with stamped seals. Cold, formal and threatening, it says that chance has been abolished and you are being counted.",
     [("Brass", "#B5A642"), ("Steel", "#8E9196"), ("Enamel", "#E8E6E1"), ("Uniform", "#6E6B4E")], None,
     ["Line-up: Collectors, Ledger-priests, Basilica clerks, Auditors", "Environment: the Basilica Ring checkpoint", "Omen display: steel numerals, never glowing"]),
    ("gilded", "GILDED FORTUNE", "FORTUNE AND ORDER", "#D4AF37", "TR 990→",
     "The style of the 99s: old money and Exchange magnates. Real gold leaf, jade, silk and living plants. In Meridian a garden is luck you can see; a bonsai on a balcony is a fortune worn in public.",
     [("Gold leaf", "#D4AF37"), ("Jade", "#00A86B"), ("Lacquer", "#B22222"), ("Silk", "#F4F1EA")], "red_envelope",
     ["Line-up: Exchange magnates, heirs, their guards", "Environment: the Exchange Terraces garden-villas", "Omen display: embroidered or gold-leaf numerals"]),
]

DIGIT_SHOW = {"nil": "0–9", "fibi": "1·1·2"}
LAND_KEYS = {"meridian": 0, "hyakki": 1, "river": 2, "sunyapura": 3, "kroton": 4, "crossroads": 5, "basilica": 6}
LAND_EMBLEM = {"meridian": "collectors", "hyakki": "yokai", "river": "exchange", "sunyapura": "observatory",
               "kroton": "synod", "crossroads": "house", "basilica": "basilica"}
LAND_GHOST = {"hyakki": "百鬼", "river": "八发港", "sunyapura": "शून्यपुर", "kroton": "Κρότων", "basilica": "∑", "meridian": "00–99", "crossroads": "7·11"}
LAND_BRIEF = {
    "meridian": ["Establishing: the Wards at dawn after rain, the Basilica's eye at the end of the street", "Battle stage: Rain Alley 9", "District keyframes: Charm Bazaar, Exchange Terraces, Basilica Ring"],
    "hyakki": ["Establishing: the Moon Pier at night", "The Night Parade crossing the red bridge", "Shrine of the Seven Lucky Gods; Tamamo's foxfire palace"],
    "river": ["Establishing: Bāfā Harbor at the Lantern Festival", "The Luck Exchange's live Omen boards", "The Ten Courts in ink-wash; Naihe Bridge"],
    "sunyapura": ["Establishing: the Great Observatory in monsoon light", "The Stepwell of a Thousand Steps", "Chitragupta's Hall of palm-leaf records"],
    "kroton": ["Establishing: the white Sieve city at noon", "The undercity of the fallen under the Sieve", "The Moirai's cave"],
    "crossroads": ["Establishing: the midnight crossroads under one streetlamp", "Lucky Strike's casino strip, the same night repeating", "The Ghost Train"],
    "basilica": ["Keyframe: the Basilica nave, every land's ledger on its walls", "The Upper Gate with seven Seal Digits", "Thale's three phases as one sequence"],
}


# ---------------------------------------------------------------- pieces
def tally_map():
    lands = [("HYAKKI", "Act I · Seal 9", 150, 120, "#E34234"), ("RIVER EMPIRE", "Act II · Seal 8", 470, 90, "#00A86B"),
             ("ŚŪNYAPURA", "Act III · Seal 0", 520, 330, "#F4A300"), ("KROTON NOVA", "Act IV · Seal 2", 300, 430, "#1F6FB2"),
             ("CROSSROADS", "Act V · Seal 7", 90, 340, "#B7410E")]
    marks = "".join(
        f'<g><circle cx="{x}" cy="{y}" r="48" fill="{c}" opacity=".22"/><circle cx="{x}" cy="{y}" r="48" fill="none" stroke="{c}" stroke-width="3" stroke-dasharray="6 5"/>'
        f'<text x="{x}" y="{y - 4}" text-anchor="middle" class="m-name">{n}</text><text x="{x}" y="{y + 16}" text-anchor="middle" class="m-act">{a}</text></g>'
        for n, a, x, y, c in lands)
    road = "M320 250 C 250 180, 180 150, 150 120 C 300 40, 400 60, 470 90 S 600 250, 520 330 S 380 470, 300 430 S 60 420, 90 340 S 220 300, 320 250"
    return f"""<svg class="map" viewBox="0 0 640 520" xmlns="http://www.w3.org/2000/svg">
<rect width="640" height="520" fill="#EFE3CC"/>
<g stroke="#141018" stroke-opacity=".07">{''.join(f'<line x1="0" y1="{y}" x2="640" y2="{y}"/>' for y in range(0, 520, 26))}</g>
<path d="{road}" fill="none" stroke="#B3261E" stroke-width="3" stroke-dasharray="2 9" stroke-linecap="round"/>
<circle cx="320" cy="250" r="72" fill="#141018"/><circle cx="320" cy="250" r="72" fill="none" stroke="#FF7A2C" stroke-width="4"/>
<text x="320" y="240" text-anchor="middle" class="m-core">MERIDIAN</text><text x="320" y="260" text-anchor="middle" class="m-core-sub">PROLOGUE · SEAL 1 · FINALE</text>
<text x="320" y="276" text-anchor="middle" class="m-core-sub">THE BASILICA · SEAL = YOUR NUMBER</text>
{marks}
<text x="548" y="500" class="m-tally">|||| |||| ||</text>
</svg>"""


def land_page(key, num):
    name, sub, colors, arts = C.LANDS[LAND_KEYS[key]]
    facts = next(f for f in C.LAND_FACTS if f[0] == key)
    _, prefix, act, law, auditor, keeper, reel, enemies = facts
    info = C.land_info(prefix)
    reel_name, reel_svg = G.REELS[reel]
    em_name, em_svg = G.EMBLEMS[LAND_EMBLEM[key]]
    base = [c for _, c in colors[:3]]
    stops = f"{base[0]} 0%, {base[1]} 55%, {base[2]} 100%"
    rows = [("Act", act), ("Inspired by", info.get("Inspired by", sub)), ("Law of the land", law), ("Auditor", auditor)]
    if keeper != "—":
        rows.append(("Keeper", keeper))
    rows += [("Enemies", enemies), ("Little things", info.get("Little things", "")), ("Sound", info.get("Sound", ""))]
    if info.get("Meridian intrusion"):
        rows.append(("Meridian intrusion", info["Meridian intrusion"]))
    dl = "".join(f'<div class="dl"><span>{E(k)}</span><p>{E(v)}</p></div>' for k, v in rows if v)
    return page(f"""
<div class="col-text land-text">{tab(name.upper())}<div class="land-sub">{E(sub)}</div>{dl}</div>
<div class="col-art land-art" style="background:linear-gradient(180deg, {stops})">
  <div class="ghost">{E(LAND_GHOST.get(key, ""))}</div>
  <div class="reel-card"><div class="reel-svg">{reel_svg}</div><div class="cap">THE REEL · {E(reel_name.upper())}</div></div>
  <div class="em-card"><div class="em-svg">{em_svg}</div><div class="cap">{E(em_name)}</div></div>
  <div class="land-chips">{chips(colors)}</div>
  {brief(name + " paintings", LAND_BRIEF[key], "land-brief")}
  {stamp("COLOUR SCRIPT", "ph")}
</div>{folio(num, name)}""", "split land")


def hero_sheet(key, n_section, num):
    name, role, digit, land, shape, colors, art, locks = CHAR[key]
    rows = C.character_rows(n_section)
    sig = next((c for _, c in colors if C_lum(c) < 0.62), "#141018")
    sample = rows.get("Sample lines", "").split(" · ")[0]
    info = [("Age / build", rows.get("Age / build", "")), ("Wardrobe", rows.get("Wardrobe", "")), ("Props", rows.get("Props", "")),
            ("Voice", rows.get("Voice", ""))]
    dl = "".join(f'<div class="dl"><span>{E(k)}</span><p>{E(v)}</p></div>' for k, v in info if v)
    lock_items = "".join(f"<li>{E(l)}</li>" for l in (rows.get("Canon locks", "").split(" · ") if rows.get("Canon locks") else locks))
    return page(f"""
<div class="hs-left">
  <div class="hs-front">{F.figure(key, "colour")}<div class="cap">FRONT · DESIGN FIGURE</div></div>
  <div class="hs-back">{F.figure(key, "ink", mirror=True)}<div class="cap">BACK · SILHOUETTE</div></div>
  <div class="hs-thumb"><div class="t64">{F.figure(key, "ink")}</div><div class="cap">64 PX TEST</div></div>
</div>
<div class="hs-right">
  <div class="hs-head" style="border-color:{sig}"><div>{tab("DESIGN SHEET")}<div class="hs-name">{E(name.upper())}</div><div class="hs-role">{E(role)} · {E(land)}</div></div>
  <div class="hs-digit{' small' if len(DIGIT_SHOW.get(key, digit)) > 2 else ''}" style="color:{sig}">{E(DIGIT_SHOW.get(key, digit))}</div></div>
  {chips(colors)}
  <div class="sub">Canon locks</div><ul class="callouts">{lock_items}</ul>
  {dl}
  <div class="hs-quote">“{E(sample.strip('"“”'))}”</div>
  {brief(name + " model pack", ["Key art (register A) and an in-game cel model (register B)", "Turnaround: front, ¾, side, back", "6 expressions · 3 attack key poses · victory pose"], "hs-brief")}
</div>{folio(num, "Characters")}""", "padded hero-sheet")


def C_lum(hexc):
    h = hexc.lstrip("#")
    r, g, b = (int(h[i:i + 2], 16) / 255 for i in (0, 2, 4))
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


# ---------------------------------------------------------------- the book
def build():
    with open(os.path.join(ROOT, "tools", "artbook.css"), encoding="utf-8") as f:
        css = f.read()
    P = []
    n = [0]

    def add(html_, label=None):
        n[0] += 1
        P.append(html_)

    # cover
    add(page(f"""
<div class="cover-art" style="background-image:url('{img("art/concepts/env_meridian_establishing.jpg")}')"></div>
<div class="cover-block"></div>
<div class="cover-text"><div class="kicker">THE OFFICIAL ART BOOK OF</div><div class="title">ZERO&#8209;SUM:<br><span>OMEN</span></div><div class="kicker">DRAFT LAYOUT · {VERSION}</div>
<div class="cover-cast">{''.join(F.figure(k, "ink") for k in HERO_KEYS)}</div></div>
{stamp("NaN", "big")}{placeholder_note()}""", "cover"))

    # foreword
    add(page(f"""
<div class="col-text">{tab("FOREWORD")}
<p class="lede">Every number in this world is spinning. This book is about the people who live under them.</p>
<p>The Tally began as a question: what would a world look like if luck were a currency everyone could see? Our answer was a city that counts and a ring of lands that remember older ways of counting: thread, karma, contracts and books of the dead.</p>
<p>We built every style from that history. The brass of the Basilica, the scrap of the Remainder Wards, the gaudy charms of the street, the gold leaf of the fortunate few, and the painted, breathing lands beyond the gate.</p>
<p class="sig">The ZERO-SUM: OMEN team</p></div>
<div class="col-art paint-block" style="--block:#FF7A2C"><div class="big-quote">"A WORLD WITHOUT LUCK<br>IS A WORLD WITHOUT LOSS."</div><div class="quote-by">Comptroller Lucan Thale</div></div>{folio(2, "Foreword")}""", "split"))

    # contents (filled after pages are known)
    contents_index = len(P)
    add("")
    sections = []

    # styles
    sections.append(("Styles: the four eras of luck", n[0] + 1))
    add(page(f"""<div class="opener">{tab("STYLES")}<div class="opener-title">THE FOUR<br>ERAS OF LUCK</div>
<p class="opener-sub">Meridian's styles come from its history: the binding of the ledgers, the Rounding, the Deficit. Every street mixes them; every outfit tells you which side of the Zero-Sum Law its owner lives on.</p>
<div class="tl"><div><b>TR 702</b>Basilica completed</div><div><b>TR 760→</b>Ledgerism</div><div><b>TR 850→</b>Charmpunk</div><div><b>TR 960→</b>Remainder</div><div><b>TR 990→</b>Gilded Fortune</div><div><b>TR 1002</b>Today</div></div>
<div class="era-row">{''.join(F.era_figure(k) for k, *_ in ERAS)}</div></div>""", "dark"))
    for key, name, motto, c, since, text, mats, charm, needs in ERAS:
        charm_svg = G.CHARMS[charm] if charm else G.EMBLEMS["basilica"][1]
        charm_cap = "Charm" if charm else "No charms · seal"
        add(page(f"""
<div class="col-text">{tab(name)}<div class="motto" style="color:{c}">→ {E(motto)} ←</div><div class="since">{E(since)}</div><p>{E(text)}</p>
{brief(name + " keyframe", needs, "era-brief")}</div>
<div class="col-art paint-block era-art" style="--block:{c}">
  <div class="era-fig">{F.era_figure(key)}</div>
  <div class="era-side">
    <div class="era-card"><div class="omen-svg big">{G.OMENS[key][1]}</div><div class="cap">OMEN DISPLAY</div></div>
    <div class="era-card"><div class="omen-svg big">{charm_svg}</div><div class="cap">{E(charm_cap.upper())}</div></div>
    <div class="era-card mats">{chips(mats)}<div class="cap">MATERIALS</div></div>
  </div>
</div>{folio(n[0] + 1, "Styles")}""", "split"))

    cols = "".join(
        f'<div class="cmp"><div class="cmp-head" style="background:{c}">{E(nm)}</div><div class="cmp-fig">{F.era_figure(k)}</div>'
        f'<div class="cmp-row"><span>Charm</span><div class="omen-svg">{G.CHARMS[ch] if ch else G.EMBLEMS["basilica"][1]}</div></div>'
        f'<div class="cmp-row"><span>Omen display</span><div class="omen-svg">{G.OMENS[k][1]}</div></div>'
        f'<div class="cmp-cap">{E(m)}</div></div>'
        for k, nm, m, c, _s, _t, _m, ch, _n in ERAS)
    add(page(f'{tab("COMPARISON")}<div class="cmp-grid">{cols}</div>'
             f'<div class="cmp-note">The same three slots per era (a person, a charm, an Omen display), side by side so the eras read as one system. Design figures stand in until the painted comparison sheet (Art Book Production Guide §7, image 3).</div>{folio(n[0] + 1, "Styles")}', "padded"))

    # the Tally
    sections.append(("The Tally", n[0] + 1))
    add(page(f"""
<div class="col-text">{tab("THE TALLY")}<p>A ring of lands around Meridian's plateau. The upper city is sealed, so to go up you must go around. Each land kept its own ledger of fate before the Basilica bound them all.</p>
<p class="small">Red dotted line: the party's road, from Meridian's Undercity through five lands and back. The Upper Gate needs seven Seal Digits: 1 (Varro), 9, 8, 0, 2, 7, and the seventh is the player's own lucky number.</p></div>
<div class="col-art">{tally_map()}{stamp("SEALED", "red")}</div>{folio(n[0] + 1, "The Tally")}""", "split"))

    # Meridian
    sections.append(("Meridian · Prologue", n[0] + 1))
    add(land_page("meridian", n[0] + 1))
    add(page(f"""
<div class="col-text">{tab("MERIDIAN · REMAINDER WARDS")}<p>Stacked in the drains and cliffs beneath the plateau. The Wards began as workers' housing for the Basilica's builders and became the place where low Omens end up. Remainder scrap meets Charmpunk colour: every door wears a different culture's charm.</p>
<p class="small"><b>What happened here:</b> the Rounding. Every fraction of luck dropped since TR 702 flowed downhill, and so did everyone who lost theirs.</p></div>
<div class="col-art bleed" style="background-image:url('{img("art/concepts/env_meridian_establishing.jpg")}')">{placeholder_note()}{stamp("REMAINDER DETECTED", "red tilt")}</div>{folio(n[0] + 1, "Meridian")}""", "split"))
    add(page(f"""
<div class="col-text">{tab("KEY · REMAINDER WARDS")}<p>Colour key over the 3D base: overcast dawn after rain. Slate, ochre and moss walls, warm windows, every culture's laundry, the brass Basilica at the end of the canyon. Nixie orange, magenta and cyan live only on the signs.</p>
<p class="small"><b>Pipeline stage 1b · colour key.</b> Perspective, scale and light are solved in 3D first (see the pipeline page). Stage 2 paints over this; stage 3 is the artist's overpaint.</p></div>
<div class="col-art bleed" style="background-image:url('{img("art/base3d/wards_colorkey_v1.png")}')">{stamp("STAGE 1b · COLOUR KEY", "ph")}</div>{folio(n[0] + 1, "Meridian")}""", "split"))
    lineup = [("remainder", dict(h_m=1.78, sw=44, skin="#8D5A3B")),
              ("charmpunk", dict(h_m=1.52, sw=40, skin="#E8C9A8", overrides={"top": "#3BB273", "cap": "#FF2E88"})),
              ("charmpunk", dict(h_m=1.70, sw=38, skin="#C68B5E", overrides={"top": "#F5E400", "num": "#FF2E88", "cap": "#00E5FF"})),
              ("ledgerism", dict(h_m=1.95, sw=54, skin="#D9B08C", overrides={"coat": "#B7410E"})),
              ("remainder", dict(h_m=1.74, sw=46, skin="#F0D2B6", overrides={"cloak": "#5E7D4A"})),
              ("remainder", dict(h_m=1.22, sw=30, skin="#B97A56", overrides={"cloak": "#C8963E"}))]
    figs = "".join(f'<div class="lu">{F.era_figure(e, **kw)}</div>' for e, kw in lineup)
    add(page(f"""
<div class="col-text">{tab("LINE-UP · REMAINDER WARDS")}<p>Six locals, shoulder to shoulder, slightly low camera, over the district painting. Ages, builds and origins vary; every outfit is evidence of the Wards' economy.</p>
{brief("Remainder Wards line-up", ["Brass-scrap mechanic (Remainder)", "Grandmother with jade and evil-eye charms (Charmpunk)", "Teen dice-gambler (Charmpunk)", "Collector in rust armour (Ledgerism)", "Noodle cook with a lemon-and-chilli charm", "Kid with a cracked Nixie-tube necklace (Remainder)"])}
<div class="inset"><img src="{img("art/base3d/lineup_base_v1.png", 900)}" alt=""><div class="cap">3D BASE FOR THIS LINE-UP · STAGE 1</div></div></div>
<div class="col-art paint-block lineup" style="--block:#C8963E"><div class="lineup-row">{figs}</div><div class="tag">wards</div></div>{folio(n[0] + 1, "Meridian")}""", "split"))

    # Hyakki
    sections.append(("Hyakki · Act I", n[0] + 1))
    add(land_page("hyakki", n[0] + 1))
    add(page(f"""
<div class="col-text">{tab("HYAKKI · MOON PIER")}<p>Volcanic islands where humans and yokai share festivals. The pier is where the party lands: lanterns, fireflies, and the Night Parade crossing the far ridge. Its deck is the Act I battle floor; the torii's three lanterns are the reel.</p>
<p class="small"><b>Meridian intrusion:</b> a Ledgerist toll gate on the shrine road.</p></div>
<div class="col-art bleed" style="background-image:url('{img("art/concepts/env_hyakki_battle_deck.jpg")}')">{placeholder_note()}</div>{folio(n[0] + 1, "Hyakki")}""", "split"))
    add(page(f"""
<div class="col-text">{tab("KEY · MOON PIER")}<p>Colour key: indigo night, vermilion torii, lantern gold, moon cream. The paint pass adds mist, fireflies, sea glints and the Night Parade on the ridge, and keeps the deck clear for the fight.</p>
<p class="small"><b>Pipeline stage 1b · colour key</b> over the 3D base on the pipeline page.</p></div>
<div class="col-art bleed" style="background-image:url('{img("art/base3d/hyakki_pier_colorkey_v1.png")}')">{stamp("STAGE 1b · COLOUR KEY", "ph")}</div>{folio(n[0] + 1, "Hyakki")}""", "split"))

    # the other lands
    for key, label in [("river", "The River Empire · Act II"), ("sunyapura", "Śūnyapura · Act III"), ("kroton", "Kroton Nova · Act IV"),
                       ("crossroads", "The Crossroads · Act V"), ("basilica", "The Basilica · Finale")]:
        sections.append((label, n[0] + 1))
        add(land_page(key, n[0] + 1))

    # the reel, land by land
    reels = "".join(f'<div class="reel"><div class="reel-svg">{s}</div><b>{E(nm)}</b><div class="eff">{E(C.LANDS[LAND_KEYS[k]][0])}</div></div>'
                    for k, (nm, s) in G.REELS.items())
    add(page(f'{tab("THE REEL, LAND BY LAND")}<p class="lead-p">The three slots where stopped digits land are always an object from the world, never a UI panel (GDD §8). Same three digits, seven cultures.</p>'
             f'<div class="reels">{reels}</div>{folio(n[0] + 1, "The lands")}', "padded"))

    # cast
    sections.append(("Characters", n[0] + 1))
    def cast_row(keys, h_mm):
        cells = ""
        for k in keys:
            w = h_mm * F.crop_width(k) / 278
            nm = CHAR[k][0].replace("Comptroller ", "").replace("Chancellor ", "").replace(" of the Ninety-Nine", "").replace(" of Kroton", "")
            cells += (f'<div class="cs" style="width:{w:.1f}mm"><div class="cs-col" style="height:{h_mm}mm">{F.figure(k)}</div>'
                      f'<b>{E(nm)}</b><i>{E(CHAR[k][2])}</i></div>')
        return cells
    ink_row = "".join(f'<div class="cs-ink" style="width:{16 * F.crop_width(k) / 278:.1f}mm">{F.figure(k, "ink")}</div>' for k in C.FIGURE_KEYS)
    add(page(f"""{tab("CAST · READABILITY")}<p class="lead-p">Every character must read as a solid black silhouette at 64 px and by colour alone (Character Bible §0). Shared scale, true relative heights: heroes on top, Auditors below.</p>
<div class="cast ink">{ink_row}</div><div class="cast col">{cast_row(HERO_KEYS, 60)}</div><div class="cast col">{cast_row(BOSS_KEYS, 60)}</div>{folio(n[0] + 1, "Characters")}""", "padded"))
    add(page(f"""
<div class="col-art bleed full" style="background-image:url('{img("art/concepts/nil_keyart.jpg")}')"></div>
<div class="kf-overlay">{tab("KEYFRAME · NIL")}<div class="spray">NaN?</div></div>{placeholder_note()}""", "kf"))
    for i, k in enumerate(HERO_KEYS, start=1):
        add(hero_sheet(k, i, n[0] + 1))

    # Auditors and keepers
    sections.append(("Auditors and Keepers", n[0] + 1))
    rules = {r[0].split(",")[0]: r[1] for r in C.md_table("docs/GDD.md", "### 4.3")}
    boss_rule_key = {"varro": "Varro", "tamamo": "Tamamo", "jin_chan": "Jin Chan", "rahu_ketu": "Rahu & Ketu", "archon": "Archon Seventeen",
                     "house": "The House", "thale": "Comptroller Thale"}
    cards = ""
    for k in BOSS_KEYS:
        name, role, digit, land, *_ = CHAR[k]
        cards += (f'<div class="boss"><div class="boss-fig">{F.figure(k)}</div><b>{E(name)}</b><div class="land">{E(role)} · {E(land)}</div>'
                  f'<div class="eff">{E(rules.get(boss_rule_key[k], ""))}</div></div>')
    add(page(f"""{tab("AUDITORS")}<div class="bosses">{cards}</div>
<div class="keepers"><b>Keepers, not villains.</b> Enma (Hyakki) · Judge Cui (the Ten Courts) · Chitragupta (Śūnyapura) · the Moirai (Kroton Nova) · the Stranger (the Crossroads). Shown with reverence, never as monsters; they test the party and are never "defeated", only satisfied (World Bible §10).</div>{folio(n[0] + 1, "Auditors")}""", "padded"))

    # factions & symbols
    sections.append(("Factions, symbols and charms", n[0] + 1))
    meanings = {"basilica": "A brass gear around the Basilica's eye, which reads as a 0. Order, the Ledger, Fixed Fate.",
                "collectors": "A hound skull on a ledger seal. Debts and bounties.",
                "bazaar": "A ring of mixed charms around a lucky 7. Folk luck, trade, survival.",
                "yokai": "Nine foxfire flames around a violet heart. The spirits of Hyakki.",
                "exchange": "The three-legged money toad with a coin. Luck as profit.",
                "ten_courts": "The Judge's brush over the river of the dead.",
                "observatory": "An astrolabe around a zero. Truth by measurement.",
                "synod": "The tetractys of ten dots inside a sieve ring. Purity of number.",
                "house": "The ouroboros around 89. The night that never ends."}
    em = "".join(f'<div class="emblem"><div class="em-svg">{svg}</div><b>{E(nm)}</b><div class="eff">{E(meanings[k])}</div></div>' for k, (nm, svg) in G.EMBLEMS.items())
    add(page(f'{tab("FACTIONS & SYMBOLS")}<div class="emblems">{em}</div>{folio(n[0] + 1, "Factions")}', "padded"))

    gdd_charms = {r[0].split(" (")[0]: (r[1], r[2]) for r in C.md_table("docs/GDD.md", "### 3.1")}
    charm_keys = [("Beckoning Cat", "beckoning_cat"), ("Daruma", "daruma"), ("Red Envelope", "red_envelope"), ("Door God", "door_god"),
                  ("Lemon and Seven Chillies", "lemon_chillies"), ("108 Beads", "beads_108"), ("Evil-Eye Bead", "evil_eye"),
                  ("Fortuna's Wheel", "fortuna_wheel"), ("Horseshoe", "horseshoe"), ("Seven-Come-Eleven Dice", "dice"),
                  ("Four-Leaf Clover", "clover"), ("Black Cat", "black_cat")]
    cards = "".join(f'<div class="charm"><div class="icon">{G.CHARMS[k]}</div><div><b>{E(nm)}</b><div class="land">{E(gdd_charms[nm][0])}</div>'
                    f'<div class="eff">{E(gdd_charms[nm][1])}</div></div></div>' for nm, k in charm_keys)
    add(page(f'{tab("CHARMS OF THE WORLD")}<div class="charms">{cards}</div><div class="cmp-note">Rules quoted from GDD §3.1. Twelve of the ~90 planned; sets by land grant set bonuses.</div>{folio(n[0] + 1, "Charms")}', "padded"))

    # pipeline
    sections.append(("How an image is made", n[0] + 1))
    def stage_cell(rel, label):
        if rel:
            return f'<div class="pl-cell"><div class="pl-img" style="background-image:url(\'{img(rel, 1000)}\')"></div><div class="cap">{E(label)}</div></div>'
        return f'<div class="pl-cell"><div class="pl-img empty"><span>PENDING</span></div><div class="cap">{E(label)}</div></div>'
    rows = ""
    for title, base, key in [("REMAINDER WARDS", "art/base3d/wards_base_clay.png", "art/base3d/wards_colorkey_v1.png"),
                             ("MOON PIER", "art/base3d/hyakki_pier_base_v1.png", "art/base3d/hyakki_pier_colorkey_v1.png")]:
        rows += (f'<div class="pl-row"><div class="pl-title">{title}</div>{stage_cell(base, "1 · 3D BASE (Blender)")}{stage_cell(key, "1b · COLOUR KEY")}'
                 f'{stage_cell(None, "2 · PAINT PASS (Higgsfield / FLUX)")}{stage_cell(None, "3 · HUMAN OVERPAINT")}</div>')
    add(page(f'{tab("PIPELINE · FROM BASE TO PAINTING")}<p class="lead-p">How every environment in this book is made (Art Book Production Guide §4): perspective and scale solved in 3D, colour decided on a flat key, then painted, then overpainted by hand.</p>'
             f'<div class="pipeline">{rows}</div>{folio(n[0] + 1, "Pipeline")}', "padded"))

    # status
    first12 = C.numbered_list("docs/ARTBOOK_PRODUCTION.md", "## 7.")
    standins = {0: "colour key", 1: "design figures + 3D base", 2: "design figures", 4: "design figure", 5: "design figure", 6: "design figure",
                7: "design figure", 8: "colour key", 10: "design figure", 11: "design figure"}
    items = "".join(f'<li><span>{E(t.rstrip("."))}</span><em>{E("stand-in: " + standins[i]) if i in standins else "pass-1 placeholder"}</em></li>'
                    for i, t in enumerate(first12))
    add(page(f"""<div class="opener">{tab("DRAFT " + VERSION)}<div class="opener-title">ART PENDING</div>
<p class="opener-sub">This draft sets the layout grammar and the design system. The paintings fill in as register-A concept art is produced, starting with these twelve (Art Book Production Guide §7). Rebuild with python3 tools/build_artbook.py.</p>
<ol class="first12">{items}</ol></div>""", "dark"))

    # contents page
    toc = "".join(f'<li><span>{E(t)}</span><b>{p:02d}</b></li>' for t, p in sections)
    P[contents_index] = page(f"""<div class="col-text">{tab("CONTENTS")}<p class="lede">A ledger of the Tally, as drawn so far.</p>
<p class="small">Page numbers in the corner of each spread. Placeholder stamps mark pass-1 art kept for layout; colour-key and design-figure stamps mark the designed stand-ins.</p></div>
<div class="col-art toc-art"><ol class="toc">{toc}</ol></div>{folio(3, "Contents")}""", "split")

    fonts = ("https://fonts.googleapis.com/css2?family=Big+Shoulders+Display:wght@700;900&family=Barlow+Semi+Condensed:wght@400;600;700"
             "&family=JetBrains+Mono:wght@400;700&family=Permanent+Marker&family=Noto+Sans+JP:wght@700&family=Noto+Sans+SC:wght@700"
             "&family=Noto+Sans+Devanagari:wght@700&display=swap")
    doc = (f'<!doctype html><html><head><meta charset="utf-8"><title>ZERO-SUM: OMEN Art Book Draft</title>'
           f'<link rel="stylesheet" href="{fonts}"><style>{css}</style></head><body>{"".join(P)}</body></html>')
    path = os.path.join(BUILD, "artbook.html")
    with open(path, "w", encoding="utf-8") as f:
        f.write(doc)
    return path


if __name__ == "__main__":
    p = build()
    r = subprocess.run(["node", os.path.join(ROOT, "tools", "render_pdf.js"), p, OUT, "landscape"])
    sys.exit(r.returncode)
