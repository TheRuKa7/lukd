"""True four-camera first-draft encounter studies for the complete OMEN catalog.

Run: blender --background --python tools/render_encounters.py -- --only debt_hound,kasa_obake
No generation service or purchased asset is used. These are editable spatial drafts,
not final topology, rigs, cultural approvals or game assets. Noise/Default are clearly
identified encounter studies rather than assertions of canonical physical anatomy.
"""
import argparse
import hashlib
import json
import math
from pathlib import Path
import random
import sys

import bpy
from mathutils import Vector

ROOT = Path(__file__).resolve().parents[1]
COL = None
MATS = {}


def material(name, color, metal=0):
    if name in MATS: return MATS[name]
    c = color.lstrip('#'); srgb = tuple(int(c[i:i+2],16)/255 for i in (0,2,4))
    rgb = tuple(v/12.92 if v <= .04045 else ((v+.055)/1.055)**2.4 for v in srgb)
    m = bpy.data.materials.new(name); m.diffuse_color = (*rgb,1); m.use_nodes = True
    bs = m.node_tree.nodes.get('Principled BSDF'); bs.inputs['Base Color'].default_value=(*rgb,1)
    bs.inputs['Roughness'].default_value=.8; bs.inputs['Metallic'].default_value=metal
    MATS[name]=m; return m


def adopt(obj, name, mat=None):
    obj.name=name
    for c in list(obj.users_collection): c.objects.unlink(obj)
    COL.objects.link(obj)
    if mat: obj.data.materials.append(mat)
    return obj


def box(name, pos, dims, mat, bevel=.04):
    bpy.ops.mesh.primitive_cube_add(size=1,location=pos);o=adopt(bpy.context.object,name,mat)
    o.dimensions=dims; bpy.ops.object.transform_apply(location=False,rotation=False,scale=True)
    if bevel:
        mod=o.modifiers.new('Soft construction edges','BEVEL');mod.width=bevel;mod.segments=2
        o.modifiers.new('Weighted normals','WEIGHTED_NORMAL')
    return o


def ball(name,pos,scale,mat):
    bpy.ops.mesh.primitive_uv_sphere_add(segments=20,ring_count=12,radius=1,location=pos)
    o=adopt(bpy.context.object,name,mat);o.scale=scale
    for p in o.data.polygons:p.use_smooth=True
    return o


def cyl(name,pos,radius,depth,mat,rotation=(0,0,0),vertices=24):
    bpy.ops.mesh.primitive_cylinder_add(vertices=vertices,radius=radius,depth=depth,location=pos,rotation=rotation)
    return adopt(bpy.context.object,name,mat)


def cone(name,pos,r1,r2,depth,mat):
    bpy.ops.mesh.primitive_cone_add(vertices=20,radius1=r1,radius2=r2,depth=depth,location=pos)
    return adopt(bpy.context.object,name,mat)


def ring(name,pos,radius,thick,mat,rotation=(0,0,0)):
    bpy.ops.mesh.primitive_torus_add(major_segments=32,minor_segments=8,location=pos,major_radius=radius,minor_radius=thick,rotation=rotation)
    return adopt(bpy.context.object,name,mat)


def rod(name,a,b,radius,mat):
    a,b=Vector(a),Vector(b); o=cyl(name,(a+b)/2,radius,(b-a).length,mat)
    o.rotation_euler=(b-a).to_track_quat('Z','Y').to_euler();return o


def tube(name,pts,radius,mat):
    curve=bpy.data.curves.new(name,'CURVE');curve.dimensions='3D';curve.bevel_depth=radius;curve.bevel_resolution=2
    spline=curve.splines.new('POLY');spline.points.add(len(pts)-1)
    for p,co in zip(spline.points,pts):p.co=(*co,1)
    o=bpy.data.objects.new(name,curve);COL.objects.link(o);o.data.materials.append(mat);return o


def face(name,verts,mat):
    mesh=bpy.data.meshes.new(name);mesh.from_pydata(verts,[],[list(range(len(verts)))]);mesh.materials.append(mat)
    o=bpy.data.objects.new(name,mesh);COL.objects.link(o);return o


def eyes(z=1.5,y=-.23,x=.12,mat=None):
    for side in (-1,1):ball('Eye socket',(side*x,y,z),(.045,.028,.045),mat or MATS['ink'])


