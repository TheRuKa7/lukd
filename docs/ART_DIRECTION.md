# ZERO-SUM: OMEN — Art Direction v2

**"Painted world, inked people."** Hand-painted, sunlit, lived-in **worlds in the spirit of Studio Ghibli's backgrounds**, inhabited by **graphic, high-contrast, neon-edged characters and action in the spirit of Studio Trigger's *Cyberpunk: Edgerunners***.

The two styles are not mixed at random. They carry the game's theme:
- **The lands** (the old, plural ways of seeing luck: nature, craft, community) are **painted**: soft air, warm light, weather, moss, laundry, cats on roofs.
- **Meridian and the Basilica** (the machine that flattens luck into one number) are **neon and graphic**, and so is **combat**, where numbers fight.
- As the story moves, the neon of the machine intrudes on the painted lands (Noise storms, Auditors), and the finale reverses it.

This file replaces the style sections of the prompt pack. If a rule here conflicts with older docs, this file wins.

---

## 1. What went wrong in pass 1 (honest diagnosis)

| Problem | Why it looks cheap | Fix in v2 |
|---|---|---|
| **AI gloss**: airbrushed gradients on skin and cloth, plastic highlights, everything rendered to the same detail | Reads as "generic AI anime illustration", not a production frame | Characters use **flat cel shading: 2 tones + 1 hard rim light**, no gradients except a hint on hair. Detail goes where the eye should go. |
| **No hierarchy between character and background**: both painted the same way | Characters don't pop; the image is mush | Anime's oldest rule: **flat cel characters on painted backgrounds**. Different rendering for each layer. |
| **Stiff, centred gacha poses** from one mannequin | Every character feels like a figurine on a turntable | Poses from **gesture and story**: lunges, leans, foreshortening, Dutch angles for action; quiet, grounded poses for drama. |
| **Muddy teal-and-orange everywhere** | No identity; characters don't read at thumbnail size | **One signature colour per character** plus a land colour script (§4). Value contrast first, hue second. |
| **Thin, uniform or missing lineart** | Shapes melt into the background | **Variable-weight coloured lines**: thick silhouette, thin interior, line colour tinted toward the local colour (never pure black on skin). |
| **Floating digits and "Nixie" glow everywhere** | The motif becomes noise and creates text artefacts | Numbers appear **only where the fiction puts them**: Omens over heads, wheels, the reel, signage. |
| **Over-detailed, evenly lit backgrounds** | No air, no time of day, no story | **Atmospheric perspective, one clear light source, weather, and lived-in details** chosen on purpose. |

---

## 2. The two halves

### 2.1 The painted world (Ghibli-inspired backgrounds)
What the research says about how those backgrounds are made (sources at the end):
- **Medium:** gouache-like *poster colour*, opaque but handled so gradations "look like transparent watercolor"; **a small palette (~21 colours) mixed subtly**; never a thick coat.
- **Process:** the base wash goes down wet, on pre-wetted paper, which is where the soft cloud edges and natural gradations come from; detail is added after it dries.
- **Philosophy:** *"He's not rendering everything. But he is rendering the little things."* The background painter extracts "the essence of important elements of the scene" and augments it. Backgrounds serve the film's vision, and they come from **on-site observation** (mist rising from valleys, the way real foliage grows), not from photos.

**Our rules:**
1. **Gouache look**: visible but soft brush texture, opaque colour, wet-edge gradients in skies, slightly matte. No photo textures, no 3D-render sheen.
2. **A limited palette per land** (≈20 colours), mixed subtly.
3. **Light tells the time.** Every background has one motivated light source and a time of day: warm late-afternoon sun, blue dusk, lantern night, rain dawn.
4. **Air.** Distant planes get lighter, cooler and softer (atmospheric perspective). Big skies with towering cumulus or layered stratus.
5. **Render the little things on purpose**: one cat, a drying futon, a bicycle, potted plants on a fire escape, a hand-written shop sign, moss on a stone. Two or three per frame, not fifty.
6. **Nature wins**: plants grow out of everything, even in Meridian. It's the visual sign of the old plural world surviving.
7. **Layouts for play**: battle plates have a clear floor plane, a calm area behind the fighters, and the reel object top-centre (GDD §8).

