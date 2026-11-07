"""Art book v1.0 sections: fixed art spec, world encyclopedia, faction styles, environment spreads, full cast spec pages.

Called from tools/build_artbook.py with a helper namespace H (img, tab, page, folio, chips, stamp). Every text block is
read from the Markdown docs (WORLD_ENCYCLOPEDIA, ART_SPEC, CHARACTER_BIBLE) through tools/canon.py, and every 3D image
comes from art/cast and art/envs (tools/render_cast.py, tools/build_envs.py, tools/postprocess_renders.py).
"""
import html
import os
import re

from PIL import Image

import canon as C
import graphics as G
from cast import CAST, GROUP_ORDER

E = html.escape
ROOT = C.ROOT
PPM = 260  # px per metre in the cast renders
ENC = "docs/WORLD_ENCYCLOPEDIA.md"
SPEC = "docs/ART_SPEC.md"
VIEWS = ["front", "left", "right", "back"]
HERO_SECTION = {"nil": 1, "vesper": 2, "maeve": 3, "hina": 4, "ba": 5, "bai_si": 6, "shunya": 7, "prima": 8, "fibi": 9}
LANDS = [("meridian", "Meridian Undercity", "Prologue"), ("hyakki", "Hyakki", "Act I"), ("river", "The River Empire", "Act II"),
         ("sunyapura", "Śūnyapura", "Act III"), ("kroton", "Kroton Nova", "Act IV"), ("crossroads", "The Crossroads Territory", "Act V"),
         ("basilica", "The Basilica", "Finale")]


def md(s):
    s = E(s)
    return re.sub(r"\*\*([^*]+)\*\*", r"<b>\1</b>", re.sub(r"\*([^*]+)\*", r"<i>\1</i>", s))


def table(headers, rows, cls="t"):
    th = "".join(f"<th>{E(h)}</th>" for h in headers)
    trs = "".join("<tr>" + "".join(f"<td>{md(c)}</td>" for c in r) + "</tr>" for r in rows)
    return f'<table class="{cls}"><thead><tr>{th}</tr></thead><tbody>{trs}</tbody></table>'


def view_path(key, v):
    return f"art/cast/views/{key}_{v}.png"


def view_size(key, v):
    with Image.open(os.path.join(ROOT, view_path(key, v))) as im:
        return im.size


def fit_k(key, max_w, max_h, views=VIEWS, gap=6):
    sizes = [view_size(key, v) for v in views]
    return min((max_w - gap * (len(views) - 1)) / sum(w for w, _ in sizes), max_h / max(h for _, h in sizes))


def views_row(H, key, max_w, max_h, views=VIEWS, labels=True, gap=6, k_cap=None):
    sizes = [view_size(key, v) for v in views]
    th = max(h for _, h in sizes)
    k = fit_k(key, max_w, max_h, views, gap)  # mm per px
    if k_cap:
        k = min(k, k_cap)
    cells = ""
    for v, (w, h) in zip(views, sizes):
        lab = f'<div class="vlab">{v.upper()}</div>' if labels else ""
        cells += f'<div class="vcell"><img src="{H.img(view_path(key, v), 1400)}" style="width:{w * k:.1f}mm;height:{h * k:.1f}mm">{lab}</div>'
    return cells, k, th


def part_opener(H, num, title, sub, items):
    lis = "".join(f"<li>{E(i)}</li>" for i in items)
    return H.page(f"""<div class="opener">{H.tab("PART " + num)}<div class="opener-title">{E(title)}</div>
<p class="opener-sub">{E(sub)}</p><ol class="part-list">{lis}</ol></div>""", "dark")


