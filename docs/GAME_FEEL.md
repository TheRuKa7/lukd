# ZERO-SUM: OMEN — Game Feel Spec (Gate A1)

Stopping a number is the whole game. If that one tap doesn't feel incredible, nothing else saves us. This spec defines the tap frame by frame, the payoff ladder, and the speed rules that keep spectacle from becoming waiting. All times in milliseconds at 60 fps.

---

## 1. Principles
1. **Response before spectacle.** The wheel reacts to the tap within one frame (16 ms). Spectacle follows; it never delays the response.
2. **Readability first.** The stopped digit is legible within 150 ms, under every effect, at 720p, on a phone.
3. **Payoff scales with rarity.** A Bust is a shrug, a Jackpot is a fireworks finale. The ladder (§4) is strict so players learn value by feel.
4. **Every animation earns its time.** The first time you see a pattern, it plays in full. The third time, it's shortened. Hold to fast-forward anything.
5. **Sound is half the feel.** Every beat below has a sound (see [`AUDIO.md`](AUDIO.md)); the stop sound always cuts through the mix.

## 2. Anatomy of one strike

| t (ms) | Event | Visual | Camera | Sound |
|---|---|---|---|---|
| 0 | Hero selected | Hero steps forward; wheel unfurls above them in 180 ms (scale 0.6 → 1.05 → 1.0) | Push in 5% on the hero over 300 ms | Wheel "unfurl" whoosh |
| 180 | Spinning | Ones digit scrolls (speed per hero); tens fixed; faces sized by odds; Pattern Sight shimmer on the 3rd striker | Idle sway ±0.5° | Tick per face passed (pitch rises with speed) |
| tap | **Stop** | Wheel decelerates over 90 ms with ease-out-back (overshoot 6%) and settles on the face the tap was over | 2-frame micro-shake (2 px) | "Clack" (layered: mechanical + Nixie zap) |
| +90 | Settle | Stopped face flashes white 1 frame, then the land's accent colour; other faces dim to 30% | — | Short resonance tail |
| +120 | Hit-stop begins | Hero snaps into attack key pose (smear frame); enemy flinch | Hit-stop 80 ms (Bust/plain) to 140 ms (your lucky digit) | Hit + voice bark (30% chance) |
| +260 | Damage number | Strike value tears off the wheel: the tens in white, **the stopped digit in the hero's colour**, 1.4× size, then shrinks to 1.0 over 120 ms | Small zoom-out | Number "tear" |
| +380 | Digit to reel | The ones digit flies along an arc (300 ms, ease-in-out) and **slams** into the next reel tube | Tube-impact shake 3 px | Slam (pitch by tube: low, mid, high) |
| +680 | Ready | Next striker can be chosen; input buffer accepts a tap from +500 | — | — |

**One strike ≈ 0.7 s after the tap.** A three-strike round, excluding player thinking time, ≈ 2.1 s + the payoff.

### Input
- Tap anywhere, **Space**, or the hero's number key. Mouse, touch and keyboard identical.
- Latency budget: input → wheel stop visible ≤ 50 ms end to end (measure on WebGL Chrome and Safari).
- Input buffer: a tap during the last 180 ms of the previous animation is queued, not lost.
- Double tap within 120 ms counts once. A tap during the unfurl (first 180 ms) is ignored, with a soft "too early" tick so it never feels like a dropped input.
- Assist mode: wheels −30% speed; **hold-to-stop** alternative (press and release; stop on release).

## 3. Enemy strike and parry
| t (ms) | Event |
|---|---|
| 0 | Enemy wheel unfurls over the enemy, faces sized by its odds; its special faces show icons |
| 0–∞ | The player stops it (same verb). 0 → **Parry**: the strike bounces, counter-flash, 120 ms hit-stop, "ting". Your lucky digit → **Fortune**: reflect with a gold trail. Otherwise: damage, hero hurt pose, Balance drop, Omen ticks down with a mechanical flip |
| Telegraphs | Any special move is shown one round ahead: an icon on the enemy's wheel and a distinct sound (BESTIARY rules) |

## 4. The payoff ladder

| Pattern | Hold before reveal | Hit-stop | Screen | Camera | Music | Cinematic | Repeat rule |
|---|---|---|---|---|---|---|---|
| **Bust** | 0 | — | Tubes flicker out | — | — | — | Always short (0.4 s) |
| **Pair** | 150 | 60 | Silver flourish over the two tubes | Small punch-in | Stinger (2 notes) | — | 0.8 s |
| **Zero-Sum** | 200 | 100 | Mirror wipe; ledger lines | — | Ledger chime | Enemy's next action icon crossed out | 1.2 s |
| **Cascade** | 200 | 100 | Time-slow bands; blue | Slow 0.5× for 300 ms | Rising arpeggio | "YOU ACT AGAIN" | 1.4 s |
| **Jackpot** | 300 | 160 | Squad panels slash down; screen crack | Crash zoom | Full fanfare | Counting Mult up to the huge number | 2.5 s first time → 1.5 s after 3 |
| **Reaper's Toll** | 300 | 200 | Red wash; four bells | Slow push | Four tolls | Every Omen with a 4 loses 44% | 2.0 s |
| **Omen Overwrite** | 400 | 220 | Everything gold; your number rings bells (count = your digit) | Spin around the party | Your hero theme, full | The city rewrites itself (land-styled) | 3.0 s first → 2.0 s after 3 |
| **Link Art** | — | — | Split-screen duo cut-in | Authored | Duo motif | 3–5 s | Skippable after first view |
| **Ultimate** | — | — | Hero's cut-in band (land-styled) | Authored | Hero theme | 3–5 s | Skippable after first view |

**The count-up:** round damage counts up over 600 ms (ease-out), then the Mult slams in and the total counts again over 900 ms, with a "ching" every power of ten. The final number stays on screen until the next tap (Balatro's best trick: let people *look* at a big number).

## 5. Speed and respect for time
- **Hold anywhere** to fast-forward (4×) any animation; a setting makes every repeat cinematic short.
- After a pattern has played **3 times** in a session, its reveal uses the short version.
- A full fight (60–90 s target) has at most **one** long cinematic unless the player triggers more.
- Never block input for more than 3 s without a skip prompt.

## 6. Juice checklist (every interaction)
Anticipation (a tell before) · Response (within one frame) · Impact (hit-stop, shake, flash, sound) · Follow-through (settle, particles) · Feedback in numbers (the digit in the hero's colour) · Recovery (back to readable calm within 1 s).

## 7. Reference clips to collect (in `art/reference/feel/`)
Balatro (score count-up; card shake) · Hi-Fi Rush (beat-synced hits) · Persona 5 (all-out attack cut-ins; menu motion) · Hades (hit-stop, dash feel) · Peggle (the "Ode to Joy" finale and slow-mo last peg) · Pachinko and slot machines (reel stop, overshoot, win lights) · Cyberpunk: Edgerunners (smear frames, flashes).

**Done when:** the browser prototype implements §2–§4 and 4 of 5 first-time testers say stopping a wheel "feels good" without being asked about it ([`PLAYTEST.md`](PLAYTEST.md)).
