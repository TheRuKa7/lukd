"""Reproducible OMEN lookdev scene, compositing approved PNGs without mirroring.

Run with Blender, not ordinary Python:
  blender --background --python tools/build_lookdev.py -- --check
  blender --background --python tools/build_lookdev.py -- --version v5

Outputs are design/render studies, never gameplay screenshots or accepted rigs.
All geometry, exact labels, seven-chamber prop and cameras are authored here.
"""
import argparse
import hashlib
import json
import math
from pathlib import Path
import sys

import bpy
from mathutils import Vector
import numpy as np

ROOT = Path(__file__).resolve().parents[1]


def options():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--version", default="v5", choices=["v4", "v5"])
    parser.add_argument("--allow-v4", action="store_true", help="Allow older fresh candidates only when v5 is missing; metadata records fallback.")
    parser.add_argument("--check", action="store_true", help="Read inputs and check alpha; write nothing.")
    parser.add_argument("--output-dir", type=Path, default=ROOT / "art/renders/lookdev")
    parser.add_argument("--source-dir", type=Path, default=ROOT / "art/source")
    parser.add_argument("--width", type=int, default=1920)
    return parser.parse_args(sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else [])


def source_paths(args):
    out = {}
    for key in ["chr_nil", "chr_vesper", "chr_varro", "enm_debthound", "env_meridian"]:
        path = ROOT / "art/concepts/fresh" / f"{key}_{args.version}.png"
        if not path.exists() and args.allow_v4:
            path = path.with_name(f"{key}_v4.png")
        if not path.is_file():
            raise FileNotFoundError(f"Missing approved candidate {path}; supply it before rendering, not an invented replacement.")
        out[key] = path
    return out


def image_info(path, needs_alpha):
    img = bpy.data.images.load(str(path), check_existing=True)
    w, h = img.size
    pixels = np.empty(w * h * 4, dtype=np.float32)
    img.pixels.foreach_get(pixels)
    alpha = pixels.reshape(h, w, 4)[:, :, 3]
    mask = alpha > 0.04
    ys, xs = np.where(mask)
    if not len(xs):
        raise ValueError("Empty image: " + str(path))
    bbox = [int(xs.min()), int(ys.min()), int(xs.max()) + 1, int(ys.max()) + 1]
    transparent = float(np.mean(alpha < 0.01))
    if needs_alpha and transparent < 0.02:
        raise ValueError("Actor needs real transparent background: " + str(path))
    return img, {"width": w, "height": h, "alpha_bbox_bottom_up": bbox,
                 "transparent_fraction": round(transparent, 5), "alpha_max": round(float(alpha.max()), 5),
                 "sha256": hashlib.sha256(path.read_bytes()).hexdigest(), "file": path.relative_to(ROOT).as_posix()}


def collection(name):
    col = bpy.data.collections.new(name)
    bpy.context.scene.collection.children.link(col)
    return col


def move(obj, col):
    for current in list(obj.users_collection):
        current.objects.unlink(obj)
    col.objects.link(obj)
    return obj


def material(name, rgb, emission=False):
    value = bpy.data.materials.new(name)
    value.diffuse_color = (*rgb, 1)
    value.use_nodes = True
    bsdf = value.node_tree.nodes.get("Principled BSDF")
    bsdf.inputs["Base Color"].default_value = (*rgb, 1)
    bsdf.inputs["Roughness"].default_value = 0.85
    if emission:
        bsdf.inputs["Emission Color"].default_value = (*rgb, 1)
        bsdf.inputs["Emission Strength"].default_value = 1
    return value


def cube(name, xyz, scale, mat, col, bevel=0):
    bpy.ops.mesh.primitive_cube_add(size=1, location=xyz)
    obj = move(bpy.context.object, col)
    obj.name = name
    obj.dimensions = scale
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    if mat:
        obj.data.materials.append(mat)
    if bevel:
        modifier = obj.modifiers.new("Manufactured edge", "BEVEL")
        modifier.width, modifier.segments = bevel, 2
        obj.modifiers.new("Weighted normals", "WEIGHTED_NORMAL")
    return obj


def cylinder(name, xyz, radius, depth, mat, col, vertices=48, axis_y=True):
    bpy.ops.mesh.primitive_cylinder_add(vertices=vertices, radius=radius, depth=depth, location=xyz)
    obj = move(bpy.context.object, col)
    obj.name = name
    if axis_y:
        obj.rotation_euler[0] = math.pi / 2
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
    if mat:
        obj.data.materials.append(mat)
    return obj


