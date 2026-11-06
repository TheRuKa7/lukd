#!/usr/bin/env python3
"""Build the ZERO-SUM: OMEN art book DRAFT (landscape spreads) as a PDF.

Layout grammar follows docs/ARTBOOK_PRODUCTION.md §1 and §6: label tabs, text column, art bleeding to the
edge, a rough colour block, stamps and tally-mark overlays. Missing art shows a brief panel.
Usage: python3 tools/build_artbook.py
"""
import html
import os
import subprocess
import sys

from PIL import Image

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import graphics as G  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BUILD = os.path.join(ROOT, "build", "artbook")
IMG = os.path.join(BUILD, "img")
OUT = os.path.join(ROOT, "docs", "ZERO-SUM_OMEN_Artbook_Draft.pdf")
os.makedirs(IMG, exist_ok=True)


def img(rel, max_side=1800):
    src = os.path.join(ROOT, rel)
    name = os.path.splitext(os.path.basename(rel))[0] + ".jpg"
    dst = os.path.join(IMG, name)
    if not os.path.exists(dst):
        im = Image.open(src).convert("RGB")
        im.thumbnail((max_side, max_side))
        im.save(dst, quality=84, optimize=True, progressive=True)
    return "img/" + name


E = html.escape


def tab(text, dark=True):
    return f'<div class="tab{" light" if not dark else ""}">{E(text)}</div>'


def stamp(text, cls=""):
    return f'<div class="stamp {cls}">{E(text)}</div>'


def placeholder_note():
    return stamp("PLACEHOLDER · PASS 1 ART", "ph")


def brief(title, lines):
    items = "".join(f"<li>{E(l)}</li>" for l in lines)
    return f'<div class="brief"><div class="brief-title">ART NEEDED · {E(title)}</div><ul>{items}</ul></div>'


def figure_slots(n, heights):
    figs = []
    for i in range(n):
        h = heights[i % len(heights)]
        figs.append(
            f'<svg class="slot-fig" viewBox="0 0 60 200" style="height:{h}%"><g fill="#141018" opacity=".82">'
            f'<circle cx="30" cy="16" r="12"/><path d="M14 34 h32 l6 70 h-8 l-2 96 h-10 l-2-60 l-2 60 h-10 l-2-96 h-8z"/></g></svg>'
        )
    return '<div class="slots">' + "".join(figs) + "</div>"


def page(inner, cls=""):
    return f'<section class="page {cls}">{inner}</section>'


def tally_map():
    lands = [
        ("HYAKKI", "Act I", 150, 120, "#E34234"),
        ("RIVER EMPIRE", "Act II", 470, 90, "#00A86B"),
        ("ŚŪNYAPURA", "Act III", 520, 330, "#F4A300"),
        ("KROTON NOVA", "Act IV", 300, 430, "#1F6FB2"),
        ("CROSSROADS", "Act V", 90, 340, "#B7410E"),
    ]
    marks = []
    for name, act, x, y, c in lands:
        marks.append(
            f'<g><circle cx="{x}" cy="{y}" r="46" fill="{c}" opacity=".22"/><circle cx="{x}" cy="{y}" r="46" fill="none" stroke="{c}" stroke-width="3" stroke-dasharray="6 5"/>'
            f'<text x="{x}" y="{y - 4}" text-anchor="middle" class="m-name">{name}</text><text x="{x}" y="{y + 16}" text-anchor="middle" class="m-act">{act}</text></g>'
        )
    path = "M150 120 C 300 40, 400 60, 470 90 S 600 250, 520 330 S 380 470, 300 430 S 60 420, 90 340 S 80 200, 150 120"
    return f"""<svg class="map" viewBox="0 0 640 520" xmlns="http://www.w3.org/2000/svg">
<rect width="640" height="520" fill="#EFE3CC"/>
<g stroke="#141018" stroke-opacity=".07">{''.join(f'<line x1="0" y1="{y}" x2="640" y2="{y}"/>' for y in range(0, 520, 26))}</g>
<path d="{path}" fill="none" stroke="#B3261E" stroke-width="3" stroke-dasharray="2 9" stroke-linecap="round"/>
<circle cx="320" cy="250" r="70" fill="#141018"/><circle cx="320" cy="250" r="70" fill="none" stroke="#FF7A2C" stroke-width="4"/>
<text x="320" y="245" text-anchor="middle" class="m-core">MERIDIAN</text><text x="320" y="268" text-anchor="middle" class="m-core-sub">THE BASILICA · PROLOGUE · FINALE</text>
{''.join(marks)}
<text x="560" y="500" class="m-tally">|||| |||| ||</text>
</svg>"""


