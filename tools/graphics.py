"""ZERO-SUM: OMEN graphic design kit: faction emblems, Omen displays, charm icons.

Style: one ink weight (3 px at 120 px), flat fills from the bible palettes, a 3 px offset "misprint" shadow
in ink at 18% (screen-print feel). Every function returns a standalone SVG string (viewBox 0 0 120 120).
Run directly to write them all to art/graphics/.
"""
import argparse
import os
from pathlib import Path
import re
import xml.etree.ElementTree as ET

INK = "#141018"
PAPER = "#F2E8D5"
NIXIE = "#FF7A2C"
RED = "#B3261E"


def svg(body, vb="0 0 120 120", shadow=True):
    sh = f'<g transform="translate(3 3)" opacity=".18" fill="{INK}" stroke="{INK}">{body}</g>' if shadow else ""
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}" stroke-linejoin="round" stroke-linecap="round">'
            f'{sh}<g stroke="{INK}" stroke-width="3">{body}</g></svg>')


def gear(cx, cy, r, teeth=12, fill=NIXIE):
    import math
    pts = []
    for i in range(teeth * 2):
        a = math.pi * i / teeth
        rr = r if i % 2 == 0 else r * 0.82
        pts.append(f"{cx + rr * math.cos(a):.1f},{cy + rr * math.sin(a):.1f}")
    return f'<polygon points="{" ".join(pts)}" fill="{fill}"/>'


# ---------------------------------------------------------------- faction emblems
EMBLEMS = {
    "basilica": ("The Basilica", svg(gear(60, 60, 50, 16, "#B5A642") + f'<circle cx="60" cy="60" r="30" fill="{PAPER}"/>'
                                     f'<ellipse cx="60" cy="60" rx="14" ry="20" fill="none" stroke-width="7" stroke="{NIXIE}"/>')),
    "collectors": ("The Collectors", svg(f'<rect x="18" y="24" width="84" height="72" rx="6" fill="#B7410E"/>'
                                         f'<path d="M36 46 L48 34 L60 44 L72 34 L84 46 L78 72 Q60 86 42 72 Z" fill="{PAPER}"/>'
                                         f'<circle cx="51" cy="56" r="5" fill="{INK}"/><circle cx="69" cy="56" r="5" fill="{INK}"/><path d="M54 70 h12" />')),
    "bazaar": ("Charm Bazaar guilds", svg(f'<circle cx="60" cy="60" r="40" fill="none" stroke-width="5"/>'
                                          f'<path d="M60 20 a8 8 0 1 0 0.1 0" fill="#3BB273"/><circle cx="100" cy="60" r="8" fill="#26428B"/>'
                                          f'<path d="M52 92 a8 8 0 0 0 16 0 v8 h-16z" fill="#D9822B"/><circle cx="20" cy="60" r="8" fill="#F2B33D"/>'
                                          f'<text x="60" y="70" text-anchor="middle" font-family="Big Shoulders Display,Impact" font-weight="900" font-size="30" fill="{INK}" stroke="none">7</text>')),
    "yokai": ("The Yokai Courts", svg("".join(
        f'<path d="M{60 + 34 * __import__("math").cos(a)} {62 + 34 * __import__("math").sin(a)} q -6 -12 0 -20 q 6 8 0 20z" fill="#7FDBFF"/>'
        for a in [__import__("math").pi * (0.75 + 0.1875 * k) for k in range(9)]) + f'<circle cx="60" cy="66" r="14" fill="#8E44AD"/>')),
    "exchange": ("The Luck Exchange", svg(f'<ellipse cx="60" cy="68" rx="36" ry="26" fill="#6B8E23"/><circle cx="46" cy="50" r="8" fill="{PAPER}"/><circle cx="74" cy="50" r="8" fill="{PAPER}"/>'
                                          f'<circle cx="46" cy="50" r="3" fill="{INK}"/><circle cx="74" cy="50" r="3" fill="{INK}"/>'
                                          f'<circle cx="60" cy="74" r="10" fill="#D4AF37"/><rect x="56" y="70" width="8" height="8" fill="{PAPER}"/>'
                                          f'<path d="M34 92 l-6 12 M60 94 v12 M86 92 l6 12"/>')),
    "ten_courts": ("The Ten Courts", svg(f'<rect x="54" y="10" width="12" height="70" rx="3" fill="#B22222"/><path d="M50 80 h20 l-4 18 q-6 14 -12 0z" fill="{INK}"/>'
                                         f'<path d="M30 104 q30 -10 60 0" fill="none" stroke-width="4"/>')),
    "observatory": ("The Observatory", svg(f'<circle cx="60" cy="60" r="44" fill="#3F3D99"/><circle cx="60" cy="60" r="30" fill="none" stroke="{PAPER}" stroke-width="4"/>'
                                           f'<path d="M16 60 h88 M60 16 v88" stroke="#F4A300" stroke-width="3"/>'
                                           f'<ellipse cx="60" cy="60" rx="10" ry="14" fill="none" stroke="#F4A300" stroke-width="6"/>')),
    "synod": ("The Pythagorean Synod", svg(f'<circle cx="60" cy="60" r="48" fill="#1F6FB2"/>' + "".join(
        f'<circle cx="{60 + 41 * __import__("math").cos(2 * __import__("math").pi * k / 24):.1f}" cy="{60 + 41 * __import__("math").sin(2 * __import__("math").pi * k / 24):.1f}" r="2.6" fill="#DDE6EE" stroke="none"/>'
        for k in range(24)) + "".join(
        f'<circle cx="{60 + (i - row / 2) * 13:.1f}" cy="{30 + row * 14}" r="5" fill="{PAPER}"/>' for row in range(4) for i in range(row + 1)))),
    "house": ("The House", svg(f'<circle cx="60" cy="60" r="42" fill="none" stroke="#C0392B" stroke-width="12"/>'
                               f'<path d="M96 40 l12 -4 l-6 12z" fill="#C0392B"/><circle cx="60" cy="60" r="22" fill="#D4AF37"/>'
                               f'<text x="60" y="69" text-anchor="middle" font-family="Big Shoulders Display,Impact" font-weight="900" font-size="24" fill="{INK}" stroke="none">89</text>')),
}

