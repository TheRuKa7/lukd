# ZERO-SUM: OMEN — Higgsfield prompt pack

Paste-ready prompts for character sketches, key art, environments and video cutscenes across every land of the Tally: Meridian (modern capital), Hyakki (Japanese folklore), the River Empire (Chinese folk religion), Śūnyapura (Indian myth and mathematics), Kroton Nova (Greek myth) and the Crossroads Territory (American folklore). Priorities: **[JAM]** = needed for the Nov 13 slice; **[LATER]** = demo and beyond.

## 1. How to use

### 1.1 Two routes
- **3D Jutsu** (Claude can drive this from the session): project **"ZERO-SUM OMEN - Look Dev"** has two layouts.
  - `CAM_pose` renders `pose_blockout.png` (2:3, full-body three-quarter pose) for every character key art, so the roster shares framing and scale.
  - `CAM_street` renders `street_blockout.png` (16:9, deep street with a tower) for city shots.
  - Call `generate_angles` with that render plus a prompt below at 2k, and start every character prompt with: *"Use the grey mannequin only as a pose and framing guide; replace it completely."*
  - Video: `generate_video` (Seedance 2.5) with an approved still as `start_image`.
- **Higgsfield web app:** image models (Nano Banana Pro, GPT Image 2.6, Seedream, Cinema Studio Image) and video models (Seedance 2.0, Kling 3.0 with a start frame, Cinema Studio Video 3.0). After a hero's key art is approved, **create an Element** and put it in every later prompt for that hero.

### 1.2 Style suffix (append to every image prompt, unchanged)
> premium anime game key art, 2.5D anime RPG character art, crisp clean lineart, cel shading with painterly soft lighting, high-detail costume design, cinematic rim light, expressive face, consistent anime proportions (about 7 heads tall), rich but controlled palette, ultra high resolution, clean silhouette that reads at small size, no text, no watermark, no logo, no extra limbs, correct hands

### 1.3 Land style lines (add to environments, VFX and cut-in textures; characters stay anime)
| Land | Style line |
|---|---|
| Meridian Undercity | *anime cyber-noir: heavy rain, neon in amber and teal, nixie-tube signage, wet reflections, stacked tenements* |
| Hyakki (Japan-inspired) | *ukiyo-e woodblock print influence: flat graphic colour fields, bold outlines, stylised Hokusai-like waves and clouds, washi paper texture, indigo, vermilion and gold* |
| River Empire (China-inspired) | harbor: *gongbi fine-line painting with gold leaf, red lanterns, lacquer and jade, festival neon* · underworld: *ink-wash shan shui, misty monochrome with vermilion seals, rice-paper texture* |
| Śūnyapura (India-inspired) | *Indian miniature painting and Pattachitra influence: ornate borders, rich mineral pigments (lapis, saffron, peacock green, gold), monsoon light, intricate geometric stepwells and stone observatory instruments* |
| Kroton Nova (Greece-inspired) | *Aegean light, white marble and deep blue sea, black- and red-figure pottery motifs, mosaic patterns, Greek key borders, bronze* |
| Crossroads Territory (America-inspired) | *Americana: desert sunset gradients, Route-66 motel neon, pulp western poster lettering style, art-deco casino lights, dust and starry night skies* |
| The Basilica | *colossal brass clockwork cathedral, monochrome with nixie amber glow, walls of scrolling numbers* |

### 1.4 Rules
- Generate 4 variations, pick 1, then iterate with the Element. Approve the style anchor before mass production.
- Log everything that ships in `docs/AI_DISCLOSURE.md`.
- Cultural review before release (World Bible §10). Deities are never shown as monsters.

---

## 2. Style anchor [JAM] (generate first, pick one)
Render: `pose_blockout.png` (2:3).
> Use the grey mannequin only as a pose and framing guide; replace it completely. Style exploration for an anime RPG called ZERO-SUM: OMEN, a world where every person has a glowing two-digit number floating above their head. A young protagonist in a long black coat standing in a rain-soaked neon alley at night, a flickering holographic "NaN" glitch above their head, glowing orange nixie-tube digits drifting in the air; around them, lucky charms from many cultures hang from wires: a horseshoe, a beckoning cat, a string of lemon and green chillies, a blue evil-eye bead, a red paper talisman. [style suffix]

