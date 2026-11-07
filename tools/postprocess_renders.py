#!/usr/bin/env python3
"""Trim and compress the Blender renders for the repo and the art book.

- art/cast/turnarounds/<key>.png (raw 4-view rows from render_cast.py) -> tight 4-view row, shared baseline, palette PNG
- art/cast/views/<key>_<view>.png  each view trimmed (same height for all four views of a character)
- art/envs/*.png -> palette PNGs
Usage: python3 tools/postprocess_renders.py
"""
import glob
import os

from PIL import Image, ImageChops

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BG = (0xEF, 0xE6, 0xD2)
VIEWS = ["front", "left", "right", "back"]


def bbox(im):
    """Content box, ignoring the outermost 4 px (the render frame's edge can carry a 1 px outline)."""
    diff = ImageChops.difference(im, Image.new("RGB", im.size, BG)).convert("L").point(lambda v: 255 if v > 12 else 0)
    inner = diff.crop((4, 4, im.width - 4, im.height - 4)).getbbox()
    return None if inner is None else (inner[0] + 4, inner[1] + 4, inner[2] + 4, inner[3] + 4)


def quant(im, colours=192):
    return im.convert("RGB").quantize(colours, method=Image.Quantize.MEDIANCUT, dither=Image.Dither.NONE)


def main():
    tdir = os.path.join(ROOT, "art", "cast", "turnarounds")
    vdir = os.path.join(ROOT, "art", "cast", "views")
    os.makedirs(vdir, exist_ok=True)
    for path in sorted(glob.glob(os.path.join(tdir, "*.png"))):
        key = os.path.splitext(os.path.basename(path))[0]
        im = Image.open(path).convert("RGB")
        if im.mode == "RGB" and im.width < 2000:   # already processed
            continue
        w = im.width // 4
        cells = [im.crop((i * w, 0, (i + 1) * w, im.height)) for i in range(4)]
        boxes = [bbox(c) for c in cells]
        top = min(b[1] for b in boxes if b) - 12
        bottom = max(b[3] for b in boxes if b) + 12
        views = []
        for v, c, b in zip(VIEWS, cells, boxes):
            x0, x1 = (b[0] - 16, b[2] + 16) if b else (0, w)
            crop = c.crop((max(0, x0), max(0, top), min(w, x1), min(c.height, bottom)))
            quant(crop).save(os.path.join(vdir, f"{key}_{v}.png"), optimize=True)
            views.append(crop)
        gap = 24
        row = Image.new("RGB", (sum(v.width for v in views) + gap * 3, views[0].height), BG)
        x = 0
        for v in views:
            row.paste(v, (x, 0))
            x += v.width + gap
        quant(row).save(path, optimize=True)
    for path in glob.glob(os.path.join(ROOT, "art", "envs", "*.png")):
        im = Image.open(path)
        if im.mode != "P":
            quant(im, 256).save(path, optimize=True)


def refit_full_width():
    """Re-trim views that hit the full cell width (from the frame-edge line) and rebuild their turnaround rows."""
    vdir = os.path.join(ROOT, "art", "cast", "views")
    keys = sorted({os.path.basename(p).rsplit("_", 1)[0] for p in glob.glob(os.path.join(vdir, "*_front.png"))})
    for key in keys:
        ims = [Image.open(os.path.join(vdir, f"{key}_{v}.png")).convert("RGB") for v in VIEWS]
        if max(im.width for im in ims) < 620:
            continue
        out = []
        for v, im in zip(VIEWS, ims):
            b = bbox(im)
            crop = im.crop((max(0, b[0] - 16), 0, min(im.width, b[2] + 16), im.height - 4)) if b else im
            quant(crop).save(os.path.join(vdir, f"{key}_{v}.png"), optimize=True)
            out.append(crop)
        gap = 24
        row = Image.new("RGB", (sum(v.width for v in out) + gap * 3, out[0].height), BG)
        x = 0
        for v in out:
            row.paste(v, (x, 0))
            x += v.width + gap
        quant(row).save(os.path.join(ROOT, "art", "cast", "turnarounds", f"{key}.png"), optimize=True)
        print("refit", key)


if __name__ == "__main__":
    main()
    refit_full_width()
