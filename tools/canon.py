"""Shared canon data for the bible and the art book: characters and lands.

Text facts come from the Markdown sources where possible (Character Bible rows, Locations Guide bullets), so the
documents stay the single source of truth. Colours here are the signature palettes from the Character Bible §0
and Art Direction §4.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CHARACTERS = [
    # name, role, digit, land, shape, colours, art (repo path or None), locks
    ("NIL", "Protagonist · the Remainder", "Player's choice", "Meridian Undercity", "rect_circle",
     [("Nixie orange", "#FF7A2C"), ("Ink black", "#141018"), ("Bone white", "#EDE6DA"), ("Rim cyan", "#00E5FF")],
     "art/concepts/nil_keyart.jpg",
     ["Decoder on the RIGHT wrist", "One orange streak in white hair", "Halo reads exactly \"NaN\"", "Coat's left tail is longer", "Amber eyes"]),
    ("Vesper Sette", "Gunslinger · companion", "7", "Meridian / Crossroads", "triangles",
     [("Crimson", "#E5243B"), ("Black", "#141018"), ("Brass", "#B5A642"), ("Shirt white", "#F4F1EA")],
     "art/concepts/vesper_keyart.jpg",
     ["Exactly 7 chambers", "Scar on the lip", "Braid over the LEFT shoulder", "Crimson + black + brass only"]),
    ("Maeve Triskel", "Charm-smith · companion", "3", "Meridian, Celtic quarter", "circles",
     [("Copper", "#D9822B"), ("Clover", "#3BB273"), ("Leather", "#6B4226"), ("Red hair", "#C0392B")],
     "art/concepts/maeve_keyart.jpg",
     ["Exactly 3 braids", "Triskele on the hammer", "Clover pin on the collar"]),
    ("Hina of the Ninety-Nine", "Tsukumogami · companion", "9", "Hyakki", "dome",
     [("Vermilion", "#E34234"), ("Indigo", "#26428B"), ("Paper", "#F2E6C9"), ("Gold", "#F2B33D")],
     "art/concepts/hina_keyart.jpg",
     ["The umbrella has ONE eye and a tongue", "Kimono numbers stop at 99", "Never reaches 100 before the finale"]),
    ("Ba Jinling", "Financier · companion", "8", "River Empire", "fan",
     [("Jade", "#00A86B"), ("Gold", "#F4C430"), ("Lacquer red", "#B22222"), ("Violet eyes", "#5D3A7A")],
     None, ["Exactly 8 bells", "Abacus-rib fan", "Jade + gold palette"]),
    ("Bai Si", "Executioner · companion", "4", "River Empire (Ten Courts)", "vertical",
     [("Mourning white", "#F4F1EA"), ("Ink", "#1B1B1B"), ("Talisman yellow", "#E8C547"), ("Lantern", "#F2B33D")],
     None, ["Always 4 lanterns, 4 talismans", "White robes only", "Never smiles before Act IV"]),
    ("Shunya", "Astronomer · companion", "0", "Śūnyapura", "astrolabe",
     [("Indigo", "#3F3D99"), ("Saffron", "#F4A300"), ("Brass", "#B5893B"), ("Mirror silver", "#C9CED6")],
     None, ["The brass astrolabe", "Mirror-work embroidery", "\"Zero isn't nothing.\""]),
    ("Prima of Kroton", "Paladin · companion", "2", "Kroton Nova", "shield",
     [("Aegean blue", "#1F6FB2"), ("White gold", "#E9DDB3"), ("Chalk", "#F4F1EA"), ("Glass blue", "#6FB7E9")],
     None, ["Sieve shield", "2-3-5-7 halo", "Short hair"]),
    ("Fibi Leone", "Dealer · companion", "Fibonacci", "Crossroads", "spiral",
     [("Gold", "#F2B33D"), ("Midnight", "#1D1A3A"), ("Card white", "#F4F1EA"), ("Neon pink", "#FF2E88")],
     None, ["1,597 nights", "Spiral irises", "Her digit changes every round"]),
    ("Varro Kade", "Prologue boss → ally", "61", "Meridian", "block",
     [("Rust", "#B7410E"), ("Gunmetal", "#4A4E54"), ("Debt-jar glow", "#FF7A2C"), ("Mask bone", "#E3DCCB")],
     "art/concepts/varro_keyart.jpg", ["Hound-skull mask", "Glass debt jars", "\"61\" in red"]),
    ("Tamamo", "Act I boss", "Nine tails", "Hyakki", "crescent",
     [("Violet", "#8E44AD"), ("Gold", "#F4C430"), ("Foxfire cyan", "#7FDBFF"), ("White", "#F4F1EA")],
     "art/concepts/tamamo_keyart.jpg", ["Nine tails, each tipped with a digit", "Foxfire is cold cyan-violet", "Layered court robes; AI-corrected before acceptance"]),
    ("Chancellor Jin Chan", "Act II boss", "88", "River Empire", "sphere",
     [("Gold", "#D4AF37"), ("Toad green", "#6B8E23"), ("Red", "#B22222")], None,
     ["Three-legged toad throne", "Coins spill from his mouth"]),
    ("Rahu & Ketu", "Act III boss", "Eclipse", "Śūnyapura", "eclipse",
     [("Eclipse purple", "#4B2A6B"), ("Corona gold", "#F4A300"), ("Night", "#141018")], None,
     ["Invented mechanical Basilica constructs, not the revered celestial figures", "Two bodies, one fight", "No external cultural approval claimed"]),
    ("Archon Seventeen", "Act IV boss", "17", "Kroton Nova", "column",
     [("Bronze", "#8C6A3F"), ("Chalk", "#F4F1EA"), ("Sieve white", "#DDE6EE")], None,
     ["Bronze laurel", "Sieve staff", "Cold \"17\""]),
    ("The House", "Act V boss", "89", "Crossroads", "ouroboros",
     [("Ivory", "#F4F1EA"), ("Casino red", "#C0392B"), ("Gold", "#D4AF37")], None,
     ["White suit", "Ouroboros tattoo", "Backwards pocket watch"]),
    ("Comptroller Lucan Thale", "Final antagonist", "50 (steel)", "Meridian", "arch",
     [("Steel white", "#E8E6E1"), ("Brass", "#B5A642"), ("Nixie", "#FF7A2C"), ("Steel", "#8E9196")],
     "art/concepts/thale_keyart.jpg", ["Gear monocle", "Steel, never glowing, \"50\"", "Never shouts"]),
]

LANDS = [
    ("Meridian Undercity", "Prologue · cosmopolitan capital · cyber-noir painted city",
     [("Wet slate", "#2E3A4B"), ("Window amber", "#E8A04B"), ("Moss", "#5E7D4A"), ("Nixie", "#FF7A2C"), ("Neon yellow", "#F5E400"), ("Neon magenta", "#FF2E88"), ("Neon cyan", "#00E5FF")],
     ["art/concepts/env_meridian_establishing.jpg", "art/concepts/env_meridian_battle_alley.jpg"]),
    ("Hyakki", "Act I · Japanese folklore · ukiyo-e + painted night",
     [("Indigo", "#1B2440"), ("Ink blue", "#2E4A7A"), ("Paper", "#F2E6C9"), ("Vermilion", "#E34234"), ("Lantern gold", "#F2B33D"), ("Firefly", "#9BD15A")],
     ["art/concepts/env_hyakki_establishing.jpg", "art/concepts/env_hyakki_battle_deck.jpg", "art/concepts/env_hyakki_battle_mock.jpg"]),
    ("The River Empire", "Act II · Chinese folk religion · gongbi gold + ink-wash underworld",
     [("Jade", "#00A86B"), ("Ochre", "#C8963E"), ("Red lacquer", "#B22222"), ("Gold leaf", "#D4AF37"), ("Rice paper", "#E9E2D0"), ("Ink green", "#3A4A3F")], []),
    ("Śūnyapura", "Act III · Indian myth & mathematics · miniature painting + monsoon light",
     [("Sandstone", "#D8A86B"), ("Peacock", "#1E7B6F"), ("Saffron", "#F4A300"), ("Indigo", "#3F3D99"), ("Brass", "#B5893B"), ("Eclipse", "#4B2A6B")], []),
    ("Kroton Nova", "Act IV · Greek myth · marble, mosaic, Aegean noon",
     [("Chalk", "#F4F1EA"), ("Aegean", "#1F6FB2"), ("Olive", "#7A8B4A"), ("Bronze", "#8C6A3F"), ("Sky", "#D6E6F2")], []),
    ("The Crossroads Territory", "Act V · American folklore · desert sunset + casino neon",
     [("Rust", "#B7410E"), ("Sage", "#9CAF88"), ("Dusk violet", "#5B3E73"), ("Sunset", "#F28C28"), ("Midnight", "#1D1A3A"), ("Neon pink", "#FF2E88")], []),
    ("The Basilica", "Finale · the machine · brass and steel",
     [("Brass", "#B5A642"), ("Steel", "#8E9196"), ("Steel white", "#E8E6E1"), ("Nixie", "#FF7A2C"), ("Ink", "#141018")], []),
]


# figure-kit key for each character, in CHARACTERS order
FIGURE_KEYS = ["nil", "vesper", "maeve", "hina", "ba", "bai_si", "shunya", "prima", "fibi",
               "varro", "tamamo", "jin_chan", "rahu_ketu", "archon", "house", "thale"]

# land key, Locations Guide heading prefix, act, law, Auditor, Keeper, reel key, enemies (World Bible §5)
LAND_FACTS = [
    ("meridian", "Meridian Undercity", "Prologue", "Debt: everyone owes luck", "Varro Kade, the Ledgerhound", "—", "meridian",
     "Debt Hounds · Collectors · Noiselings"),
    ("hyakki", "Hyakki", "Act I", "The Rule of Shi and Ku: 4 and 9 are cursed; 7 is blessed", "Tamamo, the Nine-Tailed Auditor", "Enma", "hyakki",
     "Kasa-obake · Chōchin-obake · Kappa · Oni enforcers"),
    ("river", "The River Empire", "Act II", "The Rule of Interest: luck compounds", "Chancellor Jin Chan, the Golden Toad", "Judge Cui", "river",
     "Abacus Golems · Debt Junks · Golden Koi · Ox-Head & Horse-Face · Hungry Ghosts · Jiangshi"),
    ("sunyapura", "Śūnyapura", "Act III", "The Rule of Karma: every action is recorded and returns", "Basilica Eclipse Engines (not celestial figures)", "Chitragupta", "sunyapura",
     "Vetālas · Brass Yantra Guardians · Monsoon Nāgas · invented eclipse constructs"),
    ("kroton", "Kroton Nova", "Act IV", "The Rule of Indivisibility: only primes pass", "Archon Seventeen", "the Moirai", "kroton",
     "Bronze Automata · Harpies · Composite Knights · Sirens"),
    ("crossroads", "The Crossroads Territory", "Act V", "The Rule of the House: the night loops; every deal has a price", "The House (Octavian Nine)", "the Stranger", "crossroads",
     "the Headless Horseman · Card-Sharp Automata · Tumbleweed Golems · the Ghost Train"),
    ("basilica", "The Basilica", "Finale", "Fixed Fate", "Comptroller Lucan Thale", "—", "basilica", "every Auditor's echo"),
]


def _read(rel):
    with open(os.path.join(ROOT, rel), encoding="utf-8") as f:
        return f.read()


def _clean(s):
    s = re.sub(r"\*\*|\*", "", s)
    return re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", s).strip()


def location_fields():
    """{heading prefix: {field: value}} from docs/LOCATIONS.md."""
    out, cur = {}, None
    for ln in _read("docs/LOCATIONS.md").splitlines():
        if ln.startswith("## "):
            cur = ln[3:].strip()
            out[cur] = {}
        elif cur and ln.startswith("- **"):
            m = re.match(r"- \*\*([^:*]+):\*\*\s*(.*)", ln)
            if m:
                out[cur][m.group(1).strip()] = _clean(m.group(2))
    return out


def land_info(prefix):
    for head, fields in location_fields().items():
        if head.startswith(prefix):
            return fields
    return {}


def character_rows(n):
    """Rows of section n (1 = NIL ... 9 = Fibi) of docs/CHARACTER_BIBLE.md as {key: value}."""
    text = _read("docs/CHARACTER_BIBLE.md")
    m = re.search(rf"^## {n}\. .*?$(.*?)(?=^## |\Z)", text, re.S | re.M)
    rows = {}
    if m:
        for ln in m.group(1).splitlines():
            r = re.match(r"\| \*\*([^*]+)\*\* \| (.*) \|$", ln)
            if r:
                rows[r.group(1).strip()] = _clean(r.group(2))
    return rows


def antagonist_rows():
    """{name: (look, motive, voice)} from Character Bible §10."""
    text = _read("docs/CHARACTER_BIBLE.md")
    m = re.search(r"^## 10\..*?$(.*?)(?=^## |\Z)", text, re.S | re.M)
    out = {}
    for ln in (m.group(1) if m else "").splitlines():
        r = re.match(r"\| \*\*([^*]+)\*\*[^|]* \| (.*?) \| (.*?) \| (.*?) \|$", ln)
        if r:
            out[r.group(1).strip()] = tuple(_clean(x) for x in r.group(2, 3, 4))
    return out


def md_table(rel, heading):
    """Rows (lists of cleaned cells) of the first table after a heading line that starts with `heading`."""
    lines = _read(rel).splitlines()
    out, on, in_table = [], False, False
    for ln in lines:
        if ln.startswith(heading):
            on = True
            continue
        if on:
            if ln.startswith("#"):
                break
            if ln.startswith("|"):
                in_table = True
                cells = re.split(r"(?<!\\)\|", ln.strip().strip("|"))
                if not all(re.fullmatch(r"\s*:?-+:?\s*", c) for c in cells):
                    out.append([_clean(c.replace(r"\|", "|")) for c in cells])
            elif in_table:
                break
    return out[1:]  # drop the header row


def numbered_list(rel, heading):
    lines = _read(rel).splitlines()
    out, on = [], False
    for ln in lines:
        if ln.startswith(heading):
            on = True
            continue
        if on:
            if ln.startswith("#"):
                break
            m = re.match(r"\d+\.\s+(.*)", ln)
            if m:
                out.append(_clean(m.group(1)))
    return out


def refresh_character_facts():
    """Read locks from source; this small visual index is not the whole roster."""
    summary = md_table("docs/CHARACTER_BIBLE.md", "## 0.")
    if len(summary) >= len(CHARACTERS):
        for index, row in enumerate(summary[:len(CHARACTERS)]):
            old = CHARACTERS[index]
            CHARACTERS[index] = (row[0], row[1], row[2], row[3], row[4], old[5], old[6], old[7])
    for index in range(9):
        fields = character_rows(index + 1)
        if fields.get("Canon locks"):
            old = CHARACTERS[index]
            CHARACTERS[index] = (*old[:-1], fields["Canon locks"].split(" · "))
    # Prefer current fresh candidates, retaining the legacy files as references.
    for key, rel in (("nil", "chr_nil_v4.png"), ("vesper", "chr_vesper_v4.png"), ("varro", "chr_varro_v4.png")):
        candidate = "art/concepts/fresh/" + rel.replace("v4", "v5")
        if not os.path.isfile(os.path.join(ROOT, candidate)):
            candidate = "art/concepts/fresh/" + rel
        if os.path.isfile(os.path.join(ROOT, candidate)):
            index = FIGURE_KEYS.index(key)
            old = CHARACTERS[index]
            CHARACTERS[index] = (*old[:6], candidate, old[7])


def build_options(kind, default_pdf):
    parser = argparse.ArgumentParser(description=f"Build the OMEN {kind} snapshot offline.")
    parser.add_argument("--check", action="store_true", help="Validate sources without writing files.")
    parser.add_argument("--html-only", action="store_true", help="Write HTML/assets/manifest; do not render PDF.")
    parser.add_argument("--output-dir", type=Path, help="Keep all derived output, including PDF, here.")
    parser.add_argument("--node", default="node", help="Node executable with Playwright available.")
    args = parser.parse_args()
    args.build_dir = (args.output_dir or Path(ROOT) / "build" / kind).resolve()
    args.pdf_path = (args.build_dir / default_pdf if args.output_dir else Path(ROOT) / "docs" / default_pdf).resolve()
    return args


def validate_sources():
    """Read-only structural checks; never claims visual or cultural acceptance."""
    problems = []
    for name in ("DECISIONS", "PROJECT_STATUS", "WORLD_BIBLE", "CHARACTER_BIBLE", "LOCATIONS", "ART_DIRECTION", "ARTBOOK_PRODUCTION", "GDD"):
        if not Path(ROOT, "docs", name + ".md").is_file():
            problems.append("Missing source: " + name)
    for n in range(1, 10):
        if not character_rows(n).get("Canon locks"):
            problems.append(f"Character section {n}: missing Canon locks row")
    if len(md_table("docs/SYSTEMS.md", "## 3.")) != 3:
        problems.append("SYSTEMS three-charm contract table missing")
    if len(CHARACTERS) != len(FIGURE_KEYS) or len(set(FIGURE_KEYS)) != len(FIGURE_KEYS):
        problems.append("Visual-index keys do not match characters")
    for _, _, _, _, _, _, art, _ in CHARACTERS:
        if art and not Path(ROOT, art).is_file():
            problems.append("Missing indexed art: " + art)
    if problems:
        raise ValueError("\n".join(problems))
    return "Source/index checks passed; not a runtime or layout acceptance."


def derivative_image(rel, build_dir, max_side=1500, quality=82):
    """Content+parameter-keyed JPEG cache; flatten alpha onto ledger cream."""
    from PIL import Image
    src = Path(ROOT, rel)
    params = {"path": rel, "max_side": max_side, "quality": quality, "background": "#F2E8D5", "algorithm": 2}
    key = hashlib.sha256(src.read_bytes() + json.dumps(params, sort_keys=True).encode()).hexdigest()[:20]
    name = src.stem + "_" + key + ".jpg"
    dest = Path(build_dir, "img", name)
    dest.parent.mkdir(parents=True, exist_ok=True)
    if not dest.exists():
        with Image.open(src) as source:
            rgba = source.convert("RGBA")
            background = Image.new("RGBA", rgba.size, "#F2E8D5")
            background.alpha_composite(rgba)
            result = background.convert("RGB")
            result.thumbnail((max_side, max_side), Image.Resampling.LANCZOS)
            result.save(dest, quality=quality, optimize=True, progressive=True)
    return "img/" + name


def derivative_video_still(rel, build_dir, t=0.6):
    src = Path(ROOT, rel)
    params = {"path": rel, "time_seconds": t, "qscale": 3, "algorithm": 1}
    key = hashlib.sha256(src.read_bytes() + json.dumps(params, sort_keys=True).encode()).hexdigest()[:20]
    name = src.stem + "_" + key + ".jpg"
    dest = Path(build_dir, "img", name)
    dest.parent.mkdir(parents=True, exist_ok=True)
    if not dest.exists():
        subprocess.run(["ffmpeg", "-v", "error", "-nostdin", "-y", "-ss", str(t), "-i", str(src), "-frames:v", "1", "-q:v", "3", str(dest)], check=True)
    return "img/" + name


def write_manifest(build_dir, kind):
    """Exact source hashes make stale books identifiable; no account metadata."""
    inputs = {}
    for folder in ("docs", "tools", "art"):
        for p in sorted(Path(ROOT, folder).rglob("*")):
            if not p.is_file() or "refinement" in p.parts or "__pycache__" in p.parts:
                continue
            if p.suffix.lower() not in {".md", ".py", ".js", ".css", ".csv", ".png", ".jpg", ".svg", ".mp4", ".blend", ".json"}:
                continue
            inputs[p.relative_to(ROOT).as_posix()] = hashlib.sha256(p.read_bytes()).hexdigest()
    snapshot = hashlib.sha256(json.dumps(inputs, sort_keys=True).encode()).hexdigest()
    payload = {"kind": kind, "source_sha256": snapshot, "inputs": inputs, "status": "derived specification/reference; runtime and visual acceptance not implied"}
    Path(build_dir).mkdir(parents=True, exist_ok=True)
    Path(build_dir, "source-manifest.json").write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return snapshot


def open_font_css(build_dir):
    """Portable OFL typography: no dependency on locally licensed Windows fonts."""
    fonts = [('OMENBody', 'BarlowSemiCondensed-Regular.ttf', 400),
             ('OMENBody', 'BarlowSemiCondensed-Bold.ttf', 700),
             ('OMENDisplay', 'BebasNeue-Regular.ttf', 400)]
    css = []
    for family, filename, weight in fonts:
        path = Path(ROOT, 'art', 'fonts', filename)
        if not path.is_file():
            raise FileNotFoundError('Vendored OFL font missing: ' + str(path))
        rel = Path(os.path.relpath(path, build_dir)).as_posix()
        css.append(f'@font-face{{font-family:"{family}";src:url("{rel}") format("truetype");font-weight:{weight};font-style:normal;}}')
    css.append(':root{--display:"OMENDisplay",sans-serif;--body:"OMENBody","Noto Sans JP","Noto Sans SC","Noto Sans Devanagari",sans-serif;}')
    return '\n'.join(css)


refresh_character_facts()
