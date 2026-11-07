# ZERO-SUM: OMEN — Blender blockout builder for the whole cast (run inside Blender / Higgsfield 3D Jutsu).
# Builds one collection per character from tools/cast.py `look` data (paste the JSON from `python3 tools/blender_cast_json.py`
# into CAST_JSON), excluded from render, then lays out turnaround sheets: 6 characters per sheet, 4 views per row
# (FRONT, LEFT, RIGHT, BACK) as rotated collection instances at one shared scale (1 m = 200 px in the sheet renders).
# Characters face -Y; feet at z = 0. Colours are object colours for Workbench flat rendering.
import bpy, bmesh, math, json
from mathutils import Vector

CAST_JSON = "__CAST_JSON__"
CAST = json.loads(CAST_JSON)
INK = "#141018"


def lin(h):
    h = h.lstrip('#')
    c = [int(h[i:i + 2], 16) / 255 for i in (0, 2, 4)]
    f = lambda v: v / 12.92 if v <= 0.04045 else ((v + 0.055) / 1.055) ** 2.4
    return (f(c[0]), f(c[1]), f(c[2]), 1.0)


def coll(name, parent):
    c = bpy.data.collections.get(name)
    if c is None:
        c = bpy.data.collections.new(name)
        parent.children.link(c)
    return c


