# ZERO-SUM: OMEN — Higgsfield prompt pack

Paste-ready prompts for character sketches, key art, environments and video cutscenes. Priorities are marked **[JAM]** (needed for the Nov 13 slice) or **[LATER]**.

## 1. How to use

### 1.1 Two routes
- **3D Jutsu (what Claude can drive from this session):** project **"ZERO-SUM OMEN - Look Dev"** already contains two layouts.
  - `CAM_pose` renders `pose_blockout.png` (2:3, full-body three-quarter hero pose). Use it for every character key art so the whole roster shares framing and scale.
  - `CAM_street` renders `street_blockout.png` (16:9, deep street with a tower). Use it for city establishing shots and battle stages.
  - Call `generate_angles` with that render plus a prompt below, at 2k. Start every character prompt with: *"Use the grey mannequin only as a pose and framing guide; replace it completely."*
  - Video: `generate_video` (Seedance 2.5) with an approved still as `start_image`, or text-only.
- **Higgsfield web app:** use the image models (Nano Banana Pro, GPT Image 2.6, Seedream 4.5/5, Cinema Studio Image) and video models (Seedance 2.0, Kling 3.0 with a start frame, Cinema Studio Video 3.0). After a hero's key art is approved, **create an Element** from it and put the Element placeholder in every later prompt for that hero.

### 1.2 Style suffix (append to every image prompt, unchanged)
> premium anime game key art, 2.5D anime RPG character art, crisp clean lineart, cel shading with painterly soft lighting, high-detail costume design, cinematic rim light, expressive face, consistent anime proportions (about 7 heads tall), rich but controlled palette, ultra high resolution, clean silhouette that reads at small size, no text, no watermark, no logo, no extra limbs, correct hands

For Chinese regions, add the region line from §4 (ink-wash or gongbi), but **keep the anime character rendering**: the region style applies to environments, VFX and outlines, not to the characters' faces.

### 1.3 Model notes
- Generate 4 variations, pick 1, then iterate with the Element. Never mass-produce before the style anchor is approved.
- Log everything that ships in `docs/AI_DISCLOSURE.md`.

---

## 2. Style anchor [JAM] (generate first, pick one)

Render: `pose_blockout.png` (2:3).

> Use the grey mannequin only as a pose and framing guide; replace it completely. Style exploration for an anime RPG called ZERO-SUM: OMEN, a world where every person has a glowing two-digit number floating above their head. A young protagonist in a long black coat standing in a rain-soaked neon alley at night, a flickering holographic "NaN" glitch above their head, glowing orange nixie-tube digits drifting in the air, wet reflections, teal and amber lighting. [style suffix]

Make 4 variants by adding one of: *(a) "sharper, more graphic, Persona-like bold shapes"* · *(b) "softer, painterly, Reverse:1999-like storybook light"* · *(c) "high-contrast ink outlines with brush texture"* · *(d) "glossy gacha-splash finish with strong bloom"*. Pick one; it becomes `art/lookdev/style_anchor.png`.

---

## 3. Characters

Template for each hero after key art is approved (use the Element):
- **Turnaround:** "Character turnaround sheet of {ELEMENT}: front, three-quarter, side and back views, neutral standing pose, flat light grey background, same outfit and proportions in every view. [style suffix]"
- **Expressions:** "Expression sheet of {ELEMENT}: neutral, smirk, laughing, angry, shocked, sad; head and shoulders; flat background. [style suffix]"
- **Battle key poses:** "{ELEMENT} in three sequential attack key poses for 2D game animation: anticipation, strike, follow-through; full body; consistent scale; flat background; dynamic motion lines. [style suffix]"
- **Ultimate splash:** "Full-screen ultimate cut-in illustration of {ELEMENT}: {ultimate description}, extreme dynamic perspective, speed lines, glowing digits, dramatic. 16:9. [style suffix]"
- **Reaction poses:** "{ELEMENT} reacting with {emotion}: three small poses for a battle UI, flat background. [style suffix]"

### 3.1 NIL — the Remainder [JAM]
> Use the grey mannequin only as a pose and framing guide; replace it completely. Full-body character concept of NIL, protagonist of an anime RPG. Androgynous young adult about 19, sharp amber eyes, messy silver-white hair with one glowing nixie-orange streak, a broken holographic "NaN" glyph flickering above the head like a cracked halo. Long asymmetric black actuary's coat with brass ledger clasps and a high collar, fingerless gloves, tall boots, a cracked brass decoder device fused into the RIGHT wrist leaking orange light and floating translucent digits. Right arm extended, fingers spread, a spinning ring of glowing digits 0–9 orbiting the open hand. Rainy neon night, orange and teal rim light, plain dark atmospheric background. [style suffix]

