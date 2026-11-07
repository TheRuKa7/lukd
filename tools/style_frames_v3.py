#!/usr/bin/env python3
"""Art Direction v3 style frames, made locally from the 3D blockouts (free-first pipeline).

Produces art/style_v3/: versus_card.png, impact_frame.png, gag_panel.png, manga_page.png.
They demonstrate the v3 rules (Art Direction §0): SERIOUS vs GAG registers, screentone, speed lines, impact-frame
inversion, SFX lettered from digits, the Versus card and motion-comic panels. The figures are 3D blockouts, so these
are layout and treatment studies, not final art.
Usage: python3 tools/style_frames_v3.py
"""
import math
import os
import random

from PIL import Image, ImageChops, ImageDraw, ImageFilter, ImageFont, ImageOps

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "art", "style_v3")
VIEWS = os.path.join(ROOT, "art", "cast", "views")
PAPER, INK, NIXIE, RUST, CRIMSON = (244, 239, 228), (20, 16, 24), (255, 122, 44), (183, 65, 14), (229, 36, 59)
BG = (0xEF, 0xE6, 0xD2)
W, H = 1920, 1080


def font(size, bold=True):
    for name in (["Inter-Black.ttf", "InterDisplay-Black.otf", "Inter Display Black"] if bold else ["Inter-Regular.ttf"]):
        for d in ("/usr/share/fonts", "/usr/local/share/fonts", os.path.expanduser("~/.fonts")):
            for root, _, files in os.walk(d) if os.path.isdir(d) else []:
                for f in files:
                    if f.lower().startswith(name.lower().split(".")[0].replace(" ", "")):
                        return ImageFont.truetype(os.path.join(root, f), size)
    return ImageFont.truetype("DejaVuSans-Bold.ttf" if bold else "DejaVuSans.ttf", size)


def figure(key, view="front", height=700):
    """Load a 3D view, key out the paper background, scale to height. Returns RGBA."""
    im = Image.open(os.path.join(VIEWS, f"{key}_{view}.png")).convert("RGB")
    diff = ImageChops.difference(im, Image.new("RGB", im.size, BG)).convert("L").point(lambda v: 255 if v > 14 else 0)
    diff = diff.filter(ImageFilter.MaxFilter(3))
    rgba = im.convert("RGBA")
    rgba.putalpha(diff)
    s = height / im.height
    return rgba.resize((max(1, int(im.width * s)), height), Image.LANCZOS)


def ink(fig, thick=6):
    """SERIOUS register: heavy ink silhouette under the figure + screentone in the shadows."""
    a = fig.split()[3]
    outline = a.filter(ImageFilter.MaxFilter(thick * 2 + 1))
    base = Image.new("RGBA", fig.size, INK + (0,))
    base.putalpha(outline)
    out = Image.alpha_composite(base, fig)
    # screentone: dots where the figure is darker than mid-grey
    lum = ImageOps.grayscale(fig)
    mask = lum.point(lambda v: 255 if 40 < v < 120 else 0)
    mask = ImageChops.multiply(mask, a)
    tone = halftone(fig.size, 9, 2.4)
    dots = Image.new("RGBA", fig.size, INK + (150,))
    dots.putalpha(ImageChops.multiply(tone, mask))
    return Image.alpha_composite(out, dots)


def halftone(size, step, r):
    t = Image.new("L", (size[0] + step * 4, size[1] + step * 4), 0)
    d = ImageDraw.Draw(t)
    for y in range(0, t.height, step):
        for x in range(0, t.width, step):
            d.ellipse((x - r, y - r, x + r, y + r), fill=255)
    return t.rotate(45, resample=Image.NEAREST).crop((step * 2, step * 2, step * 2 + size[0], step * 2 + size[1]))


def speed_lines(img, cx, cy, n=140, color=INK, inner=260, seed=3):
    d = ImageDraw.Draw(img)
    rnd = random.Random(seed)
    R = math.hypot(W, H)
    for _ in range(n):
        a = rnd.uniform(0, 2 * math.pi)
        w = rnd.uniform(0.004, 0.018)
        r0 = inner + rnd.uniform(0, 160)
        p = [(cx + r0 * math.cos(a), cy + r0 * math.sin(a)), (cx + R * math.cos(a - w), cy + R * math.sin(a - w)), (cx + R * math.cos(a + w), cy + R * math.sin(a + w))]
        d.polygon(p, fill=color)