Variants: add one of *(a) "bold graphic shapes, high contrast"* · *(b) "soft painterly storybook light"* · *(c) "ink outlines with brush texture"* · *(d) "glossy splash-art finish with strong bloom"*. The pick becomes `art/lookdev/style_anchor.png`.

---

## 3. Characters

**Templates** (after the key art is approved; use the Element):
- **Turnaround:** "Character turnaround sheet of {ELEMENT}: front, three-quarter, side and back views, neutral standing pose, flat light grey background, identical outfit and proportions. [style suffix]"
- **Expressions:** "Expression sheet of {ELEMENT}: neutral, smirk, laughing, angry, shocked, sad; head and shoulders; flat background. [style suffix]"
- **Battle key poses:** "{ELEMENT} in three sequential attack key poses for 2D game animation: anticipation, strike, follow-through; full body; consistent scale; flat background; motion lines. [style suffix]"
- **Ultimate splash:** "Full-screen ultimate cut-in illustration of {ELEMENT}: {ultimate}, extreme dynamic perspective, speed lines, glowing digits bursting outward. 16:9. [style suffix] [land style line]"
- **Reactions:** "{ELEMENT} reacting with {emotion}: three small poses, flat background. [style suffix]"

### 3.1 NIL, the Remainder [JAM]
> Use the grey mannequin only as a pose and framing guide; replace it completely. Full-body character concept of NIL, protagonist of an anime RPG. Androgynous young adult about 19, sharp amber eyes, messy silver-white hair with one glowing nixie-orange streak, a broken holographic "NaN" glyph flickering above the head like a cracked halo. Long asymmetric black actuary's coat with brass ledger clasps and a high collar, fingerless gloves, tall boots, a cracked brass decoder device fused into the RIGHT wrist leaking orange light and floating digits. Right arm extended, fingers spread, a spinning ring of glowing digits 0–9 orbiting the open hand. Rainy neon night, orange and teal rim light, plain dark atmospheric background. [style suffix]

Ultimate: *a fourth nixie tube tears open in the air and every digit pours out of it like a storm.*

### 3.2 Vesper Sette (7), gunslinger [JAM]
> Use the grey mannequin only as a pose and framing guide; replace it completely. Full-body character concept of Vesper Sette, a gunslinger and former casino croupier. Tall woman in her late 20s, crooked grin, small scar across her lip, black hair with a crimson underlayer in a long braid, red eyes. Crimson long coat over a black croupier's waistcoat and white shirt with rolled sleeves, wide-brim black hat with playing cards in the band, a large revolver with a seven-chamber cylinder engraved 1–7 held forward, faint red glowing "7" motifs. Mix of neon noir and western frontier. [style suffix]

Ultimate: *seven muzzle flashes in a ring around her, each bullet trailing a glowing red 7.*

### 3.3 Maeve Triskel (3), charm-smith [JAM]
> Use the grey mannequin only as a pose and framing guide; replace it completely. Full-body character concept of Maeve Triskel, a cheerful blacksmith's daughter from a Celtic immigrant quarter of a neon city. Freckled young woman around 20, bright red hair in three braids, green eyes, leather forge apron over rolled-sleeve work clothes, heavy boots, horseshoe-shaped knuckle gauntlets glowing copper-hot, a four-leaf-clover pin on her collar, a forge hammer with a triskele (triple spiral) burned into its head, sparks around her. Warm copper and green palette against a dark forge. [style suffix]

Ultimate: *three spinning red-hot horseshoes orbit her and slam down, each stamping a glowing 3.*

### 3.4 Hina of the Ninety-Nine (9), tsukumogami [JAM]
> Use the grey mannequin only as a pose and framing guide; replace it completely. Full-body character concept of Hina, a playful tsukumogami spirit born from a 99-year-old Japanese paper umbrella. Small girl-shaped spirit with a short black bob and mischievous golden eyes, a furisode kimono patterned with tiny numbers 1 to 99 in indigo and vermilion, geta sandals, holding a large red-and-white oiled-paper umbrella that has one big eye and a long tongue like a kasa-obake, umbrella ribs glowing faintly, a floating "99" above her head. Paper lanterns and fireflies, night shrine backdrop. [style suffix] Ukiyo-e flat colour accents on the kimono pattern.

Ultimate: *her umbrella spins open into a giant one-eyed moon and a parade of tiny yokai pours out beneath it.*