BASES = [
    ("art/base3d/wards_base_clay.png", "BASE · REMAINDER WARDS", "The Wards as a canyon of stacked tenements: balconies, pipes, rope bridges, laundry lines and signs, with the Basilica's eye at the end of the street.", "STAGE 1 · 3D BASE"),
    ("art/base3d/wards_colorkey_v1.png", "KEY · REMAINDER WARDS", "Colour key over the same base: overcast dawn after rain. Slate, ochre and moss walls, warm windows, mixed-culture laundry, brass Basilica. Nixie orange, magenta and cyan live only on the signs.", "STAGE 1b · COLOUR KEY"),
    ("art/base3d/hyakki_pier_base_v1.png", "BASE · MOON PIER", "Hyakki's arrival pier at night: torii with the three lantern reels, stone lanterns, the moon over the sea. Deck is the battle floor; the lanterns become the reel.", "STAGE 1 · 3D BASE"),
    ("art/base3d/hyakki_pier_colorkey_v1.png", "KEY · MOON PIER", "Colour key: indigo night, vermilion torii, lantern gold, moon cream. The paint pass adds mist, fireflies, sea glints and the night parade on the ridge.", "STAGE 1b · COLOUR KEY"),
    ("art/base3d/lineup_base_v1.png", "BASE · LINE-UP", "Six figures of different heights and builds, slightly low camera, ready for the Remainder Wards line-up paint pass.", "STAGE 1 · 3D BASE"),
]