def humanoid(body=None,h=1.8,width=.5,robe=False,head=True):
    body=body or MATS['ink'];hip=.46*h;shoulder=.77*h
    if robe:cone('Weighted robe',(0,0,.37*h),width*.72,width*.45,.68*h,body)
    else:
        box('Torso',(0,0,.64*h),(width,.28,.34*h),body)
        for s in (-1,1):rod('Leg',(s*width*.25,0,hip),(s*width*.25,-.02,.12),.09,body)
    for s in (-1,1):
        rod('Sleeve',(s*width*.55,0,shoulder),(s*width*.73,-.02,.4*h),.085,body)
        ball('Gloved hand',(s*width*.73,-.03,.39*h),(.09,.075,.11),MATS['leather'])
        box('Boot',(s*width*.25,-.07,.08),(.19,.34,.16),MATS['ink'],.025)
    cyl('Collar',(0,0,.82*h),.14,.12,MATS['brass'])
    if head:
        ball('Head',(0,-.015,.9*h),(.16,.14,.19),MATS['bone']);eyes(.92*h,-.15,.065)


def hound():
    box('Hound body',(0,.12,.88),(.48,.98,.42),MATS['ink'])
    box('Ledger spine',(0,.24,1.13),(.4,.75,.12),MATS['rust'])
    for x in (-.23,.23):
        for y in (-.25,.5):
            rod('Articulated leg',(x,y,.9),(x*1.2,y+.03,.28),.08,MATS['brass'])
            box('Stamp pad',(x*1.2,y-.04,.17),(.22,.3,.15),MATS['ink'])
    ball('Hound head',(0,-.55,1.02),(.27,.32,.24),MATS['bone'])
    box('Long snout',(0,-.82,.95),(.25,.35,.2),MATS['bone'])
    for x in (-.16,.16):cone('Ledger ear',(x,-.47,1.34),.11,0,.35,MATS['ink'])
    eyes(1.08,-.78,.18,MATS['ember']);tube('Counterweight tail',[(0,.64,.95),(0,.95,1.17),(.1,1.1,1.3)],.04,MATS['brass'])
    jar((.27,.15,1.0),.14,.36)


def jar(pos,r=.2,h=.4):
    x,y,z=pos;cyl('Smoked-glass vessel',(x,y,z),r,h,MATS['glass'])
    for dz in (-h/2,h/2):cyl('Jar clamp',(x,y,z+dz),r*1.1,.045,MATS['brass'])


def ghost(swarm=False):
    centres=[(-.95,.25,.15),(.95,.25,.15),(-.5,-.25,.1),(.5,-.25,.1),(0,.35,.65)] if swarm else [(0,0,0)]
    for x,y,z in centres:
        ball('Hunger vessel',(x,y,z+.9),(.34,.27,.46),MATS['jade'])
        cyl('Mouth void',(x,y-.27,z+1.0),.17,.045,MATS['ink'],(math.pi/2,0,0))
        ball('Long head',(x,y-.02,z+1.5),(.19,.17,.3),MATS['paper'])
        for s in (-1,1):
            ball('Eye',(x+s*.065,y-.18,z+1.55),(.035,.025,.04),MATS['ink'])
            tube('Thin reaching arm',[(x+s*.25,y,z+1.16),(x+s*.48,y-.2,z+.8),(x+s*.4,y-.45,z+.75)],.045,MATS['jade'])
        cone('Trailing cloth',(x,y,z+.37),.04,.29,.9,MATS['paper'])


def lantern():
    ball('Paper lantern',(0,0,1),(.5,.4,.62),MATS['rust'])
    for z in (.48,.65,.85,1.05,1.25,1.5):ring('Bamboo rib',(0,0,z),.47*math.sin((z-.35)/1.4*math.pi),.018,MATS['brass'])
    cyl('Lantern top',(0,0,1.6),.25,.08,MATS['ink']);cyl('Lantern foot',(0,0,.4),.22,.08,MATS['ink'])
    ball('One eye',(0,-.4,1.15),(.16,.045,.16),MATS['paper']);ball('Pupil',(0,-.447,1.15),(.065,.02,.08),MATS['ink'])
    tube('Tongue',[(0,-.41,.9),(0,-.62,.72),(.1,-.65,.56)],.07,MATS['red'])
    ring('Hanging loop',(0,0,1.85),.19,.035,MATS['brass'],(math.pi/2,0,0))