# ---------------------------------------------------------------- Omen displays (one per Meridian era)
def omen_charmpunk():
    return svg(f'<ellipse cx="60" cy="58" rx="46" ry="14" fill="none" stroke="#FF2E88" stroke-width="5"/>'
               f'<ellipse cx="60" cy="58" rx="46" ry="14" fill="none" stroke="#00E5FF" stroke-width="2" stroke-dasharray="4 6"/>'
               f'<text x="60" y="52" text-anchor="middle" font-family="Big Shoulders Display,Impact" font-weight="900" font-size="34" fill="#F5E400" stroke="{INK}" stroke-width="2">77</text>'
               f'<path d="M30 70 v14 M60 72 v18 M90 70 v14"/><circle cx="30" cy="88" r="5" fill="#3BB273"/><path d="M54 92 h12 l-6 10z" fill="#FF2E88"/><circle cx="90" cy="88" r="5" fill="#26428B"/>', shadow=False)


def omen_remainder():
    return svg(f'<path d="M60 6 v20" stroke-width="2"/><rect x="38" y="26" width="44" height="76" rx="20" fill="#2A1A14"/>'
               f'<text x="60" y="78" text-anchor="middle" font-family="Big Shoulders Display,Impact" font-weight="900" font-size="34" fill="#FF7A2C" stroke="none" opacity=".75">04</text>'
               f'<path d="M48 36 l10 14 l-6 8 l12 16" stroke="{PAPER}" stroke-width="2" fill="none"/>'
               f'<rect x="44" y="98" width="32" height="10" fill="#6B4226"/>')


def omen_ledgerism():
    return svg(f'<rect x="16" y="30" width="88" height="60" rx="4" fill="#8E9196"/><rect x="24" y="38" width="72" height="44" fill="#E8E6E1"/>'
               f'<text x="60" y="76" text-anchor="middle" font-family="Big Shoulders Display,Impact" font-weight="900" font-size="38" fill="{INK}" stroke="none">50</text>'
               f'<circle cx="22" cy="36" r="3" fill="{INK}"/><circle cx="98" cy="36" r="3" fill="{INK}"/><circle cx="22" cy="84" r="3" fill="{INK}"/><circle cx="98" cy="84" r="3" fill="{INK}"/>')


