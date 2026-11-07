# ZERO-SUM: OMEN — The Remainder: jam script and boards

Updated **7 November 2026** under [DECISIONS.md](DECISIONS.md). **Specified script, not implemented footage or playtested timing.** Complete required **10–15-minute Meridian Prologue**: JAM_SLICE controls scope; FIRST_10_MINUTES controls pacing. Full-campaign additions live in STORY. Maeve, Hyakki/Hina, Link Arts, dreams, extended reels, crafting and charged ultimates are absent from this baseline.

**E** = Unity acting/UI; **S** = layered stills with scripted movement. One Meridian stage may supply lighting/prop variants. No video, paid generation or human finishing step is required. Text/digits are runtime layers. Stable IDs below are content-import contracts; localization tables and boards remain production work.

## 1. Start, rescue and Naming (target 0:00–1:00)

Start unlocks audio; settings remain available. Reading and accessibility input are untimed. No mandatory myth film precedes input.

| ID | Board / trigger | Exact line or UI copy |
|---|---|---|
| `jam_start_010` | E, rain-wet Nixie title, NaN | THE REMAINDER / Start · Continue · Settings · Credits |
| `jam_alley_010` | S→E, short establishing pan | MERIDIAN / EVERY SOUL WEARS A NUMBER. |
| `jam_alley_020` | Ama's Civic 03→02→01, Tobi looks up | **TOBI:** Mum? |
| `jam_alley_030` | Collector silhouette, confiscation jar with six visible units | **COLLECTOR:** Ama Okoro. Your account's closed. |
| `jam_alley_040` | NIL steps between them, NaN visible | **COLLECTOR:** Move. |
| `jam_rescue_010` | Wheel available by ~17 s | STOP THE NUMBER / Tap or press Space |
| `jam_rescue_020` | Authored 07 stop; jar−6 and Ama+6 together | 01 → 07 |
| `jam_rescue_030` | Collector retains their own number | **COLLECTOR:** That one has no number. |
| `jam_rescue_040` | NIL looks toward the family's escape | **NIL:** Go. Both of you. |
| `jam_shrine_010` | S, ≤8 s chase; Naming terminal prop | **BROTHER NOUGHT:** In here. Quick. |
| `jam_shrine_020` | Door closes, ten digit buttons | **BROTHER NOUGHT:** Every soul needs a number, child. |
| `jam_shrine_030` | NIL glances at NaN | **NIL:** I don't have one. |
| `jam_shrine_040` | Optional meaning line on focus, all input modes | **BROTHER NOUGHT:** Then pick. The machine is listening. |
| `jam_naming_010` | Select 0–9, explicit confirm | STATE YOUR LUCKY NUMBER / Choose · Confirm |
| `jam_naming_020` | Resonance locks; terminal overload | REMAINDER DETECTED |
| `jam_naming_030` | Nought helps NIL out | **BROTHER NOUGHT:** Hap's watching. Run. |

Rescue 07 is explicit authored tutorial data, not evidence of natural stopping probability. Transfer six confiscated units; do not create luck or erase the Collector. Naming sets resonance once; focus help says **“A personal resonance, not your health.”** No hidden digit-specific stat buff. Normally advancing targets: first action≤20 s and choice≤60 s from Start, not download; allow voluntary reading without a countdown.

## 2. Solo Audit (target 1:00–3:00)

**One Debt Hound; NIL makes all three strikes per round.** The separately framed party Audit readout never replaces NIL's NaN. Explicit `tutorial_jackpot`: `j` is the smallest legal NIL face in 1–9 that is neither chosen resonance nor 4. Three authored stops visibly select `j-j-j`; normal priority gives Jackpot, not Overwrite/Reaper. Subsequent rounds use honest wheels. Tutorial data labels all exceptions.

| ID | Trigger | Exact line or UI copy |
|---|---|---|
| `jam_solo_010` | First legal wheel | STOP THE NUMBER. |
| `jam_solo_020` | First digit flies to reel; remaining stops still require input | THREE STOPS MAKE A PATTERN. |
| `jam_solo_030` | Authored Jackpot; settle total once | JACKPOT / THREE MATCH. |
| `jam_solo_040` | NIL reacts | **NIL:** …Huh. |
| `jam_solo_050` | First enemy intent; honestly broad legal 0 face | STOP ON 0 TO PARRY. |
| `jam_solo_060` | Successful 0 defence, only for chosen 0 | 0 PARRIES AND REFLECTS ONCE. |
| `jam_solo_070` | First natural Pair, if any | PAIR / TWO MATCH. |
| `jam_solo_080` | First natural Bust, if any | BUST / YOUR STRIKES STILL COUNT. |
| `jam_solo_090` | Ordinary hurt, no repeated bark in same round | **NIL:** Noted. |
| `jam_solo_100` | Hound stake 0, construct falls inert | AUDIT COMPLETE |