# ---------------------------------------------------------------- Part I: the fixed art spec
def spec_pages(H, n):
    P = []
    P.append(part_opener(H, "I", "FIXED ART SPEC", "The numbers and rules every artist, modeller and animator works to (docs/ART_SPEC.md).",
                         ["Art Direction v3: painted world, inked manga", "Style frames: versus, impact, gag, manga page", "Registers, line, shading, colour", "Scale and proportion", "Cameras and the battle stage", "Light by land", "Faction costume keys"]))
    AD = "docs/ART_DIRECTION.md"
    infl = C.md_table(AD, "### 0.1")
    regs = C.md_table(AD, "### 0.2")
    P.append(H.page(f"""{H.tab("ART DIRECTION v3 · PAINTED WORLD, INKED MANGA")}<p class="lead-p">v2 stays (painted Ghibli-spirit worlds, Edgerunners-spirit people, Cyberpunk-art-book method). v3 adds a coloured-manga layer learned from the methods of Berserk, One Punch Man and versus-battle manga, with witty humour as a core register. Method, never likeness.</p>
<div class="two-col"><div>{table(["Influence", "What it does", "What we take", "What we never take"], infl, "t small")}</div>
<div>{table(["", "SERIOUS", "GAG"], regs, "t small")}</div></div>{H.folio(n + 2, "Art direction v3")}""", "padded"))
    frames = "".join(f'<figure><img src="{H.img(f"art/style_v3/{k}.png", 1600)}"><figcaption>{E(c)}</figcaption></figure>'
                     for k, c in (("versus_card", "Versus card before every boss (§0.5)"), ("impact_frame", "Impact frame: ink + paper + signature colour (§0.4)"),
                                  ("gag_panel", "GAG register: flat, front-on, still (§0.2)")))
    P.append(H.page(f"""{H.tab("ART DIRECTION v3 · STYLE FRAMES")}<div class="v3-frames">{frames}</div>
<p class="cmp-note">Treatment studies built locally from the 3D blockouts (tools/style_frames_v3.py): screentone, heavy ink, speed lines, digit SFX and balloons. Final art redraws the figures by hand over these layouts.</p>{H.folio(n + 3, "Art direction v3")}""", "padded"))
    beats = C.md_table(AD, "### 0.4")
    P.append(H.page(f"""<div class="v3-page"><img src="{H.img("art/style_v3/manga_page.png", 1600)}"></div>
<div class="v3-side">{H.tab("CUTSCENES AS MANGA PAGES · FIGHT BEATS")}<p>Cutscenes are animated manga pages: panels slide in on beats, the camera pushes inside a panel, balloons pop with sound, one splash per scene. Cheap, deterministic in Unity Timeline, on-style.</p>
{table(["Beat", "Frames (60 fps)", "Visual"], beats, "t small")}</div>{H.folio(n + 4, "Art direction v3")}""", "padded v3-pagewrap"))
    n += 3
    reg = [["A · Concept / art book", "Key art, store page, art book", "Painterly semi-realistic concept art over 3D bases; human overpaint"],
           ["B · In game", "Gameplay, cutscenes, UI", "Painted world (gouache backgrounds), inked people (flat cel, coloured lines)"]]
    line = C.md_table(SPEC, "### 2.3")
    P.append(H.page(f"""{H.tab("ART SPEC · REGISTERS, LINE, SHADING, COLOUR")}
<div class="two-col"><div>{table(["Register", "For", "Look"], reg)}<div class="sub">Turnaround standard</div>
<ul class="callouts"><li>FRONT · LEFT · RIGHT · BACK, orthographic, one baseline, 1 m = 260 px</li><li>Relaxed A-pose; props in their canon hand</li>
<li>Every story outfit gets its own full turnaround</li><li>Sheet extras: height bar, palette hex, canon locks, 64 px silhouette test</li></ul></div>
<div>{table(["Element", "Rule"], line)}</div></div>{H.folio(n + 2, "Art spec")}""", "padded"))
    # scale lineup: heroes + secret recruits at one scale
    keys = ["nil", "vesper", "maeve", "hina", "ba", "bai_si", "shunya", "prima", "fibi", "varro_ally", "kyusuke", "liu_shun"]
    k = 0.135  # mm per px (all renders share 260 px/m)
    cells = ""
    for key in keys:
        w, h = view_size(key, "front")
        c = next(c for c in CAST if c["key"] == key)
        cells += (f'<div class="lu-cell"><img src="{H.img(view_path(key, "front"), 900)}" style="width:{w * k:.1f}mm;height:{h * k:.1f}mm">'
                  f'<b>{E(c["name"].split(" (")[0].replace("Granny ", "").replace(" the Kappa", ""))}</b><i>{c["h"]:.2f} m</i></div>')
    rule = "".join(f'<div class="hline" style="bottom:{14 + m * PPM * k:.1f}mm"><span>{m:.1f} m</span></div>' for m in (0.5, 1.0, 1.5, 2.0))
    cls = C.md_table(SPEC, "### 2.1")
    P.append(H.page(f"""{H.tab("ART SPEC · SCALE AND PROPORTION")}<p class="lead-p">Heroes and secret recruits at one scale (1 m = 260 px in the model sheets). Adults are 7.5 heads tall; children 5–6; elders 6.5; bosses 8–9. Heights are canon locks.</p>
<div class="scale-box">{rule}<div class="lineup-scale">{cells}</div></div>
<div class="scale-table">{table(["Class", "Height range", "Shoulder width", "Notes"], cls, "t small")}</div>{H.folio(n + 3, "Art spec")}""", "padded scale-page"))
    cams = C.md_table(SPEC, "### 3.2")
    stage = """<svg viewBox="0 0 300 90" class="stage-svg"><rect x="10" y="30" width="280" height="50" fill="#E9E2D0" stroke="#141018" stroke-width="1.5"/>
<text x="150" y="22" text-anchor="middle" class="sv">BATTLE STAGE · 24 m × 6 m, flat, clear</text>
<rect x="135" y="4" width="30" height="10" fill="#FF7A2C"/><text x="150" y="12" text-anchor="middle" class="sv2">REEL</text>
""" + "".join(f'<circle cx="{x}" cy="55" r="6" fill="#141018"/>' for x in (45, 70, 95)) + """
<rect x="195" y="38" width="40" height="34" fill="#B3261E"/><text x="70" y="75" text-anchor="middle" class="sv2">PARTY x −8…−3</text>
<text x="215" y="86" text-anchor="middle" class="sv2">ENEMY x +3…+9</text></svg>"""
    thumbs = "".join(f'<figure><img src="{H.img(f"art/envs/{l}_{v}.png", 900)}"><figcaption>{E(c)}</figcaption></figure>'
                     for l, v, c in (("hyakki", "front", "Battle · front view"), ("meridian", "iso", "Exploration · 2.5D"), ("meridian", "top", "Plan · top-down")))
    P.append(H.page(f"""{H.tab("ART SPEC · CAMERAS AND THE STAGE")}<div class="two-col"><div>{table(["Camera", "Projection", "Angle", "Use"], cams)}{stage}</div>
<div class="thumbs3">{thumbs}</div></div>{H.folio(n + 4, "Art spec")}""", "padded"))
    light = C.md_table(SPEC, "### 3.4")
    keys_ = C.md_table(SPEC, "### 2.5")
    P.append(H.page(f"""{H.tab("ART SPEC · LIGHT BY LAND · FACTION COSTUME KEYS")}<div class="two-col"><div>{table(["Land", "Time", "Key light", "Fill / ambient", "Atmosphere"], light, "t small")}</div>
<div>{table(["Faction", "Base colours", "Materials", "Must have", "Never"], keys_, "t small")}</div></div>{H.folio(n + 5, "Art spec")}""", "padded"))
    return P


