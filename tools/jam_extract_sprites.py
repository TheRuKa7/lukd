"""Cut transparent jam sprites and background plates from the selected concept boards.

Boards are four views (front, left-facing, right-facing, back) on a flat cream
background. Each view is isolated by empty columns, the background is removed by a
border-connected flood fill with a soft edge, and the result is trimmed and scaled.
Output goes into the Unity jam project's Resources folder.
"""
import json, pathlib, sys
import numpy as np
from PIL import Image, ImageDraw, ImageFilter

ROOT = pathlib.Path(__file__).resolve().parents[1]
SRC = ROOT / 'art/concepts/complete'
OUT = ROOT / 'jam/RemainderJam/Assets/Resources/Art'

# id: (board, views to export {name: column index})
CAST = {
    'nil': ('cast_001_nil', {'front': 0, 'side': 2}),
    'vesper': ('cast_005_vesper', {'front': 0, 'side': 2}),
    'varro': ('cast_016_varro', {'front': 0, 'side': 2}),
    'hound': ('cast_057_debt_hound', {'side': 1}),
    'ama': ('cast_030_ama', {'front': 0}),
    'tobi': ('cast_031_tobi', {'front': 0}),
    'nought': ('cast_032_brother_nought', {'front': 0}),
    'gus': ('cast_034_gus', {'front': 0}),
    'collector': ('cast_048_f_collector', {'front': 0, 'side': 1}),
    'livia': ('cast_033_livia', {'front': 0}),
}
MAX_H = 760


def background_colour(a):
    edge = np.concatenate([a[:8].reshape(-1, 3), a[-8:].reshape(-1, 3), a[:, :8].reshape(-1, 3), a[:, -8:].reshape(-1, 3)])
    return np.median(edge, axis=0)


def columns(mask, n=4):
    """Split a board into n views using runs of empty columns."""
    occupied = mask.sum(axis=0) > 30  # ignore thin ground shadows bridging views
    runs, start = [], None
    for x, v in enumerate(occupied):
        if v and start is None:
            start = x
        if not v and start is not None:
            runs.append([start, x]); start = None
    if start is not None:
        runs.append([start, len(occupied)])
    runs = [r for r in runs if r[1] - r[0] > 20]
    while len(runs) > n:  # merge the closest neighbours (e.g. a weapon gap)
        gaps = [runs[i + 1][0] - runs[i][1] for i in range(len(runs) - 1)]
        i = int(np.argmin(gaps)); runs[i][1] = runs[i + 1][1]; del runs[i + 1]
    if len(runs) != n:
        raise ValueError(f'expected {n} views, found {len(runs)}')
    return runs


def cutout(board_path):
    im = Image.open(board_path).convert('RGB')
    a = np.asarray(im).astype(np.int16)
    bg = background_colour(a)
    dist = np.sqrt(((a - bg) ** 2).sum(axis=2))
    near = (dist < 34).astype(np.uint8) * 255
    m = Image.fromarray(near).copy()
    w, h = m.size
    for seed in [(0, 0), (w - 1, 0), (0, h - 1), (w - 1, h - 1), (w // 2, 0), (w // 2, h - 1)]:
        if m.getpixel(seed) == 255:
            ImageDraw.floodfill(m, seed, 128)
    outside = np.asarray(m) == 128
    # enclosed paper (between legs, under a hound's belly): flood the tolerant mask
    # from seeds that sit inside a 15 px patch of flat background colour
    seeds = Image.fromarray(((dist < 12) & ~outside).astype(np.uint8) * 255).filter(ImageFilter.MinFilter(15))
    seeds = np.asarray(seeds) > 0
    marr = np.asarray(m)
    for _ in range(64):
        ys, xs = np.nonzero(seeds & (marr == 255))
        if len(ys) == 0:
            break
        ImageDraw.floodfill(m, (int(xs[0]), int(ys[0])), 128)
        marr = np.asarray(m)
    outside = marr == 128
    # soft edge: fade pixels close to the background colour near the boundary
    alpha = np.where(outside, 0, 255).astype(np.uint8)
    soft = np.clip((dist - 10) / 30.0, 0, 1)
    edge = np.asarray(Image.fromarray(alpha).filter(ImageFilter.MaxFilter(5))) > 0
    edge &= np.asarray(Image.fromarray(alpha).filter(ImageFilter.MinFilter(5))) == 0
    alpha = np.where(edge, (soft * 255).astype(np.uint8), alpha)
    rgba = np.dstack([a.astype(np.uint8), alpha])
    return rgba, alpha > 40


def export_cast():
    manifest = {}
    for cid, (board, views) in CAST.items():
        rgba, solid = cutout(SRC / f'{board}.png')
        runs = columns(solid)
        for name, col in views.items():
            x0, x1 = runs[col]
            sub = rgba[:, x0:x1]
            ys = np.where(sub[:, :, 3].max(axis=1) > 40)[0]
            xs = np.where(sub[:, :, 3].max(axis=0) > 40)[0]
            sub = sub[ys[0]:ys[-1] + 1, xs[0]:xs[-1] + 1]
            img = Image.fromarray(sub, 'RGBA')
            scale = min(1.0, MAX_H / img.height)
            img = img.resize((max(1, round(img.width * scale)), round(img.height * scale)), Image.LANCZOS)
            path = OUT / 'chars' / f'{cid}_{name}.png'
            path.parent.mkdir(parents=True, exist_ok=True)
            img.save(path, optimize=True)
            manifest[f'{cid}_{name}'] = dict(board=f'art/concepts/complete/{board}.png', column=col, size=img.size)
    return manifest


def export_plates():
    """The Meridian board's lower panel is the street plate; its upper-right panel is the aerial map."""
    im = Image.open(SRC / 'env_meridian.png').convert('RGB')
    a = np.asarray(im).astype(np.int16)
    bg = background_colour(a)
    content = np.sqrt(((a - bg) ** 2).sum(axis=2)) > 30
    h, w = content.shape
    rows = content.sum(axis=1) > w * 0.2
    bands, start = [], None
    for y, v in enumerate(rows):
        if v and start is None: start = y
        if not v and start is not None: bands.append((start, y)); start = None
    if start is not None: bands.append((start, h))
    bands = [b for b in bands if b[1] - b[0] > 100]
    plates = {}
    def crop_band(y0, y1, which):
        cols = content[y0:y1].sum(axis=0) > (y1 - y0) * 0.5
        segs, s = [], None
        for x, v in enumerate(cols):
            if v and s is None: s = x
            if not v and s is not None: segs.append((s, x)); s = None
        if s is not None: segs.append((s, w))
        segs = [g for g in segs if g[1] - g[0] > 200]
        x0, x1 = segs[which]
        return im.crop((x0 + 4, y0 + 4, x1 - 4, y1 - 4))
    street = crop_band(*bands[-1], 0)
    aerial = crop_band(*bands[0], -1)
    plan = crop_band(*bands[0], 0)
    for name, img in (('meridian_street', street), ('meridian_aerial', aerial), ('meridian_plan', plan)):
        img.thumbnail((1600, 900), Image.LANCZOS)
        path = OUT / 'plates' / f'{name}.jpg'
        path.parent.mkdir(parents=True, exist_ok=True)
        img.save(path, quality=86, optimize=True)
        plates[name] = dict(source='art/concepts/complete/env_meridian.png', size=img.size)
    return plates


if __name__ == '__main__':
    report = dict(cast=export_cast(), plates=export_plates())
    (OUT / 'art_manifest.json').write_text(json.dumps(report, indent=1))
    print(json.dumps({k: len(v) for k, v in report.items()}))