### 3.5 Varro Kade, the Ledgerhound [JAM] (Prologue boss)
> Use the grey mannequin only as a pose and framing guide; replace it completely. Full-body boss concept of Varro Kade, a debt collector and bounty hunter in a neon slum. Hulking man, heavy riot-armour trench coat in rust and gunmetal, a hound-skull mask with glowing red eyes, chains of glass debt jars on his belt each holding a floating glowing digit, a massive hooked collection baton, his Omen "61" floating above his head in red. Rain, neon, steam, low angle. [style suffix]

### 3.6 Tamamo, the Nine-Tailed Auditor [JAM] (Act I boss)
> Use the grey mannequin only as a pose and framing guide; replace it completely. Full-body boss concept of Tamamo, an elegant and dangerous nine-tailed fox spirit from Japanese folklore. Tall, beautiful woman with fox ears, long gold-white hair, sly violet eyes with red eye-liner, layered Heian-style courtly robes in gold, violet and white, nine enormous glowing fox tails fanned behind her, each tail tip holding a floating glowing digit, blue-white foxfire flames drifting around her, a folding fan in one hand. Moonlit palace, ukiyo-e cloud shapes in the background. [style suffix] [Hyakki style line]

### 3.7 Comptroller Lucan Thale [JAM] (intro narrator; teaser)
> Full-body character concept of Comptroller Lucan Thale, the calm and sympathetic villain. Tall ageless man, swept-back silver hair, immaculate white and brass vestments shaped like a clockwork cathedral, a monocle with a slowly turning gear, gloved hands folded, a steel (not glowing) "50" floating above his head. Before enormous brass gears and a wall of scrolling numbers in cold gold light. [style suffix]

### 3.8 Later roster and bosses [LATER]
- **Ba Jinling (8), River Empire:** elegant woman in a modern jade-and-gold qipao, eight tiny golden bells in her hair ornaments and anklets, a folding fan whose ribs are abacus rods, smoky violet eyes, red lips; red lanterns and gold-leaf harbor behind. [gongbi line]
- **Bai Si (4), River Empire underworld:** very tall pale man, long white hair bound with black funeral ribbons, white mourning robes with black ink 四 sigils, a huge guandao-style blade hung with four paper talismans, joss paper swirling, four lanterns behind him. [ink-wash line]
- **Shunya (0), Śūnyapura:** young woman astronomer-mathematician, long dark braid with brass astrolabe hairpins, indigo-and-saffron layered clothing with mirror-work embroidery, a large brass astrolabe spinning in her hand like a weapon, palm-leaf manuscripts tied at her hip, ink-stained fingers, a glowing "0" that looks like a full circle of light; stone observatory instruments behind. [Śūnyapura line]
- **Prima of Kroton (2), Kroton Nova:** earnest young paladin, short blonde hair, blue eyes, white-and-gold armour with Greek-key borders, a giant round shield shaped like a sieve set with blue glass, a halo of floating glyphs 2-3-5-7; white marble and Aegean sea behind. [Kroton line]
- **Fibi Leone (Fibonacci), Crossroads:** 18-year-old casino dealer, golden spiral-curled hair, spiral-patterned irises, tailored croupier tailcoat with headset, glowing cards flowing around her in a golden spiral; desert casino neon behind. [Crossroads line]
- **Chancellor Jin Chan, the Golden Toad:** enormous jovial lord robed in gold coins on a three-legged toad throne, coins spilling from his mouth. [gongbi line]
- **Rahu & Ketu, the Eclipse** (cosmic, tragic, awe-inspiring, *not* demonic or grotesque): a vast crowned celestial head devouring a sun's light, and a separate headless serpentine body with a comet's tail, in a star-filled monsoon sky. [Śūnyapura line] *Have a cultural reviewer check before use.*
- **Archon Seventeen:** gaunt, beautiful, severe hierarch in white and bronze, laurel crown of bronze, a staff topped with a sieve-shaped disc, a cold "17" overhead. [Kroton line]
- **The House (Mr. Eighty-Nine):** elegant old croupier in a white suit at a desert crossroads under a single streetlamp at midnight, ouroboros tattoo around his throat, a pocket watch running backwards. [Crossroads line]
- **Keepers (shown with reverence):** Enma as a towering, solemn judge in red robes with a great ledger (Hyakki) · Judge Cui with a giant brush and the Book of Life and Death (River Empire) · Chitragupta as a serene scribe writing on palm leaves by lamplight (Śūnyapura) · the Moirai spinning, measuring and cutting a glowing thread in a cave (Kroton Nova).

