"""ZERO-SUM: OMEN figure kit: flat-colour model-sheet figures for every hero and boss, plus Meridian era outfits.

Each figure is built from simple parts (limbs as round-capped strokes, torsos and garments as polygons) so it reads
as a clean silhouette. Heights follow the Character Bible (1 m = 112 px; ground at y = 244 in a 160 x 250 box).

figure(key, mode) -> SVG string
  mode "colour": signature colours with an ink outline (the "inked people" rule)
  mode "ink":    solid ink silhouette (the 64 px readability test in Character Bible §0)
  mirror=True    flips horizontally (a back view reads as the mirrored front silhouette)
Run directly to write every figure to art/graphics/figures/.
"""
import math
import os

INK = "#141018"
G = 244          # ground line
CX = 80          # centre x
M = 112          # px per metre


# ---------------------------------------------------------------- primitives: (role, kind, data)
def poly(role, pts):
    return (role, "poly", pts)


def line(role, x1, y1, x2, y2, w):
    return (role, "line", (x1, y1, x2, y2, w))


def circ(role, cx, cy, r):
    return (role, "circ", (cx, cy, r))


def ell(role, cx, cy, rx, ry):
    return (role, "ell", (cx, cy, rx, ry))


def path(role, d):
    return (role, "path", d)


def ring(role, cx, cy, r, w):
    return (role, "ring", (cx, cy, r, w))


def arc(role, cx, cy, r, a0, a1, w):
    return (role, "arc", (cx, cy, r, a0, a1, w))


def text(role, x, y, s, size):
    return (role, "text", (x, y, s, size))


def cap(role, hy, r, depth=0.1, fringe=0.35):
    """Hair as a cap over the top of the head, leaving the face visible."""
    return path(role, f"M{CX - r * 1.08:.1f} {hy + r * depth:.1f} A{r * 1.08:.1f} {r * 1.08:.1f} 0 0 1 {CX + r * 1.08:.1f} {hy + r * depth:.1f} "
                      f"Q{CX + r * 0.5:.1f} {hy - r * fringe:.1f} {CX:.1f} {hy - r * (fringe - 0.1):.1f} Q{CX - r * 0.5:.1f} {hy - r * fringe:.1f} {CX - r * 1.08:.1f} {hy + r * depth:.1f} Z")


def _el(kind, data, fill, extra=0, outline=False):
    sw = 3 if outline else 0
    if kind == "poly":
        pts = " ".join(f"{x:.1f},{y:.1f}" for x, y in data)
        st = f' stroke="{fill}" stroke-width="{sw}" stroke-linejoin="round"' if outline else ""
        return f'<polygon points="{pts}" fill="{fill}"{st}/>'
    if kind == "path":
        st = f' stroke="{fill}" stroke-width="{sw}" stroke-linejoin="round"' if outline else ""
        return f'<path d="{data}" fill="{fill}"{st}/>'
    if kind == "line":
        x1, y1, x2, y2, w = data
        return f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{fill}" stroke-width="{w + extra:.1f}" stroke-linecap="round"/>'
    if kind == "circ":
        cx, cy, r = data
        return f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r + extra / 2:.1f}" fill="{fill}"/>'
    if kind == "ell":
        cx, cy, rx, ry = data
        return f'<ellipse cx="{cx:.1f}" cy="{cy:.1f}" rx="{rx + extra / 2:.1f}" ry="{ry + extra / 2:.1f}" fill="{fill}"/>'
    if kind == "ring":
        cx, cy, r, w = data
        return f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r:.1f}" fill="none" stroke="{fill}" stroke-width="{w + extra:.1f}"/>'
    if kind == "arc":
        cx, cy, r, a0, a1, w = data
        x0, y0 = cx + r * math.cos(math.radians(a0)), cy + r * math.sin(math.radians(a0))
        x1, y1 = cx + r * math.cos(math.radians(a1)), cy + r * math.sin(math.radians(a1))
        large = 1 if (a1 - a0) % 360 > 180 else 0
        return (f'<path d="M{x0:.1f} {y0:.1f} A{r} {r} 0 {large} 1 {x1:.1f} {y1:.1f}" fill="none" stroke="{fill}" '
                f'stroke-width="{w + extra:.1f}" stroke-linecap="round"/>')
    if kind == "text":
        x, y, s, size = data
        return (f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="middle" font-family="Big Shoulders Display,Impact,sans-serif" '
                f'font-weight="900" font-size="{size}" fill="{fill}">{s}</text>')
    raise ValueError(kind)


def render(parts, colours, mode="colour", mirror=False, vb="-24 -28 208 278", cls="fig", par="xMidYMax meet"):
    body = []
    if mode == "colour":  # ink outline layer first, then colour on top
        for role, kind, data in parts:
            if role == "fx" or kind == "text":
                continue
            body.append(_el(kind, data, INK, extra=4, outline=True))
        for role, kind, data in parts:
            body.append(_el(kind, data, colours.get(role, INK)))
    else:
        for role, kind, data in parts:
            if role == "fx":
                continue
            body.append(_el(kind, data, INK, extra=0 if kind != "text" else 0))
    g = "".join(body)
    if mirror:
        g = f'<g transform="translate(160 0) scale(-1 1)">{g}</g>'
    return f'<svg class="{cls}" xmlns="http://www.w3.org/2000/svg" viewBox="{vb}" preserveAspectRatio="{par}">{g}</svg>'