# ---------------------------------------------------------------- Part II: the world
def luck_flow_svg():
    boxes = [("HAP", "the god of luck, caged", "#141026", "#F4F1EA"), ("EVEN HAND ENGINE", "the Basilica's heart", "#B5A642", "#141018"),
             ("DAWN TALLY", "divides the god at sunrise", "#E8E6E1", "#141018"), ("OMENS 00–99", "every soul's share", "#FF7A2C", "#141018"),
             ("AUDITS · DEBTS", "luck moves between people", "#B7410E", "#F4F1EA"), ("SETTLED", "00: luck returns to the pool", "#4A4E54", "#F4F1EA")]
    out, x = [], 6
    for i, (t, s, bg, fg) in enumerate(boxes):
        out.append(f'<rect x="{x}" y="20" width="92" height="44" rx="4" fill="{bg}" stroke="#141018" stroke-width="1.5"/>'
                   f'<text x="{x + 46}" y="40" text-anchor="middle" class="fl1" fill="{fg}">{t}</text><text x="{x + 46}" y="54" text-anchor="middle" class="fl2" fill="{fg}">{s}</text>')
        if i < len(boxes) - 1:
            out.append(f'<path d="M{x + 94} 42 h10" stroke="#141018" stroke-width="2" marker-end="url(#ar)"/>')
        x += 106
    out.append('<path d="M576 64 v24 H52 v-24" fill="none" stroke="#141018" stroke-width="1.5" stroke-dasharray="4 3" marker-end="url(#ar)"/>'
               '<text x="314" y="100" text-anchor="middle" class="fl2" fill="#141018">luck is conserved: every gain is someone else\'s loss</text>'
               '<path d="M264 20 v-12 H600" fill="none" stroke="#FF7A2C" stroke-width="2" stroke-dasharray="3 3"/>'
               '<rect x="600" y="0" width="34" height="18" rx="3" fill="#FF7A2C"/><text x="617" y="13" text-anchor="middle" class="fl1" fill="#141018">NIL</text>'
               '<text x="430" y="5" text-anchor="middle" class="fl2" fill="#B3261E">the Rounding: fractions shaved off every dawn → the Remainder</text>')
    return ('<svg viewBox="0 0 640 108" class="flow-svg"><defs><marker id="ar" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto">'
            '<path d="M0 0 L10 5 L0 10z" fill="#141018"/></marker></defs>' + "".join(out) + "</svg>")