def build():
    with open(os.path.join(ROOT, "tools", "artbook.css"), encoding="utf-8") as f:
        css = f.read()
    P = []

    # 1 cover
    P.append(page(f"""
<div class="cover-art" style="background-image:url('{img("art/concepts/env_meridian_establishing.jpg")}')"></div>
<div class="cover-block"></div>
<div class="cover-text"><div class="kicker">THE OFFICIAL ART BOOK OF</div><div class="title">ZERO&#8209;SUM:<br><span>OMEN</span></div><div class="kicker">DRAFT LAYOUT · v0.1</div></div>
{stamp("NaN", "big")}{placeholder_note()}""", "cover"))

    # 2 foreword
    P.append(page(f"""
<div class="col-text">{tab("FOREWORD")}
<p class="lede">Every number in this world is spinning. This book is about the people who live under them.</p>
<p>The Tally began as a question: what would a world look like if luck were a currency everyone could see? Our answer was a city that counts and a ring of lands that remember older ways of counting: thread, karma, contracts and books of the dead.</p>
<p>We built every style from that history. The brass of the Basilica, the scrap of the Remainder Wards, the gaudy charms of the street, the gold leaf of the fortunate few, and the painted, breathing lands beyond the gate.</p>
<p class="sig">The ZERO-SUM: OMEN team</p></div>
<div class="col-art paint-block" style="--block:#FF7A2C"><div class="big-quote">"A WORLD WITHOUT LUCK<br>IS A WORLD WITHOUT LOSS."</div><div class="quote-by">Comptroller Lucan Thale</div></div>""", "split"))

    # 3 styles opener
    P.append(page(f"""<div class="opener">{tab("STYLES")}<div class="opener-title">THE FOUR<br>ERAS OF LUCK</div>
<p class="opener-sub">Meridian's styles come from its history: the binding of the ledgers, the Rounding, the Deficit. Every street mixes them; every outfit tells you which side of the Zero-Sum Law its owner lives on.</p>
<div class="tl"><div><b>TR 702</b>Basilica completed</div><div><b>TR 760→</b>Ledgerism</div><div><b>TR 850→</b>Charmpunk</div><div><b>TR 960→</b>Remainder</div><div><b>TR 990→</b>Gilded Fortune</div><div><b>TR 1002</b>Today</div></div></div>""", "dark"))

    eras = [
        ("CHARMPUNK", "LUCK OVER SENSE", "#FF2E88",
         "The street's lingua franca. Every culture's charms worn at once, hand-painted lucky numbers, plastic gold and neon. Charmpunk is loud because luck is a performance: if you can't raise your Omen, you can at least look like you're winning.",
         ["Line-up of 6 Bazaar locals in Charmpunk", "Keyframe: the Charm Bazaar at night, every stall a different culture", "Omen display: gaudy holo-halos, fake Omen projectors"]),
        ("REMAINDER", "SURVIVAL OVER LUCK", "#8A7F72",
         "The style of the Undercity, where Omens run low. Scrap brass from old Basilica parts, patched cloth, salvaged Nixie tubes and rope. Durable, ugly, honest. People hide their numbers here out of shame.",
         ["Line-up: Remainder Wards residents (mechanic, cook, debt-ridden mother, kids)", "Environment: Rain Alley 9 at dawn", "Omen display: a cracked tube on a cord"]),
        ("LEDGERISM", "ORDER OVER CHANCE", "#B5A642",
         "The style of the Basilica and its servants. Brass, steel and white enamel; cathedral arches; clockwork; uniforms with stamped seals. Cold, formal and threatening, it says that chance has been abolished and you are being counted.",
         ["Line-up: Collectors, Ledger-priests, Basilica clerks, Auditors", "Environment: the Basilica Ring checkpoint", "Omen display: steel numerals, never glowing"]),
        ("GILDED FORTUNE", "FORTUNE AND ORDER", "#D4AF37",
         "The style of the 99s: old money and Exchange magnates. Real gold leaf, jade, silk and living plants. In Meridian a garden is luck you can see; a bonsai on a balcony is a fortune worn in public.",
         ["Line-up: Exchange magnates, heirs, their guards", "Environment: the Exchange Terraces garden-villas", "Omen display: embroidered or gold-leaf numerals"]),
    ]
    for name, motto, c, text, needs in eras:
        P.append(page(f"""
<div class="col-text">{tab(name)}<div class="motto" style="color:{c}">→ {E(motto)} ←</div><p>{E(text)}</p></div>
<div class="col-art paint-block" style="--block:{c}">{brief(name + " keyframe", needs)}</div>""", "split"))

    # comparison
    cols = "".join(
        f'<div class="cmp"><div class="cmp-head" style="background:{c}">{E(n)}</div>{figure_slots(1, [86])}'
        f'<div class="cmp-row"><span>Charm</span><div class="mini-slot"></div></div><div class="cmp-row omen"><span>Omen display</span><div class="omen-svg">{G.OMENS[k][1]}</div></div>'
        f'<div class="cmp-cap">{E(m)}</div></div>'
        for (n, m, c, *_), k in zip(eras, ["charmpunk", "remainder", "ledgerism", "gilded"]))
    P.append(page(f'{tab("COMPARISON")}<div class="cmp-grid">{cols}</div>'
                  f'<div class="cmp-note">Same three slots per era (a person, a charm, an Omen display), drawn side by side so the eras read as one system. First Meridian concept task.</div>', "padded"))

    # map
    P.append(page(f"""
<div class="col-text">{tab("THE TALLY")}<p>A ring of lands around Meridian's plateau. The upper city is sealed, so to go up you must go around. Each land kept its own ledger of fate before the Basilica bound them all.</p>
<p class="small">Red dotted line: the party's road. Each land holds one Seal Digit; the seventh is the player's lucky number.</p></div>
<div class="col-art">{tally_map()}{stamp("SEALED", "red")}</div>""", "split"))

    # Meridian district
    P.append(page(f"""
<div class="col-text">{tab("MERIDIAN · REMAINDER WARDS")}<p>Stacked in the drains and cliffs beneath the plateau. The Wards began as workers' housing for the Basilica's builders and became the place where low Omens end up. Remainder scrap meets Charmpunk colour: every door wears a different culture's charm.</p>
<p class="small"><b>What happened here:</b> the Rounding. Every fraction of luck dropped since TR 702 flowed downhill, and so did everyone who lost theirs.</p></div>
<div class="col-art bleed" style="background-image:url('{img("art/concepts/env_meridian_establishing.jpg")}')">{placeholder_note()}{stamp("REMAINDER DETECTED", "red tilt")}</div>""", "split"))

    # line-up template
    P.append(page(f"""
<div class="col-text">{tab("LINE-UP · REMAINDER WARDS")}<p>Six locals, shoulder to shoulder, slightly low camera, over the district painting. Ages, builds and origins vary; every outfit is evidence of the Wards' economy.</p>
{brief("Remainder Wards line-up", ["Brass-scrap mechanic (Remainder)", "Grandmother with jade and evil-eye charms (Charmpunk)", "Teen dice-gambler (Charmpunk)", "Collector in rust armour (Ledgerism)", "Noodle cook with a lemon-and-chilli charm", "Kid with a cracked Nixie-tube necklace (Remainder)"])}</div>
<div class="col-art paint-block lineup" style="--block:#C8963E">{figure_slots(6, [78, 92, 70, 100, 84, 60])}<div class="tag">wards</div></div>""", "split"))

    # Hyakki
    P.append(page(f"""
<div class="col-text">{tab("HYAKKI · MOON PIER")}<p>Volcanic islands where humans and yokai share festivals. The pier is where the party lands: lanterns, fireflies, and the Night Parade crossing the far ridge.</p>
<p class="small"><b>Meridian intrusion:</b> a Ledgerist toll gate on the shrine road.</p></div>
<div class="col-art bleed" style="background-image:url('{img("art/concepts/env_hyakki_battle_deck.jpg")}')">{placeholder_note()}</div>""", "split"))

    # NIL keyframe
    P.append(page(f"""
<div class="col-art bleed full" style="background-image:url('{img("art/concepts/nil_keyart.jpg")}')"></div>
<div class="kf-overlay">{tab("KEYFRAME · NIL")}<div class="spray">NaN?</div></div>{placeholder_note()}""", "kf"))

    # NIL design sheet
    pal = "".join(f'<div class="chip" style="background:{c}"><span>{n}<br>{c}</span></div>' for n, c in
                  [("Nixie", "#FF7A2C"), ("Ink", "#141018"), ("Bone", "#EDE6DA"), ("Rim cyan", "#00E5FF")])
    callouts = ["Decoder on the RIGHT wrist: cracked brass, leaks orange light", "Coat: black actuary's coat, left tail longer, 3 brass ledger clasps",
                "Hair: bone white, one Nixie-orange streak", "Halo: broken holographic \"NaN\" (exact spelling)", "Gloves: fingerless; boots: tall, scuffed"]
    P.append(page(f"""
{tab("DESIGN SHEET · NIL")}
<div class="sheet">
  <div class="turn">{figure_slots(3, [92, 92, 92])}<div class="turn-cap"><span>FRONT</span><span>SIDE</span><span>BACK</span></div></div>
  <div class="sheet-side"><div class="sub">Callouts</div><ul class="callouts">{''.join(f'<li>{E(c)}</li>' for c in callouts)}</ul>
  <div class="sub">Palette</div><div class="pal">{pal}</div>
  <div class="sub">Expressions</div><div class="expr">{''.join('<div class="mini-slot round"></div>' for _ in range(6))}</div>
  <div class="sub">Props</div><div class="expr">{''.join('<div class="mini-slot"></div>' for _ in range(3))}</div></div>
</div>""", "padded"))

    # factions & symbols
    meanings = {"basilica": "A gear around the Basilica's eye. Order, the Ledger, Fixed Fate.",
                "collectors": "A hound skull on a ledger seal. Debts and bounties.",
                "bazaar": "A ring of mixed charms around a lucky 7. Folk luck, trade, survival.",
                "yokai": "Nine foxfire flames around a violet heart. The spirits of Hyakki.",
                "exchange": "The three-legged money toad with a coin. Luck as profit.",
                "ten_courts": "The Judge's brush over the river of the dead.",
                "observatory": "An astrolabe around a zero. Truth by measurement.",
                "synod": "The tetractys of ten dots on Aegean blue. Purity of number.",
                "house": "The ouroboros around 89. The night that never ends."}
    em = "".join(f'<div class="emblem"><div class="em-svg">{svg}</div><b>{E(name)}</b><div class="eff">{E(meanings[k])}</div></div>' for k, (name, svg) in G.EMBLEMS.items())
    P.append(page(f'{tab("FACTIONS & SYMBOLS")}<div class="emblems">{em}</div>', "padded"))

    # stage 1: 3D bases
    for rel, title, text, stage in BASES:
        if os.path.exists(os.path.join(ROOT, rel)):
            P.append(page(f"""
<div class="col-text">{tab(title)}<p>{E(text)}</p><p class="small"><b>Pipeline {stage.lower()}.</b> Perspective, scale and light are solved in 3D before any painting. Stage 2 paints over this render; stage 3 is the artist's overpaint (Art Book Production Guide §4).</p></div>
<div class="col-art bleed" style="background-image:url('{img(rel)}')">{stamp(stage, "ph")}</div>""", "split"))

    # charms catalog
    charms = [("Beckoning Cat", "Hyakki", "+1 fen per strike ending in your digit.", "beckoning_cat"), ("Daruma", "Hyakki", "Paint the second eye for ×2 Mult.", "daruma"),
              ("Red Envelope", "River Empire", "+8 fen on a Jackpot.", "red_envelope"), ("Door God", "River Empire", "Parries strike back.", "door_god"),
              ("Lemon & Seven Chillies", "Śūnyapura", "Cancels one curse; +7 per 7.", "lemon_chillies"), ("108 Beads", "Śūnyapura", "Every 108th point counts double.", "beads_108"),
              ("Evil-Eye Bead", "Kroton Nova", "See the enemy's next digit.", "evil_eye"), ("Fortuna's Wheel", "Kroton Nova", "Re-roll the reel once.", "fortuna_wheel"),
              ("Horseshoe", "Crossroads", "Your digit's cells 50% wider.", "horseshoe"), ("Seven-Come-Eleven Dice", "Crossroads", "×7 Mult on 7 or 11.", "dice"),
              ("Four-Leaf Clover", "Meridian", "1 in 4: duplicate a digit.", "clover"), ("Black Cat", "Meridian", "First Bust becomes a Pair.", "black_cat")]
    cards = "".join(f'<div class="charm"><div class="icon">{G.CHARMS[k]}</div><div><b>{E(n)}</b><div class="land">{E(l)}</div><div class="eff">{E(e)}</div></div></div>' for n, l, e, k in charms)
    P.append(page(f'{tab("CHARMS OF THE WORLD")}<div class="charms">{cards}</div>', "padded"))

    P.append(page(f"""<div class="opener">{tab("DRAFT")}<div class="opener-title">ART PENDING</div>
<p class="opener-sub">This draft sets the layout grammar. The art slots fill in as register-A concept art is produced (docs/ARTBOOK_PRODUCTION.md §7). Rebuild with python3 tools/build_artbook.py.</p></div>""", "dark"))

    fonts = ("https://fonts.googleapis.com/css2?family=Big+Shoulders+Display:wght@700;900&family=Barlow+Semi+Condensed:wght@400;600;700"
             "&family=JetBrains+Mono:wght@400;700&family=Permanent+Marker&family=Noto+Sans+JP:wght@700&family=Noto+Sans+Devanagari:wght@700&display=swap")
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