def umbrella():
    cone('Oiled-paper umbrella',(0,0,1.65),.85,.06,.42,MATS['purple'])
    ring('Umbrella rim',(0,0,1.44),.85,.025,MATS['brass'])
    for a in range(8):
        t=a*math.tau/8;rod('Umbrella rib',(0,0,1.86),(.85*math.cos(t),.85*math.sin(t),1.44),.015,MATS['paper'])
    rod('Umbrella single leg',(0,0,1.75),(0,0,.25),.065,MATS['leather'])
    box('Hopping foot',(0,-.12,.15),(.24,.45,.15),MATS['ink'])
    ball('Single umbrella eye',(0,-.59,1.62),(.15,.08,.15),MATS['paper']);ball('Pupil',(0,-.65,1.62),(.065,.04,.085),MATS['ink'])
    tube('Umbrella tongue',[(.26,-.6,1.55),(.28,-.8,1.34),(.12,-.84,1.25)],.05,MATS['red'])


def kappa():
    humanoid(MATS['jade'],1.35,.5);ball('Turtle shell',(0,.23,.83),(.39,.25,.45),MATS['olive'])
    ball('Beak',(0,-.25,1.2),(.13,.2,.075),MATS['brass'])
    ring('Water dish',(0,0,1.4),.2,.045,MATS['brass']);cyl('Water',(0,0,1.4),.18,.02,MATS['blue'])
    for i in range(5):rod('Shell seam',(-.3+i*.15,.44,.55),(-.3+i*.15,.44,1.05),.013,MATS['brass'])


def abacus():
    for x in (-.45,.45):box('Abacus upright',(x,0,1.3),(.13,.3,1.2),MATS['brass'])
    for z in (.7,1.9):box('Abacus crossbar',(0,0,z),(1.0,.3,.12),MATS['brass'])
    for x in (-.3,-.15,0,.15,.3):
        rod('Counting rod',(x,0,.8),(x,0,1.8),.018,MATS['ink'])
        for z in (.95,1.15,1.5,1.7):ball('Counting bead',(x,0,z),(.07,.12,.065),MATS['jade'])
    box('Head',(0,0,2.1),(.5,.35,.28),MATS['rust']);eyes(2.13,-.2,.12,MATS['ember'])
    for s in (-1,1):
        box('Leg',(s*.3,0,.37),(.25,.3,.65),MATS['ink']);box('Foot',(s*.3,-.1,.1),(.34,.5,.2),MATS['brass'])
        rod('Arm',(s*.5,0,1.7),(s*.8,0,1.1),.11,MATS['rust'])


def junk():
    verts=[(-.6,-1.5,.35),(.6,-1.5,.35),(.6,1.5,.35),(-.6,1.5,.35),(-.85,-1.2,.85),(.85,-1.2,.85),(.85,1.2,.85),(-.85,1.2,.85)]
    mesh=bpy.data.meshes.new('Junk hull');mesh.from_pydata(verts,[],[(0,1,2,3),(0,4,5,1),(1,5,6,2),(2,6,7,3),(3,7,4,0),(4,7,6,5)]);o=bpy.data.objects.new('Armoured debt junk',mesh);COL.objects.link(o);mesh.materials.append(MATS['leather'])
    for y in (-.6,.65):
        rod('Mast',(0,y,.8),(0,y,2.8),.055,MATS['brass'])
        for i in range(5):box('Reinforced sail strip',(.25,y,1.35+i*.28),(1.15,.06,.24),MATS['red'],.015)
    box('Deckhouse',(0,.8,1.05),(.65,.7,.6),MATS['rust'])


def koi():
    ball('Golden koi',(0,0,.9),(.35,.85,.4),MATS['gold'])
    ball('Fish snout',(0,-.76,.92),(.24,.25,.27),MATS['bone'])
    for s in (-1,1):
        ball('Fish eye',(s*.21,-.8,1.02),(.05,.04,.05),MATS['ink'])
        face('Pectoral fin',[(s*.25,-.2,.85),(s*.8,.2,.72),(s*.3,.35,.78)],MATS['rust'])
        tube('Barbel',[(s*.14,-.95,.82),(s*.32,-1.18,.76),(s*.42,-1.14,.72)],.015,MATS['brass'])
    face('Tail',[(0,.65,.9),(-.6,1.3,1.2),(0,1.12,.85),(.6,1.3,.5)],MATS['rust'])
    for y in (-.4,-.1,.2,.5):ring('Scale construction',(0,y,.9),.34,.014,MATS['brass'],(math.pi/2,0,0))