### 2.2 The inked people and the fights (Edgerunners-inspired)
What the research says:
- **Colour carries character and emotion.** Imaishi (director): small differences in age and clothing texture vanish in 2D animation, so **characters are told apart mainly by colour**. There are **no rules for rim-light colours; they're matched to the scene's emotion**. The high-contrast palette came out of *Promare* (Shigeto Koyama's colour design).
- **Motion:** in the famous slow-motion sequences, each frame of a movement is drawn and **tinted a different colour**, spreading the frames out to stretch time.
- **Design:** Yoh Yoshinari's designs are deliberately cartoon-ish and stylish. In his words, the look is "associated with very retro anime". A large library of hand-drawn effects animation does the heavy lifting.
- The neon identity leans on a **loud yellow / magenta / cyan** scheme.

**Our rules for characters:**
1. **Silhouette first.** Each character is built on one dominant shape and readable as a black fill at 64 px tall:

| Character | Shape | Signature colour | Secondary |
|---|---|---|---|
| NIL | Tall rectangle + broken circle (the NaN halo, the coat) | Nixie orange `#FF7A2C` | Ink black, bone white |
| Vesper | Triangles (hat brim, coat tails, gun) | Crimson `#E5243B` | Black, brass |
| Maeve | Circles and arcs (braids, horseshoes) | Copper `#D9822B` | Clover green `#3BB273` |
| Hina | Dome (the umbrella) on a small body | Vermilion `#E34234` | Indigo `#26428B` |
| Tamamo | Fan and crescent (tails) | Violet `#8E44AD` | Gold `#F4C430` |
| Varro | Square block | Rust `#B7410E` | Gunmetal |
| Thale | Cathedral arch | Steel white `#E8E6E1` | Brass `#B5A642` |

2. **Proportions:** lean and long-legged (about 7.5–8 heads), small heads, angular jaws and wrists, big readable hands. Faces are simple: clean eye shapes, no glossy multi-highlight eyes, small nose and mouth marks.
3. **Cel shading:** **base + one shadow tone** with hard edges, plus **one hard rim light** whose colour follows the emotion (Imaishi's rule): orange for resolve, cyan for cold fear, magenta for danger, gold for luck. No airbrush.
4. **Lineart:** coloured lines (dark wine on skin, deep navy on clothes), thicker on the outside silhouette and thinner inside; slightly tapered, as if inked.
5. **Expressions are big.** Trigger-style exaggeration for comedy and shock, then calm, still drawing for sincere moments (the Ghibli half).
6. **Costume logic:** every costume detail is a story detail (NIL's ledger clasps, Vesper's 7-chamber cylinder, Maeve's three braids, Hina's numbered kimono). If it isn't story, cut it.

**Our rules for action and effects:**
1. **Limited animation, strong timing:** key poses on 2s and 3s, holds before payoffs, **smear frames** on fast moves.
2. **Hand-drawn FX** with hard shapes: angular sparks, chunky smoke with flat shadow, speed lines, debris silhouettes.
3. **Impact frames:** 1–2 frames of inverted or two-colour flat graphics (black and the attacker's signature colour) on every big hit.
4. **The colour-step slow-mo** (each frame a different hue) is reserved for **Overwrite and Jackpot** moments, our version of the famous sequence.
5. **Glitch, chromatic aberration and scanlines appear only in Noise and Basilica moments**, never as a default filter.
6. Neon accent triad for combat and Meridian: **acid yellow `#F5E400`, hot magenta `#FF2E88`, cyan `#00E5FF`**, used as light, never as fill for whole areas.

---

## 3. Composition and camera
- **Exploration and story:** wide, calm, eye-level or slightly low; characters small in big painted spaces; long holds. Let the world breathe.
- **Combat:** tighter; low angles, Dutch tilts on hits, foreshortened limbs toward camera, diagonal staging; crash zooms on ultimates.
- **Cut-ins:** flat graphic panels in the character's signature colour with halftone or speed-line texture; one bold diagonal.
- **Readability:** fighters on the left, enemy on the right, reel top-centre, floor clear.

---

## 4. Colour script by land

| Land | Default time and light | Base palette | Accent | Neon intrusion |
|---|---|---|---|---|
| Meridian Undercity | Rainy dusk → night; dawn for the intro | Wet slate blues, warm window ambers, moss greens | Nixie orange | **Full**: yellow, magenta, cyan signage |
| Hyakki (Japan-inspired) | Summer night, full moon; festival lanterns | Deep indigo, ink blue, paper cream | Vermilion, lantern gold, firefly green | Only Tamamo's foxfire (cold cyan-violet) |
| River Empire (China-inspired) | Golden afternoon over the harbour; misty underworld | Jade, warm ochre, red lacquer | Gold leaf | Luck Exchange boards |
| Śūnyapura (India-inspired) | Monsoon break: wet stone, sun through cloud | Sandstone, peacock green, saffron | Brass | Eclipse purple during Rahu & Ketu |
| Kroton Nova (Greece-inspired) | Hard Mediterranean noon | Chalk white, Aegean blue, olive | Bronze | The Sieve's cold white glow |
| Crossroads (America-inspired) | Desert sunset → neon night | Rust, sage, dusk violet | Sunset orange | Casino neon (full) |
| The Basilica | Interior, no sun | Brass and steel greys | Nixie orange | Total, until the finale's sunrise |

---

## 5. Production pipeline (how we get polish, not just pictures)
1. **Colour script first:** one thumbnail per land and beat before any final art.
2. **Style frames:** 3–4 frames that define the look (a character key art, a painted establishing shot, a battle frame). Nothing scales up until they're approved.
3. **Characters are generated on a flat neutral background**, never inside a scene, so they stay cel-like and cut out cleanly.
4. **Backgrounds are generated as empty plates**, then split into parallax layers.
5. **Compositing happens in engine**: characters get rim light from the background's light colour; grade the whole frame per land.
6. **Paint-over pass** against the checklist below. AI output is a draft, never final.
7. **Animation:** rigs for idles (breathing, hair, cloth), drawn key poses + smears for attacks, hand-made FX.

### QC checklist (every image)
- [ ] Silhouette reads as a black fill at thumbnail size
- [ ] Signature colour is the most saturated thing on the character
- [ ] Characters: 2 tones + 1 rim; no airbrush; coloured variable-weight lines
- [ ] Background: one light source, a time of day, atmospheric depth, 2–3 deliberate "little things"
- [ ] Neon only where the fiction allows it
- [ ] No stray text, no warped digits, correct hands, correct prop handedness
- [ ] Culture details checked against the World Bible §10

---

## 6. Prompt grammar for Higgsfield (replaces the old style suffix)
Describe the **medium and technique**, not "premium anime key art". Studio names are used here only as a team reference; in prompts we describe traits.

**Character suffix:**
> 2D cel animation character design, flat colours, hard-edged two-tone cel shading with a single hard rim light in {emotion colour}, crisp variable-weight coloured lineart (thick outer contour, thin interior lines), bold graphic silhouette, lean stylised proportions, retro-modern TV anime look, saturated limited palette dominated by {signature colour}, plain flat light-grey background, no gradients on skin or clothes, no airbrush, no glossy highlights, no 3D render, no text

**Background suffix:**
> hand-painted animation background, gouache / poster-colour painting on paper, soft wet-edge gradients in the sky, visible soft brushwork, limited harmonious palette, one clear light source ({time of day}), atmospheric perspective, warm lived-in details, nature growing over everything, painted in the tradition of classic Japanese animated films, no characters, no text, no photo texture, no 3D render

**Battle-frame suffix:**
> frame from a 2D anime fight scene: flat cel-shaded characters with bold coloured outlines over a hand-painted gouache background, {neon accent} light from the action, hand-drawn angular effects animation, speed lines, dynamic diagonal composition, no text

---

## 7. Reference library (study, never trace or copy)
- **Painted worlds:** *Kiki's Delivery Service* (a sunlit port town), *Spirited Away* (the bathhouse town at dusk), *Howl's Moving Castle* (rooftop towns), *Castle in the Sky* (skies and clouds), *The Boy and the Heron*; Kazuo Oga's background art books.
- **Inked action:** *Cyberpunk: Edgerunners*; *Promare* (high-contrast colour design); *Akira* (neon, light trails); *Mob Psycho 100* (effects animation).
- **Games doing this well:** *Ni no Kuni* (a game made with Studio Ghibli's animation), *Guilty Gear Strive* (3D that animates on 2s like 2D), *Hi-Fi Rush* (cel shading and timing), *Zenless Zone Zero* (urban anime and UI), *Sable* (Moebius-style flat colour), *Hades II* (painterly 2D characters with strong silhouettes), *Persona 5* (graphic UI).
- **Engine reference:** Epic's write-up on *Orbitals* (retro-anime cel shading quantised to about three tones, with noise to fake hand-painting).

---

## 8. Lessons from *The Official Digital Artbook of Cyberpunk 2077*
Studied from the 61-page digital art book (styles chapter, district spreads, character line-ups). We take its **methods**, not its look. Night City's yellow-and-black trade dress, logos and designs stay theirs.

### 8.1 What the book teaches
1. **Every style is grounded in the world's history.** CD PROJEKT RED wanted styles that are "interesting, colorful, distinctive and, most importantly of all, plausible". Wars, crises and booms each leave "a logical and perceivable impact" on design. Four eras coexist on the same street: *Kitsch* ("style over substance", street rebellion), *Entropism* ("necessity over style", poverty, crude and durable), *Neomilitarism* ("substance over style", cold corporate elegance) and *Neokitsch* ("style and substance", the ultra-rich: gold, real wood, natural fur).
2. **A visible design system.** The "Comparison" spread draws the same character type, phone and drink in each style, so artists and players can tell the eras apart at a glance.
3. **Districts are mixes of styles, and travelling should feel like changing countries.** "When traveling between them, you should feel as if you're visiting different countries." And: "above all Night City is about contrasts."
4. **Lived-in logic.** In Little China, people live whole lives in one repurposed office building: they sleep on the balcony, repair limbs in a supply closet and cook in a former office kitchen. In Kabuki, "Far East meets Wild West", with low shacks that let the sun through. Every space answers *who lives here, and what happened to this place?*
5. **Status through scarcity.** In North Oak, "green is the new gold": a bonsai on a balcony is a luxury watch.
6. **Contrast as storytelling.** Pacifica's abandoned resort pairs "funhouse signs riddled with bullet holes" with "luxury pools filled with chemical sludge".
7. **Graphic identity is part of the art.** The book's pages are one loud base colour with black type, overlaid with spray-paint tags, marker crosses, stickers and collage, so the presentation itself feels like the street.

### 8.2 Applied to the Tally: Meridian's four eras of luck
Meridian gets its own history-grounded style system, built on our lore (the Basilica, the Rounding, the Deficit). Each era has a motto, materials and its own way of **showing your Omen**, because in our world the number is the status symbol.

| Era | Motto | Who | Materials and shapes | How the Omen is shown |
|---|---|---|---|---|
| **Charmpunk** (street) | *Luck over sense* | Gamblers, kids, gangs, small shops | Every culture's charms worn at once, hand-painted lucky numbers, plastic gold, neon, stickers | Gaudy holo-halos, numbers painted on jackets, fake Omen projectors |
| **Remainder** (poverty) | *Survival over luck* | The Undercity, the Settled | Scrap brass from old Basilica parts, patched cloth, salvaged Nixie tubes, rope | A cracked tube on a cord; often hidden out of shame |
| **Ledgerism** (power) | *Order over chance* | The Basilica, Auditors, Collectors | Brass, steel, white enamel, cathedral arches, clockwork, uniforms | Steel numerals, stamped seals, never glowing |
| **Gilded Fortune** (the 99s elite) | *Fortune and order* | Old money, Exchange magnates | Real gold leaf, jade, living plants (in Meridian, **a garden is luck you can see**), silk | Embroidered or gold-leaf numerals, discreet |

**The comparison sheet:** for each era, draw the same three things, *a person, a lucky charm and an Omen display*, side by side (in the manner of the book's Comparison spread). It's the first concept-art task for Meridian.

**Districts of Meridian** mix eras: the Remainder Wards (Remainder + Charmpunk), the Exchange (Gilded Fortune over Ledgerism), the Basilica Ring (pure Ledgerism), and the Charm Bazaar (pure Charmpunk, "every culture meets on one street").

### 8.3 Applied to the other lands
Each land has its **own traditional style** (the painted world, §2.1). **Meridian's eras intrude** wherever the Basilica's influence reaches: Ledgerist toll gates on a Hyakki shrine road, Charmpunk stalls in Bāfā's festival, Remainder shanties under Kroton Nova's sieve. Those collisions are where our "contrast storytelling" lives.

### 8.4 Graphic identity (menus, title, marketing)
Borrow the **energy**, not the trade dress: one confident base colour, heavy type, hand-made overlays.
- **Our base:** ledger-paper cream `#F2E8D5` with ink black `#141018` and Nixie orange `#FF7A2C`. Not Cyberpunk yellow.
- **Overlays:** lucky-charm stickers, hand-stamped ledger seals, red-ink corrections and tally marks (||||), ink brush strokes from the lands, and spray tags for Charmpunk screens.
- Every land's map, menus and cut-ins use that land's medium for overlays (woodblock stamps in Hyakki, gold leaf in Bāfā, palm-leaf script in Śūnyapura).

---

## Sources
- [What Kazuo Oga Thinks About When He Thinks About Backgrounds (Animation Obsessive)](https://animationobsessive.substack.com/p/what-kazuo-oga-thinks-about-when)
- [Painting in Ghibli style (Gurney Journey)](https://gurneyjourney.blogspot.com/2018/05/painting-in-ghibli-style.html)
- [Kazuo Oga's painting process (Open Culture)](https://www.openculture.com/2021/01/a-look-inside-the-painting-process-of-the-studio-ghibli-artist-kazuo-oga.html)
- [Roundtable interview: Imaishi and Wakabayashi, Anime NYC 2025 (Yattatachi)](https://yattatachi.com/roundtable-interview-imaishi-and-wakabayashi-anime-nyc-2025)
- [Reddit AMA recap: Hiroyuki Imaishi (Bubbleblabber)](https://www.bubbleblabber.com/2022/12/reddit-ama-recap-hiroyuki-imaishi/)
- [A pair of conversations with Studio Trigger (Anime Herald)](https://animeherald.com/2025/11/19/a-pair-of-conversations-with-studio-trigger/)
- [Cyberpunk: Edgerunners, a vibrant ode to retro anime (AWN)](https://www.awn.com/animationworld/cyberpunk-edgerunners-vibrant-ode-retro-anime)
- [Review of *The Art of Cyberpunk: Edgerunners* (Reframe)](https://buttondown.com/reframe/archive/cyberpunk-edgerunners-artbook-review/)
- [Rendering of Orbitals, a retro-anime-inspired game (Unreal Engine tech blog)](https://www.unrealengine.com/tech-blog/stepping-inside-a-retro-anime-inspired-game-a-look-into-the-rendering-of-orbitals)
- *The Official Digital Artbook of Cyberpunk 2077* (CD PROJEKT RED, 2020; [cyberpunk.net/artbook](https://www.cyberpunk.net/artbook/en/)), provided by the team as a PDF and studied for §8. Not stored in this repo.