def text(name, value, x, y, z, size, mat, col):
    curve = bpy.data.curves.new(name, type="FONT")
    curve.body, curve.size = value, size
    curve.align_x, curve.align_y = "CENTER", "CENTER"
    curve.extrude = 0
    obj = bpy.data.objects.new(name, curve)
    col.objects.link(obj)
    obj.location = (x, y, z)
    obj.rotation_euler[0] = math.pi / 2
    obj.data.materials.append(mat)
    return obj


def curve_line(name, points, radius, mat, col):
    curve = bpy.data.curves.new(name, "CURVE")
    curve.dimensions, curve.bevel_depth, curve.bevel_resolution = "3D", radius, 2
    poly = curve.splines.new("POLY")
    poly.points.add(len(points) - 1)
    for p, xyz in zip(poly.points, points):
        p.co = (*xyz, 1)
    obj = bpy.data.objects.new(name, curve)
    col.objects.link(obj)
    curve.materials.append(mat)
    return obj


def camera(name, xyz, target, scale=16):
    data = bpy.data.cameras.new(name)
    obj = bpy.data.objects.new(name, data)
    bpy.context.scene.collection.objects.link(obj)
    obj.location = xyz
    obj.rotation_euler = (Vector(target) - obj.location).to_track_quat("-Z", "Y").to_euler()
    data.type, data.ortho_scale = "ORTHO", scale
    return obj


def image_plane(name, image, xyz, width, height, col, uv=(0, 0, 1, 1)):
    x, y, z = xyz
    mesh = bpy.data.meshes.new(name)
    mesh.from_pydata([(x - width / 2, y, z), (x + width / 2, y, z),
                     (x + width / 2, y, z + height), (x - width / 2, y, z + height)], [], [(0, 1, 2, 3)])
    mesh.uv_layers.new()
    u0, v0, u1, v1 = uv
    for loop, coords in zip(mesh.uv_layers.active.data, [(u0, v0), (u1, v0), (u1, v1), (u0, v1)]):
        loop.uv = coords
    obj = bpy.data.objects.new(name, mesh)
    col.objects.link(obj)
    mat = bpy.data.materials.new(name + "_RGBA")
    mat.use_nodes = True
    mat.surface_render_method = "DITHERED"
    nodes = mat.node_tree.nodes
    nodes.clear()
    output, emission, transparent, mix, tex = [nodes.new(n) for n in ["ShaderNodeOutputMaterial", "ShaderNodeEmission", "ShaderNodeBsdfTransparent", "ShaderNodeMixShader", "ShaderNodeTexImage"]]
    tex.image = image
    links = mat.node_tree.links
    links.new(tex.outputs["Color"], emission.inputs["Color"])
    links.new(tex.outputs["Alpha"], mix.inputs[0])
    links.new(transparent.outputs[0], mix.inputs[1])
    links.new(emission.outputs[0], mix.inputs[2])
    links.new(mix.outputs[0], output.inputs["Surface"])
    mesh.materials.append(mat)
    obj["source_role"] = "lookdev composited reference; not a game rig"
    obj["unmirrored"] = True
    return obj


def seven_chamber_prop(col, brass, dark, cream):
    center = (-2.3, 0, 4.5)
    cylinder_obj = cylinder("Vesper cylinder - exactly SEVEN through bores", center, 1.45, 0.7, brass, col, vertices=96)
    cylinder_obj["chamber_count"] = 7
    for i in range(7):
        angle = 2 * math.pi * i / 7 + math.pi / 2
        x, z = center[0] + 1.00 * math.cos(angle), center[2] + 1.00 * math.sin(angle)
        cutter = cylinder(f"Bore cutter {i + 1}", (x, 0, z), 0.265, 1.8, None, col, vertices=40)
        bpy.context.view_layer.objects.active = cylinder_obj
        modifier = cylinder_obj.modifiers.new(f"Physical bore {i + 1}", "BOOLEAN")
        modifier.operation, modifier.solver, modifier.object = "DIFFERENCE", "EXACT", cutter
        bpy.ops.object.modifier_apply(modifier=modifier.name)
        bpy.data.objects.remove(cutter, do_unlink=True)
        # Recessed darkness lies behind the real opening, not a painted-on false hole.
        cylinder(f"Bore interior {i + 1}", (x, 0.39, z), 0.26, 0.02, dark, col)
    cylinder("Solid central axle (not a chamber)", (-2.3, -0.39, 4.5), 0.17, 0.10, cream, col)
    text("Prop title", "VESPER / SEVEN-CHAMBER CYLINDER", 2.2, -0.6, 5.25, 0.32, cream, col)
    text("Prop note", "7 physical bores / solid central axle", 2.2, -0.6, 4.55, 0.23, cream, col)
    text("Prop status", "SCRIPTED DESIGN STUDY - NOT GAMEPLAY", 0, -0.6, 2.35, 0.22, cream, col)
    return cylinder_obj


