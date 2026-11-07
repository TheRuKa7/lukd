#!/usr/bin/env python3
"""Build and render the seven environment blockouts: top-down, 2.5D (isometric) and front (battle camera) views.

Usage: EGL_PLATFORM=surfaceless python tools/build_envs.py [path/to/3d_jutsu_scene.blend]
The Wards and the Moon Pier come from the 3D Jutsu project file (pass its path); the other five lands are built here.
Outputs art/envs/<land>_{top,iso,front}.png and art/envs/zso_envs_blockout.blend.
"""
import math
import os
import random
import sys

import bpy  # noqa: I001  (bpy must load before bmesh)
import bmesh
from mathutils import Euler, Matrix, Vector

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "art", "envs")
INK = "#141018"


def lin(h):
    h = h.lstrip('#')
    c = [int(h[i:i + 2], 16) / 255 for i in (0, 2, 4)]
    f = lambda v: v / 12.92 if v <= 0.04045 else ((v + 0.055) / 1.055) ** 2.4
    return (f(c[0]), f(c[1]), f(c[2]), 1.0)


class E:
    """Tiny geometry kit; every object gets a flat object colour."""

    def __init__(self, name, ox, oy=0.0):
        self.col = bpy.data.collections.new(name)
        bpy.context.scene.collection.children.link(self.col)
        self.ox, self.oy, self.n = ox, oy, 0

    def _ob(self, bm, color, loc, rot=(0, 0, 0), scale=(1, 1, 1)):
        self.n += 1
        me = bpy.data.meshes.new(f"{self.col.name}_{self.n}")
        bm.to_mesh(me)
        bm.free()
        ob = bpy.data.objects.new(me.name, me)
        self.col.objects.link(ob)
        ob.location = (loc[0] + self.ox, loc[1] + self.oy, loc[2])
        ob.rotation_euler, ob.scale = rot, scale
        ob.color = lin(color)
        return ob

    def box(self, sx, sy, sz, x, y, z, color, rz=0.0, rx=0.0, ry=0.0):
        """Box with its BASE at z."""
        bm = bmesh.new()
        bmesh.ops.create_cube(bm, size=1.0)
        return self._ob(bm, color, (x, y, z + sz / 2), (rx, ry, rz), (sx, sy, sz))

    def cyl(self, r1, r2, h, x, y, z, color, seg=24, sx=1.0, sy=1.0, rot=(0, 0, 0)):
        bm = bmesh.new()
        bmesh.ops.create_cone(bm, cap_ends=True, cap_tris=False, segments=seg, radius1=max(r1, 1e-4), radius2=max(r2, 1e-4), depth=h)
        return self._ob(bm, color, (x, y, z + h / 2), rot, (sx, sy, 1))

    def sph(self, r, x, y, z, color, scale=(1, 1, 1), seg=16):
        bm = bmesh.new()
        bmesh.ops.create_uvsphere(bm, u_segments=seg, v_segments=max(8, seg // 2), radius=r)
        return self._ob(bm, color, (x, y, z), scale=scale)

    def pyramid(self, w, d, h, x, y, z, color, rz=0.0):
        """Square-based pyramid roof (rotation baked into the mesh so scaling stays axis-aligned)."""
        bm = bmesh.new()
        bmesh.ops.create_cone(bm, cap_ends=True, cap_tris=False, segments=4, radius1=1.0 / math.sqrt(2), radius2=1e-4, depth=h)
        bmesh.ops.rotate(bm, verts=bm.verts, cent=(0, 0, 0), matrix=Matrix.Rotation(math.pi / 4, 3, 'Z'))
        return self._ob(bm, color, (x, y, z + h / 2), (0, 0, rz), (w, d, 1))

    def rod(self, p0, p1, r, color):
        p0, p1 = Vector(p0), Vector(p1)
        d = p1 - p0
        bm = bmesh.new()
        bmesh.ops.create_cone(bm, cap_ends=True, cap_tris=False, segments=8, radius1=r, radius2=r, depth=max(d.length, 1e-3))
        rot = Vector((0, 0, 1)).rotation_difference(d.normalized()).to_euler()
        return self._ob(bm, color, tuple((p0 + p1) / 2), rot)

    def torus(self, R, r, x, y, z, color, rot=(0, 0, 0), seg=32, arc=1.0):
        bm = bmesh.new()
        n = seg if arc >= 1 else int(seg * arc) + 1
        rings = []
        for i in range(n):
            a = 2 * math.pi * arc * i / seg
            rings.append([bm.verts.new(((R + r * math.cos(b)) * math.cos(a), (R + r * math.cos(b)) * math.sin(a), r * math.sin(b)))
                          for b in [2 * math.pi * j / 8 for j in range(8)]])
        for i in range(n if arc >= 1 else n - 1):
            a, b2 = rings[i], rings[(i + 1) % n]
            for j in range(8):
                bm.faces.new((a[j], a[(j + 1) % 8], b2[(j + 1) % 8], b2[j]))
        return self._ob(bm, color, (x, y, z), rot)

    def figure(self, x, y, color, h=1.75):
        """Scale figure for reading size: a simple person."""
        self.cyl(0.18, 0.22, h * 0.82, x, y, 0, color, seg=10)
        self.sph(0.13, x, y, h * 0.9, "#E0C0A0", seg=10)


# ---------------------------------------------------------------- the five new lands
def river(ox):
    e = E("ENV_RIVER", ox)
    W = {"jade": "#00A86B", "ochre": "#C8963E", "lacquer": "#B22222", "gold": "#D4AF37", "paper": "#E9E2D0", "ink": "#3A4A3F", "water": "#2F6B6A", "stone": "#9C9486"}
    e.box(90, 90, 0.2, 0, 0, -0.2, "#8C8270")
    e.box(90, 16, 0.1, 0, 18, -0.05, W["water"])                      # the river
    e.box(90, 3, 0.6, 0, 9.5, -0.4, W["stone"])                        # quay
    e.box(90, 3, 0.6, 0, 26.5, -0.4, W["stone"])
    # the Luck Exchange: tiered hall with gold roofs
    e.box(24, 16, 8, 0, -12, 0, W["lacquer"])
    for k, (w, d, z) in enumerate([(28, 20, 8), (20, 13, 12.5), (13, 8, 16.5)]):
        e.pyramid(w, d, 3.2 - k * 0.3, 0, -12, z, W["gold"])
        if k < 2:
            e.box(w * 0.66, d * 0.62, 3.6, 0, -12, z + 1.0, W["lacquer"])
    for x in (-10, -5, 0, 5, 10):
        e.cyl(0.5, 0.5, 8, x, -3.6, 0, W["lacquer"])
    e.box(18, 0.4, 3, 0, -3.3, 4.5, W["gold"])                        # live Omen price board
    for i in range(9):
        e.box(1.5, 0.2, 1.1, -7.2 + i * 1.8, -3.0, 5.4, "#141018")
        e.box(1.1, 0.15, 0.7, -7.2 + i * 1.8, -2.95, 5.6, "#FF7A2C" if i % 3 else "#00E5FF")
    # plaza with the money toad
    e.box(30, 14, 0.15, 0, 3, 0, W["paper"])
    e.sph(2.0, 0, 3, 1.2, W["jade"], scale=(1.3, 1, 0.7))
    for x, y in ((-1.6, 2), (1.6, 2), (0, 4.6)):
        e.cyl(0.35, 0.4, 0.8, x, y, 0, W["jade"])
    e.cyl(0.7, 0.7, 0.3, 0, 1.0, 2.0, W["gold"], rot=(math.pi / 2, 0, 0))
    # shophouses both banks
    rnd = random.Random(8)
    for side, y0 in ((-1, -30), (1, 34)):
        for i in range(10):
            x = -40 + i * 8.6
            h = rnd.choice([6, 7.5, 9])
            e.box(7.6, 7, h, x, y0, 0, rnd.choice([W["paper"], "#D9CDB0", W["ochre"]]))
            e.pyramid(8.6, 8, 2.2, x, y0, h, rnd.choice([W["jade"], W["lacquer"], "#2E5E4E"]))
            e.box(5, 0.3, 1.4, x, y0 - side * 3.6, 3.0, W["lacquer"] if i % 2 else W["gold"])
    # arched bridge and dragon boats
    for k in range(9):
        a = math.pi * k / 8
        e.box(4, 2.2, 0.5, -24, 18 - 8 * math.cos(a), 1.6 * math.sin(a), W["lacquer"], rx=0)
    for x, y in ((8, 15), (22, 21), (-36, 20)):
        e.box(12, 1.6, 0.8, x, y, 0, W["lacquer"])
        e.sph(0.8, x - 6.5, y, 1.2, W["gold"])
    # lantern strings
    for y in (-2, 8):
        for i in range(18):
            e.sph(0.35, -26 + i * 3.1, y, 6.5 - 0.6 * math.sin(math.pi * i / 17), "#E34234")
    for x, y in ((-6, 6), (5, 7), (11, 0), (-12, 0)):
        e.figure(x, y, "#3A4A3F")
    return e, dict(center=(ox, 0, 0), top=96, iso=110, front=((ox + 11, 14, 1.8), (ox, -10, 6.0), 24), sky="#E9C98A")


def sunyapura(ox):
    e = E("ENV_SUNYAPURA", ox)
    S = {"sand": "#D8A86B", "stone": "#C98F55", "peacock": "#1E7B6F", "saffron": "#F4A300", "indigo": "#3F3D99", "brass": "#B5893B", "white": "#EFE6D2"}
    e.box(100, 100, 0.2, 0, 0, -0.2, "#CDA06A")
    e.box(70, 50, 0.2, 0, 0, 0, S["stone"])
    # Samrat Yantra: the giant sundial (triangular gnomon + quadrants)
    bm = bmesh.new()
    vs = [bm.verts.new(v) for v in [(-1.5, -12, 0), (1.5, -12, 0), (1.5, 12, 0), (-1.5, 12, 0), (-1.5, 12, 22), (1.5, 12, 22)]]
    for f in [(0, 1, 2, 3), (0, 3, 4), (1, 5, 2), (0, 1, 5, 4), (3, 2, 5, 4)]:
        bm.faces.new([vs[i] for i in f])
    e._ob(bm, S["white"], (0, -2, 0))
    for s in (-1, 1):
        e.torus(10, 0.9, s * 6, 0, 2, S["white"], rot=(0, math.pi / 2, 0), arc=0.5)
        e.box(2, 24, 1.5, s * 6, -2, 0, S["white"])
    # Ram Yantra: cylindrical instrument with pillars
    cx, cy = -22, 12
    e.cyl(9, 9, 0.6, cx, cy, 0, S["white"])
    for k in range(16):
        a = 2 * math.pi * k / 16
        e.box(1.2, 1.2, 6, cx + 8.4 * math.cos(a), cy + 8.4 * math.sin(a), 0.6, S["white"], rz=a)
    e.cyl(0.6, 0.6, 8, cx, cy, 0.6, S["brass"])
    # Jai Prakash bowls
    for x in (20, 28):
        e.sph(4, x, 14, 0.4, S["white"], scale=(1, 1, 0.45))
    # the stepwell: an inverted stepped pyramid
    sx, sy = 22, -16
    for k in range(9):
        w = 22 - k * 2.2
        e.box(w, w, 0.5, sx, sy, -k * 0.9, S["stone"] if k % 2 else "#B07A44")
    e.box(3, 3, 0.2, sx, sy, -8.6, "#1E5E66")
    # observatory dial reel (three dials) and houses with chhatris
    e.box(22, 4, 3, 0, 26, 0, S["stone"])                               # the land's reel: three dials on a plinth
    for i in range(3):
        e.cyl(2, 2, 0.4, -6 + i * 6, 26, 5.2, S["brass"], rot=(math.pi / 2, 0, 0))
    rnd = random.Random(3)
    for i in range(12):
        x, y = -44 + (i % 6) * 17, (-38 if i < 6 else 38)
        h = rnd.choice([5, 7, 9])
        e.box(12, 9, h, x, y, 0, rnd.choice(["#E6C79A", "#D9B07A", "#EFE6D2"]))
        e.sph(1.8, x, y, h + 0.6, S["white"], scale=(1, 1, 0.8))
        e.cyl(0.25, 0.25, 1.2, x, y, h + 2.2, S["saffron"])
    for x, y in ((-34, -8), (34, 2), (-30, 30), (38, -30), (-40, -26)):
        e.cyl(0.6, 0.8, 5, x, y, 0, "#6B4226")
        e.sph(4.2, x, y, 7.5, S["peacock"], scale=(1, 1, 0.8))
    for x, y in ((-12, -10), (8, 8), (-30, -16)):
        e.box(5, 3, 0.05, x, y, 0.21, "#9FC4CC")                                  # monsoon puddles
    for x, y in ((-4, -14), (3, -15), (10, -10)):
        e.figure(x, y, S["indigo"])
    return e, dict(center=(ox, 0, 0), top=100, iso=118, front=((ox, -30, 1.8), (ox, 0, 8.0), 22), sky="#9FB7C0")


def kroton(ox):
    e = E("ENV_KROTON", ox)
    K = {"chalk": "#F4F1EA", "aegean": "#1F6FB2", "olive": "#7A8B4A", "bronze": "#8C6A3F", "sky": "#D6E6F2", "shadow": "#2B3440"}
    e.box(120, 120, 0.2, 0, 0, -0.4, K["aegean"])
    # undercity of the fallen, under the sieve
    rnd = random.Random(5)
    for i in range(26):
        a = rnd.uniform(0, 2 * math.pi)
        r = rnd.uniform(8, 24)
        e.box(rnd.uniform(2.5, 4.5), rnd.uniform(2.5, 4.5), rnd.uniform(2, 4), r * math.cos(a), r * math.sin(a), 0, rnd.choice(["#8A7F72", "#B5A642", "#6B5F52", "#4A6E8C"]), rz=a)
    for k in range(12):
        a = 2 * math.pi * k / 12
        e.cyl(1.2, 1.2, 9, 22 * math.cos(a), 22 * math.sin(a), 0, K["chalk"])
    # the Sieve: a white disc on pillars, pierced by holes
    e.cyl(28, 28, 1.2, 0, 0, 9, K["chalk"], seg=64)
    for gx in range(-5, 6):
        for gy in range(-5, 6):
            x, y = gx * 4.4, gy * 4.4
            if 6 < math.hypot(x, y) < 25:
                e.cyl(1.1, 1.1, 0.06, x, y, 10.2, K["shadow"], seg=12)
    # terraces rising to the Archon's temple
    for k, (r, h) in enumerate([(14, 1.5), (10, 1.5), (7, 1.5)]):
        e.cyl(r, r, h, 0, 0, 10.2 + k * h, K["chalk"] if k % 2 == 0 else "#E9E2D0", seg=48)
    tz = 14.7
    e.box(10, 6, 0.8, 0, 0, tz, K["chalk"])
    for x in (-4, -2, 0, 2, 4):
        for y in (-2.4, 2.4):
            e.cyl(0.35, 0.3, 5, x, y, tz + 0.8, K["chalk"])
    e.box(10.4, 6.4, 0.7, 0, 0, tz + 5.8, K["chalk"])
    e.pyramid(10.4, 6.4, 1.6, 0, 0, tz + 6.5, K["bronze"])
    # olive trees, goats, columns reel and the Moirai's cave mouth
    for k in range(10):
        a = 2 * math.pi * k / 10 + 0.3
        x, y = 18 * math.cos(a), 18 * math.sin(a)
        e.cyl(0.25, 0.3, 1.6, x, y, 10.2, "#6B4226")
        e.sph(1.4, x, y, 12.2, K["olive"], scale=(1, 1, 0.7))
    for i in range(3):
        e.cyl(0.6, 0.6, 4, -4 + i * 4, -26, 10.2, K["chalk"])
    e.sph(6, 0, 34, -1, "#5E5A52", scale=(1.6, 1, 1.2))
    e.box(4, 3, 4, 0, 30, 0, "#141018")
    for x, y in ((-3, -12), (2, -13), (6, -10)):
        e.figure(x, y, K["aegean"])
    for ob in list(e.col.objects)[-6:]:
        ob.location.z += 10.2
    return e, dict(center=(ox, 0, 6), top=110, iso=120, front=((ox, -62, 12.0), (ox, 0, 12.0), 26), sky="#D6E6F2")


def crossroads(ox):
    e = E("ENV_CROSSROADS", ox)
    C = {"sand": "#D9A86C", "rust": "#B7410E", "sage": "#9CAF88", "violet": "#5B3E73", "sunset": "#F28C28", "mid": "#1D1A3A", "pink": "#FF2E88", "asphalt": "#3A3640"}
    e.box(130, 130, 0.2, 0, 0, -0.2, C["sand"])
    e.box(130, 9, 0.05, 0, 0, 0, C["asphalt"])
    e.box(9, 130, 0.05, 0, 0, 0, C["asphalt"])
    for k in range(-12, 13):
        if abs(k) > 1:
            e.box(2.2, 0.25, 0.02, k * 5, 0, 0.05, "#F2E8D5")
            e.box(0.25, 2.2, 0.02, 0, k * 5, 0.05, "#F2E8D5")
    e.cyl(0.15, 0.15, 7, 5.5, -5.5, 0, "#2A2530")                    # the one streetlamp
    e.box(1.8, 0.3, 0.3, 4.8, -5.5, 7, "#2A2530")
    e.sph(0.4, 4.0, -5.5, 6.8, "#F2B33D")
    # the House's casino: Lucky Strike
    e.box(34, 18, 12, -26, 24, 0, "#F4F1EA")
    e.box(30, 0.6, 7, -26, 14.7, 12, C["mid"])
    for i in range(3):
        e.box(5.5, 0.8, 4.6, -32 + i * 6, 14.3, 13.1, "#C0392B")
        e.box(3.8, 0.4, 3.2, -32 + i * 6, 13.9, 13.8, "#F4F1EA")
    e.torus(6, 0.5, -26, 14.2, 20.5, C["pink"], rot=(math.pi / 2, 0, 0), arc=0.5)
    e.box(10, 6, 5, -26, 12, 0, "#C0392B")                               # porte-cochère
    # Route 7 motel row
    for i in range(8):
        e.box(5.5, 7, 3.6, 18 + (i % 4) * 6, 18 + (i // 4) * 10, 0, ["#F28C28", "#9CAF88", "#F4F1EA", "#E5B87A"][i % 4])
    e.box(1, 1, 12, 14, 12, 0, "#2A2530")
    e.box(5, 0.5, 2.5, 14, 12, 12, C["pink"])
    # water tower, railway, cacti, mesas
    for s in (-1, 1):
        for t in (-1, 1):
            e.rod((32 + s * 2, -26 + t * 2, 0), (32 + s * 1.2, -26 + t * 1.2, 10), 0.2, "#6B4226")
    e.cyl(3.2, 3.2, 4.5, 32, -26, 10, "#8C6A3F")
    e.pyramid(7, 7, 2, 32, -26, 14.5, "#6B4226")
    for k in range(-26, 27):
        e.box(0.3, 3.4, 0.15, k * 2.4, -40, 0, "#6B4226")
    for s in (-0.8, 0.8):
        e.box(130, 0.15, 0.2, 0, -40 + s, 0.15, "#8E9196")
    rnd = random.Random(11)
    for i in range(18):
        x, y = rnd.uniform(-60, 60), rnd.uniform(-60, 60)
        if abs(x) > 8 and abs(y) > 8 and not (-45 < x < -7 and 10 < y < 38) and not (12 < x < 42 and 12 < y < 36):
            e.cyl(0.5, 0.5, 3, x, y, 0, "#5E7D4A")
            e.rod((x, y, 1.8), (x + 1.3, y, 2.6), 0.35, "#5E7D4A")
    for x, y, w, h in ((-50, -58, 30, 18), (40, -62, 26, 22), (58, 40, 16, 26)):
        e.box(w, 14, h, x, y, 0, C["rust"])
    for x, y in ((-2, -7), (3, -8), (6, -6)):
        e.figure(x, y, C["mid"])
    return e, dict(center=(ox, 0, 0), top=130, iso=140, front=((ox, -55, 2.0), (ox, 10, 7.0), 26), sky="#E9A06A")


def basilica(ox):
    e = E("ENV_BASILICA", ox)
    B = {"brass": "#B5A642", "steel": "#8E9196", "white": "#E8E6E1", "nixie": "#FF7A2C", "ink": "#141018", "floor": "#C9C2B4"}
    e.box(40, 90, 0.2, 0, 0, -0.2, B["floor"])
    for gx in range(-4, 5):
        for gy in range(-20, 21):
            if (gx + gy) % 2 == 0:
                e.box(4, 2, 0.02, gx * 4, gy * 2, 0.0, "#B5AE9E")
    for s in (-1, 1):
        e.box(1.2, 90, 22, s * 20, 0, 0, B["white"])                     # walls (no roof, for the plan view)
        for k in range(10):
            y = -40 + k * 9
            e.cyl(0.9, 0.9, 18, s * 13, y, 0, B["steel"])
            e.cyl(1.3, 1.3, 1.0, s * 13, y, 18, B["brass"])
        land = ["#E34234", "#00A86B", "#F4A300", "#1F6FB2", "#B7410E", "#FF7A2C"]
        for k in range(6):
            e.box(0.3, 6, 9, s * 19.3, -30 + k * 11, 4, land[k])          # every land's ledger on the walls
    e.box(40, 1.2, 26, 0, 45, 0, B["white"])
    e.torus(9, 0.6, 0, 44, 18, B["brass"], rot=(math.pi / 2, 0, 0))     # rose window gear
    for k in range(18):
        a = 2 * math.pi * k / 18
        e.box(1.4, 0.6, 1.4, 9.8 * math.cos(a), 44, 18 + 9.8 * math.sin(a), B["brass"], ry=-a)
    # the Even Hand engine: a brass fist around Hap's eye
    e.cyl(7, 8, 2, 0, 30, 0, B["brass"])
    e.sph(5.2, 0, 30, 8, B["brass"], scale=(1.1, 0.9, 1.0))
    for k in range(4):
        e.rod((-3.6 + k * 2.4, 27, 11.5), (-3.6 + k * 2.4, 25.4, 7), 1.1, B["brass"])
    e.rod((5, 28, 6), (3.6, 25.2, 9.5), 1.2, B["brass"])
    e.sph(1.6, 0, 25.2, 9, B["nixie"])
    for s in (-1, 1):
        e.box(2, 30, 0.8, s * 4, -10, 0, "#9E2B25")                         # the processional carpets
    for k in range(6):
        e.box(5, 1, 1.2, -7, -30 + k * 6, 0, "#6B5F52")
        e.box(5, 1, 1.2, 7, -30 + k * 6, 0, "#6B5F52")
    for x, y in ((-2, -20), (1, -21), (4, -19)):
        e.figure(x, y, B["ink"])
    e.figure(0, 20, B["white"], h=1.9)
    return e, dict(center=(ox, 0, 0), top=96, iso=110, front=((ox, -44, 1.8), (ox, 30, 9.0), 24), sky="#2A2530")


def meridian_context():
    """The Undercity around the Wards street (x = 600, y 0..160) and the plateau of the Upper City and the Basilica (y = 220)."""
    e = E("ENV_MERIDIAN_CTX", 0)
    rnd = random.Random(21)
    e.box(320, 340, 0.2, 600, 110, -0.4, "#4F555A")
    pal = ['#8C8273', '#7A7F80', '#9A8A6E', '#6F7774', '#A08F78', '#857A6A']
    for gx in range(-12, 13):
        for gy in range(-3, 15):
            x, y = 600 + gx * 11, gy * 11
            if abs(x - 600) < 16 or (535 < x < 575 and 45 < y < 80) or (630 < x < 650):
                continue
            if math.hypot(x - 600, y - 225) < 75:
                continue
            h = rnd.choice([8, 12, 16, 20, 26])
            e.box(9.5, 9.5, h, x, y, 0, rnd.choice(pal))
            if rnd.random() < 0.35:
                e.box(6, 6, 0.6, x, y, h, rnd.choice(['#5F7A4A', '#6E8A52']))          # roof gardens
            if rnd.random() < 0.25:
                e.box(4, 0.4, 2, x, y - 4.9, h * 0.6, rnd.choice(['#FF7A2C', '#FF2E88', '#2EC4D6', '#F5E400']))
    e.box(12, 300, 0.3, 640, 100, -0.1, "#3B5560")                                     # the drain canal
    e.box(38, 34, 0.15, 555, 62, 0, "#6B5F52")                                         # the Charm Bazaar square
    for i in range(16):
        x, y = 543 + (i % 4) * 8, 50 + (i // 4) * 8
        e.box(5, 4, 2.4, x, y, 0, rnd.choice(['#FF2E88', '#F5E400', '#2EC4D6', '#3BB273', '#D9822B']))
        e.box(6, 5, 0.3, x, y, 2.4, '#F2E8D5')
    e.cyl(72, 76, 24, 600, 230, 0, "#B9B2A4", seg=64)                                 # the plateau
    e.torus(70, 1.8, 600, 230, 24, "#8E9196")                                           # the Basilica Ring wall
    for k in range(24):
        a = 2 * math.pi * k / 24
        r = rnd.uniform(30, 62)
        e.box(10, 10, rnd.choice([10, 14, 18]), 600 + r * math.cos(a), 230 + r * math.sin(a), 24, rnd.choice(['#E8E6E1', '#D9D4CC', '#C9C2B4']))
    for k in range(5):                                                                  # stairs and lifts up the cliff
        e.box(4, 14, 24, 560 + k * 20, 160, 0, "#9C9486")
    return e


# ---------------------------------------------------------------- imported lands (from the 3D Jutsu project)
def import_project(path):
    found = {}
    with bpy.data.libraries.load(path, link=False) as (src, dst):
        dst.collections = [n for n in src.collections if n in ("WARDS", "PIER")]
    for c in dst.collections:
        bpy.context.scene.collection.children.link(c)
        c.hide_render = False
        for o in c.all_objects:
            if o is not None:
                o.hide_render = o.hide_viewport = False
        found[c.name] = c
    return found


def colour_wards(col):
    rnd = random.Random(7)
    W = {'bld': ['#8C8273', '#7A7F80', '#9A8A6E', '#6F7774', '#A08F78', '#857A6A'], 'win': ['#F2C27A', '#E8B46A', '#3A3F48', '#3A3F48', '#F5D59A'],
         'balc': ['#5E5348', '#6B5F52'], 'plant': ['#5F7A4A', '#6E8A52', '#4E6B3F'], 'pipe': ['#8A5A3A', '#7A4E34'], 'cable': ['#2A2630'],
         'cloth': ['#C9BFAE', '#B3261E', '#5E7C8C', '#D8CBA8', '#8C6E8F', '#E2D6BC'], 'sign': ['#FF7A2C', '#E0E0D0', '#FF2E88', '#2EC4D6', '#F5E400', '#D9CDB7'],
         'bridge': ['#6B5A44'], 'ground': ['#5A6066']}
    for o in col.all_objects:
        if o.type != 'MESH':
            continue
        n = o.name
        if n.startswith('WARDS_basilica'):
            o.color = lin('#FFB347' if 'eye' in n else '#B08A4A')
        else:
            pal = W.get(n.split('_')[1])
            if pal:
                o.color = lin(rnd.choice(pal))


def colour_pier(col):
    for o in col.all_objects:
        if o.type != 'MESH':
            continue
        d, z, y, n = o.dimensions, o.matrix_world.translation.z, o.matrix_world.translation.y, o.name
        if n.startswith('Sphere'):
            o.color = lin('#F4E6B8' if (max(d) > 20 and y > 150) else '#26324F')
        elif n.startswith('Cylinder'):
            o.color = lin('#D2452B' if d.z > 4 else '#FFC864')
        elif d.x > 60 or d.y > 60:
            o.color = lin('#1C2848')
        elif z > 5:
            o.color = lin('#D2452B')
        elif d.x > 15 and d.z < 1.0:
            o.color = lin('#6E2B22')
        elif d.z < 1.6 and z > 0.5:
            o.color = lin('#B33A27')
        else:
            o.color = lin('#7D8597')


def bounds(col, zmin=-1e9):
    pts = [o.matrix_world @ Vector(c) for o in col.all_objects if o.type == 'MESH' for c in o.bound_box]
    pts = [p for p in pts if p.z > zmin]
    lo = Vector((min(p.x for p in pts), min(p.y for p in pts), min(p.z for p in pts)))
    hi = Vector((max(p.x for p in pts), max(p.y for p in pts), max(p.z for p in pts)))
    return lo, hi


# ---------------------------------------------------------------- render
def setup(sc):
    sc.render.engine = 'BLENDER_WORKBENCH'
    s = sc.display.shading
    s.light, s.color_type = 'STUDIO', 'OBJECT'
    s.show_cavity, s.cavity_type = True, 'BOTH'
    s.show_object_outline, s.object_outline_color = True, (0.08, 0.06, 0.09)
    s.show_shadows, s.shadow_intensity = True, 0.4
    s.show_specular_highlight = False
    sc.display.render_aa = '8'
    sc.view_settings.view_transform = 'Standard'
    sc.render.resolution_x, sc.render.resolution_y = 1600, 900
    sc.render.image_settings.file_format = 'PNG'
    if sc.world is None:
        sc.world = bpy.data.worlds.new("w")


def solo(sc, keep):
    for c in sc.collection.children:
        c.hide_render = c.name not in keep


def render(sc, cam, name):
    sc.camera = cam
    sc.render.filepath = os.path.join(OUT, name)
    bpy.ops.render.render(write_still=True)


def cameras(sc, info, key):
    cx, cy, cz = info["center"]
    out = []
    top = bpy.data.objects.new(f"CAM_{key}_top", bpy.data.cameras.new(f"CAM_{key}_top"))
    top.data.type, top.data.ortho_scale = 'ORTHO', info["top"]
    top.location, top.rotation_euler = (cx, cy, 400), (0, 0, info.get("top_rot", 0.0))
    top.data.clip_end = 1000
    iso = bpy.data.objects.new(f"CAM_{key}_iso", bpy.data.cameras.new(f"CAM_{key}_iso"))
    iso.data.type, iso.data.ortho_scale = 'ORTHO', info["iso"]
    iso.rotation_euler = Euler((math.radians(57), 0, math.radians(-38)))
    d = iso.rotation_euler.to_matrix() @ Vector((0, 0, -1))
    iso.location = Vector((cx, cy, cz)) - d * 300
    iso.data.clip_end = 1000
    fr = bpy.data.objects.new(f"CAM_{key}_front", bpy.data.cameras.new(f"CAM_{key}_front"))
    loc, look, lens = info["front"]
    fr.location = loc
    fr.rotation_euler = (Vector(look) - Vector(loc)).to_track_quat('-Z', 'Y').to_euler()
    fr.data.lens, fr.data.clip_end = lens, 2000
    for c in (top, iso, fr):
        sc.collection.objects.link(c)
    return [("top", top), ("iso", iso), ("front", fr)]


def main():
    os.makedirs(OUT, exist_ok=True)
    blend = next((a for a in sys.argv[1:] if a.endswith(".blend")), None)
    bpy.ops.wm.read_factory_settings(use_empty=True)
    sc = bpy.context.scene
    setup(sc)
    lands = {}
    if blend and os.path.exists(blend):
        got = import_project(blend)
        if "WARDS" in got:
            colour_wards(got["WARDS"])
            # the Wards: an 18 m canyon street running 160 m along +Y, the Basilica at y = 220
            ctx = meridian_context()
            lands["meridian"] = (("WARDS", ctx.col.name), dict(center=(600, 110, 20), top=330, top_rot=math.pi / 2, iso=300,
                                               front=((600, -2, 1.7), (600, 60, 9.0), 18), sky="#A9B3B8"))
        if "PIER" in got:
            colour_pier(got["PIER"])
            lands["hyakki"] = ("PIER", dict(center=(1200, 2, 0), top=48, iso=56, front=((1200, -17, 3.2), (1200, 6, 4.2), 30), sky="#1E2A4A"))
    for key, fn, x in (("river", river, 5000), ("sunyapura", sunyapura, 5300), ("kroton", kroton, 5600), ("crossroads", crossroads, 5900), ("basilica", basilica, 6200)):
        e, info = fn(x)
        lands[key] = (e.col.name, info)
    for key, (colname, info) in lands.items():
        names = set(colname) if isinstance(colname, tuple) else {colname}
        solo(sc, names)
        colname = colname[0] if isinstance(colname, tuple) else colname
        sc.world.color = lin(info["sky"])[:3]
        sea = [o for o in bpy.data.collections[colname].all_objects if o.type == 'MESH' and max(o.dimensions) > 300] if key == "hyakki" else []
        for view, cam in cameras(sc, info, key):
            sc.world.color = lin("#EFE6D2" if view != "front" else info["sky"])[:3]
            for o in sea:  # plan views use a lighter "map" sea so the pier reads
                o.color = lin("#4A6EA8" if view != "front" else "#1C2848")
            render(sc, cam, f"{key}_{view}.png")
        print("rendered", key)
    for c in sc.collection.children:
        c.hide_render = False
    bpy.ops.wm.save_as_mainfile(filepath=os.path.join(OUT, "zso_envs_blockout.blend"), compress=True)


if __name__ == "__main__":
    main()