def omen_gilded():
    return svg(f'<path d="M60 14 L100 60 L60 106 L20 60 Z" fill="#00A86B"/><path d="M60 26 L88 60 L60 94 L32 60 Z" fill="#F4F1EA"/>'
               f'<text x="60" y="72" text-anchor="middle" font-family="Big Shoulders Display,Impact" font-weight="900" font-size="32" fill="#D4AF37" stroke="#8C6A3F" stroke-width="1.5">99</text>'
               f'<path d="M40 40 q6 -8 12 0 M68 40 q6 -8 12 0" stroke="#D4AF37" fill="none"/>')


OMENS = {"charmpunk": ("Charmpunk", omen_charmpunk()), "remainder": ("Remainder", omen_remainder()),
         "ledgerism": ("Ledgerism", omen_ledgerism()), "gilded": ("Gilded Fortune", omen_gilded())}

# ---------------------------------------------------------------- charm icons
CHARMS = {
    "ofuda": svg(f'<rect x="36" y="10" width="48" height="100" rx="3" fill="{PAPER}"/><rect x="44" y="22" width="32" height="32" fill="#B3261E"/>'
                 f'<path d="M48 72 h24 M48 84 h24 M52 96 h16" fill="none" stroke="#B3261E" stroke-width="4"/>'),
    "beckoning_cat": svg(f'<path d="M30 104 V58 q0 -26 30 -26 q30 0 30 26 V104 z" fill="{PAPER}"/><path d="M34 40 l6 -20 l12 14 M86 40 l-6 -20 l-12 14" fill="{PAPER}"/>'
                         f'<path d="M84 58 q14 -14 6 -30" fill="none" stroke-width="10" stroke="{PAPER}"/><path d="M84 58 q14 -14 6 -30" fill="none"/>'
                         f'<rect x="36" y="78" width="48" height="10" fill="#C0392B"/><circle cx="60" cy="92" r="6" fill="#D4AF37"/><path d="M48 54 q4 -4 8 0 M64 54 q4 -4 8 0"/>'),
    "daruma": svg(f'<path d="M60 14 q40 0 40 50 q0 44 -40 44 q-40 0 -40 -44 q0 -50 40 -50z" fill="#C0392B"/><ellipse cx="60" cy="54" rx="24" ry="22" fill="{PAPER}"/>'
                  f'<circle cx="50" cy="52" r="6" fill="{INK}"/><circle cx="70" cy="52" r="6" fill="{PAPER}"/><path d="M52 66 q8 6 16 0"/>'),
    "red_envelope": svg(f'<rect x="28" y="14" width="64" height="92" rx="4" fill="#B22222"/><path d="M28 30 l32 24 l32 -24"/><circle cx="60" cy="56" r="12" fill="#D4AF37"/>'
                        f'<text x="60" y="62" text-anchor="middle" font-family="Big Shoulders Display,Impact" font-weight="900" font-size="16" fill="#B22222" stroke="none">8</text>'),
    "door_god": svg(f'<path d="M30 20 h60 v50 q0 30 -30 36 q-30 -6 -30 -36z" fill="#B22222"/><path d="M40 46 l14 6 M80 46 l-14 6" stroke-width="5"/>'
                    f'<circle cx="48" cy="58" r="5" fill="{PAPER}"/><circle cx="72" cy="58" r="5" fill="{PAPER}"/><path d="M44 82 q16 10 32 0" stroke-width="4"/><path d="M30 20 l-8 -8 M90 20 l8 -8" />'),
    "lemon_chillies": svg(f'<path d="M60 8 v86" stroke-width="2"/><ellipse cx="60" cy="102" rx="12" ry="10" fill="#F5E400"/>' + "".join(
        f'<path d="M60 {24 + i * 10} q{(-1) ** i * 22} 4 {(-1) ** i * 26} 14" stroke="#2E8B3D" stroke-width="6" fill="none"/>' for i in range(7))),
    "beads_108": svg("".join(
        f'<circle cx="{60 + 42 * __import__("math").cos(2 * __import__("math").pi * i / 27):.1f}" cy="{56 + 42 * __import__("math").sin(2 * __import__("math").pi * i / 27):.1f}" r="5" fill="#8C5A2B"/>'
        for i in range(27)) + f'<path d="M60 98 v14" stroke-width="3"/><path d="M54 112 h12" stroke="#B22222" stroke-width="5"/>'),
    "evil_eye": svg(f'<circle cx="60" cy="60" r="46" fill="#1F4FB2"/><circle cx="60" cy="60" r="30" fill="{PAPER}"/><circle cx="60" cy="60" r="18" fill="#6FB7E9"/><circle cx="60" cy="60" r="9" fill="{INK}"/>'),
    "fortuna_wheel": svg(f'<circle cx="60" cy="60" r="46" fill="#D4AF37"/><circle cx="60" cy="60" r="12" fill="{PAPER}"/>' + "".join(
        f'<line x1="60" y1="60" x2="{60 + 46 * __import__("math").cos(__import__("math").pi * k / 4):.1f}" y2="{60 + 46 * __import__("math").sin(__import__("math").pi * k / 4):.1f}"/>' for k in range(8))),
    "horseshoe": svg(f'<path d="M30 20 v40 q0 40 30 40 q30 0 30 -40 v-40 h-16 v40 q0 22 -14 22 q-14 0 -14 -22 v-40z" fill="#D9822B"/>'
                     + "".join(f'<circle cx="{x}" cy="{y}" r="3" fill="{INK}"/>' for x, y in [(38, 30), (38, 50), (82, 30), (82, 50)])),
    "dice": svg(f'<rect x="14" y="40" width="48" height="48" rx="8" fill="{PAPER}" transform="rotate(-12 38 64)"/><rect x="58" y="30" width="48" height="48" rx="8" fill="#C0392B" transform="rotate(10 82 54)"/>'
                + "".join(f'<circle cx="{x}" cy="{y}" r="4" fill="{INK}" stroke="none"/>' for x, y in [(28, 56), (38, 66), (48, 76)])
                + "".join(f'<circle cx="{x}" cy="{y}" r="4" fill="{PAPER}" stroke="none"/>' for x, y in [(72, 42), (92, 46), (82, 54), (72, 62), (92, 66)])),
    "clover": svg("".join(f'<circle cx="{60 + dx}" cy="{56 + dy}" r="18" fill="#3BB273"/>' for dx, dy in [(-14, -14), (14, -14), (-14, 14), (14, 14)])
                  + f'<path d="M60 70 q4 24 18 38" stroke-width="5" fill="none" stroke="#2E7D4F"/>'),
    "black_cat": svg(f'<path d="M34 104 q-8 -40 18 -58 l-6 -22 l16 12 h8 l16 -12 l-6 22 q26 18 18 58z" fill="{INK}"/><circle cx="52" cy="58" r="5" fill="#F5E400" stroke="none"/><circle cx="72" cy="58" r="5" fill="#F5E400" stroke="none"/>'
                     f'<path d="M86 100 q22 -6 14 -30" fill="none" stroke-width="7"/>'),
}