class B:
    def __init__(self, col):
        self.col = col
        self.n = 0

    def _ob(self, bm, color, loc, rot=(0, 0, 0), scale=(1, 1, 1)):
        self.n += 1
        name = f"{self.col.name}_{self.n:03d}"
        me = bpy.data.meshes.new(name)
        bm.to_mesh(me)
        bm.free()
        ob = bpy.data.objects.new(name, me)
        self.col.objects.link(ob)
        ob.location, ob.rotation_euler, ob.scale = loc, rot, scale
        ob.color = lin(color)
        return ob

    def cyl(self, r1, r2, z0, z1, color, x=0, y=0, sx=1, sy=1, seg=20):
        bm = bmesh.new()
        bmesh.ops.create_cone(bm, cap_ends=True, cap_tris=False, segments=seg, radius1=max(r1, 1e-4), radius2=max(r2, 1e-4), depth=max(z1 - z0, 1e-3))
        return self._ob(bm, color, (x, y, (z0 + z1) / 2), scale=(sx, sy, 1))

    def rod(self, p0, p1, r, color, r2=None, seg=12):
        p0, p1 = Vector(p0), Vector(p1)
        d = p1 - p0
        bm = bmesh.new()
        bmesh.ops.create_cone(bm, cap_ends=True, cap_tris=False, segments=seg, radius1=r, radius2=r if r2 is None else max(r2, 1e-4), depth=max(d.length, 1e-3))
        rot = Vector((0, 0, 1)).rotation_difference(d.normalized()).to_euler()
        return self._ob(bm, color, tuple((p0 + p1) / 2), rot)

    def sph(self, r, loc, color, scale=(1, 1, 1), seg=20):
        bm = bmesh.new()
        bmesh.ops.create_uvsphere(bm, u_segments=seg, v_segments=max(8, seg // 2), radius=r)
        return self._ob(bm, color, loc, scale=scale)

    def box(self, size, loc, color, rot=(0, 0, 0)):
        bm = bmesh.new()
        bmesh.ops.create_cube(bm, size=1.0)
        return self._ob(bm, color, loc, rot, size)

    def torus(self, R, r, loc, color, rot=(0, 0, 0), seg=28, rs=8, arc=1.0):
        bm = bmesh.new()
        rings = []
        n = seg if arc >= 1 else int(seg * arc) + 1
        for i in range(n):
            a = 2 * math.pi * arc * i / seg
            ring = []
            for j in range(rs):
                b = 2 * math.pi * j / rs
                ring.append(bm.verts.new(((R + r * math.cos(b)) * math.cos(a), (R + r * math.cos(b)) * math.sin(a), r * math.sin(b))))
            rings.append(ring)
        last = n if arc >= 1 else n - 1
        for i in range(last):
            a, b2 = rings[i], rings[(i + 1) % n]
            for j in range(rs):
                bm.faces.new((a[j], a[(j + 1) % rs], b2[(j + 1) % rs], b2[j]))
        return self._ob(bm, color, loc, rot)

    def text(self, s, loc, size, color):
        self.n += 1
        cu = bpy.data.curves.new(f"{self.col.name}_t{self.n}", 'FONT')
        cu.body, cu.size, cu.align_x, cu.align_y, cu.extrude = s, size, 'CENTER', 'CENTER', 0.01
        ob = bpy.data.objects.new(cu.name, cu)
        self.col.objects.link(ob)
        ob.location, ob.rotation_euler = loc, (math.pi / 2, 0, 0)
        ob.color = lin(color)
        return ob


# ---------------------------------------------------------------- body
def human(b, c, ox=0.0, oy=0.0, H=None, W=None, head="human", noprops=False):
    L = c["look"]
    H = H or c["h"]
    W = W or c["w"]
    skin, eyes = c.get("skin", "#E0C0A0"), c.get("eyes", INK)
    hr = H * 0.066
    hz = H - hr
    sh, hip = H * 0.81, H * 0.52
    top = L.get("top") or ["tunic", "#888888", 0.3, 1.0]
    ttype, tcol, tlen, flare = top
    inner = L.get("inner", tcol)
    legs, shoes = L.get("legs", "#333333"), L.get("shoes", "#222222")
    belt = L.get("belt")
    A = dict(H=H, W=W, hr=hr, hz=hz, sh=sh, hip=hip, ox=ox, oy=oy,
             RH=(ox - W * 0.58, oy - 0.02, H * 0.52), LH=(ox + W * 0.58, oy - 0.02, H * 0.52))
    # legs and shoes
    for s in (-1, 1):
        b.cyl(W * 0.105, W * 0.15, 0.07, hip + 0.02, legs, x=ox + s * W * 0.19, y=oy)
        b.box((W * 0.2, W * 0.44, 0.09), (ox + s * W * 0.19, oy - W * 0.1, 0.045), shoes)
    # torso
    torso_col = inner if ttype in ("vest",) else tcol
    b.cyl(W * 0.37, W * 0.5, hip - 0.03, sh + 0.01, torso_col, x=ox, y=oy, sy=0.56)
    if ttype in ("coat", "jacket", "suit", "vest", "apron_dress") or inner != tcol:
        b.box((W * 0.16, 0.02, sh - hip - 0.05), (ox, oy - W * 0.29, (sh + hip) / 2 + 0.01), inner)
    # skirts / coat lengths
    zb = hip - tlen * (hip - 0.06)
    if tlen > 0.05:
        if ttype == "poncho":
            b.cyl(W * 0.62 * flare, W * 0.34, zb, sh + 0.06, tcol, x=ox, y=oy, sy=0.62)
        elif ttype == "apron_dress":
            b.cyl(W * 0.4 * flare, W * 0.37, zb, hip + 0.02, tcol, x=ox, y=oy, sy=0.6)
            b.box((W * 0.5, 0.025, sh - zb - 0.12), (ox, oy - W * 0.36, (sh - 0.1 + zb) / 2), tcol)
        else:
            b.cyl(W * 0.38 * flare, W * 0.37, zb, hip + 0.02, tcol, x=ox, y=oy, sy=0.6)
    tails = L.get("tails")
    if tails:
        for s, tl in ((1, tails[0]), (-1, tails[1])):  # s=+1 is the character's LEFT (+X)
            zt = hip - tl * (hip - 0.06)
            b.box((W * 0.32, 0.025, hip - zt), (ox + s * W * 0.17, oy + W * 0.25, (hip + zt) / 2), tcol, rot=(-0.12, 0, 0))
    if ttype in ("coat", "jacket"):
        b.cyl(W * 0.2, W * 0.17, sh - 0.02, sh + hr * 0.95, tcol, x=ox, y=oy + 0.01, sy=0.9)
    if ttype == "armor":
        for s in (-1, 1):
            b.sph(W * 0.17, (ox + s * W * 0.5, oy, sh - 0.02), belt or tcol, scale=(1, 1, 0.75))
    if belt:
        b.torus(W * 0.37, 0.018, (ox, oy, hip + 0.03), belt).scale = (1, 0.58, 1)
    # arms (sleeves in the garment colour)
    sleeve = tcol if ttype not in ("vest", "apron_dress") else (inner if ttype == "apron_dress" else skin)
    for s, hand in ((-1, A["RH"]), (1, A["LH"])):
        b.rod((ox + s * W * 0.47, oy, sh - 0.04), hand, W * 0.11, sleeve, r2=W * 0.09)
        b.sph(W * 0.09, hand, skin)
        if ttype == "kimono":
            b.box((W * 0.2, W * 0.32, H * 0.2), (ox + s * W * 0.6, oy + 0.02, H * 0.6), tcol)
    # neck and head
    b.cyl(hr * 0.42, hr * 0.4, sh - 0.02, hz - hr * 0.6, skin, x=ox, y=oy)
    if head == "human":
        b.sph(hr, (ox, oy, hz), skin)
        bm = bmesh.new()
        bmesh.ops.create_cone(bm, cap_ends=True, cap_tris=False, segments=8, radius1=hr * 0.13, radius2=1e-4, depth=hr * 0.28)
        b._ob(bm, skin, (ox, oy - hr * 1.02, hz - hr * 0.08), (math.pi / 2, 0, 0))
        for s in (-1, 1):
            b.sph(hr * 0.13, (ox + s * hr * 0.36, oy - hr * 0.86, hz + hr * 0.1), eyes, scale=(1, 0.5, 1))
            b.sph(hr * 0.2, (ox + s * hr * 0.98, oy + hr * 0.05, hz), skin, scale=(0.5, 1, 1))
    elif head == "ox":
        b.sph(hr * 1.25, (ox, oy, hz), skin, scale=(1, 1.1, 1))
        b.box((hr * 1.3, hr * 1.1, hr * 0.9), (ox, oy - hr * 1.25, hz - hr * 0.4), "#8C6A3F")
        for s in (-1, 1):
            b.rod((ox + s * hr, oy, hz + hr * 0.6), (ox + s * hr * 2.6, oy, hz + hr * 1.6), hr * 0.22, "#E3DCCB", r2=0.004)
            b.sph(hr * 0.15, (ox + s * hr * 0.5, oy - hr * 1.1, hz + hr * 0.25), eyes)
    elif head == "horse":
        b.sph(hr * 1.1, (ox, oy, hz), skin)
        b.rod((ox, oy - hr * 0.4, hz), (ox, oy - hr * 2.2, hz - hr * 0.7), hr * 0.65, skin, r2=hr * 0.5)
        b.box((hr * 0.5, hr * 1.6, hr * 2.2), (ox, oy + hr * 0.8, hz - hr * 0.6), INK)
        for s in (-1, 1):
            b.rod((ox + s * hr * 0.5, oy, hz + hr * 0.8), (ox + s * hr * 0.6, oy, hz + hr * 1.7), hr * 0.18, skin, r2=0.004)
            b.sph(hr * 0.15, (ox + s * hr * 0.55, oy - hr * 0.95, hz + hr * 0.2), eyes)
    elif head == "kappa":
        b.sph(hr * 1.2, (ox, oy, hz), skin)
        bm = bmesh.new()
        bmesh.ops.create_cone(bm, cap_ends=True, cap_tris=False, segments=8, radius1=hr * 0.45, radius2=1e-4, depth=hr * 0.7)
        b._ob(bm, "#E8C547", (ox, oy - hr * 1.35, hz - hr * 0.2), (math.pi / 2, 0, 0))
        for s in (-1, 1):
            b.sph(hr * 0.2, (ox + s * hr * 0.45, oy - hr * 1.0, hz + hr * 0.2), eyes, scale=(1, 0.5, 1))
    if head == "human":
        hair(b, L.get("hair"), A, c)
        hat(b, L.get("hat"), A, c)
    elif head == "kappa":
        hat(b, L.get("hat"), A, c)
    if not noprops:
        for p in L.get("props", []):
            prop(b, p, A, c)
    return A


def hair(b, h, A, c):
    if not h:
        return
    style, col = h[0], h[1]
    acc = h[2] if len(h) > 2 else None
    ox, oy, hz, hr, H, W, sh, hip = A["ox"], A["oy"], A["hz"], A["hr"], A["H"], A["W"], A["sh"], A["hip"]
    if style in ("bald", "kerchief_hair"):
        return
    b.sph(hr * 1.06, (ox, oy + hr * 0.25, hz + hr * 0.3), col, scale=(1, 1, 0.95 if style != "slick" else 0.85))
    if style == "messy":
        for k in range(8):
            a = math.radians(-40 + k * 30)
            p0 = (ox + hr * 0.6 * math.sin(a), oy + hr * 0.5 * math.cos(a), hz + hr * 0.9)
            p1 = (ox + hr * 1.5 * math.sin(a), oy + hr * 1.2 * math.cos(a), hz + hr * (1.0 + 0.4 * math.cos(a)))
            b.rod(p0, p1, hr * 0.3, col, r2=0.004)
        b.rod((ox - hr * 0.6, oy - hr * 0.7, hz + hr * 0.8), (ox - hr * 0.9, oy - hr * 0.95, hz + hr * 0.1), hr * 0.18, col, r2=0.004)
        if acc:
            b.rod((ox + hr * 0.2, oy - hr * 0.75, hz + hr * 1.0), (ox + hr * 0.55, oy - hr * 0.95, hz + hr * 0.2), hr * 0.14, acc, r2=0.004)
    elif style == "spiky":
        for k in range(8):
            a = 2 * math.pi * k / 8
            b.rod((ox + hr * 0.5 * math.cos(a), oy + hr * 0.3 + hr * 0.5 * math.sin(a), hz + hr * 0.9),
                  (ox + hr * 0.9 * math.cos(a), oy + hr * 0.3 + hr * 0.9 * math.sin(a), hz + hr * 1.8), hr * 0.25, col, r2=0.004)
    elif style == "bob":
        for s in (-1, 1):
            b.sph(hr * 0.55, (ox + s * hr * 0.82, oy + hr * 0.1, hz - hr * 0.3), col, scale=(0.7, 1, 1.2))
        b.sph(hr * 0.9, (ox, oy + hr * 0.6, hz - hr * 0.2), col)
    elif style in ("long", "long_white"):
        ln = H * (0.26 if style == "long" else 0.4)
        b.box((hr * 1.9, hr * 0.55, ln), (ox, oy + hr * 0.75, hz - ln / 2), col)
    elif style in ("braid_l", "braid_r", "three_braids", "twin", "ponytail"):
        sides = {"braid_l": [1], "braid_r": [-1], "three_braids": [-1, 1], "twin": [-1, 1], "ponytail": []}[style]
        for s in sides:
            for k in range(6):
                t = k / 5
                p = (ox + s * (hr * 0.8 + W * 0.05 * t), oy + hr * 0.4 - (hr * 1.0 + W * 0.18) * t, hz - hr * 0.4 - (hz - hr - (sh + 0.04) + H * 0.12) * t)
                b.sph(hr * (0.28 - 0.07 * t), p, col)
            if acc:
                b.sph(hr * 0.15, (ox + s * (hr * 0.8 + W * 0.05), oy + hr * 0.4 - (hr * 1.0 + W * 0.18), sh - H * 0.08), acc)
        if style == "three_braids":
            for k in range(4):
                b.sph(hr * (0.26 - 0.04 * k), (ox, oy + hr * 0.6, hz + hr * (1.2 + 0.35 * k)), col)
        if style == "ponytail":
            b.rod((ox, oy + hr * 0.9, hz + hr * 0.5), (ox, oy + hr * 1.3, sh - 0.05), hr * 0.3, col, r2=hr * 0.1)
    elif style == "bun":
        b.sph(hr * 0.5, (ox, oy + hr * 0.75, hz + hr * 0.95), col)
        if acc:
            for k in range(8):
                a = 2 * math.pi * k / 8
                b.sph(hr * 0.1, (ox + hr * 0.55 * math.cos(a), oy + hr * 0.75 + hr * 0.2 * math.sin(a), hz + hr * 0.95 + hr * 0.4 * math.sin(a)), acc)
    elif style == "curly":
        for k in range(10):
            a = math.radians(-30 + k * 26)
            b.sph(hr * 0.36, (ox + hr * 1.0 * math.sin(a), oy + hr * 0.2 + hr * 0.95 * math.cos(a), hz + hr * (0.35 + 0.25 * math.cos(a * 2))), col)
    elif style == "topknot":
        b.sph(hr * 0.35, (ox, oy + hr * 0.2, hz + hr * 1.35), col)


def hat(b, h, A, c):
    if not h:
        return
    t, col = h
    ox, oy, hz, hr, H, W, sh = A["ox"], A["oy"], A["hz"], A["hr"], A["H"], A["W"], A["sh"]
    top = hz + hr * 0.75
    if t in ("wide_brim", "cowboy"):
        b.cyl(hr * (2.7 if t == "wide_brim" else 2.2), hr * (2.7 if t == "wide_brim" else 2.2), top - 0.01, top + 0.012, col, x=ox, y=oy + hr * 0.1)
        b.cyl(hr * 0.98, hr * 0.8, top, top + hr * (1.0 if t == "wide_brim" else 0.85), col, x=ox, y=oy + hr * 0.1)
        if t == "wide_brim":
            b.box((hr * 0.35, 0.01, hr * 0.5), (ox + hr * 0.6, oy - hr * 0.75, top + hr * 0.45), "#F4F1EA")
    elif t == "cap":
        b.sph(hr * 1.05, (ox, oy + hr * 0.1, hz + hr * 0.35), col, scale=(1, 1, 0.75))
        b.box((hr * 1.4, hr * 1.1, 0.012), (ox + hr * 0.5, oy - hr * 0.9, hz + hr * 0.55), col, rot=(0, 0, 0.5))
    elif t == "peaked":
        b.cyl(hr * 1.02, hr * 1.12, hz + hr * 0.45, hz + hr * 1.1, col, x=ox, y=oy + hr * 0.1)
        b.box((hr * 1.6, hr * 0.9, 0.015), (ox, oy - hr * 0.95, hz + hr * 0.48), INK)
    elif t == "hood":
        b.sph(hr * 1.32, (ox, oy + hr * 0.5, hz + hr * 0.12), col)
    elif t in ("mask_hound", "mask_up"):
        up = t == "mask_up" or c["key"] == "varro_ally"
        z = hz + (hr * 1.1 if up else 0)
        b.sph(hr * 1.1, (ox, oy - hr * 0.05, z), col, scale=(1, 1.1, 1.05))
        b.box((hr * 0.95, hr * 1.2, hr * 0.7), (ox, oy - hr * 1.15, z - hr * 0.35), col)
        for s in (-1, 1):
            b.sph(hr * 0.22, (ox + s * hr * 0.4, oy - hr * 1.0, z + hr * 0.15), "#FF7A2C" if not up else INK)
            b.rod((ox + s * hr * 0.7, oy, z + hr * 0.7), (ox + s * hr * 1.0, oy + hr * 0.2, z + hr * 1.4), hr * 0.18, col, r2=0.004)
    elif t == "fox_ears":
        for s in (-1, 1):
            b.rod((ox + s * hr * 0.55, oy + hr * 0.1, hz + hr * 0.75), (ox + s * hr * 0.9, oy + hr * 0.1, hz + hr * 1.75), hr * 0.32, col, r2=0.004)
    elif t == "crown":
        b.cyl(hr * 0.95, hr * 1.0, hz + hr * 0.55, hz + hr * 0.95, col, x=ox, y=oy + hr * 0.1)
        for k in range(7):
            a = 2 * math.pi * k / 7
            b.rod((ox + hr * 0.9 * math.cos(a), oy + hr * 0.1 + hr * 0.9 * math.sin(a), hz + hr * 0.95),
                  (ox + hr * 0.9 * math.cos(a), oy + hr * 0.1 + hr * 0.9 * math.sin(a), hz + hr * 1.5), hr * 0.15, col, r2=0.004)
    elif t == "laurel":
        b.torus(hr * 1.02, hr * 0.12, (ox, oy + hr * 0.1, hz + hr * 0.5), col, rot=(0.15, 0, 0), arc=0.8)
        for k in range(10):
            a = math.radians(110 + k * 32)
            b.sph(hr * 0.16, (ox + hr * 1.05 * math.cos(a), oy + hr * 0.1 - hr * 1.05 * math.sin(a), hz + hr * 0.55), col, scale=(1.6, 1, 0.6))
    elif t == "straw":
        bm = bmesh.new()
        bmesh.ops.create_cone(bm, cap_ends=True, cap_tris=False, segments=24, radius1=hr * 2.6, radius2=1e-4, depth=hr * 0.9)
        b._ob(bm, col, (ox, oy, hz + hr * 0.95))
    elif t == "water_dish":
        b.cyl(hr * 0.7, hr * 0.8, hz + hr * 0.95, hz + hr * 1.12, "#E9E2D0", x=ox, y=oy)
        b.cyl(hr * 0.62, hr * 0.62, hz + hr * 1.1, hz + hr * 1.14, col, x=ox, y=oy)
    elif t == "headset":
        b.torus(hr * 1.12, hr * 0.06, (ox, oy, hz + hr * 0.1), col, rot=(0, math.pi / 2, 0), arc=0.5)
        b.rod((ox - hr * 1.1, oy, hz), (ox - hr * 0.6, oy - hr * 0.9, hz - hr * 0.5), hr * 0.06, col)
    elif t == "mitre":
        b.cyl(hr * 0.9, hr * 0.5, hz + hr * 0.6, hz + hr * 2.3, col, x=ox, y=oy + hr * 0.1, sy=0.75)
        b.torus(hr * 0.42, hr * 0.08, (ox, oy - hr * 0.4, hz + hr * 2.1), "#B5A642", rot=(math.pi / 2, 0, 0))
    elif t == "veil":
        b.sph(hr * 1.18, (ox, oy + hr * 0.35, hz + hr * 0.2), col)
        b.box((hr * 2.1, hr * 0.4, H * 0.25), (ox, oy + hr * 0.9, hz - H * 0.1), col)
    elif t == "kerchief":
        b.sph(hr * 1.12, (ox, oy + hr * 0.3, hz + hr * 0.35), col, scale=(1, 1, 0.9))
        b.sph(hr * 0.4, (ox, oy + hr * 1.1, hz + hr * 0.5), col)
    elif t == "topknot":
        b.box((hr * 1.2, hr * 1.0, hr * 0.5), (ox, oy + hr * 0.1, hz + hr * 1.05), col)


def prop(b, p, A, c):
    t, col = p[0], p[1]
    ox, oy, hz, hr, H, W, sh, hip = A["ox"], A["oy"], A["hz"], A["hr"], A["H"], A["W"], A["sh"], A["hip"]
    RH, LH = A["RH"], A["LH"]
    if t == "decoder":
        b.torus(W * 0.11, 0.022, (RH[0], RH[1], RH[2] + 0.07), col)
        for k in range(3):
            b.sph(0.016, (RH[0] - 0.05 + 0.05 * k, RH[1] - 0.06, RH[2] + 0.2 + 0.06 * k), col)
    elif t in ("halo_nan", "halo_digit", "halo_digits"):
        s = {"halo_nan": "NaN", "halo_digit": "7", "halo_digits": "2 3 5 7"}[t]
        b.torus(hr * 1.2, hr * 0.07, (ox, oy, hz + hr * 1.7), col, arc=0.85 if t == "halo_nan" else 1.0)
        b.text(s, (ox, oy - hr * 0.2, hz + hr * 2.35), hr * 0.9, col)
    elif t == "satchel":
        b.box((W * 0.3, W * 0.14, W * 0.3), (ox + W * 0.45, oy, hip + 0.02), col)
        b.rod((ox - W * 0.35, oy - W * 0.29, sh), (ox + W * 0.45, oy - W * 0.1, hip + 0.1), 0.012, col)
    elif t == "lantern":
        b.cyl(0.08, 0.08, LH[2] - 0.22, LH[2] - 0.06, col, x=LH[0], y=LH[1] - 0.05)
        b.rod((LH[0], LH[1] - 0.05, LH[2] - 0.06), LH, 0.008, INK)
    elif t == "mask_fox_side":
        b.sph(hr * 0.6, (ox + hr * 0.95, oy - hr * 0.2, hz + hr * 0.15), col, scale=(0.35, 1, 1.15))
        for s in (-1, 1):
            b.rod((ox + hr * 1.1, oy - hr * 0.2 + s * hr * 0.3, hz + hr * 0.7), (ox + hr * 1.12, oy - hr * 0.2 + s * hr * 0.4, hz + hr * 1.1), hr * 0.12, col, r2=0.003)
        b.sph(hr * 0.1, (ox + hr * 1.18, oy - hr * 0.4, hz + hr * 0.3), "#E34234")
    elif t == "revolver":
        b.box((0.045, 0.3, 0.06), (RH[0], RH[1] - 0.14, RH[2] + 0.02), col)
        ob = b.cyl(0.045, 0.045, -0.035, 0.035, "#B5A642", x=RH[0], y=RH[1] - 0.06)
        ob.location.z = RH[2] + 0.04
        ob.rotation_euler = (math.pi / 2, 0, 0)
    elif t == "cards":
        for k in range(7):
            a = math.radians(-60 + k * 25)
            r = 0.22 + 0.04 * k
            b.box((0.07, 0.005, 0.1), (LH[0] + r * math.cos(a) * 0.6, LH[1] - 0.1, LH[2] + 0.15 + r * math.sin(a)), col, rot=(0, a, 0))
    elif t == "hammer":
        top = (ox + W * 0.42, oy + 0.08, sh + 0.28)
        b.rod(LH, top, 0.02, "#6B4226")
        b.box((0.2, 0.12, 0.12), top, col, rot=(0, 0.6, 0))
    elif t == "charms":
        for k, cc in enumerate([col, "#26428B", "#F2B33D"]):
            b.rod((ox - W * 0.2 + k * W * 0.2, oy - W * 0.3, hip + 0.03), (ox - W * 0.2 + k * W * 0.2, oy - W * 0.3, hip - 0.08), 0.004, INK)
            b.sph(0.022, (ox - W * 0.2 + k * W * 0.2, oy - W * 0.31, hip - 0.1), cc)
    elif t == "umbrella":
        tip = (RH[0] - 0.05, RH[1], H + 0.28)
        b.rod(RH, tip, 0.012, "#6B4226")
        bm = bmesh.new()
        bmesh.ops.create_cone(bm, cap_ends=True, cap_tris=False, segments=16, radius1=0.55, radius2=1e-4, depth=0.3)
        b._ob(bm, col, (tip[0], tip[1], tip[2] - 0.05))
        b.sph(0.07, (tip[0], tip[1] - 0.4, tip[2] - 0.13), "#F2E6C9", scale=(1, 0.4, 1))
        b.sph(0.03, (tip[0], tip[1] - 0.43, tip[2] - 0.13), INK)
        b.box((0.04, 0.02, 0.12), (tip[0] + 0.12, tip[1] - 0.42, tip[2] - 0.24), "#FF6F91")
    elif t == "fan":
        ob = b.cyl(0.26, 0.26, -0.006, 0.006, col, seg=24)
        ob.location = (LH[0] + 0.12, LH[1] - 0.12, LH[2] + 0.28)
        ob.rotation_euler = (math.pi / 2, 0, 0.3)
    elif t == "bells":
        for s in (-1, 1):
            b.sph(0.02, (ox + s * W * 0.19, oy - 0.02, 0.16), col)
    elif t == "guandao":
        x = ox - W * 0.8
        b.rod((x, oy, 0.02), (x, oy, H + 0.12), 0.022, "#3A2E28")
        b.box((0.07, 0.03, 0.38), (x - 0.07, oy, H + 0.22), col, rot=(0, 0.25, 0))
        b.sph(0.05, (x, oy, H + 0.02), "#B22222")
        for k in range(4):
            b.box((0.05, 0.004, 0.12), (x + 0.05, oy - 0.02, H - 0.05 - k * 0.15), "#E8C547")
    elif t == "lanterns4":
        for k in range(4):
            b.cyl(0.07, 0.07, sh + 0.1 + (k % 2) * 0.12, sh + 0.26 + (k % 2) * 0.12, col, x=ox - 0.45 + k * 0.3, y=oy + 0.35)
    elif t == "astrolabe":
        cx, cz = LH[0] + 0.18, LH[2] + 0.12
        b.torus(0.22, 0.02, (cx, LH[1] - 0.05, cz), col, rot=(math.pi / 2, 0, 0))
        b.torus(0.12, 0.012, (cx, LH[1] - 0.05, cz), col, rot=(math.pi / 2, 0, 0.6))
        b.rod((cx - 0.22, LH[1] - 0.05, cz), (cx + 0.22, LH[1] - 0.05, cz), 0.008, col)
    elif t in ("ledger", "book_black", "clipboard"):
        b.box((0.2, 0.05, 0.28), (LH[0] + 0.02, LH[1] - 0.06, LH[2] + 0.1), col)
    elif t == "shield":
        ob = b.cyl(0.34, 0.34, -0.02, 0.02, col, seg=28)
        ob.location = (LH[0] + 0.06, oy - W * 0.45, hip + 0.05)
        ob.rotation_euler = (math.pi / 2, 0, 0)
        b.torus(0.33, 0.025, (LH[0] + 0.06, oy - W * 0.45 - 0.02, hip + 0.05), "#6FB7E9" if c["key"] == "prima" else "#B5A642", rot=(math.pi / 2, 0, 0))
        for dx, dz in [(-0.12, 0.12), (0, 0.16), (0.12, 0.12), (-0.16, 0), (0, 0), (0.16, 0), (-0.12, -0.12), (0, -0.16), (0.12, -0.12)]:
            b.sph(0.03, (LH[0] + 0.06 + dx, oy - W * 0.45 - 0.025, hip + 0.05 + dz), "#F4F1EA")
    elif t == "staff_sieve":
        x = ox - W * 0.75
        b.rod((x, oy, 0.02), (x, oy, H + 0.15), 0.02, col)
        ob = b.cyl(0.17, 0.17, -0.012, 0.012, "#DDE6EE")
        ob.location, ob.rotation_euler = (x, oy, H + 0.3), (math.pi / 2, 0, 0)
        for dx, dz in [(-0.06, 0.06), (0.06, 0.06), (-0.06, -0.06), (0.06, -0.06), (0, 0)]:
            b.sph(0.022, (x + dx, oy - 0.015, H + 0.3 + dz), col)
    elif t == "jars":
        for k in range(4):
            b.cyl(0.035, 0.035, hip - 0.12, hip - 0.02, col, x=ox - W * 0.3 + k * W * 0.2, y=oy - W * 0.3)
    elif t == "watch":
        ob = b.cyl(0.05, 0.05, -0.008, 0.008, col)
        ob.location, ob.rotation_euler = (LH[0], LH[1] - 0.06, LH[2] + 0.03), (math.pi / 2, 0, 0)
    elif t == "ouroboros":
        b.torus(0.85, 0.055, (ox, oy + 0.4, H * 0.55), col, rot=(math.pi / 2, 0, 0), arc=0.93)
        b.sph(0.11, (ox + 0.85, oy + 0.4, H * 0.55 + 0.15), col, scale=(1, 1, 0.7))
    elif t == "gear_halo":
        b.torus(hr * 1.7, hr * 0.12, (ox, oy + hr * 1.2, hz), col, rot=(math.pi / 2, 0, 0), seg=32)
        for k in range(16):
            a = 2 * math.pi * k / 16
            b.box((hr * 0.28, hr * 0.12, hr * 0.28), (ox + hr * 1.95 * math.cos(a), oy + hr * 1.2, hz + hr * 1.95 * math.sin(a)), col, rot=(0, -a, 0))
    elif t == "tails9":
        for k in range(9):
            a = math.radians(-80 + k * 20)
            base = (ox, oy + 0.18, hip)
            tip = (ox + 0.85 * math.sin(a), oy + 0.35, hip + 0.85 * math.cos(a) * 0.85 + 0.1)
            b.rod(base, tip, 0.07, col, r2=0.03)
            b.sph(0.05, tip, "#7FDBFF")
    elif t == "fox_fire":
        for k, (dx, dz) in enumerate([(-0.45, 0.3), (0.5, 0.1), (0.35, 0.6)]):
            b.sph(0.05, (ox + dx, oy - 0.2, H * 0.5 + dz), col)
    elif t == "coins":
        for k in range(9):
            a = 2 * math.pi * k / 9
            b.cyl(0.05, 0.05, 0.0, 0.015, col, x=ox + 0.85 * math.cos(a), y=oy + 0.6 * math.sin(a))
    elif t == "brush":
        b.rod(RH, (RH[0] - 0.1, RH[1] - 0.1, RH[2] + 0.55), 0.015, col)
        b.rod((RH[0] - 0.1, RH[1] - 0.1, RH[2] + 0.55), (RH[0] - 0.12, RH[1] - 0.12, RH[2] + 0.68), 0.03, INK, r2=0.005)
    elif t == "cart":
        x = ox + W * 0.9
        b.box((0.42, 0.3, 0.2), (x, oy, 0.28), col)
        for s in (-1, 1):
            b.torus(0.12, 0.02, (x, oy + s * 0.17, 0.13), "#3A2E28", rot=(math.pi / 2, 0, 0))
        for k in range(4):
            b.rod((x - 0.15 + k * 0.1, oy - 0.08, 0.4), (x - 0.15 + k * 0.1, oy + 0.08, 0.4), 0.025, "#3BB273")
    elif t == "tiles":
        for k in range(3):
            b.box((0.05, 0.03, 0.07), (LH[0], LH[1] - 0.05, LH[2] + 0.04 + k * 0.075), col)
    elif t == "cane":
        b.rod(RH, (RH[0] - 0.05, RH[1], 0.0), 0.012, col)
    elif t == "abacus":
        b.box((0.24, 0.03, 0.16), (LH[0] + 0.05, LH[1] - 0.06, LH[2] + 0.08), col)
    elif t == "dice":
        b.box((0.06, 0.06, 0.06), (ox, oy - W * 0.32, sh - 0.12), col, rot=(0.6, 0.4, 0.2))
    elif t == "badge":
        ob = b.cyl(0.035, 0.035, -0.006, 0.006, col, seg=5)
        ob.location, ob.rotation_euler = (ox + W * 0.18, oy - W * 0.29, sh - 0.12), (math.pi / 2, 0, 0)
    elif t == "oar":
        b.rod((RH[0], RH[1], 0.05), (RH[0] + 0.1, RH[1], H + 0.15), 0.02, col)
        b.box((0.12, 0.02, 0.35), (RH[0], RH[1], 0.2), col)
    elif t == "rope":
        b.torus(0.1, 0.025, (ox + W * 0.45, oy, hip), col, rot=(0, math.pi / 2, 0))
    elif t == "goat_crook":
        b.rod((RH[0], RH[1], 0.0), (RH[0], RH[1], H + 0.2), 0.015, col)
        b.torus(0.07, 0.015, (RH[0] + 0.07, RH[1], H + 0.2), col, rot=(math.pi / 2, 0, 0), arc=0.6)
    elif t == "pennies":
        b.cyl(0.07, 0.07, LH[2] - 0.05, LH[2] + 0.12, "#C9E4E8", x=LH[0], y=LH[1] - 0.05)
        b.cyl(0.06, 0.06, LH[2] - 0.04, LH[2] + 0.04, col, x=LH[0], y=LH[1] - 0.05)
    elif t == "shawl":
        b.cyl(W * 0.62, W * 0.4, sh - 0.25, sh + 0.06, col, x=ox, y=oy, sy=0.65)
    elif t == "thread":
        pass


# ---------------------------------------------------------------- special bodies
def build(b, c):
    body = c["look"].get("body", "human")
    L = c["look"]
    if body == "human":
        human(b, c)
    elif body == "kappa":
        A = human(b, c, head="kappa", noprops=True)
        b.sph(c["w"] * 0.62, (0, c["w"] * 0.32, c["h"] * 0.62), "#4E6B3F", scale=(1, 0.5, 1.2))
        for p in L.get("props", []):
            prop(b, p, A, c)
    elif body == "sphere":
        b.sph(0.7, (0, 0.05, 0.32), "#6B8E23", scale=(1, 0.8, 0.45))
        for x in (-0.45, 0, 0.45):
            b.cyl(0.08, 0.1, 0.0, 0.2, "#6B8E23", x=x, y=-0.35 if x == 0 else 0.3)
        b.sph(0.08, (-0.25, -0.5, 0.5), INK)
        b.sph(0.08, (0.25, -0.5, 0.5), INK)
        b.sph(0.55, (0, 0, 1.05), L["top"][1])
        b.sph(0.14, (0, -0.52, 1.0), "#B22222", scale=(1, 0.4, 1))
        for s in (-1, 1):
            b.sph(0.14, (s * 0.58, -0.05, 1.05), L["top"][1])
            b.sph(0.08, (s * 0.65, -0.15, 0.85), c["skin"])
        b.sph(0.17, (0, 0, 1.72), c["skin"])
        for s in (-1, 1):
            b.sph(0.022, (s * 0.06, -0.15, 1.75), INK)
        b.cyl(0.16, 0.18, 1.85, 1.98, "#B22222", y=0.0)
        for p in L.get("props", []):
            if p[0] == "coins":
                prop(b, p, dict(ox=0, oy=0, hz=1.7, hr=0.17, H=2.0, W=0.9, sh=1.5, hip=1.0, RH=(-0.6, 0, 1), LH=(0.6, 0, 1)), c)
    elif body == "eclipse":
        b.sph(0.55, (0, 0, 1.8), "#4B2A6B")
        for k in range(9):
            a = 2 * math.pi * k / 9
            b.rod((0.42 * math.cos(a), 0.42 * math.sin(a), 2.2), (0.5 * math.cos(a), 0.5 * math.sin(a), 2.45), 0.06, "#F4A300", r2=0.004)
        for s in (-1, 1):
            b.sph(0.08, (s * 0.2, -0.5, 1.88), INK, scale=(1.3, 0.4, 0.35))
        b.sph(0.06, (0, -0.53, 2.02), "#F4A300", scale=(0.7, 0.4, 1))
        pts = [(0.3, -0.1, 1.3), (0.6, 0.0, 1.0), (0.75, 0.1, 0.65), (0.55, 0.15, 0.35), (0.15, 0.1, 0.18), (-0.3, 0.0, 0.15),
               (-0.65, -0.05, 0.25), (-0.85, 0.0, 0.45), (-0.95, 0.05, 0.7)]
        for k, p in enumerate(pts):
            b.sph(0.2 - k * 0.015, p, "#4B2A6B")
        for k in range(3):
            b.rod((-0.95, 0.05, 0.7), (-1.05 + k * 0.05, 0.1 * (k - 1), 1.1 + k * 0.08), 0.06, "#F4A300", r2=0.004)
    elif body == "trio":
        props = ["spindle", "rod", "shears"]
        for k, x in enumerate((-0.6, 0.0, 0.6)):
            A = human(b, c, ox=x, H=c["h"] - (0.05 if k == 1 else 0), W=c["w"], noprops=True)
            if k == 0:
                b.rod((A["LH"][0], A["LH"][1] - 0.05, A["LH"][2] - 0.1), (A["LH"][0], A["LH"][1] - 0.05, A["LH"][2] + 0.25), 0.015, "#8C6A3F")
            elif k == 1:
                b.rod((A["RH"][0], A["RH"][1] - 0.05, A["RH"][2]), (A["RH"][0], A["RH"][1] - 0.05, A["RH"][2] + 0.6), 0.01, "#D4AF37")
            else:
                for s in (-1, 1):
                    b.box((0.03, 0.01, 0.2), (A["RH"][0], A["RH"][1] - 0.06, A["RH"][2] + 0.1), "#C9CED6", rot=(0, s * 0.35, 0))
        b.rod((-0.6 + 0.2, -0.05, 0.95), (0.6 - 0.2, -0.05, 0.95), 0.008, "#C0392B")
    elif body == "duo":
        for x, head in ((-0.45, "ox"), (0.45, "horse")):
            cc = dict(c)
            cc["look"] = dict(L, props=[["guandao", "#8C6A3F"]] if head == "ox" else [])
            A = human(b, cc, ox=x, H=c["h"], W=c["w"], head=head)
            if head == "horse":
                b.rod((A["LH"][0] + 0.15, 0, 0.02), (A["LH"][0] + 0.15, 0, c["h"] + 0.1), 0.022, "#3A2E28")
                b.box((0.06, 0.03, 0.3), (A["LH"][0] + 0.2, 0, c["h"] + 0.22), "#8C6A3F")
    elif body == "hap":
        H = c["h"]
        b.cyl(0.62, 0.3, 0.0, H * 0.82, "#141026", sy=0.7, seg=28)
        b.cyl(0.32, 0.26, H * 0.82, H * 0.86, "#141026")
        b.sph(0.17, (0, 0, H * 0.9), "#1E1A3A")
        for s in (-1, 1):
            b.box((0.07, 0.07, 0.07), (s * 0.065, -0.15, H * 0.91), "#F4F1EA", rot=(0, 0, 0.3 * s))
            b.sph(0.012, (s * 0.065, -0.19, H * 0.91), INK)
        import random
        rnd = random.Random(7)
        for k in range(40):
            z = rnd.uniform(0.1, H * 0.8)
            r = 0.62 - (0.32 * z / (H * 0.82))
            a = rnd.uniform(0, 2 * math.pi)
            b.sph(0.012 + rnd.random() * 0.01, (r * math.cos(a) * 1.01, r * 0.7 * math.sin(a) * 1.01, z), "#F4F1EA", seg=8)
        accents = ["#FF7A2C", "#E34234", "#00A86B", "#F4A300", "#1F6FB2", "#F28C28", "#FF2E88", "#F2B33D", "#7FDBFF", "#D4AF37"]
        for d in range(10):
            a = math.pi / 2 - 2 * math.pi * d / 10
            b.text(str(d), (0.34 * math.cos(a), -0.05, H * 0.9 + 0.34 * math.sin(a)), 0.1, accents[d])
        b.box((0.26, 0.05, 0.2), (0, -0.55, H * 0.5), "#2A2550")
        for k in range(4):
            b.rod((-0.1 + k * 0.067, -0.55, H * 0.5 + 0.1), (-0.1 + k * 0.067, -0.6, H * 0.5 + 0.26), 0.022, "#2A2550")
        b.rod((0.13, -0.55, H * 0.5), (0.24, -0.6, H * 0.5 + 0.1), 0.025, "#2A2550")
        b.box((0.09, 0.09, 0.09), (0, -0.62, H * 0.5 + 0.13), "#F4F1EA", rot=(0.5, 0.3, 0.6))
        for s in (-1, 1):
            b.rod((s * 0.3, -0.1, H * 0.78), (s * 0.12, -0.5, H * 0.5), 0.07, "#141026")


# ---------------------------------------------------------------- run
scene = bpy.context.scene
ROOT = coll("CAST", scene.collection)
MASTERS = coll("CAST_MASTERS", ROOT)
SHEETS = coll("CAST_SHEETS", ROOT)
for col in list(MASTERS.children) + [SHEETS]:
    for ob in list(col.objects):
        bpy.data.objects.remove(ob, do_unlink=True)
for col in list(MASTERS.children):
    bpy.data.collections.remove(col)

counts = {}
for c in CAST:
    col = bpy.data.collections.new("C_" + c["key"])
    MASTERS.children.link(col)
    b = B(col)
    build(b, c)
    counts[c["key"]] = b.n


def find_lc(lc, name):
    if lc.name == name:
        return lc
    for ch in lc.children:
        r = find_lc(ch, name)
        if r:
            return r


find_lc(bpy.context.view_layer.layer_collection, "CAST_MASTERS").exclude = True

X0, CW, RH_, ROWS = 3000.0, 2.4, 2.8, 6
VIEWS = [("FRONT", 0.0), ("LEFT", -math.pi / 2), ("RIGHT", math.pi / 2), ("BACK", math.pi)]
layout = []
for i, c in enumerate(CAST):
    s, r = divmod(i, ROWS)
    for k, (vn, rz) in enumerate(VIEWS):
        # linked copies (shared mesh data, own object colour) under a rotated empty; Workbench ignores
        # per-object colours inside collection instances, so instances would render grey
        e = bpy.data.objects.new(f"V_{c['key']}_{vn}", None)
        e.location = (X0 + s * 12 + k * CW, 0, -r * RH_)
        e.rotation_euler = (0, 0, rz)
        SHEETS.objects.link(e)
        for ob in bpy.data.collections["C_" + c["key"]].objects:
            cp = ob.copy()
            SHEETS.objects.link(cp)
            cp.parent = e
    layout.append([c["key"], s, r])
result = {"characters": len(CAST), "objects": sum(counts.values()), "sheets": (len(CAST) + ROWS - 1) // ROWS, "layout": layout}