def timeline_svg(rows):
    eras = [("THE NOISE", -300, -200, "#4A4E54"), ("MANY LEDGERS", -200, 0, "#7A8B4A"), ("FOUNDING", 0, 380, "#C8963E"), ("THE BINDING", 380, 702, "#8C6A3F"),
            ("LEDGERISM", 702, 850, "#B5A642"), ("CHARMPUNK", 850, 960, "#FF2E88"), ("REMAINDER · DEFICIT", 960, 990, "#8A7F72"), ("GILDED", 990, 1002, "#D4AF37")]
    def X(t):
        return 20 + (t + 300) / 1320 * 600
    out = []
    for name, a, b, c in eras:
        out.append(f'<rect x="{X(a):.1f}" y="40" width="{X(b) - X(a):.1f}" height="22" fill="{c}"/>'
                   f'<text x="{(X(a) + X(b)) / 2:.1f}" y="76" text-anchor="middle" class="tl1">{name}</text>')
    for t, lab in ((0, "TR 0"), (380, "380"), (702, "702 · Hap caged"), (960, "960"), (1002, "1002 · now")):
        out.append(f'<path d="M{X(t):.1f} 34 v34" stroke="#141018" stroke-width="1.5"/><text x="{X(t):.1f}" y="28" text-anchor="middle" class="tl2">{lab}</text>')
    return '<svg viewBox="0 0 640 86" class="tl-svg">' + "".join(out) + "</svg>"


def politics_svg():
    def box(x, y, w, h, t, s, bg="#E9E2D0", fg="#141018"):
        return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="4" fill="{bg}" stroke="#141018" stroke-width="1.5"/>'
                f'<text x="{x + w / 2}" y="{y + h / 2 - 2}" text-anchor="middle" class="fl1" fill="{fg}">{t}</text>'
                f'<text x="{x + w / 2}" y="{y + h / 2 + 11}" text-anchor="middle" class="fl2" fill="{fg}">{s}</text>')
    lands = [("HYAKKI", "Tamamo"), ("RIVER EMPIRE", "Jin Chan"), ("ŚŪNYAPURA", "Rahu & Ketu"), ("KROTON NOVA", "Archon Seventeen"), ("CROSSROADS", "The House")]
    out = [box(230, 4, 180, 40, "THE COMPTROLLER", "Lucan Thale, for life", "#E8E6E1"),
           box(20, 70, 180, 40, "BOARD OF ACTUARIES", "12 seniors · choose the Comptroller"),
           box(440, 70, 180, 40, "LEDGER ASSEMBLY", "votes weighted by Omen"),
           box(230, 70, 180, 40, "THE BASILICA", "Dawn Tally · Seals · Collectors", "#B5A642"),
           '<path d="M320 44 v26 M200 90 h30 M410 90 h30" stroke="#141018" stroke-width="1.5"/>']
    for i, (l, a) in enumerate(lands):
        x = 8 + i * 126
        out.append(box(x, 150, 116, 40, l, "Seal · " + a, "#F2E8D5"))
        out.append(f'<path d="M320 110 L{x + 58} 150" stroke="#B3261E" stroke-width="1.2" stroke-dasharray="3 3"/>')
    out.append('<text x="320" y="138" text-anchor="middle" class="fl2" fill="#B3261E">SEAL PACTS (TR 999): protection now, permanence under Fixed Fate</text>')
    return '<svg viewBox="0 0 640 196" class="pol-svg">' + "".join(out) + "</svg>"