# ---------------------------------------------------------------- the reel, styled per land (GDD §8)
def _tubes(x0, y0, w, h, gap, fill, digits, dfill, size=22):
    out = ""
    for i, d in enumerate(digits):
        x = x0 + i * (w + gap)
        out += f'<rect x="{x}" y="{y0}" width="{w}" height="{h}" rx="4" fill="{fill}"/>'
        out += (f'<text x="{x + w / 2}" y="{y0 + h / 2 + size * 0.36}" text-anchor="middle" font-family="Big Shoulders Display,Impact" '
                f'font-weight="900" font-size="{size}" fill="{dfill}" stroke="none">{d}</text>')
    return out


REELS = {
    "meridian": ("Neon sign", svg(f'<rect x="8" y="30" width="104" height="54" rx="6" fill="#2E3A4B"/>' + _tubes(16, 38, 26, 38, 6, INK, "777", "#FF2E88")
                                  + f'<path d="M30 30 v-14 M90 30 v-14" stroke-width="2"/><path d="M14 92 l8 -8 M106 92 l-8 -8" stroke="#00E5FF" stroke-width="3"/>')),
    "hyakki": ("Torii with three lanterns", svg(f'<path d="M6 22 q54 -12 108 0 v8 q-54 -8 -108 0z" fill="#E34234"/><rect x="14" y="36" width="92" height="6" fill="#E34234"/>'
                                               f'<rect x="20" y="30" width="8" height="84" fill="#E34234"/><rect x="92" y="30" width="8" height="84" fill="#E34234"/>'
                                               + _tubes(31, 48, 17, 30, 4, "#F2B33D", "777", INK, 18))),
    "river": ("Golden abacus", svg(f'<rect x="8" y="22" width="104" height="76" rx="4" fill="#B22222"/><rect x="14" y="28" width="92" height="64" fill="#E9E2D0"/>'
                                   f'<path d="M14 46 h92" stroke-width="3"/>' + "".join(f'<path d="M{26 + k * 34} 28 v64" stroke-width="2"/>' for k in range(3))
                                   + "".join(f'<ellipse cx="{26 + k * 34}" cy="{y}" rx="9" ry="5" fill="#D4AF37"/>' for k in range(3) for y in (38, 60, 70, 80)))),
    "sunyapura": ("Observatory dials", svg("".join(f'<circle cx="{24 + k * 36}" cy="64" r="16" fill="#D8A86B"/><path d="M{24 + k * 36} 64 l{10 - k * 8} -12" stroke="#4B2A6B" stroke-width="3"/>'
                                                   f'<path d="M{8 + k * 36} 64 a16 16 0 0 1 32 0" fill="none" stroke="#B5893B" stroke-width="2"/>' for k in range(3))
                                           + f'<path d="M6 92 h108 v8 h-108z" fill="#B5893B"/><path d="M60 14 l10 18 h-20z" fill="#F4A300"/>')),
    "kroton": ("Marble columns", svg("".join(f'<rect x="{12 + k * 36}" y="26" width="24" height="76" fill="#F4F1EA"/><rect x="{8 + k * 36}" y="18" width="32" height="8" fill="#F4F1EA"/>'
                                             f'<rect x="{8 + k * 36}" y="102" width="32" height="8" fill="#F4F1EA"/>'
                                             f'<text x="{24 + k * 36}" y="72" text-anchor="middle" font-family="Big Shoulders Display,Impact" font-weight="900" font-size="22" fill="#1F6FB2" stroke="none">{"257"[k]}</text>' for k in range(3)))),
    "crossroads": ("Slot machine", svg(f'<rect x="16" y="14" width="80" height="96" rx="10" fill="#C0392B"/><rect x="22" y="20" width="68" height="14" rx="3" fill="#F2B33D"/>'
                                       + _tubes(24, 44, 18, 32, 4, "#F4F1EA", "777", "#C0392B", 20)
                                       + f'<path d="M96 40 h8 v-20" stroke-width="4" fill="none"/><circle cx="104" cy="16" r="6" fill="{INK}"/>')),
    "basilica": ("The Basilica clock", svg(gear(60, 60, 52, 18, "#B5A642") + f'<circle cx="60" cy="60" r="38" fill="#E8E6E1"/>' + _tubes(27, 46, 19, 28, 3, INK, "050", NIXIE, 18))),
}