Ultimate: *"Remainder Release": NIL slams the decoder wrist forward and a fourth nixie tube tears open in the air, a storm of every digit pouring out.*

### 3.2 Vesper Sette — 7 [JAM]
> Use the grey mannequin only as a pose and framing guide; replace it completely. Full-body character concept of Vesper Sette, a gunslinger and former casino croupier in an anime RPG. Tall woman in her late 20s, confident crooked grin, small scar across her lip, black hair with crimson underlayer in a long braid, sharp red eyes. Crimson long coat over a black croupier's waistcoat and white shirt with rolled sleeves, wide-brim black hat with playing cards tucked in the band, cards in her garters, a large revolver with a seven-chamber cylinder engraved with digits 1–7 held forward in her extended hand, faint red glowing "7" motifs. Neon casino-noir lighting, plain dark background. [style suffix]

Ultimate: *"Seven-Chamber Requiem": seven muzzle flashes in a ring around her, each bullet trailing a glowing red 7.*

### 3.3 Ling 零 — 0 [JAM]
> Use the grey mannequin only as a pose and framing guide; replace it completely. Full-body character concept of Ling, a blind wandering monk in an anime RPG with Chinese ink-wash influences. Man in his 40s with a calm half-smile, shaved head with a black ink ensō circle tattooed on the crown, white cloth blindfold, tattered layered grey monk robes with ink-stain edges, prayer beads, a wooden begging bowl whose inside shows a starless void, a tall monk's staff with ten iron rings held in the extended hand. A faint floating "00" above his head that never fades. Misty mountain light, soft grey and white palette with one vermilion accent, plain pale background. [style suffix] Ink-wash brush texture on the outlines only.

Ultimate: *"Ensō": Ling draws a perfect black ink circle in the air with his staff; everything inside it freezes.*

### 3.4 Bai Si 白四 — 4 [JAM] (Act I boss, then companion)
> Use the grey mannequin only as a pose and framing guide; replace it completely. Full-body character concept of Bai Si, the White Executioner, a tragic boss and later companion in an anime RPG set in Chinese ink-wash mountains. Very tall pale man, stern beautiful face, long straight white hair bound with black funeral ribbons, white mourning robes with black ink calligraphy sigils of the number four (四), a huge guandao-style polearm blade hung with four yellow paper talismans, joss paper swirling around him, four small paper lanterns floating behind him. Cold moonlight, misty mountain backdrop, monochrome palette with vermilion seal accents. [style suffix]

Ultimate: *"Four Lanterns Out": the four lanterns behind him go out one by one, each blackout a white slash across the screen.*

### 3.5 Varro Kade — the Ledgerhound [JAM] (Prologue boss)
> Use the grey mannequin only as a pose and framing guide; replace it completely. Full-body boss concept of Varro Kade, a debt collector and bounty hunter in an anime cyber-noir slum. Hulking man, heavy riot-armour trench coat in rust and gunmetal, a mask shaped like a hound's skull with glowing red eyes, chains of glass debt jars on his belt each holding a floating glowing digit, a massive hooked collection baton, his Omen number "61" floating above his head in red. Rain, neon, steam, low angle. [style suffix]

### 3.6 Comptroller Lucan Thale [JAM] (intro narrator; seen in teaser)
> Full-body character concept of Comptroller Lucan Thale, the calm and sympathetic villain of an anime RPG. Tall ageless man with an immaculate face, swept-back silver hair, immaculate white and brass vestments shaped like a clockwork cathedral, a monocle with a slowly turning gear, gloved hands folded, a steel (not glowing) number "50" floating above his head. Standing before enormous brass gears and a wall of scrolling numbers. Cold gold light. [style suffix]