def operations():
    text = open(os.path.join(ROOT, ENC), encoding="utf-8").read()
    sec = text.split("## 6.")[1].split("\n## ")[0]
    out = []
    for ln in sec.splitlines():
        m = re.match(r"\*\*([^*]+)\.\*\*\s*(.*)", ln.strip())
        if m:
            out.append((m.group(1), m.group(2)))
    return out


FACTION_VIS = {  # name prefix -> (emblem svg, archetype keys for 3D views, palette)
    "The Basilica": (G.EMBLEMS["basilica"][1], ["f_ledger_priest", "f_auditor"], [("Steel white", "#E8E6E1"), ("Brass", "#B5A642"), ("Olive", "#6E6B4E"), ("Nixie", "#FF7A2C")]),
    "The Collectors": (G.EMBLEMS["collectors"][1], ["f_collector", "varro"], [("Rust", "#B7410E"), ("Gunmetal", "#4A4E54"), ("Debt glow", "#FF7A2C"), ("Bone", "#E3DCCB")]),
    "Charm Bazaar guilds": (G.EMBLEMS["bazaar"][1], ["f_charmpunk", "gus"], [("Magenta", "#FF2E88"), ("Sign yellow", "#F5E400"), ("Cyan", "#00E5FF"), ("Clover", "#3BB273")]),
    "The Remainder Wards": (G.OMENS["remainder"][1], ["f_remainder", "ama"], [("Ash", "#8A7F72"), ("Old brass", "#C8963E"), ("Moss", "#5E7D4A"), ("Leather", "#6B4226")]),
    "The Yokai Courts": (G.EMBLEMS["yokai"][1], ["tamamo", "ao"], [("Violet", "#8E44AD"), ("Vermilion", "#E34234"), ("Foxfire", "#7FDBFF"), ("Gold", "#F4C430")]),
    "The Luck Exchange": (G.EMBLEMS["exchange"][1], ["f_broker", "jin_chan"], [("Jade", "#00A86B"), ("Gold", "#D4AF37"), ("Lacquer", "#B22222"), ("Paper", "#E9E2D0")]),
    "The Ten Courts": (G.EMBLEMS["ten_courts"][1], ["judge_cui", "oxhead_horseface"], [("Ink", "#1B1B1B"), ("Rice paper", "#E9E2D0"), ("Seal red", "#B22222"), ("Bronze", "#8C6A3F")]),
    "The Observatory": (G.EMBLEMS["observatory"][1], ["vidya_rao", "shunya"], [("Indigo", "#3F3D99"), ("Saffron", "#F4A300"), ("Brass", "#B5893B"), ("Sandstone", "#D8A86B")]),
    "The Pythagorean Synod": (G.EMBLEMS["synod"][1], ["f_synod", "archon"], [("Bronze", "#8C6A3F"), ("Chalk", "#F4F1EA"), ("Aegean", "#1F6FB2"), ("Olive", "#7A8B4A")]),
    "The House": (G.EMBLEMS["house"][1], ["f_dealer", "house"], [("Casino red", "#C0392B"), ("Ivory", "#F4F1EA"), ("Gold", "#D4AF37"), ("Midnight", "#1D1A3A")]),
    "The Open Hand": (None, ["f_pilgrim", "brother_nought"], [("Road dust", "#B9A58A"), ("Open Hand gold", "#D4AF37"), ("Homespun", "#8C6A3F"), ("Ink", "#141018")]),
}
OPEN_HAND_SVG = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120"><g stroke="#141018" stroke-width="3" stroke-linejoin="round">'
                 '<path d="M30 70 V40 q0 -6 6 -6 q6 0 6 6 V60 V28 q0 -6 6 -6 q6 0 6 6 V58 V24 q0 -6 6 -6 q6 0 6 6 V58 V30 q0 -6 6 -6 q6 0 6 6 V78 '
                 'q0 26 -26 26 h-6 q-18 0 -26 -16 L14 66 q-3 -6 3 -9 q6 -3 10 3z" fill="#D4AF37"/>'
                 '<rect x="46" y="62" width="22" height="22" rx="4" fill="#F4F1EA" transform="rotate(-12 57 73)"/>'
                 '<circle cx="51" cy="68" r="2.5" fill="#141018"/><circle cx="57" cy="73" r="2.5" fill="#141018"/><circle cx="63" cy="78" r="2.5" fill="#141018"/></g></svg>')


