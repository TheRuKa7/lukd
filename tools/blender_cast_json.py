#!/usr/bin/env python3
"""Write the Blender cast script with the cast data embedded: python3 tools/blender_cast_json.py > build/blender_cast_run.py"""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cast import CAST
data = [dict(key=c["key"], h=c["h"], w=c["w"], skin=c.get("skin"), eyes=c.get("eyes"), look=c["look"]) for c in CAST]
src = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "blender_cast.py")).read()
print(src.replace('"__CAST_JSON__"', "r'''" + json.dumps(data, separators=(",", ":")) + "'''"))