def wing(origin,side,mat):
    x,y,z=origin
    for i in range(7):
        a=(i/6)*1.1; tip=(x+side*(.7+i*.15),y+.18+i*.08,z+.65-i*.13)
        rod('Feather shaft',(x,y,z),tip,.018,MATS['brass'])
        face('Layered flight feather',[(x+side*.05,y-.03,z+.06),(tip[0],tip[1]-.07,tip[2]+.07),(tip[0]+side*.09,tip[1]+.12,tip[2]-.24),(x+side*.15,y+.1,z-.1)],mat)


def harpy(queen=False):
    humanoid(MATS['blue'],2.0 if queen else 1.6,.45,robe=False)
    h=2.0 if queen else 1.6
    for s in (-1,1):wing((s*.2,.15,h*.75),s,MATS['purple'] if queen else MATS['olive'])
    cone('Bird crest',(0,.02,h+.05),.22,.03,.3,MATS['brass'])
    for s in (-1,1):
        for x in (-.055,.055):rod('Talon',(s*.13,0,.12),(s*.13+x,-.28,.03),.025,MATS['brass'])


def serpent():
    pts=[(.8*math.sin(i*.3),.5*math.cos(i*.3),.3+i*.065) for i in range(31)]
    tube('Monsoon serpent',pts,.18,MATS['blue']);p=pts[-1]
    ball('Naga head',(p[0],p[1]-.12,p[2]+.12),(.28,.35,.2),MATS['jade'])
    for s in (-1,1):ball('Hood',(p[0]+s*.22,p[1]+.06,p[2]-.1),(.26,.12,.5),MATS['blue'])


def humanoid_recipe(key):
    if key=='oni_enforcer':
        humanoid(MATS['red'],2.1,.8);cone('Horn L',(-.16,0,2.13),.08,0,.28,MATS['bone']);cone('Horn R',(.16,0,2.13),.08,0,.28,MATS['bone']);rod('Iron club',(.8,-.1,.4),(.8,-.1,1.9),.13,MATS['ink'])
    elif key=='jiangshi':
        humanoid(MATS['blue'],1.8,.55,True);box('Blank forehead paper',(0,-.16,1.68),(.08,.025,.28),MATS['paper'],0)
        for s in (-1,1):rod('Stiff reaching sleeve',(s*.2,-.02,1.35),(s*.2,-.65,1.35),.09,MATS['blue'])
        cyl('Court cap',(0,0,1.84),.22,.14,MATS['ink'])
    elif key=='bronze_automaton':
        humanoid(MATS['bronze'],2.05,.62);cyl('Sieve shield',(.55,-.3,1.15),.47,.08,MATS['brass'],(math.pi/2,0,0));rod('Bronze pike',(-.7,0,.15),(-.7,0,2.5),.035,MATS['bronze'])
    elif key=='siren':
        humanoid(MATS['blue'],1.8,.45,True);ring('Lyre frame',(.55,-.2,1.1),.32,.04,MATS['brass'],(math.pi/2,0,0))
        for x in (.4,.5,.6,.7):rod('Lyre string',(x,-.2,.85),(x,-.2,1.35),.007,MATS['paper'])
    elif key=='collector_captain':
        humanoid(MATS['rust'],2.05,.77);box('Ledger breastplate',(0,-.2,1.3),(.65,.16,.6),MATS['ink']);box('Hound-mask snout',(0,-.26,1.86),(.24,.24,.15),MATS['bone']);jar((.45,-.2,.8),.16,.4);rod('Ratchet hook',(-.65,0,.15),(-.65,0,1.8),.045,MATS['brass'])
    elif key=='basilica_surveyor':
        humanoid(MATS['paper'],1.85,.48,True);box('Survey plate',(0,-.23,1.25),(.45,.07,.4),MATS['brass']);rod('Survey pole',(.6,0,.05),(.6,0,2.1),.025,MATS['brass']);ring('Survey sight',(.6,0,2.05),.18,.025,MATS['brass'],(math.pi/2,0,0))
    elif key=='card_sharp_automaton':
        humanoid(MATS['ink'],1.8,.5);box('Blank card face',(0,-.15,1.65),(.33,.07,.38),MATS['paper']);box('Dealer waistcoat',(0,-.18,1.1),(.42,.05,.4),MATS['red'])
        for i in range(5):o=box('Card fan',(.5+i*.06,-.25,.9+i*.06),(.21,.035,.31),MATS['paper'],.012);o.rotation_euler.y=i*.14
    elif key=='loop_echo':
        humanoid(MATS['glass'],1.8,.45)
        for i in (1,2):
            for z in (.6,1.1,1.65):ring('Temporal contour',(i*.2,i*.23,z),.22,.015,MATS['blue'],(math.pi/2,0,0))