# ---------------------------------------------------------------- a generic body
def body(h_m, sw, *, legs=True, arms=("down", "down"), torso_role="top", leg_role="legs", arm_role=None, skin="skin",
         shoes="shoes", head=True, hunch=0):
    """Return (parts, anchors). arms: per side ('down' | 'out' | 'up' | 'bent' | None), side 0 = viewer's left."""
    H = h_m * M
    t = G - H
    r = H * 0.064
    hy = t + r + hunch
    sh = t + H * 0.185
    waist = t + H * 0.40
    hip = t + H * 0.52
    hand_y = t + H * 0.53
    a = dict(t=t, H=H, r=r, hy=hy, sh=sh, waist=waist, hip=hip, sw=sw, hand=[None, None])
    p = []
    lw = max(6, sw * 0.24)
    if legs:
        for s in (-1, 1):
            p.append(line(leg_role, CX + s * sw * 0.2, hip, CX + s * sw * 0.16, G - 6, lw))
            p.append(ell(shoes, CX + s * (sw * 0.16 + 2), G - 3, lw * 0.75, 3.5))
    arm_role = arm_role or torso_role
    aw = max(5, sw * 0.17)
    for i, (s, kind) in enumerate(zip((-1, 1), arms)):
        if kind is None:
            continue
        x0, y0 = CX + s * (sw / 2 - aw / 2), sh + aw / 2
        if kind == "down":
            x1, y1 = CX + s * (sw / 2 + 2), hand_y
        elif kind == "out":
            x1, y1 = CX + s * (sw / 2 + H * 0.30), sh + 6
        elif kind == "up":
            x1, y1 = CX + s * (sw / 2 + 6), sh - H * 0.20
        else:  # bent: hand in front of the hip
            x1, y1 = CX + s * (sw * 0.15), waist + 8
        p.append(line(arm_role, x0, y0, x1, y1, aw))
        p.append(circ(skin, x1, y1, aw * 0.55))
        a["hand"][i] = (x1, y1)
    p.append(poly(torso_role, [(CX - sw / 2, sh), (CX + sw / 2, sh), (CX + sw * 0.34, waist), (CX + sw * 0.38, hip),
                               (CX - sw * 0.38, hip), (CX - sw * 0.34, waist)]))
    if head:
        p.append(line(skin, CX, hy + r * 0.6, CX, sh + 2, r * 0.8))
        p.append(circ(skin, CX, hy, r))
    return p, a


# ---------------------------------------------------------------- heroes
def nil():
    p, a = body(1.74, 40, arms=("down", "down"), torso_role="coat", leg_role="legs")
    t, H, r, hy, sh, hip = a["t"], a["H"], a["r"], a["hy"], a["sh"], a["hip"]
    coat = [(CX - 20, sh), (CX + 20, sh), (CX + 18, hip), (CX + 27, G - 34), (CX + 6, hip + 18),
            (CX - 6, hip + 18), (CX - 22, G - 62), (CX - 18, hip)]  # NIL's left tail (viewer's right) is longer
    p.insert(4, poly("coat", coat))
    p.append(poly("coat", [(CX - 11, sh + 3), (CX - 9, hy + r * 1.05), (CX + 9, hy + r * 1.05), (CX + 11, sh + 3)]))
    for i in range(3):
        p.append(circ("acc", CX - 9, sh + 14 + i * 11, 2.2))
    hair = [(CX - r - 2, hy + 2), (CX - r - 5, hy - r * 0.6), (CX - r * 0.5, hy - r - 5), (CX - 2, hy - r - 1),
            (CX + r * 0.4, hy - r - 7), (CX + r + 4, hy - r * 0.5), (CX + r + 2, hy + 3), (CX + r * 0.6, hy - r * 0.3),
            (CX - r * 0.6, hy - r * 0.2)]
    p.append(poly("hair", hair))
    p.append(line("acc", CX + r * 0.2, hy - r - 3, CX + r * 0.7, hy - r * 0.2, 2.5))  # the orange streak
    hx, hyy = a["hand"][0]  # NIL's right wrist is on the viewer's left
    p.append(ring("fx", hx, hyy - 6, 7, 2))
    p.append(circ("acc", hx, hyy - 6, 4))
    p.append(arc("acc", CX, t - 10, 13, 200, 520, 3))  # broken halo
    p.append(text("acc", CX, t - 6, "NaN", 9))
    return p, {"coat": INK, "legs": "#2A2530", "shoes": "#3A2E28", "skin": "#E9D6C4", "hair": "#EDE6DA", "acc": "#FF7A2C", "fx": "#FFB27A"}


def vesper():
    p, a = body(1.82, 44, arms=("out", "down"), torso_role="coat", leg_role="legs")
    t, H, r, hy, sh, hip = a["t"], a["H"], a["r"], a["hy"], a["sh"], a["hip"]
    p.insert(4, poly("coat", [(CX - 22, sh), (CX + 22, sh), (CX + 24, hip), (CX + 40, G - 22), (CX + 8, hip + 30),
                              (CX - 8, hip + 30), (CX - 40, G - 22), (CX - 24, hip)]))
    p.append(poly("vest", [(CX - 9, sh + 4), (CX + 9, sh + 4), (CX + 8, hip - 4), (CX, hip + 4), (CX - 8, hip - 4)]))
    p.append(line("hair", CX + r * 0.7, hy + 2, CX + 13, hip - 10, 5))  # braid over HER left shoulder
    p.append(cap("hair", hy, r, 0.5))
    p.append(ell("hat", CX, hy - r * 0.55, r * 2.7, 4.5))
    p.append(poly("hat", [(CX - r * 1.05, hy - r * 0.6), (CX - r * 0.7, hy - r * 1.9), (CX + r * 0.7, hy - r * 1.9),
                          (CX + r * 1.05, hy - r * 0.6)]))
    p.append(poly("card", [(CX + r * 0.35, hy - r * 0.8), (CX + r * 0.65, hy - r * 1.75), (CX + r * 0.95, hy - r * 1.65), (CX + r * 0.75, hy - r * 0.7)]))
    gx, gy = a["hand"][0]
    p.append(poly("gun", [(gx + 2, gy - 4), (gx - 26, gy - 5), (gx - 26, gy + 1), (gx - 6, gy + 2), (gx - 2, gy + 12), (gx + 4, gy + 11)]))
    p.append(circ("brass", gx - 7, gy - 1, 3.5))
    return p, {"coat": "#E5243B", "vest": INK, "legs": INK, "shoes": INK, "skin": "#E6C3A5", "hair": INK, "hat": INK,
               "card": "#F4F1EA", "gun": "#4A4E54", "brass": "#B5A642"}


