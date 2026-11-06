# ZERO-SUM: OMEN — Audio Direction and Sound List (Gate A7)

Sound is half the game feel. A reel that clicks on the beat feels twice as good. Every interaction in [`GAME_FEEL.md`](GAME_FEEL.md) has a named sound here.

---

## 1. Direction
- **One musical identity, many lands:** a synth-noir core (Meridian) that every land re-voices with its own instruments. The player should hear the journey.
- **The beat clock rules the reel.** Music runs on a beat clock; wheel ticks are quantised to the beat; the stop "clack" is not quantised (response comes first), but its tail lands on the next beat.
- **Stems fill with the reel:** stem 1 (pads/rhythm) always; stem 2 (bass) when the first digit lands; stem 3 (lead) on the second; stem 4 (choir/brass) on a pattern.
- **Silence is a tool:** the Ten Courts, Chitragupta's Hall and Hap's Dreams use near-silence.

## 2. Music

| Cue | Land / moment | Tempo | Instruments | Stems | Tag (jam) |
|---|---|---|---|---|---|
| Meridian theme | Prologue | 96 BPM | Analog synth bass, Nixie-hum pads, rain, muted trumpet | 4 | M |
| Varro boss | Prologue boss | 120 | Distorted bass, sirens, stomps | 4 | S (use Meridian battle remix) |
| Hyakki theme | Act I | 90 | Shamisen, shakuhachi, taiko over synth pads, wind chimes | 4 | M |
| Tamamo boss | Act I boss | 132 | Taiko ensemble, koto runs, choir, synth arps | 4 | M |
| Hap's Dream | Interludes | free | Music box of dice, celesta, reversed bells | 1 | S |
| River Empire | Act II | 100 | Erhu, guzheng, dizi, gongs over synth | 4 | — |
| Ten Courts | Act II underworld | — | Near silence, brush strokes, low drones | 1 | — |
| Śūnyapura | Act III | 84 | Sitar, tabla, tanpura drone, rain on stone | 4 | — |
| Kroton Nova | Act IV | 108 | Lyre, bouzouki, frame drum, male chant of primes | 4 | — |
| Crossroads | Act V | 92 | Slide guitar, harmonica, upright bass, slot-machine choir | 4 | — |
| Thale | Finale | 72 → 140 | Cathedral organ, brass, then every land's instrument in Phase 3 | 6 | — |
| Title | Title | 80 | Solo Nixie hum → the main motif on synth | 1 | M |

**The main motif:** seven notes (the "lucky seven"), rising; every hero theme quotes it in their land's mode.

## 3. SFX vocabulary (jam must-haves)

| Id | Sound | Recognisable as |
|---|---|---|
| sfx_wheel_unfurl | Paper-and-brass whoosh | "A wheel appeared" |
| sfx_wheel_tick | Soft mechanical tick per face, pitch rising with speed | Spinning |
| sfx_stop | **Clack**: mechanical latch + Nixie zap + low thump | The stop. Must cut through everything |
| sfx_hit_light / heavy | Punch + digital crunch | Damage |
| sfx_digit_slam_1/2/3 | Tube slams, low → mid → high | The reel filling up |
| sfx_bust | Tubes flicker out, a sigh | Nothing |
| sfx_pair | Two bright notes | Something good |
| sfx_zero_sum | Ledger chime + paper flip | Balanced |
| sfx_cascade | Rising three-note arpeggio | Again! |
| sfx_jackpot | Slot fanfare + coins + crowd "oh" | Big win |
| sfx_reaper | Four funeral bells | Danger |
| sfx_overwrite | Bells rung your digit's number of times + choir | Miracle |
| sfx_parry | "Ting" + whoosh | Saved |
| sfx_fortune | Gold shimmer + reversed hit | Reflected |
| sfx_favour_warm / haps_hand | Two dice rattling in a palm / dice thrown and landing | Luck turning |
| sfx_settle | Departure-board flip to 00 + wind | Defeat (never gory) |
| sfx_count_up | Ticks accelerating, "ching" per power of ten | The big number |
| sfx_ui_tap / back / buy | Paper, stamp, bell | Menus |

## 4. Voice
- Jam: **barks only** (3–5 per hero: strike, hurt, pattern, ultimate) + a few story lines; subtitles always.
- Voice direction per character from [`CHARACTER_BIBLE.md`](CHARACTER_BIBLE.md) (Voice rows).
- Optional AI voice for the Basilica's announcements and Thale's narration **must be disclosed**; human actors preferred for heroes.

## 5. Mix rules
- Priority: sfx_stop > dialogue > pattern stingers > hits > music > ambience.
- Duck music −6 dB during stingers and dialogue.
- Loudness target −16 LUFS integrated (web); true peak −1 dBTP.
- Every sound has a reduced-intensity variant for Reduced Motion mode (softer transients).

## 6. Sources and licences
Original compositions; SFX from licensed libraries (record which in `audio/LICENSES.md`); culturally specific instruments recorded or licensed from performers of that tradition where possible. Any AI-generated audio is logged in [`AI_DISCLOSURE.md`](AI_DISCLOSURE.md).

**Done when:** every Must interaction in GAME_FEEL has a named sound here, and the temp music runs on the beat clock in the prototype.