def world_pages(H, start):
    P = []
    n = start
    P.append(part_opener(H, "II", "THE WORLD", "How the Tally works: the god of luck, the logic of luck, the schools of power, the people, the money, the politics and the past (docs/WORLD_ENCYCLOPEDIA.md).",
                         ["Hap, the god of luck", "The logic of luck", "The six schools of power", "How people use power", "History and timeline", "Politics and power",
                          "How things operate", "Jobs", "Stores", "Factions and their styles"]))
    n += 1
    cells, k, th = views_row(H, "hap", 160, 120)
    hap_text = ("Hap is the Tally's one god of luck: the will inside chance. Hap never commands; it deals. Every land built its own way of talking to Hap, "
                "and those ways became the many ledgers. In TR 702 the Basilica's Even Hand engine closed around the god itself: the amber eye over Meridian is Hap's eye, caged. "
                "The Rounding shaves the god every dawn, and the shavings became NIL: the part of luck that refused to be counted.")
    P.append(H.page(f"""{H.tab("THE GOD OF LUCK · HAP")}<div class="hap-grid"><div class="views">{cells}</div>
<div><p class="lede">"Hap deals. People choose."</p><p>{E(hap_text)}</p>
<ul class="callouts"><li>Never the same face twice (each land's face, in its art style)</li><li>Dice eyes and orbiting digits 0–9 never change</li><li>Never a monster, a boss, or a stand-in for a real deity</li><li>Speaks only in dreams, coincidences and the finale</li></ul>
<div class="em-inline">{OPEN_HAND_SVG}<span>The Open Hand: Hap's symbol</span></div></div></div>{H.folio(n + 1, "The world")}""", "padded"))
    n += 1
    rules = C.md_table(ENC, "## 1.")
    P.append(H.page(f"""{H.tab("THE LOGIC OF LUCK")}{table(["Rule", "What it means", "Consequence"], rules, "t small")}
{luck_flow_svg()}{H.folio(n + 1, "The world")}""", "padded"))
    n += 1
    steps = C.numbered_list(ENC, "### How a Fate Wheel works")
    cards = "".join(f'<div class="step"><b>{i + 1}</b><p>{md(s)}</p></div>' for i, s in enumerate(steps))
    P.append(H.page(f"""{H.tab("HOW A FATE WHEEL WORKS")}<p class="lead-p">The in-world physics behind the one verb: stop the number.</p><div class="steps">{cards}</div>
<div class="reel-row">{''.join(f'<div>{s}<span>{E(nm)}</span></div>' for nm, s in list(G.REELS.values())[:4])}</div>{H.folio(n + 1, "The world")}""", "padded"))
    n += 1
    schools = C.md_table(ENC, "## 2.")
    P.append(H.page(f"""{H.tab("THE SIX SCHOOLS OF POWER")}{table(["School", "Land", "Source of power", "How it looks", "Signature techniques", "Practitioners"], schools, "t small")}
<p class="cmp-note">Licensing: since TR 760 only Ledger Auditing is licensed. Every other school is folk practice: tolerated at home, illegal in Meridian unless registered.</p>{H.folio(n + 1, "The world")}""", "padded"))
    n += 1
    uses = C.md_table(ENC, "## 3.")
    P.append(H.page(f"""{H.tab("HOW PEOPLE USE POWER")}{table(["Use", "Who", "How"], uses)}{H.folio(n + 1, "The world")}""", "padded"))
    n += 1
    tl = C.md_table(ENC, "## 9.")
    half = (len(tl) + 1) // 2
    P.append(H.page(f"""{H.tab("HISTORY AND TIMELINE")}{timeline_svg(tl)}<div class="two-col">{table(["When", "Era", "Event"], tl[:half], "t small")}{table(["When", "Era", "Event"], tl[half:], "t small")}</div>{H.folio(n + 1, "The world")}""", "padded"))
    n += 1
    pacts = C.md_table(ENC, "## 8.")
    P.append(H.page(f"""{H.tab("POLITICS AND POWER")}{politics_svg()}{table(["Land", "Who rules", "The Basilica's grip", "What the pact promised"], pacts, "t small")}
<p class="cmp-note">Luck is wealth, health and safety at once, so whoever controls the count controls everything. The game's politics is unmasking that.</p>{H.folio(n + 1, "The world")}""", "padded"))
    n += 1
    ops = "".join(f'<div class="op"><b>{E(t)}</b><p>{md(d)}</p></div>' for t, d in operations())
    P.append(H.page(f"""{H.tab("HOW THINGS OPERATE")}<div class="ops">{ops}</div>{H.folio(n + 1, "The world")}""", "padded"))
    n += 1
    jobs = C.md_table(ENC, "## 5.")
    for i, chunk in enumerate((jobs[:11], jobs[11:])):
        P.append(H.page(f"""{H.tab("JOBS IN THE TALLY" + (" (CONT.)" if i else ""))}{table(["Job", "Where", "What they do", "Typical Omen", "Tools / look"], chunk)}{H.folio(n + 1, "The world")}""", "padded"))
        n += 1
    stores = C.md_table(ENC, "## 7.")
    P.append(H.page(f"""{H.tab("STORES AND SERVICES")}{table(["Store", "Land", "What it sells", "Sign", "In play"], stores, "t small")}{H.folio(n + 1, "The world")}""", "padded"))
    n += 1
    facs = C.md_table(ENC, "## 4.")
    for row in facs:
        name = row[0]
        vis = next((v for k, v in FACTION_VIS.items() if name.startswith(k)), None)
        if not vis:
            continue
        emb, arche, pal = vis
        emb = emb or OPEN_HAND_SVG
        fields = list(zip(["Seat", "Wants", "Power", "Style", "Uniform / look", "Ranks", "Tools and weapons"], row[1:]))
        dl = "".join(f'<div class="dl"><span>{E(k)}</span><p>{md(v)}</p></div>' for k, v in fields)
        figs = ""
        kk = min(fit_k(key, 78, 118, ["front", "back"], 2) for key in arche)
        for key in arche:
            c = next((c for c in CAST if c["key"] == key), None)
            if c:
                cells, _, _ = views_row(H, key, 78, 118, views=["front", "back"], labels=False, gap=2, k_cap=kk)
                figs += f'<div class="fac-fig"><div class="views">{cells}</div><i>{E(c["name"])}</i></div>'
        P.append(H.page(f"""<div class="fac-left">{H.tab("FACTION")}<div class="fac-head"><div class="fac-em">{emb}</div><div class="fac-name">{E(name)}</div></div>
{H.chips(pal)}{dl}</div><div class="fac-right">{figs}</div>{H.folio(n + 1, "Factions")}""", "padded faction-page"))
        n += 1
    return P