def maeve():
    p, a = body(1.65, 46, arms=("down", "up"), torso_role="shirt", leg_role="legs")
    t, H, r, hy, sh, hip, waist = a["t"], a["H"], a["r"], a["hy"], a["sh"], a["hip"], a["waist"]
    p.append(poly("apron", [(CX - 15, sh + 10), (CX + 15, sh + 10), (CX + 20, hip + 30), (CX - 20, hip + 30)]))
    p.append(circ("clover", CX - 12, sh + 6, 3))
    for s in (-1, 1):
        p.append(line("hair", CX + s * r * 0.95, hy, CX + s * (r + 6), sh + 22, 5))
        p.append(circ("hair", CX + s * (r + 6), sh + 24, 3.5))
    p.append(line("hair", CX, hy - r, CX + 3, hy - r - 12, 5))  # third braid, tied up
    p.append(cap("hair", hy, r, 0.3))
    for i, hd in enumerate(a["hand"]):
        p.append(arc("copper", hd[0], hd[1], 6, 200 if i == 0 else 20, 340 if i == 0 else 160, 4))
    hx, hyy = a["hand"][1]
    p.append(line("handle", hx, hyy + 6, hx - 6, hyy + 58, 4))
    p.append(poly("copper", [(hx - 14, hyy - 4), (hx + 12, hyy - 10), (hx + 15, hyy + 2), (hx - 11, hyy + 8)]))
    return p, {"shirt": "#3BB273", "apron": "#6B4226", "legs": "#4A3A2C", "shoes": "#2A1E16", "skin": "#F1D2B8",
               "hair": "#C0392B", "clover": "#3BB273", "copper": "#D9822B", "handle": "#6B4226"}


def hina():
    p, a = body(1.35, 32, arms=("down", "up"), torso_role="kimono", leg_role="legs", shoes="geta")
    t, H, r, hy, sh, hip = a["t"], a["H"], a["r"], a["hy"], a["sh"], a["hip"]
    p.insert(4, poly("kimono", [(CX - 16, sh), (CX + 16, sh), (CX + 19, G - 8), (CX - 19, G - 8)]))
    p.append(poly("kimono", [(CX - 16, sh + 2), (CX - 30, sh + 30), (CX - 26, hip + 10), (CX - 14, hip - 4)]))  # long sleeve
    p.append(poly("obi", [(CX - 17, a["waist"] - 2), (CX + 17, a["waist"] - 2), (CX + 17, a["waist"] + 10), (CX - 17, a["waist"] + 10)]))
    p.append(path("hair", f"M{CX - r - 2} {hy + r * 0.5} Q{CX - r - 2} {hy - r - 3} {CX} {hy - r - 3} Q{CX + r + 2} {hy - r - 3} {CX + r + 2} {hy + r * 0.5} Z"))
    hx, hyy = a["hand"][1]
    top = t - 18
    p.append(line("handle", hx, hyy + 4, hx - 4, top + 2, 3))
    p.append(path("umbrella", f"M{hx - 4 - 50} {top + 8} Q{hx - 4} {top - 64} {hx - 4 + 50} {top + 8} Z"))
    for k in (-30, -12, 6, 24):
        p.append(line("rib", hx - 4, top - 26, hx - 4 + k * 1.5, top + 8, 1.6))
    p.append(circ("paper", hx - 4 - 8, top - 10, 7))
    p.append(circ("pupil", hx - 4 - 8, top - 10, 3))
    p.append(poly("tongue", [(hx - 4 + 4, top + 7), (hx - 4 + 12, top + 7), (hx - 4 + 9, top + 22)]))
    return p, {"kimono": "#E34234", "obi": "#26428B", "legs": "#F2E6C9", "geta": "#6B4226", "skin": "#F3DCC8", "hair": INK,
               "handle": "#6B4226", "umbrella": "#E34234", "rib": "#F2E6C9", "paper": "#F2E6C9", "pupil": INK, "tongue": "#FF6F91"}