def vetala():
    rod('Banyan trunk',(.55,.2,0),(.55,.2,2.6),.12,MATS['leather']);rod('Hanging branch',(.55,.2,2.5),(-.6,.2,2.5),.07,MATS['leather'])
    ball('Inverted spirit head',(-.3,-.1,.65),(.18,.16,.22),MATS['bone']);box('Suspended cloth',(-.3,.02,1.3),(.45,.25,.7),MATS['olive'])
    for s in (-1,1):tube('Folded leg',[(-.3+s*.12,0,1.65),(-.3+s*.27,0,2.2),(-.3+s*.08,0,2.45)],.06,MATS['bone'])
    for x in (-.4,-.2):rod('Hanging arm',(x,0,1.5),(x,-.2,.8),.045,MATS['bone'])


def yantra():
    ball('Measuring core',(0,0,1.1),(.48,.48,.48),MATS['purple'])
    for rotation in ((0,0,0),(math.pi/2,0,0),(0,math.pi/2,0)):ring('Instrument gimbal',(0,0,1.1),.7,.045,MATS['brass'],rotation)
    for s in (-1,1):
        for t in (-1,1):rod('Instrument support',(s*.35,t*.35,.9),(s*.65,t*.65,.1),.045,MATS['brass'])


def tumbleweed():
    rng=random.Random(42)
    for i in range(28):
        a=i*math.tau/28;b=rng.random()*math.pi
        pts=[(.65*math.cos(a)*math.sin(t+b),.65*math.sin(a)*math.sin(t+b),.85+.65*math.cos(t+b)) for t in [j*.28 for j in range(23)]]
        tube('Dry branching stem',pts,.018,MATS['leather'])
    for s in (-1,1):rod('Root leg',(s*.3,0,.5),(s*.4,-.1,.08),.06,MATS['leather'])
    ball('Seed eye',(-.15,-.65,.95),(.05,.03,.07),MATS['ember']);ball('Seed eye',(.15,-.65,.95),(.05,.03,.07),MATS['ember'])


def horseman():
    ball('Horse body',(0,0,1.15),(.45,.9,.45),MATS['ink']);ball('Horse neck',(0,-.75,1.55),(.25,.35,.6),MATS['ink']);ball('Horse head',(0,-1.0,1.95),(.23,.4,.25),MATS['bone'])
    for x in (-.3,.3):
        for y in (-.55,.55):rod('Horse leg',(x,y,1),(x,y-.1,.12),.075,MATS['ink']);box('Hoof',(x,y-.15,.08),(.18,.25,.14),MATS['leather'])
    for x in (-.13,.13):cone('Horse ear',(x,-.95,2.23),.07,0,.25,MATS['ink'])
    cone('Rider coat',(0,.05,1.95),.38,.25,.85,MATS['rust']);cyl('Closed collar',(0,.05,2.43),.13,.08,MATS['ink'])
    rod('Lantern arm',(.25,0,2.2),(.6,-.2,2.0),.07,MATS['ink']);jar((.65,-.2,1.77),.18,.35)
    tube('Horse tail',[(0,.8,1.35),(.1,1.2,1.15),(.15,1.35,.6)],.07,MATS['ink'])


def train():
    for y in (-1.8,0,1.8):
        box('Ghost carriage',(0,y,.9),(.8,1.55,.8),MATS['glass']);box('Carriage roof',(0,y,1.36),(.95,1.65,.15),MATS['ink'])
        for side in (-1,1):
            for wy in (y-.48,y+.48):cyl('Train wheel',(side*.48,wy,.4),.25,.1,MATS['brass'],(0,math.pi/2,0))
    cyl('Boiler',(0,-2.35,.9),.34,1.0,MATS['ink'],(math.pi/2,0,0));cyl('Chimney',(0,-2.4,1.48),.12,.5,MATS['brass'])
    for x in (-.38,.38):rod('Rail',(x,-3.0,.07),(x,2.75,.07),.025,MATS['bronze'])
    for i in range(6):ball('Draft vapour',(.1*math.sin(i),-2.4+i*.15,1.9+i*.2),(.12+i*.025,)*3,MATS['glass'])