A missed defence deals its stated damage; never label a miss as Parry. If Balance reaches0, offer the ordinary safe encounter retry restoring full checkpoint Balance/seed and transient flags (TECH_DESIGN), not another rescue debit or Naming choice. No hidden auto-win, immunity or mandatory extra fight teaches missed vocabulary.

## 3. Vesper joins and two-hero Audit (target 3:00–6:00)

S, ~12 s entrance within the 3:00–4:00 window: **one fresh Debt Hound** leaps in. A shot, a hat, then Vesper. The two-hero Audit targets 4:00–6:00. This is encounter two, not three additional opponents.

| ID | Trigger | Exact line or UI copy |
|---|---|---|
| `jam_vesper_010` | Vesper lands | **VESPER:** Need a hand? Seven fen. |
| `jam_vesper_020` | NIL looks at empty hand | **NIL:** I don't have seven fen. |
| `jam_vesper_030` | Vesper flips without looking | **VESPER:** Then owe me a good story, kid. |
| `jam_duo_010` | Recruit commits before combat | CHOOSE WHO STRIKES. |
| `jam_duo_020` | Three legal strike slots | BOTH HEROES ACT. ONE ACTS TWICE. |
| `jam_duo_030` | Pattern Sight on legal third-wheel faces | SHIMMERING FACES FINISH A PATTERN. |
| `jam_duo_040` | First natural Cascade, if any | CASCADE / GO AGAIN. |
| `jam_duo_050` | First natural Zero-Sum, if any | ZERO-SUM / THEIR NEXT ACTION IS CANCELLED. |
| `jam_favour_010` | First natural Bust, warm sigil | LUCK IS TURNING. |
| `jam_favour_020` | Two natural Busts, visible repair before scoring | **VESPER:** Hap's watching. |
| `jam_duo_060` | Victory | AUDIT COMPLETE |

Do not force Busts or falsify stopped digits to demonstrate Favour. If it never triggers, pause rules cards remain available. Cascade grants another round, not a story encounter. A chosen 0 defence combines Parry/Fortune with one reflection and one defensive proc (SYSTEMS).

## 4. One charm choice (target 6:00–7:00)

E/S, Gus's stall is a prop/portrait variant. **Free reward, no wallet/shop/loan/crafting subsystem.** Award and equip exactly one of three, once.

| ID | Trigger | Exact line or UI copy |
|---|---|---|
| `jam_charm_010` | Three focusable objects | **GUS:** One for the road. Pick what you trust. |
| `jam_charm_020` | Vesper regards the stall | **VESPER:** Generous today? |
| `jam_charm_030` | Gus shrugs | **GUS:** Alive customers come back. |
| `jam_charm_horseshoe` | `charm_horseshoe` | HORSESHOE / Your resonance face is 50% wider where it appears. |
| `jam_charm_cat` | `charm_black_cat` | BLACK CAT / First Bust each fight: the third digit copies the first. |
| `jam_charm_ofuda` | `charm_ofuda` | OFUDA WARD / Automatically parry the first enemy action each fight. |
| `jam_charm_confirm` | Selected object pins to frame | Charm equipped. |

Black Cat visibly changes scoring slot 3→slot 1 then reevaluates once; never merely relabels Bust. Ofuda grants one defensive proc, no accepted-stop event or reflection. Horseshoe affects only present legal chosen faces. SYSTEMS owns priority with Favour/jar. Continue follows confirmation; reload cannot duplicate rewards.

## 5. Varro's Debt Jar (target 7:00–11:00)

Drain-gate lighting variant. **Varro alone, no adds.** Intro Civic 61 badge is distinct from current Audit 99–00.