# ---------------------------------------------------------------- Part III: environment spreads
def env_spread(H, key, num):
    land = next(l for l in LANDS if l[0] == key)
    light = {r[0].split(" (")[0]: r for r in C.md_table(SPEC, "### 3.4")}
    lrow = next((v for k, v in light.items() if k.startswith(land[1].replace("The ", "").split(" ")[0]) or land[1].startswith(k)), None)
    notes = ""
    if lrow:
        notes = "".join(f'<div class="dl"><span>{E(h)}</span><p>{E(v)}</p></div>' for h, v in zip(["Time", "Key light", "Fill", "Atmosphere"], lrow[1:]))
    return H.page(f"""<div class="env-left">{H.tab(land[1].upper() + " · 3D BLOCKOUT")}
<figure class="env-iso"><img src="{H.img(f'art/envs/{key}_iso.png', 1600)}"><figcaption>2.5D · orthographic, pitch 57°, yaw −38°</figcaption></figure>
<figure class="env-top"><img src="{H.img(f'art/envs/{key}_top.png', 1600)}"><figcaption>TOP-DOWN · plan</figcaption></figure></div>
<div class="env-right"><figure><img src="{H.img(f'art/envs/{key}_front.png', 1400)}"><figcaption>FRONT · battle camera (perspective)</figcaption></figure>
<div class="sub">{E(land[2])} · light and atmosphere (Art Spec §3.4)</div>{notes}
<p class="small">First-draft 3D blockout at true scale (1 unit = 1 m), flat colour key from the land's palette. Built by <code>tools/build_envs.py</code>; the painted register-A version paints over these exact cameras.</p>
{H.stamp("STAGE 1 · 3D BLOCKOUT", "ph")}</div>{H.folio(num, land[1])}""", "env-spread")