def noise(storm=False):
    rng=random.Random(77);n=36 if storm else 15
    for i in range(n):
        pos=(rng.uniform(-1,1),rng.uniform(-.6,.6),rng.uniform(.2,2.0))
        o=box('Unresolved chance fragment',pos,(rng.uniform(.08,.3),)*3,[MATS['purple'],MATS['blue'],MATS['paper']][i%3],0);o.rotation_euler=(rng.random(),rng.random(),rng.random())
    if storm: ring('Encounter boundary',(0,0,1.1),1.2,.015,MATS['brass'],(math.pi/2,0,0))


def eclipse():
    for x in (-1.0,1.0):box('Machine footing',(x,0,.1),(.8,.65,.2),MATS['ink'])
    rod('Occluder support',(-1,0,.2),(-1,0,1.75),.12,MATS['brass'])
    ring('Rahu occluder ring',(-1,0,1.6),.75,.09,MATS['brass'],(math.pi/2,0,0))
    cyl('Occluder disc',(-1,.03,1.6),.61,.1,MATS['purple'],(math.pi/2,0,0))
    for a in range(6):
        t=a*math.tau/6;box('Occluder clamp',(-1+.75*math.sin(t),-.06,1.6+.75*math.cos(t)),(.12,.16,.18),MATS['ink'])
    for x in (.65,1.35):box('Ketu surveyor rail',(x,0,1.25),(.1,.16,2.2),MATS['brass'])
    for z in (.35,.7,1.05,1.4,1.75,2.1):box('Graduated blank rail tie',(1,0,z),(.8,.13,.055),MATS['ink'])
    box('Mechanical cursor',(1,-.14,1.65),(.5,.24,.28),MATS['purple']);ring('Surveyor aperture',(1,-.3,1.65),.16,.025,MATS['brass'],(math.pi/2,0,0))
    tube('Instrument cable',[(-.5,.2,.3),(0,.4,.22),(.6,.2,.3)],.035,MATS['ink'])


def default_study():
    # Contextual stillness study, never a proposed body or the orbit/wheel language of Hap.
    grey=material('Stillness grey','#77777B')
    for x,height,depth in ((-.75,1.1,.28),(0,1.75,.4),(.75,1.35,.3)):
        box('Frozen grey volume',(x,0,height/2+.08),(.48,depth,height),grey,.015)
        box('Quiet rectangular void',(x,-depth/2-.008,height*.68),(.25,.012,height*.24),MATS['ink'],0)
    for x in (-.95,-.35,.45,.95):
        box('Immobile ground trace',(x,-.42,.075),(.28,.4,.015),grey,0)
    box('Contextual ground',(0,.1,.02),(2.7,1.5,.04),MATS['paper'],0)


RECIPES={'debt_hound':hound,'noiseling':lambda:noise(False),'chochin_obake':lantern,'kasa_obake':umbrella,'kappa':kappa,
         'abacus_golem':abacus,'debt_junk':junk,'golden_koi':koi,'hungry_ghost':ghost,'hungry_ghost_swarm':lambda:ghost(True),
         'vetala':vetala,'yantra_guardian':yantra,'monsoon_naga':serpent,'harpy':harpy,'harpy_queen':lambda:harpy(True),
         'tumbleweed_golem':tumbleweed,'headless_horseman':horseman,'ghost_train':train,'noise_storm':lambda:noise(True),
         'default':default_study,'rahu_ketu':eclipse}
for _id in ('oni_enforcer','jiangshi','bronze_automaton','siren','collector_captain','basilica_surveyor','card_sharp_automaton','loop_echo'):
    RECIPES[_id]=lambda key=_id:humanoid_recipe(key)