def ba():
    p, a = body(1.70, 38, arms=("out", "bent"), torso_role="qipao", leg_role="legs")
    t, H, r, hy, sh, hip = a["t"], a["H"], a["r"], a["hy"], a["sh"], a["hip"]
    p.insert(4, poly("qipao", [(CX - 19, sh), (CX + 19, sh), (CX + 14, a["waist"]), (CX + 16, hip), (CX + 12, G - 14),
                               (CX + 2, G - 14), (CX, hip + 30), (CX - 6, G - 14), (CX - 12, G - 14), (CX - 16, hip), (CX - 14, a["waist"])]))
    p.append(poly("gold", [(CX - 21, sh - 2), (CX - 12, sh - 2), (CX - 14, sh + 6), (CX - 23, sh + 6)]))
    p.append(poly("gold", [(CX + 12, sh - 2), (CX + 21, sh - 2), (CX + 23, sh + 6), (CX + 14, sh + 6)]))
    p.append(cap("hair", hy, r, 0.3))
    p.append(circ("hair", CX + 2, hy - r - 5, r * 0.6))
    for i in range(8):
        ang = math.radians(200 + i * 20)
        p.append(circ("gold", CX + 2 + (r * 0.8) * math.cos(ang), hy - r - 5 + (r * 0.8) * math.sin(ang), 1.6))
    fx, fy = a["hand"][0]
    p.append(path("fan", f"M{fx} {fy} L{fx - 30} {fy - 26} A40 40 0 0 1 {fx + 8} {fy - 40} Z"))
    for k in range(5):
        ang = math.radians(-138 + k * 13)
        p.append(line("rib", fx, fy, fx + 38 * math.cos(ang), fy + 38 * math.sin(ang), 1.2))
    return p, {"qipao": "#00A86B", "gold": "#F4C430", "legs": "#E2C3A6", "shoes": "#B22222", "skin": "#EBCDB0", "hair": INK,
               "fan": "#F4C430", "rib": "#B22222"}


def bai_si():
    p, a = body(1.95, 52, arms=("down", "down"), torso_role="robe", legs=False)
    t, H, r, hy, sh, hip = a["t"], a["H"], a["r"], a["hy"], a["sh"], a["hip"]
    p.insert(0, poly("hairb", [(CX - r, hy), (CX + r, hy), (CX + 12, hip - 6), (CX - 12, hip - 6)]))
    p.insert(1, poly("robe", [(CX - 26, sh), (CX + 26, sh), (CX + 24, G - 2), (CX - 24, G - 2)]))
    p.append(poly("robe", [(CX - 26, sh), (CX + 26, sh), (CX + 26, sh + 8), (CX - 26, sh + 8)]))
    p.append(text("ink", CX, hip + 18, "四", 18))
    p.append(cap("hair", hy, r, 0.4))
    p.append(line("ribbon", CX - r - 1, hy - 1, CX - r - 7, hy + 9, 3))
    px = CX + 40
    p.append(line("pole", px, G - 2, px, t - 26, 4))
    p.append(path("blade", f"M{px} {t - 26} Q{px + 22} {t - 8} {px + 4} {t + 22} Q{px + 10} {t} {px} {t - 26} Z"))
    for i in range(4):
        p.append(poly("talisman", [(px - 3, t + 30 + i * 13), (px - 9, t + 30 + i * 13), (px - 9, t + 41 + i * 13), (px - 3, t + 41 + i * 13)]))
    return p, {"robe": "#F4F1EA", "hairb": "#E8E4DC", "hair": "#E8E4DC", "skin": "#EDE4DA", "ink": INK, "ribbon": INK,
               "pole": "#3A2E28", "blade": "#C9CED6", "talisman": "#E8C547"}


def shunya():
    p, a = body(1.62, 36, arms=("out", "down"), torso_role="top", leg_role="legs")
    t, H, r, hy, sh, hip = a["t"], a["H"], a["r"], a["hy"], a["sh"], a["hip"]
    p.insert(4, poly("skirt", [(CX - 16, a["waist"]), (CX + 16, a["waist"]), (CX + 30, G - 6), (CX - 30, G - 6)]))
    p.append(poly("sash", [(CX - 18, sh), (CX - 8, sh), (CX + 16, a["waist"]), (CX + 6, a["waist"])]))
    for i in range(6):
        p.append(circ("mirror", CX - 22 + i * 9, G - 18 - (i % 2) * 8, 2))
    p.append(line("hair", CX + r * 0.6, hy + 2, CX + 16, hip + 6, 5))  # long braid
    p.append(cap("hair", hy, r, 0.3))
    p.append(circ("brass", CX - r * 0.6, hy - r * 0.8, 2.2))
    ax, ay = a["hand"][0]
    p.append(ring("brass", ax - 8, ay - 4, 17, 4))
    p.append(ring("brass", ax - 8, ay - 4, 8, 2))
    p.append(line("brass", ax - 25, ay - 4, ax + 9, ay - 4, 2))
    p.append(poly("leaf", [(CX + 16, hip - 4), (CX + 24, hip - 2), (CX + 22, hip + 14), (CX + 14, hip + 12)]))
    return p, {"top": "#3F3D99", "skirt": "#F4A300", "sash": "#3F3D99", "legs": "#B97A56", "shoes": "#6B4226", "skin": "#B97A56",
               "hair": INK, "mirror": "#C9CED6", "brass": "#B5893B", "leaf": "#D8C08A"}