def reel_frame(key):
    """Blank frame for runtime: all meaningful digits must be separate engine text."""
    return re.sub(r"<text\b[^>]*>.*?</text>", "", REELS[key][1], flags=re.S)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate candidate SVG identity kit; preview digits are not runtime data.")
    parser.add_argument("--output-dir", type=Path, help="Default build/graphics; preserves tracked historical references.")
    parser.add_argument("--check", action="store_true", help="Validate generated XML without writing files.")
    parser.add_argument("--runtime-frames", action="store_true", help="Also export digit-free reel frames.")
    args = parser.parse_args()
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    out = args.output_dir or Path(root, "build", "graphics")
    values = {**{f"emblem_{k}": s for k, (_, s) in EMBLEMS.items()},
              **{f"omen_{k}": s for k, (_, s) in OMENS.items()},
              **{f"charm_{k}": s for k, s in CHARMS.items()},
              **{f"reel_{k}": s for k, (_, s) in REELS.items()}}
    if args.runtime_frames:
        values.update({f"reel_{k}_blank": reel_frame(k) for k in REELS})
    for name, value in values.items():
        ET.fromstring(value)
    if not args.check:
        out.mkdir(parents=True, exist_ok=True)
        for name, value in values.items():
            (out / (name + ".svg")).write_text(value, encoding="utf-8")
    print("validated" if args.check else "wrote", len(values), "candidate SVGs", "" if args.check else str(out))