def register_rendered_catalog(manifest):
    """Promote only four verified files, preserving the original specification basis."""
    path=ROOT/'art/catalog/characters.json'
    catalog=json.loads(path.read_text(encoding='utf-8-sig'))
    records={r['id']:r for r in manifest['records']}
    for entry in catalog['entries']:
        record=records.get(entry['id'])
        if not record: continue
        for view in ('front','left','right','back'):
            file=ROOT/record['views'][view]['path']
            if not file.is_file() or hashlib.sha256(file.read_bytes()).hexdigest()!=record['views'][view]['sha256']:
                raise ValueError('Unverified render: '+str(file))
        prior=entry.setdefault('provenance',{})
        prior.setdefault('historical_render_status',prior.get('render_status'))
        if entry.get('source3d_path') and entry['source3d_path']!=manifest['source']:
            prior.setdefault('historical_source3d_path',entry['source3d_path'])
        entry['view_paths']={v:d['path'] for v,d in record['views'].items()}
        entry['source3d_path']=manifest['source']
        contextual=entry['id'] in ('noise_storm','default')
        prior.update(status='First-draft spatial encounter study' if contextual else 'Design specification with editable first-draft 3D reference; not final painted concept/rig.',
                     render_status='Four actual orthographic camera studies; contextual encounter proxy, not anatomical canon.' if contextual else 'Four actual orthographic camera renders from the local procedural spatial draft.',
                     render_scope=record['render_scope'],four_view_files_present=True,
                     render_manifest=manifest.get('manifest_path','art/source/encounter_drafts.json'),
                     height_status='Procedural study dimensions; not calibrated to the narrative/model height specification.',
                     view_orientation='Front -Y; wearer left +X; wearer right -X; back +Y. One orthographic scale per set; no mirrored panels.',
                     acceptance='Spatial draft only. Anatomy, hands, face, linework, material wear, topology, rigging and game import remain unapproved.')
    present=[e for e in catalog['entries'] if all(e.get('view_paths',{}).get(v) and (ROOT/e['view_paths'][v]).is_file() for v in ('front','left','right','back'))]
    unique={tuple(e['view_paths'][v] for v in ('front','left','right','back')) for e in present}
    catalog.setdefault('status_vocabulary',{})['procedural_spatial_draft']='Actual editable geometric study and four camera evidence; not final concept/rig'
    coverage=catalog.setdefault('coverage_summary',{})
    coverage.update(records_with_present_view_files=len(present),unique_present_four_view_sets=len(unique),
                    encounter_study_records_with_actual_views=sum(str(e.get('provenance',{}).get('render_manifest','')).startswith('art/source/encounter_drafts') for e in present),
                    contextual_non_anatomical_records=['noise_storm','default'],
                    note='91 catalog records are not 91 unique models or final asset acceptance. Five named keepers use explicitly shared compound models; contextual hazard/concept cameras do not establish physical anatomy. Procedural drafts are not the finished manga art direction.')
    catalog['updated']=manifest['date']
    path.write_text(json.dumps(catalog,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')


def main():
    global COL
    ap=argparse.ArgumentParser();ap.add_argument('--only',default='');ap.add_argument('--height',type=int,default=768);ap.add_argument('--samples',type=int,default=16);ap.add_argument('--update-catalog',action='store_true');ap.add_argument('--date',default='2026-11-08')
    args=ap.parse_args(sys.argv[sys.argv.index('--')+1:] if '--' in sys.argv else[])
    catalog=json.loads((ROOT/'art/catalog/characters.json').read_text(encoding='utf-8-sig'))['entries']
    keys=args.only.split(',') if args.only else list(RECIPES)
    if any(k not in RECIPES for k in keys):raise ValueError('No geometry recipe: '+str(set(keys)-set(RECIPES)))
    bpy.ops.object.select_all(action='SELECT');bpy.ops.object.delete(use_global=False)
    colors={'ink':'#17131B','paper':'#F2E8D5','bone':'#DED5BE','brass':'#B5A642','gold':'#D4AF37','rust':'#B7410E','red':'#B3261E','jade':'#3E806A','olive':'#627552','purple':'#53456B','blue':'#3B7191','glass':'#8FA6AD','leather':'#6E4F3C','bronze':'#8C6A3F','ember':'#E8A04B'}
    for name,c in colors.items():material(name,c,.15 if name in ('brass','gold','bronze') else 0)
    scene=bpy.context.scene;scene.render.engine='BLENDER_EEVEE';scene.render.resolution_x=args.height;scene.render.resolution_y=args.height;scene.render.resolution_percentage=100
    if hasattr(scene,'eevee') and hasattr(scene.eevee,'taa_render_samples'):scene.eevee.taa_render_samples=args.samples
    scene.render.image_settings.file_format='PNG';scene.render.image_settings.color_mode='RGB';scene.render.film_transparent=False
    scene.world.color=(.8,.75,.65);scene.world.use_nodes=True;scene.world.node_tree.nodes['Background'].inputs[0].default_value=(.78,.78,.78,1);scene.world.node_tree.nodes['Background'].inputs[1].default_value=.7
    scene.view_settings.view_transform='Standard';scene.render.image_settings.color_depth='8'
    support=bpy.data.collections.new('Studio');scene.collection.children.link(support);COL=support
    ground=box('Paper floor',(0,0,-.08),(200,200,.1),MATS['paper'],0)
    for name,pos,power,size in [('Key',(4,-5,7),650,5),('Fill',(-4,-2,4),260,5),('Rim',(2,5,6),450,4)]:
        data=bpy.data.lights.new(name,'AREA');data.energy=power;data.shape='DISK';data.size=size;o=bpy.data.objects.new(name,data);support.objects.link(o);o.location=pos;o.rotation_euler=(-o.location).to_track_quat('-Z','Y').to_euler()
    data=bpy.data.cameras.new('Orthographic study camera');cam=bpy.data.objects.new('Orthographic study camera',data);support.objects.link(cam);scene.camera=cam;data.type='ORTHO'
    models=[]
    for index,key in enumerate(keys):
        COL=bpy.data.collections.new(key);scene.collection.children.link(COL);RECIPES[key]()
        root=bpy.data.objects.new(key+'_source',None);COL.objects.link(root)
        objects=[o for o in COL.objects if o!=root]
        for o in objects:o.parent=root
        models.append((key,COL,root,objects));COL.hide_render=True
    out=ROOT/'art/cast/views';out.mkdir(parents=True,exist_ok=True);records=[]
    for index,(key,col,root,objects) in enumerate(models):
        col.hide_render=False;bpy.context.view_layer.update()
        corners=[o.matrix_world@Vector(v) for o in objects if o.type in ('MESH','CURVE') for v in o.bound_box]
        mins=Vector(tuple(min(v[i] for v in corners) for i in range(3)));maxs=Vector(tuple(max(v[i] for v in corners) for i in range(3)));centre=(mins+maxs)/2;extent=maxs-mins
        data.ortho_scale=max(extent)*1.24;distance=max(extent)*3+6
        paths={}
        for view,offset in [('front',(0,-distance,0)),('left',(distance,0,0)),('right',(-distance,0,0)),('back',(0,distance,0))]:
            cam.location=centre+Vector(offset);cam.rotation_euler=(centre-cam.location).to_track_quat('-Z','Y').to_euler()
            target=out/f'{key}_{view}.png';scene.render.filepath=str(target);bpy.ops.render.render(write_still=True)
            paths[view]=dict(path=str(target.relative_to(ROOT)).replace('\\','/'),sha256=hashlib.sha256(target.read_bytes()).hexdigest())
        records.append(dict(id=key,views=paths,object_count=len(objects),bounds_min=list(mins),bounds_max=list(maxs),render_scope='encounter design study' if key in ('noise_storm','default','noiseling') else 'isolated procedural spatial draft'))
        col.hide_render=True
    for index,(_,col,root,_) in enumerate(models):
        root.location=((index%6)*8,(index//6)*8,0);col.hide_render=False
    # A smoke/subset render cannot silently replace the complete editable source.
    stem='encounter_drafts' if not args.only else 'encounter_drafts_'+hashlib.sha256(','.join(keys).encode()).hexdigest()[:10]
    source=ROOT/f'art/source/{stem}.blend';source.parent.mkdir(parents=True,exist_ok=True);bpy.ops.wm.save_as_mainfile(filepath=str(source))
    manifest_path=ROOT/f'art/source/{stem}.json'
    manifest=dict(schema_version=1,date=args.date,tool='Blender local scripted geometry',source=str(source.relative_to(ROOT)).replace('\\','/'),manifest_path=str(manifest_path.relative_to(ROOT)).replace('\\','/'),records=records,status='First-draft spatial studies; no final-rig, cultural, runtime or painted-art approval')
    manifest_path.write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf-8')
    if args.update_catalog:register_rendered_catalog(manifest)
    print('ENCOUNTER_DRAFTS_COMPLETE',len(records),source)


if __name__=='__main__':main()