def prima():
    p, a = body(1.68, 48, arms=("bent", "down"), torso_role="armour", leg_role="legs")
    t, H, r, hy, sh, hip = a["t"], a["H"], a["r"], a["hy"], a["sh"], a["hip"]
    for k in range(5):
        x = CX - 18 + k * 9
        p.append(poly("armour", [(x, hip - 2), (x + 7, hip - 2), (x + 7, hip + 22), (x, hip + 22)]))
    for s in (-1, 1):
        p.append(path("gold", f"M{CX + s * 14} {sh + 2} A13 13 0 0 {1 if s > 0 else 0} {CX + s * 34} {sh + 6} L{CX + s * 24} {sh + 4} Z"))
    p.append(poly("gold", [(CX - 20, a["waist"]), (CX + 20, a["waist"]), (CX + 20, a["waist"] + 4), (CX - 20, a["waist"] + 4)]))
    p.append(path("hair", f"M{CX - r - 2} {hy + 3} Q{CX - r} {hy - r - 4} {CX + 2} {hy - r - 3} Q{CX + r + 3} {hy - r} {CX + r + 2} {hy + 3} Z"))
    sx, sy = CX - 30, hip - 14
    p.append(circ("shield", sx, sy, 27))
    p.append(ring("glass", sx, sy, 24, 3))
    for i, (dx, dy) in enumerate([(-10, -10), (0, -12), (10, -10), (-12, 0), (0, 0), (12, 0), (-10, 10), (0, 12), (10, 10)]):
        p.append(circ("chalk", sx + dx, sy + dy, 2.4))
    for i, d in enumerate("2357"):
        p.append(text("halo", CX - 18 + i * 12, t - 6 + (4 if i in (0, 3) else 0), d, 10))
    return p, {"armour": "#1F6FB2", "gold": "#E9DDB3", "legs": "#F4F1EA", "shoes": "#8C6A3F", "skin": "#F2D7C0",
               "hair": "#E9C46A", "halo": "#B8860B", "shield": "#1F6FB2", "glass": "#6FB7E9", "chalk": "#F4F1EA"}


def fibi():
    p, a = body(1.60, 34, arms=("bent", "out"), torso_role="coat", leg_role="legs")
    t, H, r, hy, sh, hip = a["t"], a["H"], a["r"], a["hy"], a["sh"], a["hip"]
    p.insert(4, poly("coat", [(CX - 17, sh), (CX + 17, sh), (CX + 15, hip), (CX + 14, hip + 34), (CX + 4, hip + 4),
                              (CX - 4, hip + 4), (CX - 14, hip + 34), (CX - 15, hip)]))
    p.append(poly("shirt", [(CX - 5, sh + 2), (CX + 5, sh + 2), (CX, a["waist"])]))
    p.append(cap("hair", hy, r, 0.3))
    for k in range(7):
        ang = math.radians(150 + k * 40)
        p.append(circ("hair", CX + (r + 2) * math.cos(ang), hy - 2 + (r + 2) * math.sin(ang) * 0.9, 4))
    p.append(arc("headset", CX, hy, r + 3, 200, 340, 1.6))
    cx0, cy0 = a["hand"][1]
    fib = [1, 1, 2, 3, 5, 8]
    for i, f in enumerate(fib):
        ang = math.radians(-100 + i * 42)
        rr = 8 + f * 3.2
        x, y = cx0 + rr * math.cos(ang), cy0 - 8 + rr * math.sin(ang)
        p.append(poly("card" if i % 2 else "gold", [(x - 3.5, y - 5), (x + 3.5, y - 5), (x + 3.5, y + 5), (x - 3.5, y + 5)]))
    return p, {"coat": "#1D1A3A", "shirt": "#F4F1EA", "legs": "#1D1A3A", "shoes": INK, "skin": "#F3D9C4", "hair": "#F2B33D",
               "headset": "#C9CED6", "card": "#F4F1EA", "gold": "#F2B33D"}


# ---------------------------------------------------------------- bosses
def varro():
    p, a = body(2.05, 76, arms=("down", "down"), torso_role="armour", leg_role="legs")
    t, H, r, hy, sh, hip = a["t"], a["H"], a["r"], a["hy"], a["sh"], a["hip"]
    p.insert(4, poly("armour", [(CX - 38, sh), (CX + 38, sh), (CX + 34, hip + 40), (CX - 34, hip + 40)]))
    p.append(poly("gun", [(CX - 34, hip - 6), (CX + 34, hip - 6), (CX + 34, hip + 2), (CX - 34, hip + 2)]))
    for i in range(4):
        p.append(poly("jar", [(CX - 26 + i * 15, hip + 2), (CX - 18 + i * 15, hip + 2), (CX - 18 + i * 15, hip + 14), (CX - 26 + i * 15, hip + 14)]))
    p.append(poly("bone", [(CX - r, hy - r), (CX + r, hy - r), (CX + r * 0.8, hy + r * 0.4), (CX + r * 0.35, hy + r * 1.4),
                           (CX - r * 0.35, hy + r * 1.4), (CX - r * 0.8, hy + r * 0.4)]))
    p.append(circ("gun", CX - r * 0.4, hy - r * 0.2, 2.6))
    p.append(circ("gun", CX + r * 0.4, hy - r * 0.2, 2.6))
    p.append(text("red", CX, t - 6, "61", 16))
    return p, {"armour": "#B7410E", "legs": "#4A4E54", "shoes": INK, "skin": "#C9A27E", "gun": "#4A4E54", "jar": "#FF7A2C",
               "bone": "#E3DCCB", "red": "#B3261E"}


def tamamo():
    p, a = body(1.85, 38, arms=("bent", "bent"), torso_role="robe", legs=False)
    t, H, r, hy, sh, hip = a["t"], a["H"], a["r"], a["hy"], a["sh"], a["hip"]
    tails = []
    for k in range(9):
        ang = math.radians(-160 + k * 17.5)
        x2, y2 = CX + 70 * math.cos(ang), hip - 10 + 70 * math.sin(ang)
        tails.append(path("tail", f"M{CX} {hip} Q{CX + 30 * math.cos(ang - 0.5)} {hip - 10 + 30 * math.sin(ang - 0.5)} {x2:.1f} {y2:.1f} "
                                  f"Q{CX + 40 * math.cos(ang + 0.3)} {hip - 10 + 40 * math.sin(ang + 0.3)} {CX + 6} {hip}"))
        tails.append(circ("fx", x2, y2, 3))
    p[0:0] = tails
    p.insert(len(tails), poly("robe", [(CX - 20, sh), (CX + 20, sh), (CX + 46, G - 2), (CX - 46, G - 2)]))
    p.append(poly("gold", [(CX - 20, sh), (CX + 20, sh), (CX + 6, sh + 26), (CX - 6, sh + 26)]))
    p.append(cap("hair", hy, r, 0.5))
    for s in (-1, 1):
        p.append(poly("hair", [(CX + s * r * 0.3, hy - r * 0.8), (CX + s * r * 1.2, hy - r * 2.1), (CX + s * r * 1.1, hy - r * 0.4)]))
    return p, {"robe": "#8E44AD", "gold": "#F4C430", "tail": "#F4F1EA", "fx": "#7FDBFF", "skin": "#F4E3D3", "hair": "#F4F1EA"}