### 3.7 Later roster [LATER]
- **Ba Jinling 八金铃 (8):** elegant woman, modern jade-and-gold qipao, eight tiny golden bells in her hair ornaments and anklets, a folding fan whose ribs are abacus rods, smoky violet eyes, red lips, gold-leaf (gongbi) accents; Bāfā Harbor lanterns behind.
- **San 三 (3):** 16-year-old rooftop thief, cat-eared hood (a hood, not real ears), three red ribbon tails, three-section staff, patched layered streetwear with festival motifs, bandaged knuckles, cocky grin; red lantern rooftops at night.
- **Meng Lan 孟岚 (9):** sleepy-eyed young woman, lavender-grey hair in twin buns with ladle-shaped hairpins, flowing pale-blue hanfu trailing mist, lacquered soup gourd and porcelain bowl; ghost-blue underworld bridge; Dunhuang mural palette.
- **Sister Prima (2):** earnest young paladin, short blonde hair, blue eyes, white-and-gold armour, a giant stained-glass shield shaped like a sieve, a halo of floating glyphs 2-3-5-7; gothic cathedral light.
- **Fibi Leone (Fibonacci):** 18, golden spiral-curled hair, spiral-patterned irises, tailored croupier tailcoat with headset, a deck of glowing cards flowing around her in a golden spiral; art-deco casino at night.
- **Bosses:** Chancellor Jin Chan (enormous jovial lord robed in gold coins on a three-legged toad throne) · Judge Cui (ancient magistrate in black and crimson robes with a winged hat, holding a giant calligraphy brush, the Book of Life and Death open in the air) · Cardinal Seventeen (gaunt and beautiful, stained-glass halo, sieve-shaped crozier) · The House / Mr. Eighty-Nine (elegant old croupier, ouroboros tattoo around his throat, a pocket watch running backwards).

---

## 4. Environments

Battle-stage rule: **16:9, empty centre-left floor for 3 heroes, empty right side for the enemy, clear space top-centre for the reel object, horizon at about 60%.** Generate the establishing shot and battle stage as separate images.

### 4.1 Remainder Wards (Prologue) [JAM]
- **Establishing** (render `street_blockout.png`): "Anime cyber-noir slum beneath a giant cathedral-like tower of brass, stacked tenements, neon signs in orange and teal showing two-digit numbers, laundry lines, steam, heavy rain, wet street reflections, crowds with small glowing two-digit numbers floating above their heads, the tower's searchlight beam sweeping the alley at dawn. [style suffix]"
- **Battle stage:** "Wide side-on anime battle background: a rain-soaked neon alley with a broken drain gate, puddles, a large dead neon sign shaped like three nixie tubes hanging at top centre, empty floor space for characters, depth with foreground pipes. [style suffix]"
- **Naming shrine interior:** "A cramped black-market shrine in a neon slum, an old jury-rigged terminal of brass dials and ten glowing nixie tubes on an altar, incense smoke, paper charms, cables, a single amber lamp. [style suffix]"

### 4.2 Sì Shan 四山, the Fourth Gate Mountains (Act I) [JAM]
Region line: *"Chinese ink-wash shan shui painting style for the environment: misty layered mountains, brush-stroke pines, monochrome ink with vermilion seal accents, rice-paper texture."*
- **Establishing:** "Sheer misty mountains with stone stairways climbing between pines, four great stone gates on the path each with a glowing paper lantern, a Taoist-style monastery clinging to the cliff, paper talismans fluttering. [region line] [style suffix]"
- **Battle stage A (mountain path):** "Wide side-on battle background on a mountain stair landing, a tall stone stele carved with three numeral slots at top centre, mist below, pines, hanging lanterns, empty floor for characters. [region line] [style suffix]"
- **Battle stage B (the Fourth Gate):** "Wide side-on battle background before an enormous stone gate carved with 四, four tall lanterns, falling joss paper, moonlight, empty floor for characters. [region line] [style suffix]"

### 4.3 Later regions [LATER]
- **Bāfā Harbor 八发港:** gongbi fine-line and gold leaf + neon; red lanterns, dragon boats, abacus towers, festival fireworks; reel = a golden abacus.
- **The Ten Courts 十殿:** Dunhuang mural palette (lapis, malachite, ochre), Naihe Bridge over a ghost river, endless ledgers on shelves; reel = a floating ghost ledger.
- **The Sieve:** white marble cathedral-city shaped like a sieve, stained glass, citizens falling through holes; reel = a rose window.
- **Ouroboros Isles:** art-deco casino islands, magenta neon, clocks running backwards; reel = a giant slot machine.
- **Meridian / the Basilica:** clockwork cathedral interior, walls of scrolling numbers; reel = the Basilica clock.

---