| ID | Trigger | Exact line or UI copy |
|---|---|---|
| `jam_varro_010` | Varro bars the gate, jar lit | **VARRO:** NaN. Worth more than my whole street. |
| `jam_varro_020` | Vesper notices exemption token | **VESPER:** They promised your sister an exemption? |
| `jam_varro_030` | Varro grips token | **VARRO:** Don't talk about her. |
| `jam_varro_card` | Name and labelled Civic badge | VARRO KADE / THE LEDGERHOUND / CIVIC 61 |
| `jam_jar_warn` | Before capture, preview scoring slot 3 debt | HE HOLDS YOUR LAST DIGIT. IT SCORES AS 0 WHILE HELD. |
| `jam_jar_help` | Show defence and affected-round counters | **VESPER:** Three defences—or three rounds. Then you get it back. |
| `jam_jar_restore` | Saved scoring digit visibly restored next player round | DIGIT RETURNED |
| `jam_varro_phase2` | ≤50%, actual upcoming hit shown | **VARRO:** Final notice. |
| `jam_varro_win` | Audit stake 0, Varro kneels alive | AUDIT COMPLETE |

**Contract:** once after first completed nonterminal player round, snapshot resolved slot 3 into a visible debt token. Next three affected player rounds override scoring slot 3→0 before Favour repair; actual stops still drive landing effects. Three successful defended enemy actions (Parry/Fortune/Ofuda) open early; otherwise three affected player rounds expire it, including Cascade rounds. Following player round restores saved scoring slot 3 after its third stop, then clears token; no stack/recapture/free damage. At≤50%, first enemy action after crossing still uses base 40;80 is announced for the following action. No retroactive change to an announced hit. Exact rules/data: SYSTEMS/BESTIARY/TUNING.

## 6. Mercy, rooftop and results (target 11:00–13:00; total 10–15 minutes)

Optional in-engine seven-shot defeat flourish is **presentation only**, no charge tutorial, rare trigger, extra damage or mandatory input. Skip/reduced motion cannot change the win.

| ID | Board | Exact line or UI copy |
|---|---|---|
| `jam_mercy_010` | Varro remains present, exhausted | **VARRO:** Go on. Settle the rest. |
| `jam_mercy_020` | NIL lowers decoder | **NIL:** No. |
| `jam_mercy_030` | Varro breathes | **VARRO:** …You'll regret that. |
| `jam_mercy_035` | Vesper reads the runtime exemption label, no new scene asset | **VESPER:** Livia. She still waiting? |
| `jam_mercy_037` | Varro grips the token | **VARRO:** Every morning. |
| `jam_mercy_040` | Varro limps away alive; lock releases 1 | SEAL 1 RELEASED |
| `jam_roof_010` | S, ~20–30 s, quiet future map | **VESPER:** Six Auditors. Six Seal Digits. Then the Upper Gate. |
| `jam_roof_020` | NIL counts gate sockets | **NIL:** Seven locks. |
| `jam_roof_030` | Vesper points to chosen resonance | **VESPER:** The last one's yours. You told the whole city. |
| `jam_roof_040` | NIL looks back toward Ama's street | **NIL:** They got away? |
| `jam_roof_050` | Two safe silhouettes in a lit window; coin put away | **VESPER:** Both of them. Come on. |
| `jam_end_010` | Local resolution, brief invitation | THE REMAINDER / A beginning in the Tally. |
| `jam_results_010` | Actual run data | Biggest round · Patterns found · Time |
| `jam_results_020` | Separate actions | Retry this number · New number · Credits · Title |

Map depicts the fictional future, not playable Hyakki in this jam. Mercy sets `varro_spared`/`seal.1` once. No kill branch, campaign ending selector or bond gate. New number confirms a fresh run; retry preserves resonance and resets run/encounter data. Continue resumes a valid checkpoint, not an unexplained jump to Naming.

## 7. Boards, skip and verification

One board per beat/transition: actor/reference ID, prop side, Civic/Audit labels, camera, duration hypothesis, subtitle ID, input return, sound cue, reduced-motion substitute, committed state. AI-authored Blender/SVG/still edits feed Unity. Boards and an in-engine timing capture precede optional film work.

Skippable from first view; skip commits the same atomic flags/recruit/reward outcomes. It pauses at mandatory choices. Pause, blocked storage, replay and duplicate callbacks cannot duplicate a charm, Seal, recruit or rescue transfer. Check ten resonances, three charm paths, watch/skip, mouse/keyboard, reduced motion, no successful parries and retries. Record actual timing/comprehension separately; this text is not a passing animatic, study or proof of fun.