def jin_chan():
    p = []
    p.append(ell("toad", CX, G - 20, 58, 20))
    for x in (CX - 40, CX, CX + 40):
        p.append(line("toad", x, G - 16, x, G - 2, 9))
    p.append(circ("gold", CX, G - 82, 54))
    p.append(circ("red", CX, G - 82, 14))
    p.append(poly("gold", [(CX - 4, G - 86), (CX + 4, G - 86), (CX + 4, G - 78), (CX - 4, G - 78)]))
    p.append(circ("skin", CX, G - 148, 16))
    p.append(poly("red", [(CX - 22, G - 160), (CX + 22, G - 160), (CX + 14, G - 176), (CX - 14, G - 176)]))
    for i in range(6):
        p.append(circ("gold", CX - 30 + i * 12, G - 44 + (i % 2) * 4, 4))
    p.append(text("gold", CX, G - 184, "88", 16))
    return p, {"toad": "#6B8E23", "gold": "#D4AF37", "red": "#B22222", "skin": "#E9C9A0"}


def rahu_ketu():
    p = []
    p.append(path("serpent", f"M{CX + 10} {G - 70} C{CX + 70} {G - 120}, {CX + 80} {G - 20}, {CX + 40} {G - 14} "
                             f"S{CX - 40} {G - 2}, {CX - 70} {G - 30} L{CX - 74} {G - 22} C{CX - 40} {G + 4}, {CX + 30} {G - 6}, {CX + 46} {G - 24} "
                             f"C{CX + 64} {G - 50}, {CX + 46} {G - 92}, {CX + 14} {G - 62} Z"))
    p.append(path("corona", f"M{CX - 74} {G - 26} l-14 -6 l4 10 l-12 2 l12 4 z"))
    p.append(circ("head", CX - 6, G - 140, 46))
    for k in range(7):
        x = CX - 40 + k * 11.5
        p.append(poly("corona", [(x, G - 176), (x + 5, G - 200 + (k % 2) * 8), (x + 10, G - 176)]))
    p.append(arc("night", CX - 22, G - 150, 8, 20, 160, 3))
    p.append(arc("night", CX + 10, G - 150, 8, 20, 160, 3))
    p.append(poly("corona", [(CX - 6, G - 172), (CX - 1, G - 164), (CX - 6, G - 156), (CX - 11, G - 164)]))
    p.append(line("night", CX - 14, G - 118, CX + 2, G - 118, 2.5))
    return p, {"serpent": "#4B2A6B", "head": "#4B2A6B", "corona": "#F4A300", "night": "#141018"}


def archon():
    p, a = body(2.00, 34, arms=("down", "out"), torso_role="robe", legs=False)
    t, H, r, hy, sh, hip = a["t"], a["H"], a["r"], a["hy"], a["sh"], a["hip"]
    p.insert(0, poly("robe", [(CX - 17, sh), (CX + 17, sh), (CX + 15, G - 2), (CX - 15, G - 2)]))
    p.append(poly("bronze", [(CX - 15, G - 12), (CX + 15, G - 12), (CX + 15, G - 2), (CX - 15, G - 2)]))
    p.append(line("bronze", CX - 4, sh + 4, CX - 4, G - 12, 3))
    for k in range(7):
        ang = math.radians(190 + k * 26)
        p.append(ell("bronze", CX + (r + 1) * math.cos(ang), hy - 1 + (r + 1) * math.sin(ang), 3.5, 2))
    sx, sy = a["hand"][1]
    p.append(line("staff", sx, G - 2, sx, t - 10, 3.5))
    p.append(circ("sieve", sx, t - 18, 13))
    for dx, dy in [(-5, -5), (5, -5), (-5, 5), (5, 5), (0, 0)]:
        p.append(circ("staff", sx + dx, t - 18 + dy, 1.8))
    p.append(text("steel", CX, t - 12, "17", 14))
    return p, {"robe": "#F4F1EA", "bronze": "#8C6A3F", "skin": "#E2D2C0", "staff": "#8C6A3F", "sieve": "#DDE6EE", "steel": "#4A4E54"}


def house():
    p, a = body(1.80, 40, arms=("down", "bent"), torso_role="suit", leg_role="suit")
    t, H, r, hy, sh, hip = a["t"], a["H"], a["r"], a["hy"], a["sh"], a["hip"]
    p.insert(0, ring("red", CX, a["waist"] - 6, 62, 8))
    p.insert(1, poly("red", [(CX + 56, a["waist"] - 40), (CX + 72, a["waist"] - 46), (CX + 64, a["waist"] - 30)]))
    p.append(poly("tie", [(CX - 3, sh + 2), (CX + 3, sh + 2), (CX + 4, a["waist"]), (CX, a["waist"] + 6), (CX - 4, a["waist"])]))
    p.append(path("hair", f"M{CX - r - 1} {hy} Q{CX} {hy - r * 1.5} {CX + r + 1} {hy} Q{CX} {hy - r * 0.7} {CX - r - 1} {hy} Z"))
    wx, wy = a["hand"][1]
    p.append(circ("gold", wx + 4, wy + 2, 6))
    p.append(text("gold", CX, t - 8, "89", 14))
    return p, {"suit": "#F4F1EA", "shoes": "#C0392B", "skin": "#E8D2BE", "red": "#C0392B", "tie": "#C0392B", "hair": "#D9D4CC", "gold": "#D4AF37"}


