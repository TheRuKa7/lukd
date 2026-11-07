#!/usr/bin/env python3
"""Build every character blockout in Blender (bpy 5.2) and render turnaround sheets.

Usage (needs `pip install bpy==5.2.3 pillow`; headless needs Mesa EGL and EGL_PLATFORM=surfaceless):
    EGL_PLATFORM=surfaceless python tools/render_cast.py
Outputs:
    art/cast/sheets/sheet_NN.png        6 characters x 4 views per sheet (1 m = 200 px)
    art/cast/turnarounds/<key>.png      one row per character: FRONT, LEFT, RIGHT, BACK
    art/cast/zso_cast_blockout.blend    the scene (masters + instanced sheets)
"""
import math
import os
import subprocess
import sys

import bpy
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
OUT = os.path.join(ROOT, "art", "cast")
PPM = 260          # pixels per metre
CW, RH, ROWS, COLS = 2.4, 2.8, 6, 4


def lin(h):
    h = h.lstrip('#')
    c = [int(h[i:i + 2], 16) / 255 for i in (0, 2, 4)]
    f = lambda v: v / 12.92 if v <= 0.04045 else ((v + 0.055) / 1.055) ** 2.4
    return tuple(f(x) for x in c)


def main():
    os.makedirs(os.path.join(ROOT, "build", "cast_sheets"), exist_ok=True)
    os.makedirs(os.path.join(OUT, "turnarounds"), exist_ok=True)
    bpy.ops.wm.read_factory_settings(use_empty=True)
    code = subprocess.run([sys.executable, os.path.join(HERE, "blender_cast_json.py")], capture_output=True, text=True, check=True).stdout
    ns = {}
    exec(compile(code, "blender_cast_run.py", "exec"), ns)
    layout = ns["result"]["layout"]
    print("built", ns["result"]["characters"], "characters,", ns["result"]["objects"], "objects")

    sc = bpy.context.scene
    sc.render.engine = 'BLENDER_WORKBENCH'
    sh = sc.display.shading
    sh.light, sh.color_type = 'STUDIO', 'OBJECT'
    sh.show_cavity, sh.cavity_type = True, 'BOTH'
    sh.show_object_outline, sh.object_outline_color = True, (0.08, 0.06, 0.09)
    sh.show_shadows, sh.shadow_intensity = True, 0.3
    sh.show_specular_highlight = False
    sc.display.render_aa = '8'
    sc.view_settings.view_transform = 'Standard'
    sc.world = bpy.data.worlds.new("paper")
    sc.world.color = lin("#EFE6D2")
    sc.render.image_settings.file_format = 'PNG'
    sc.render.film_transparent = False

    cam = bpy.data.objects.new("CAM_sheet", bpy.data.cameras.new("CAM_sheet"))
    sc.collection.objects.link(cam)
    cam.data.type = 'ORTHO'
    cam.rotation_euler = (math.pi / 2, 0, 0)
    sc.camera = cam
    n_sheets = max(s for _, s, _ in layout) + 1
    W, H = COLS * CW, ROWS * RH
    sc.render.resolution_x, sc.render.resolution_y = int(W * PPM), int(H * PPM)
    cam.data.ortho_scale = max(W, H)
    for s in range(n_sheets):
        x0 = 3000.0 + s * 12
        cam.location = (x0 + (COLS - 1) * CW / 2, -30, (2.65 + (-(ROWS - 1) * RH - 0.15)) / 2)
        path = os.path.join(ROOT, "build", "cast_sheets", f"sheet_{s + 1:02d}.png")
        sc.render.filepath = path
        bpy.ops.render.render(write_still=True)
        im = Image.open(path).convert("RGB")
        for key, ss, r in layout:
            if ss == s:
                row = im.crop((0, r * int(RH * PPM), im.width, (r + 1) * int(RH * PPM)))
                row.save(os.path.join(OUT, "turnarounds", f"{key}.png"), optimize=True)
        print("sheet", s + 1, "of", n_sheets)
    bpy.ops.wm.save_as_mainfile(filepath=os.path.join(OUT, "zso_cast_blockout.blend"), compress=True)


if __name__ == "__main__":
    main()