def main():
    args = options()
    if args.width < 640 or args.width > 3840:
        raise ValueError("Width must be 640..3840")
    paths = source_paths(args)
    bpy.ops.wm.read_factory_settings(use_empty=True)
    loaded = {key: image_info(path, key != "env_meridian") for key, path in paths.items()}
    if args.check:
        print(json.dumps({key: info for key, (_, info) in loaded.items()}, indent=2))
        print("Input and real-alpha checks passed; no output written.")
        return
    args.output_dir.mkdir(parents=True, exist_ok=True)
    args.source_dir.mkdir(parents=True, exist_ok=True)
    scene = bpy.context.scene
    scene.render.engine = "BLENDER_EEVEE"
    scene.render.resolution_x, scene.render.resolution_y = args.width, round(args.width * 9 / 16)
    scene.render.resolution_percentage = 100
    scene.render.image_settings.file_format = "PNG"
    scene.render.image_settings.color_mode = "RGBA"
    scene.render.film_transparent = False
    scene.view_settings.view_transform = "Standard"
    scene.world = bpy.data.worlds.new("Matte slate world")
    scene.world.use_nodes = True
    scene.world.node_tree.nodes["Background"].inputs[0].default_value = (0.015, 0.022, 0.035, 1)
    scene.world.node_tree.nodes["Background"].inputs[1].default_value = 0.5
    bg, actors, reel, labels, stage, prop = [collection(n) for n in ["Painted reference plate", "Unmirrored RGBA actors", "Separate exact reel", "Lookdev labels", "Reproducible stage geometry", "Vesper seven-chamber prop"]]
    ink = material("Ink", (0.016, 0.012, 0.021), True)
    cream = material("Ledger cream", (0.88, 0.82, 0.68), True)
    orange = material("Nixie orange", (1, 0.23, 0.035), True)
    brass = material("Worn brass", (0.40, 0.23, 0.07))
    slate = material("Slate clay", (0.12, 0.16, 0.19))
    grey = material("Warm clay", (0.33, 0.31, 0.27))
    env, env_info = loaded["env_meridian"]
    aspect = env_info["width"] / env_info["height"]
    target = 16 / 9
    if aspect > target:
        crop = target / aspect
        uv = ((1 - crop) / 2, 0, (1 + crop) / 2, 1)
    else:
        crop = aspect / target
        uv = (0, (1 - crop) / 2, 1, (1 + crop) / 2)
    image_plane("Empty painted Meridian plate - reference", env, (0, 3.5, 0), 16, 9, bg, uv)
    placements = {"chr_nil": (-5.1, -1.1, 1.05, 4.85), "chr_vesper": (-2.4, -0.9, 1.05, 5.00),
                  "chr_varro": (5.0, -0.7, 1.05, 5.25), "enm_debthound": (2.0, -1.0, 1.05, 1.90)}
    for key, (x, y, z, height) in placements.items():
        img, info = loaded[key]
        x0, y0, x1, y1 = info["alpha_bbox_bottom_up"]
        ratio = (x1 - x0) / (y1 - y0)
        image_plane(key + " / unchanged handedness", img, (x, y, z), height * ratio, height, actors,
                    (x0 / info["width"], y0 / info["height"], x1 / info["width"], y1 / info["height"]))
    # Three physical frame slots and exact source-authored digits; no image-model writing.
    cube("Reel brass back", (0, -2.0, 7.25), (4.25, 0.16, 1.3), brass, reel, 0.08)
    for i, digit in enumerate("070"):
        x = (i - 1) * 1.32
        cube(f"Tube {i + 1} dark well", (x, -2.12, 7.25), (1.12, 0.1, 1.12), ink, reel, 0.1)
        points = [(x + 0.51 * math.cos(t), -2.2, 7.25 + 0.57 * math.sin(t)) for t in np.linspace(0, 2 * math.pi, 65)]
        curve_line(f"Tube {i + 1} rim", points, 0.028, orange, reel)
        text(f"Exact slot {i + 1}", digit, x, -2.25, 7.22, 0.85, orange, reel)
    text("Reel label", "REEL / LAYOUT EXAMPLE", 0, -2.3, 8.15, 0.19, cream, labels)
    text("Exact NIL identity", "NaN", -5.1, -2.3, 6.38, 0.43, orange, labels)
    cube("Separate Audit readout frame", (5.3, -2.05, 7.2), (2.55, 0.12, 0.9), ink, labels, 0.05)
    text("Audit caption", "AUDIT / PREVIEW", 5.3, -2.18, 7.48, 0.18, cream, labels)
    text("Illustrative stake", "68", 5.3, -2.2, 7.06, 0.5, orange, labels)
    cube("Study disclaimer band", (0, -3.2, 0.4), (16, 0.08, 0.65), ink, labels)
    text("Study disclaimer", "ZERO-SUM: OMEN / LOOKDEV & POSE STUDY / NOT A UNITY GAMEPLAY CAPTURE", 0, -3.3, 0.42, 0.21, cream, labels)
    # Physical stage/blockout retained as a reusable source; beauty uses the painted plate.
    cube("Clear battle floor", (0, 1.0, 0.45), (18, 9, 0.3), slate, stage)
    for side in [-1, 1]:
        for index in range(5):
            x = side * (7.8 + 0.15 * index)
            y = 0.8 + index * 1.3
            height = 5 + (index % 3)
            cube(f"Tenement {side} {index}", (x, y, height / 2 + 0.6), (2.0, 1.1, height), grey, stage, 0.06)
            for row in range(3):
                cube(f"Window repair frame {side} {index} {row}", (x - side * 1.01, y - 0.57, 1.9 + row * 1.35), (0.1, 0.12, 0.65), brass, stage)
    cube("Drain gate lintel", (0, 5.0, 3.3), (9.6, 0.7, 0.6), grey, stage, 0.05)
    for x in np.linspace(-4, 4, 13):
        cube("Drain gate bar", (float(x), 5.0, 1.8), (0.1, 0.18, 2.4), brass, stage)
    for x in [-6.7, 6.7]:
        curve_line("Salvaged drain pipe", [(x, -0.3, 5.6), (x, -0.3, 1.3), (x + (1 if x < 0 else -1), -0.3, 1.3)], 0.1, brass, stage)
    bpy.ops.object.light_add(type="AREA", location=(0, -5, 10))
    light = bpy.context.object
    light.name, light.data.energy, light.data.shape, light.data.size = "Soft sky key", 1500, "DISK", 10
    light.rotation_euler = (Vector((0, 2, 1)) - light.location).to_track_quat("-Z", "Y").to_euler()
    game_cam = camera("CAM_game_locked_16x9", (0, -25, 4.5), (0, 0, 4.5), 16)
    clay_cam = camera("CAM_stage_clay", (11, -17, 11), (0, 2, 2.7), 21)
    prop_cam = camera("CAM_seven_bores_front", (0, -15, 4.5), (0, 0, 4.5), 12)
    seven_chamber_prop(prop, brass, ink, cream)
    allcols = [bg, actors, reel, labels, stage, prop]

    def render(name, visible, cam):
        for col in allcols:
            col.hide_render = col not in visible
        scene.camera = cam
        scene.render.filepath = str(args.output_dir / name)
        bpy.ops.render.render(write_still=True)
        return name

    outputs = []
    outputs.append(render(f"omen_battle_{args.version}.png", [bg, actors, reel, labels], game_cam))
    outputs.append(render(f"meridian_empty_{args.version}.png", [bg], game_cam))
    outputs.append(render(f"meridian_clay_{args.version}.png", [stage], clay_cam))
    outputs.append(render(f"vesper_cylinder_detail_{args.version}.png", [prop], prop_cam))
    for col in allcols:
        col.hide_render = col not in [bg, actors, reel, labels]
    scene.camera = game_cam
    for image, _ in loaded.values():
        image.pack()
    blend = args.source_dir / f"omen_lookdev_{args.version}.blend"
    bpy.ops.wm.save_as_mainfile(filepath=str(blend))
    manifest = {"status": "lookdev render / not gameplay or runtime-rig acceptance", "source_script": "tools/build_lookdev.py",
                "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(), "blender": bpy.app.version_string,
                "resolution": [scene.render.resolution_x, scene.render.resolution_y], "actors_mirrored": False,
                "inputs": {key: info for key, (_, info) in loaded.items()}, "seven_physical_chambers": 7,
                "exact_labels": ["NaN", "070", "AUDIT / PREVIEW", "68"], "outputs": outputs,
                "scene": blend.relative_to(ROOT).as_posix(), "limitations": ["Flattened candidate actors, no animation rigs", "Illustrative readouts are not simulated game state", "Painted background is a single reference plate", "Empty clay scene is source geometry, not a finished region"]}
    (args.output_dir / f"lookdev_{args.version}.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print("LOOKDEV COMPLETE:", blend)


if __name__ == "__main__":
    main()