def jag_split(w, h, x_top, x_bot, teeth=14, amp=26):
    pts = [(0, 0), (x_top, 0)]
    for i in range(1, teeth):
        t = i / teeth
        x = x_top + (x_bot - x_top) * t + (amp if i % 2 else -amp)
        pts.append((x, h * t))
    pts += [(x_bot, h), (0, h)]
    return pts


def outlined_text(d, xy, text, f, fill, stroke=INK, sw=8, anchor="la"):
    d.text(xy, text, font=f, fill=fill, stroke_width=sw, stroke_fill=stroke, anchor=anchor)


def balloon(d, box, text, f, kind="rect"):
    x0, y0, x1, y1 = box
    if kind == "jag":
        cx, cy = (x0 + x1) / 2, (y0 + y1) / 2
        pts = []
        for k in range(28):
            a = 2 * math.pi * k / 28
            rr = 1.0 if k % 2 else 1.18
            pts.append((cx + (x1 - x0) / 2 * rr * math.cos(a), cy + (y1 - y0) / 2 * rr * math.sin(a)))
        d.polygon(pts, fill=PAPER, outline=INK, width=5)
    else:
        d.rectangle(box, fill=PAPER, outline=INK, width=5)
    d.multiline_text(((x0 + x1) / 2, (y0 + y1) / 2), text, font=f, fill=INK, anchor="mm", align="center", spacing=8)