## 5. Enemies [JAM]
- **Debt Hound:** "Lean cyber-dog with a debt-collector's collar, glowing red digit display on its flank, sparking jaw, side view, flat background. [style suffix]"
- **Collector:** "Armoured slum bailiff with a riot shield stamped with a ledger seal and a glowing number above his head, side view. [style suffix]"
- **Noiseling:** "Small glitch creature made of scrambled floating digits and static, cute but unsettling, side view. [style suffix]"
- **Jiangshi:** "Chinese hopping vampire in Qing-style official robes with a yellow paper talisman on the forehead, arms outstretched, pale ink-wash shading, side view. [style suffix]"
- **Paper Effigy:** "Life-size joss-paper soldier made of folded red-and-gold funeral paper, ink-painted face, side view. [style suffix]"
- **Tetrad Acolyte:** "Masked Tetrad monk in white mourning robes with the character 四 on the mask, holding a lantern staff, side view. [style suffix]"

---

## 6. Intro cinematic shots (video) [JAM]

Make a still for each shot first (same Elements), then animate it as the **start image**. 720p, 16:9. Durations match the World Bible §8.

| # | Length | Start still prompt | Video (motion) prompt |
|---|---|---|---|
| 1 | 10–15 s | Ink-wash painting of a world in chaos: flooding rivers, toppling pagodas, hail shaped like dice, tiny fleeing people, monochrome ink with vermilion | Slow push-in; ink bleeds and swirls like water; dice-hail falls; brush strokes animate the flood; no text |
| 2 | 10–15 s | An ancient judge in black-and-crimson robes writing with a giant brush in an enormous open book; calligraphy characters lifting off the page | The characters rise from the page and turn into glowing two-digit numbers that float up over a crowd of ink-wash people; ink-wash shifts to gold |
| 3 | 10–12 s | A colossal brass clockwork cathedral rising over a Western city, gears swallowing a glowing book, a searchlight beam sweeping the world | Gears turn; the cathedral's eye opens; a wide beam sweeps across the land at sunrise and numbers above every head flicker as it passes |
| 5 | 10–15 s | Dawn in a neon slum: crowds with floating glowing numbers; a tired mother with "01" above her head, her small son staring up at it | Camera cranes down through rain and neon; numbers above the crowd tick up and down; the mother's number flickers to 01; the boy grabs her sleeve |
| 6 | 8–12 s | Armoured debt collectors with hound masks pushing through the crowd; the crowd parting; one hooded figure stays still with a broken "NaN" glitch above their head | Collectors advance in slow motion; the hood lifts slightly to reveal NIL's amber eyes; the NaN glitch crackles |
| 7 | 6–10 s | NIL's hand reaching toward the mother; a ring of glowing digits spinning around her number "01" | The digits spin like a slot reel and lock on "07" with a flash; the collectors freeze, turning their heads toward NIL |
| 8 | 10–15 s | NIL running through narrow neon alleys, coat flaring, collectors and cyber-dogs behind | Fast anime chase: low tracking shots, splashing puddles, jumping a fence, sliding under pipes, ducking into a shrine doorway lit by amber light |
| 10 | 8–12 s | Every screen and sign across the neon city glitching to the words "REMAINDER DETECTED"; the cathedral's eye glowing red | Glitch spreads screen to screen across the city; numbers above every head scramble; bounty posters with NIL's face print and flutter down in the rain |

Shots 4 (title), 9 (lucky-number choice) and 11 (logo slam) are built in-engine.

---

## 7. Cut-ins, ultimates and Link Arts [JAM]
- **Ultimate clips (3–4 s each):** start image = the hero's ultimate splash (§3). Motion prompt: *"Explosive anime ultimate move, fast camera push, speed lines, glowing digits bursting outward, impact flash at the end, then a hold."*
- **Link Art (example, Vesper + NIL Twins on 7):** start still *"Vesper and NIL back to back in a neon alley, Vesper's revolver and NIL's ring of digits both aimed forward, seven glowing red 7s orbiting them"*; motion *"they spin back to back, firing; seven 7s converge into one giant blazing 7 that slams forward."*
- **Region cut-in bands:** neon-glitch bands for the Wards; **ink-brush stroke bands** for Sì Shan (make these in-engine with brush textures; still generation is only for the textures).

---

## 8. Region-styled reel objects [JAM]
- Wards: "A dead neon sign shaped like three nixie tubes in a rusted brass frame, front view, flat background."
- Sì Shan: "A weathered stone stele with three carved recessed numeral slots, moss and paper talismans, front view, flat background."