def thale():
    p, a = body(1.90, 44, arms=("bent", "bent"), torso_role="robe", legs=False)
    t, H, r, hy, sh, hip = a["t"], a["H"], a["r"], a["hy"], a["sh"], a["hip"]
    teeth = []
    for i in range(24):
        ang = math.pi * i / 12
        rr = 24 if i % 2 == 0 else 20
        teeth.append((CX + rr * math.cos(ang), hy + rr * math.sin(ang)))
    p.insert(0, poly("brass", teeth))
    p.insert(1, poly("robe", [(CX - 22, sh), (CX + 22, sh), (CX + 34, G - 2), (CX - 34, G - 2)]))
    for s in (-1, 1):  # cathedral spires on the shoulders
        p.append(poly("robe", [(CX + s * 14, sh + 2), (CX + s * 24, sh - 26), (CX + s * 30, sh + 4)]))
    p.append(path("brass", f"M{CX - 10} {G - 2} V{hip} A10 10 0 0 1 {CX + 10} {hip} V{G - 2} Z"))
    p.append(line("brass", CX, sh + 2, CX, hip - 6, 3))
    p.append(ring("brass", CX + r * 0.35, hy - 1, 3.2, 1.5))
    p.append(text("steel", CX, t - 18, "50", 14))
    return p, {"robe": "#E8E6E1", "brass": "#B5A642", "skin": "#EADFD3", "steel": "#8E9196"}


# ---------------------------------------------------------------- Meridian era outfits (comparison + line-ups)
ERA_COLOURS = {"charmpunk": "#FF2E88", "remainder": "#8A7F72", "ledgerism": "#B5A642", "gilded": "#D4AF37"}


def era_person(era, h_m=1.72, sw=42, skin="#D9B08C", variant=0):
    c = ERA_COLOURS[era]
    if era == "charmpunk":
        p, a = body(h_m, sw + 8, arms=("down", "bent"), torso_role="top", leg_role="legs", shoes="shoes")
        t, r, hy, sh, hip = a["t"], a["r"], a["hy"], a["sh"], a["hip"]
        p.insert(4, path("top", f"M{CX - sw / 2 - 6} {sh + 4} Q{CX} {sh - 10} {CX + sw / 2 + 6} {sh + 4} L{CX + sw / 2 + 2} {hip + 4} Q{CX} {hip + 12} {CX - sw / 2 - 2} {hip + 4} Z"))
        p.append(poly("cap", [(CX - r - 1, hy - r * 0.2), (CX + r + 1, hy - r * 0.2), (CX + r + 12, hy - r * 0.1), (CX + r + 1, hy - r * 1.1), (CX - r, hy - r * 1.1)]))
        for i, col in enumerate(["#3BB273", "#26428B", "#F5E400", "#D9822B"]):
            p.append(line("thread", CX - 14 + i * 9, a["sh"] + 6, CX - 14 + i * 9, a["sh"] + 20 + (i % 2) * 6, 1.2))
            p.append(circ(f"c{i}", CX - 14 + i * 9, a["sh"] + 22 + (i % 2) * 6, 3))
        p.append(text("num", CX, a["waist"] + 6, "77", 12))
        return p, {"top": c, "legs": "#26428B", "shoes": "#F4F1EA", "skin": skin, "cap": "#F5E400", "thread": INK,
                   "c0": "#3BB273", "c1": "#26428B", "c2": "#F5E400", "c3": "#D9822B", "num": "#F5E400"}
    if era == "remainder":
        p, a = body(h_m, sw, arms=("bent", "down"), torso_role="cloak", leg_role="legs", hunch=4)
        t, r, hy, sh, hip = a["t"], a["r"], a["hy"], a["sh"], a["hip"]
        p.append(path("cloak", f"M{CX} {hy - r - 4} Q{CX - r - 8} {hy - r} {CX - r - 6} {hy + r} L{CX - sw / 2 - 8} {hip + 34} L{CX + sw / 2 + 8} {hip + 30} L{CX + r + 6} {hy + r} Q{CX + r + 8} {hy - r} {CX} {hy - r - 4} Z"))
        p.append(circ("skin", CX, hy + 2, r * 0.7))
        p.append(poly("patch", [(CX - 12, hip - 4), (CX - 2, hip - 6), (CX - 1, hip + 6), (CX - 11, hip + 8)]))
        p.append(poly("patch2", [(CX + 6, sh + 14), (CX + 15, sh + 12), (CX + 16, sh + 21), (CX + 7, sh + 22)]))
        p.append(line("strap", CX - 14, sh + 4, CX + 20, hip, 2.5))
        p.append(poly("bag", [(CX + 14, hip - 4), (CX + 28, hip - 4), (CX + 28, hip + 10), (CX + 14, hip + 10)]))
        return p, {"cloak": c, "legs": "#4A4E54", "shoes": "#3A2E28", "skin": skin, "patch": "#C8963E", "patch2": "#5E7D4A",
                   "strap": "#6B4226", "bag": "#6B4226"}
    if era == "ledgerism":
        p, a = body(h_m, sw, arms=("down", "down"), torso_role="coat", leg_role="legs")
        t, r, hy, sh, hip = a["t"], a["r"], a["hy"], a["sh"], a["hip"]
        p.insert(4, poly("coat", [(CX - sw / 2, sh), (CX + sw / 2, sh), (CX + sw * 0.42, G - 34), (CX - sw * 0.42, G - 34)]))
        p.append(poly("steel", [(CX - sw / 2 - 3, sh - 2), (CX - sw / 2 + 10, sh - 2), (CX - sw / 2 + 10, sh + 3), (CX - sw / 2 - 3, sh + 3)]))
        p.append(poly("steel", [(CX + sw / 2 - 10, sh - 2), (CX + sw / 2 + 3, sh - 2), (CX + sw / 2 + 3, sh + 3), (CX + sw / 2 - 10, sh + 3)]))
        p.append(poly("belt", [(CX - sw * 0.36, a["waist"]), (CX + sw * 0.36, a["waist"]), (CX + sw * 0.36, a["waist"] + 5), (CX - sw * 0.36, a["waist"] + 5)]))
        p.append(poly("cap", [(CX - r - 4, hy - r * 0.3), (CX + r + 4, hy - r * 0.3), (CX + r + 1, hy - r * 1.5), (CX - r - 1, hy - r * 1.5)]))
        p.append(ell("cap", CX + 3, hy - r * 0.25, r + 5, 2.5))
        p.append(text("steeln", CX, a["waist"] - 6, "50", 11))
        return p, {"coat": "#6E6B4E", "legs": "#3A3A3A", "shoes": INK, "skin": skin, "steel": "#C9CED6", "belt": c, "cap": "#3A3A3A", "steeln": "#E8E6E1"}
    # gilded
    p, a = body(h_m, sw, arms=("bent", "bent"), torso_role="robe", legs=False)
    t, r, hy, sh, hip = a["t"], a["r"], a["hy"], a["sh"], a["hip"]
    p.insert(0, poly("robe", [(CX - sw / 2, sh), (CX + sw / 2, sh), (CX + sw * 0.8, G - 2), (CX - sw * 0.8, G - 2)]))
    p.append(poly("collar", [(CX - 12, sh + 2), (CX - 14, hy - 2), (CX - 4, sh - 4), (CX + 4, sh - 4), (CX + 14, hy - 2), (CX + 12, sh + 2)]))
    p.append(poly("jade", [(CX - sw * 0.8, G - 14), (CX + sw * 0.8, G - 14), (CX + sw * 0.8, G - 2), (CX - sw * 0.8, G - 2)]))
    p.append(cap("hair", hy, r, 0.2))
    p.append(circ("jade", CX, hy - r - 3, 3.5))
    p.append(path("plant", f"M{CX + 22} {a['waist']} q-2 -14 6 -22 q2 12 -6 22 z M{CX + 22} {a['waist']} q8 -10 16 -12 q-6 12 -16 12 z"))
    p.append(poly("pot", [(CX + 16, a["waist"]), (CX + 30, a["waist"]), (CX + 27, a["waist"] + 10), (CX + 19, a["waist"] + 10)]))
    return p, {"robe": c, "collar": "#00A86B", "jade": "#00A86B", "skin": skin, "hair": INK, "plant": "#3BB273", "pot": "#B22222"}