def versus_card():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img, "RGBA")
    left = jag_split(W, H, 1010, 870)
    d.polygon(left, fill=(46, 58, 75))                               # Meridian wet slate
    right = [(p[0], p[1]) for p in left[1:-2]][::-1]
    d.polygon([(W, 0)] + left[1:-2] + [(W, H)], fill=RUST)
    d.line(left[1:-2], fill=INK, width=16)
    d.line(left[1:-2], fill=PAPER, width=5)
    # speed lines on each side
    sl = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    speed_lines(sl, 420, 560, 90, (255, 255, 255, 40), 330, 4)
    speed_lines(sl, 1500, 560, 90, (20, 16, 24, 70), 330, 5)
    img.paste(sl, (0, 0), sl)
    nil = ink(figure("nil", "front", 560))
    ves = ink(figure("vesper", "front", 590))
    var = ink(figure("varro", "front", 760))
    img.paste(ves, (60, H - 92 - ves.height + 10), ves)
    img.paste(nil, (360, H - 92 - nil.height + 10), nil)
    img.paste(var, (1330, H - 92 - var.height + 10), var)
    big, mid, small = font(120), font(54), font(34, False)
    outlined_text(d, (60, 40), "NIL & VESPER", big, PAPER)
    outlined_text(d, (64, 172), "OMEN  NaN  ·  77", mid, NIXIE, sw=6)
    outlined_text(d, (W - 60, 40), "VARRO KADE", big, PAPER, anchor="ra")
    outlined_text(d, (W - 64, 172), "THE LEDGERHOUND  ·  OMEN 61", mid, (255, 214, 160), sw=6, anchor="ra")
    balloon(d, (60, 260, 640, 380), "Seven chambers, Varro.\nYou've got one face.", font(34))
    balloon(d, (1060, 250, 1420, 350), "And one bounty.", font(38), "jag")
    # VS made of two crossed 7s
    vs = Image.new("RGBA", (420, 420), (0, 0, 0, 0))
    vd = ImageDraw.Draw(vs)
    f7 = font(330)
    outlined_text(vd, (210, 200), "7", f7, NIXIE, sw=14, anchor="mm")
    seven2 = vs.rotate(0)
    img.paste(seven2, (W // 2 - 230, H // 2 - 230), seven2)
    outlined_text(d, (W // 2 - 60, H // 2 + 150), "VS", font(150), PAPER, sw=12, anchor="mm")
    d.rectangle((0, H - 92, W, H), fill=INK)
    d.text((W // 2, H - 46), "RULE  ·  HE STEALS YOUR LAST DIGIT INTO A DEBT JAR. THREE PARRIES SHATTER IT.", font=font(36), fill=PAPER, anchor="mm")
    return img


def impact_frame():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    speed_lines(img, 980, 520, 220, INK, 300, 9)
    # burst
    pts = []
    for k in range(36):
        a = 2 * math.pi * k / 36
        r = 300 if k % 2 else 470
        pts.append((980 + r * math.cos(a), 520 + r * 0.8 * math.sin(a)))
    d.polygon(pts, fill=INK)
    # NIL silhouette, inverted to paper + nixie edge
    fig = figure("nil", "front", 760)
    a = fig.split()[3]
    sil = Image.new("RGBA", fig.size, PAPER + (255,))
    sil.putalpha(a)
    edge = Image.new("RGBA", fig.size, NIXIE + (255,))
    edge.putalpha(a.filter(ImageFilter.MaxFilter(13)))
    img.paste(edge, (560, 300), edge)
    img.paste(sil, (560, 300), sil)
    outlined_text(d, (1180, 470), "7 7 7", font(260), NIXIE, sw=16, anchor="mm")
    outlined_text(d, (1500, 820), "K-7-K!!", font(150), PAPER, sw=12, anchor="mm")
    d.rectangle((0, H - 100, W, H), fill=PAPER)
    d.line((0, H - 100, W, H - 100), fill=INK, width=6)
    d.text((60, H - 50), "IMPACT FRAME · 2–3 frames · ink + paper + the attacker's signature colour only (Art Direction v3 §0.4)", font=font(30, False), fill=INK, anchor="lm")
    return img


def gag_panel():
    img = Image.new("RGB", (W, H), (255, 214, 226))                  # GAG register: pastel swap
    d = ImageDraw.Draw(img)
    fig = figure("nil", "front", 700)
    a = fig.split()[3]
    flat = Image.new("RGBA", fig.size, (40, 34, 48, 255))
    flat.putalpha(a)
    img.paste(flat, (W // 2 - fig.width // 2, H - fig.height - 60), flat)
    balloon(d, (W // 2 + 170, 120, W // 2 + 610, 280), "…Huh.", font(80))
    d.text((W // 2 + 180, 320), "(the Jackpot is still\nexploding behind him)", font=font(40, False), fill=INK)
    for k in range(3):
        d.line((300 + k * 40, 200, 340 + k * 40, 260), fill=INK, width=6)
    d.text((60, H - 70), "GAG REGISTER · flat, front-on, still · hold 0.6–1.0 s · only after a big beat (Art Direction v3 §0.2)", font=font(28, False), fill=INK)
    return img


def manga_page(vs, imp, gag):
    page = Image.new("RGB", (1600, 2260), INK)
    g = 24

    def panel(src, box, crop=None):
        x0, y0, x1, y1 = box
        im = src.crop(crop) if crop else src
        im = ImageOps.fit(im, (x1 - x0, y1 - y0), Image.LANCZOS)
        page.paste(im, (x0, y0))

    env = Image.open(os.path.join(ROOT, "art", "envs", "meridian_front.png")).convert("RGB")
    panel(env, (g, g, 1600 - g, 620))                                   # wide establishing
    d = ImageDraw.Draw(page)
    balloon(d, (60, 60, 900, 170), "Rain Alley 9. Dawn Tally in three minutes.", font(34))
    panel(vs, (g, 620 + g, 1040, 1180), (0, 0, 1100, 640))               # versus split
    panel(gag, (1040 + g, 620 + g, 1600 - g, 1180), (560, 80, 1360, 1080))  # reaction close-up
    panel(imp, (g, 1180 + g, 1600 - g, 2260 - g))                        # splash
    return page


def main():
    os.makedirs(OUT, exist_ok=True)
    vs, imp, gag = versus_card(), impact_frame(), gag_panel()
    vs.save(os.path.join(OUT, "versus_card.png"), optimize=True)
    imp.save(os.path.join(OUT, "impact_frame.png"), optimize=True)
    gag.save(os.path.join(OUT, "gag_panel.png"), optimize=True)
    manga_page(vs, imp, gag).save(os.path.join(OUT, "manga_page.png"), optimize=True)
    print("wrote 4 style frames to", OUT)


if __name__ == "__main__":
    main()