---

## 4. Environments
Battle-stage rule: **16:9, empty centre-left floor for 3 heroes, empty right side for the enemy, clear space top-centre for the land's reel object, horizon around 60%.**

### 4.1 Meridian Undercity (Prologue) [JAM]
- **Establishing** (render `street_blockout.png`): "Anime cyber-noir slum beneath a giant brass cathedral tower, stacked tenements, neon signs showing two-digit numbers, charms from many cultures hanging over doorways (horseshoes, beckoning cats, lemon-and-chilli strings, evil-eye beads, red paper talismans), heavy rain, crowds with small glowing numbers above their heads, a searchlight beam sweeping the alley at dawn. [Meridian line] [style suffix]"
- **Battle stage:** "Wide side-on battle background: a rain-soaked neon alley with a broken drain gate, puddles, a dead neon sign shaped like three nixie tubes at top centre, empty floor space, foreground pipes. [Meridian line] [style suffix]"
- **Naming shrine:** "A cramped black-market shrine, an old jury-rigged terminal of brass dials and ten glowing nixie tubes on an altar, incense smoke, charms from many cultures, a single amber lamp. [style suffix]"

### 4.2 Hyakki (Act I) [JAM]
- **Establishing:** "A misty Japanese-inspired island town at night under a giant full moon, a huge stylised wave curling around the harbor, a long red bridge with a Night Parade of one hundred yokai crossing it (umbrella spirits, lantern ghosts, kappa, foxes), torii gates climbing a hill, paper lanterns everywhere. [Hyakki line] [style suffix]"
- **Battle stage A (the Night Parade bridge):** "Wide side-on battle background on a red arched bridge at night, rows of paper lanterns, a torii gate at top centre with three large hanging lanterns (the reel), fog over dark water below, distant yokai silhouettes, empty floor space. [Hyakki line] [style suffix]"
- **Battle stage B (Tamamo's foxfire palace):** "Wide side-on battle background inside a moonlit palace hall with sliding shoji doors painted with nine-tailed foxes, blue-white foxfire floating, gold-leaf folding screens, empty floor space. [Hyakki line] [style suffix]"
- **Shrine of the Seven Lucky Gods:** "A small hillside shrine with seven statues of the Seven Lucky Gods, a treasure ship carving, daruma dolls and beckoning cats on the steps, morning mist. [Hyakki line] [style suffix]"

### 4.3 Later lands [LATER]
- **River Empire:** Bāfā Harbor Lantern Festival over the Luck Exchange (golden abacus reel), and the Ten Courts with Naihe Bridge and endless shelves of ledgers.
- **Śūnyapura:** "a monsoon city built around a colossal stone open-air observatory with giant sundials and astrolabes, a geometric stepwell descending in perfect symmetry, lamps reflecting in rain pools" (reel = three sundial dials).
- **Kroton Nova:** "a white marble island city shaped like a gigantic stone sieve above a deep blue Aegean sea, mosaics of numbers, bronze automata on patrol" (reel = three columns with mosaic numerals).
- **Crossroads Territory:** "a desert crossroads at midnight under one streetlamp, a lone signpost, starry sky; beyond it the casino boomtown of Lucky Strike glowing with art-deco neon, a ghost train crossing the horizon" (reel = a giant slot machine).
- **The Basilica:** clockwork cathedral interior whose walls show every land's original ledger.

---

## 5. Enemies [JAM]
- **Debt Hound:** "Lean cyber-dog with a debt-collector's collar, red digit display on its flank, sparking jaw, side view, flat background. [style suffix]"
- **Collector:** "Armoured slum bailiff with a riot shield stamped with a ledger seal and a glowing number overhead, side view. [style suffix]"
- **Noiseling:** "Small glitch creature made of scrambled floating digits and static, cute but unsettling, side view. [style suffix]"
- **Kasa-obake:** "Hopping one-eyed paper umbrella spirit with a long tongue and a single wooden leg, mischievous, side view. [Hyakki line] [style suffix]"
- **Chōchin-obake:** "Floating paper lantern ghost with a torn mouth and glowing eyes, flames inside, side view. [Hyakki line] [style suffix]"
- **Kappa:** "Turtle-shelled river imp with a water-filled dish on its head, webbed hands, cheeky expression, side view. [Hyakki line] [style suffix]"
- **Oni enforcer:** "Red-skinned horned ogre in a debt-collector's haori jacket with an iron club studded with numbers, side view. [Hyakki line] [style suffix]"

---

## 6. Intro cinematic (video) [JAM]
Make a still for each shot (same Elements), then animate it as the **start image**. 720p, 16:9.

| # | Length | Start still prompt | Motion prompt |
|---|---|---|---|
| 1 | 8 s | Abstract chaos: floods, toppling towers, hail shaped like dice, rendered in ink splashes and digital static | Ink and static churn violently; dice-hail falls; slow push-in |
| 2a | 4 s | Three women of Greek myth spinning, measuring and cutting a glowing thread, in red-figure pottery style on black | The thread glows and runs off-frame to the right like a fuse |
| 2b | 4 s | A serene scribe writing on palm-leaf pages by lamplight, Indian miniature painting style with ornate border | Script glows on the palm leaves and lifts into the air as numbers |
| 2c | 4 s | A judge with a giant brush writing in an enormous Book of Life and Death, ink-wash style | Characters lift off the page and become glowing numbers |
| 2d | 4 s | A towering solemn judge in red robes opening a great ledger as a lantern-lit parade of yokai passes, ukiyo-e woodblock style | Lanterns sway; the ledger's pages flip in the wind |
| 2e | 4 s | A hand signing a black book under a lone streetlamp at a desert crossroads at midnight, Americana woodcut style | The ink signature glows red; the streetlamp flickers |
| 3 | 12 s | A colossal brass clockwork cathedral rising over a modern city; brass chains reaching out to five glowing books and scrolls from different art styles | The chains drag the five ledgers into the cathedral; gears swallow them; its eye opens and a sunrise beam sweeps the world as a number appears above every head |
| 5 | 15 s | Dawn in a neon slum: crowds with glowing numbers overhead; a tired mother with "01", her small son staring at it | Camera cranes down through rain; numbers tick; the mother's number flickers to 01; the boy grabs her sleeve |
| 6 | 10 s | Armoured debt collectors with hound masks pushing through the crowd; one hooded figure with a broken "NaN" glitch stays still | Collectors advance in slow motion; the hood lifts to reveal NIL's amber eyes; NaN crackles |
| 7 | 8 s | NIL's hand reaching toward the mother; a ring of glowing digits spinning around her "01" | Digits spin like a slot reel and lock on "07" with a flash; collectors turn toward NIL |
| 8 | 12 s | NIL running through neon alleys hung with charms from many cultures, collectors and cyber-dogs behind | Fast anime chase: low tracking, splashing puddles, sliding under pipes, ducking into an amber-lit shrine doorway |
| 10 | 10 s | Every screen and sign in the city glitching to "REMAINDER DETECTED"; the cathedral's eye glowing red | The glitch spreads screen to screen; numbers above every head scramble; bounty posters with NIL's face flutter down in the rain |

Shots 4 (title), 9 (lucky-number choice) and 11 (logo slam) are built in-engine.

---

## 7. Ultimates and Link Arts [JAM]
- **Ultimate clips (3–4 s):** start image = the hero's ultimate splash. Motion: *"Explosive anime ultimate, fast camera push, speed lines, glowing digits bursting outward, impact flash, hold."*
- **Lucky Strike (Vesper + Maeve):** still: *"Maeve hurling a red-hot horseshoe through the air while Vesper aims her revolver at it, neon alley"*; motion: *"Vesper shoots the horseshoe mid-air; it shatters into seven glowing ricochets that converge on the target."*
- **Midnight Parade (Hina + Vesper):** still: *"Hina riding her one-eyed umbrella over swinging saloon doors as a parade of ukiyo-e yokai pours through behind her, Vesper tipping her hat"*; motion: *"the yokai stampede across the screen in woodblock style while Vesper fires through the gaps."*
- **Land cut-in bands:** neon-glitch bands (Meridian) and **woodblock-print wave bands** (Hyakki), built in-engine from generated textures.

---

## 8. Land-styled reel objects [JAM]
- Meridian: "A dead neon sign shaped like three nixie tubes in a rusted brass frame, front view, flat background."
- Hyakki: "A vermilion torii gate with three large paper lanterns hanging from its beam, each lantern able to show one painted numeral, front view, flat background."