# ---------------------------------------------------------------- Part IV: the cast
def group_divider(H, group, num):
    members = [c for c in CAST if c["group"] == group]
    sizes = [view_size(c["key"], "front") for c in members]
    k = min(240 / (sum(w for w, _ in sizes) + 40 * len(sizes)), 112 / max(h for _, h in sizes), 0.22)
    cells = ""
    for c in members:
        w, h = view_size(c["key"], "front")
        nm = c["name"] if group != "Main character" else c.get("outfit", "").split(" (")[0]
        cells += f'<div class="lu-cell"><img src="{H.img(view_path(c["key"], "front"), 800)}" style="width:{w * k:.1f}mm;height:{h * k:.1f}mm"><b>{E(nm)}</b></div>'
    return H.page(f"""<div class="opener">{H.tab("THE CAST")}<div class="opener-title small">{E(group.upper())}</div>
<p class="opener-sub">{len(members)} model{"s" if len(members) != 1 else ""} · front views at one shared scale.</p><div class="lineup-scale dark">{cells}</div></div>{H.folio(num, "Cast")}""", "dark")


def cast_page(H, c, num):
    key = c["key"]
    cells, k, th = views_row(H, key, 186, 128, k_cap=0.2)  # one scale for every cast page unless a model is too wide
    bar_h = c["h"] * PPM * k
    bar = f'<div class="hbar" style="height:{bar_h:.1f}mm"><span>{c["h"]:.2f} m</span></div>'
    rows = C.character_rows(HERO_SECTION[key]) if key in HERO_SECTION else {}
    spec = c.get("spec") or rows.get("Wardrobe", "")
    props = rows.get("Props", "")
    locks = c.get("locks") or (rows.get("Canon locks", "").split(" · ") if rows.get("Canon locks") else [])
    facts = [("Group", c["group"]), ("Role", c["role"]), ("Land", c["land"]), ("Lucky digit", c["digit"]), ("Omen", c["omen"]), ("Height", f'{c["h"]:.2f} m')]
    if c.get("outfit"):
        facts.insert(1, ("Outfit", c["outfit"]))
    dl = "".join(f'<div class="dl"><span>{E(a)}</span><p>{E(b)}</p></div>' for a, b in facts)
    extra = ""
    if spec:
        extra += f'<div class="sub">Design</div><p class="spec">{E(spec)}</p>'
    if props and key in HERO_SECTION:
        extra += f'<div class="sub">Props</div><p class="spec">{E(props)}</p>'
    if locks:
        extra += '<div class="sub">Canon locks</div><ul class="callouts">' + "".join(f"<li>{E(l)}</li>" for l in locks) + "</ul>"
    review = H.stamp("CULTURAL REVIEW REQUIRED", "ph") if c["group"] == "Keepers" or key == "rahu_ketu" else H.stamp("3D BLOCKOUT · FIRST DRAFT", "ph")
    return H.page(f"""<div class="cast-left"><div class="cast-head">{H.tab(c["group"].upper())}<div class="cast-name">{E(c["name"])}</div></div>
<div class="turn">{bar}<div class="views">{cells}</div></div></div>
<div class="cast-right">{H.chips(c["palette"])}{dl}{extra}</div>{review}{H.folio(num, "Cast")}""", "padded cast-page")


def nil_outfits(H, num):
    outs = [c for c in CAST if c["group"] == "Main character"]
    k = 0.2
    cells = ""
    for c in outs:
        w, h = view_size(c["key"], "front")
        bw, bh = view_size(c["key"], "back")
        cells += (f'<div class="outfit"><div class="pair"><img src="{H.img(view_path(c["key"], "front"), 900)}" style="width:{w * k:.1f}mm;height:{h * k:.1f}mm">'
                  f'<img src="{H.img(view_path(c["key"], "back"), 900)}" style="width:{bw * k:.1f}mm;height:{bh * k:.1f}mm"></div>'
                  f'<b>{E(c["outfit"])}</b><p>{E(c.get("spec", ""))}</p></div>')
    return H.page(f"""{H.tab("NIL · OUTFITS")}<p class="lead-p">The main character's four story outfits, front and back at one scale. Each gets a full turnaround on its own page.</p>
<div class="outfits">{cells}</div>{H.folio(num, "Cast")}""", "padded")