# ---------------------------------------------------------------- registry
BUILDERS = {
    "nil": nil, "vesper": vesper, "maeve": maeve, "hina": hina, "ba": ba, "bai_si": bai_si, "shunya": shunya,
    "prima": prima, "fibi": fibi, "varro": varro, "tamamo": tamamo, "jin_chan": jin_chan, "rahu_ketu": rahu_ketu,
    "archon": archon, "house": house, "thale": thale,
}


# horizontal extent of each figure (x0, x1) in the 160-wide frame, for tight crops at a shared scale
CROPS = {"nil": (45, 115), "vesper": (-32, 124), "maeve": (44, 128), "hina": (46, 150), "ba": (-24, 104), "bai_si": (50, 146),
         "shunya": (-14, 112), "prima": (18, 112), "fibi": (54, 180), "varro": (34, 126), "tamamo": (6, 154), "jin_chan": (18, 142),
         "rahu_ketu": (-12, 160), "archon": (58, 182), "house": (12, 148), "thale": (42, 118)}
ERA_CROP = (44, 116)


def crop_vb(x0, x1):
    return f"{x0} -28 {x1 - x0} 278"


def crop_width(key):
    x0, x1 = CROPS[key]
    return x1 - x0


def figure(key, mode="colour", mirror=False, cls="fig", crop=True):
    parts, colours = BUILDERS[key]()
    vb = "-24 -28 208 278"
    if crop:
        x0, x1 = CROPS[key]
        vb = crop_vb(160 - x1, 160 - x0) if mirror else crop_vb(x0, x1)
    return render(parts, colours, mode, mirror, vb=vb, cls=cls)


def era_figure(era, mode="colour", cls="fig", overrides=None, **kw):
    parts, colours = era_person(era, **kw)
    colours.update(overrides or {})
    return render(parts, colours, mode, vb=crop_vb(*ERA_CROP), cls=cls)


if __name__ == "__main__":
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    out = os.path.join(root, "art", "graphics", "figures")
    os.makedirs(out, exist_ok=True)
    n = 0
    for k in BUILDERS:
        for mode in ("colour", "ink"):
            with open(os.path.join(out, f"{k}_{mode}.svg"), "w") as f:
                f.write(figure(k, mode))
            n += 1
    for era in ERA_COLOURS:
        with open(os.path.join(out, f"era_{era}.svg"), "w") as f:
            f.write(era_figure(era))
        n += 1
    print("wrote", n, "figures to", out)
