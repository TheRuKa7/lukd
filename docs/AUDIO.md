# ZERO-SUM: OMEN — Audio Direction and Contracts

Updated 7 November 2026. Meridian Prologue; DECISIONS D01/D02/D08. **Specified; no accepted runtime audio/listening/mix test recorded.** AI authors synthesis, arrangement, editing and processing; no human performer/finishing dependency.

## 1. Identity and timing

Synth-noir core: mechanical/brass clicks, warm windows/rain and an original rising seven-note motif. This is a composition brief, not seven notes already supplied. Future lands revoice it with source research and honest limits on instrumental authenticity.

The **wheel face follows gameplay clock/input**, never music quantization. Ticks follow actual face crossings; optional ornaments/tails can align with a beat. Stop, Parry/Fortune and state feedback respond immediately. Audio must not delay acknowledgement or change the accepted face. A clip cannot implement a rule or imply a second damage payment.

## 2. Music scope

| ID | Brief | Jam status |
|---|---|---|
| mus_meridian | 96 BPM starting brief, synth pad/bass, sparse mechanical rhythm; seamless loop | Required; specified |
| mus_varro | Same-source intensity/arrangement variant | Required intensity change; may reuse Meridian |
| mus_title_end | Sparse motif/held pad from same source | Reuse, not another commissioned song |
| mus_hyakki / mus_tamamo | Festival/night and boss revoicing | Future gate |
| mus_hap / later lands / Thale | Near-silence, regional instruments, combined finale motifs | Future; no production claim |

Multi-stem adaptive music is future/optional. Later stems must share start/length/tempo/loop points; scheduled crossfades never affect game timing. Ship one coherent loop/variant first.

## 3. Required SFX events

| ID | Sound brief | Rule/readability |
|---|---|---|
| sfx_wheel_unfurl / sfx_wheel_tick | Paper/brass whoosh; soft tick | Actual active faces; rate/polyphony caps |
| sfx_stop | Latch + synthetic zap + short thump | Highest priority, immediate |
| sfx_hit_light / sfx_hit_heavy | Contact + digital crunch | Provisional contact distinct from settlement |
| sfx_digit_slam_1 / 2 / 3 | Low→mid→high latch | Slot placement, not extra score |
| sfx_bust / sfx_pair / sfx_zero_sum / sfx_cascade | Dry tube / two notes / ledger chime / three-step rise | Exact runtime label/icon |
| sfx_jackpot / sfx_reaper / sfx_overwrite | Compact fanfare / four dark pulses / motif resolution | Equal perceptual payoff for digits including 0; not zero bells for 0 |
| sfx_parry / sfx_fortune | Ting / reflected sweep | Lucky-0 overlap uses one combined defensive event/cue |
| sfx_favour_warm / sfx_haps_hand | Warm rattle / repair latch | Match actual third→first repair |
| sfx_jar_store / sfx_jar_progress / sfx_jar_open | Glass latch / progress steps / release | Align token, counters, restoration |
| sfx_audit_settle | Departure-board flip + wind | Audit Omen 00 means exhausted stake, not automatic civic death |
| sfx_count_up / sfx_ui_tap / sfx_ui_back / sfx_charm_pick | Bounded ticks / paper / stamp / chime | Skip stops tails; no purchase cue required |
| amb_meridian | Rain/window/gear bed | Stop/dialogue remain clear |

Each imported cue has duration, priority and simultaneous-instance cap. Avoid tick floods at high speed. Audio/VFX never schedule gameplay events.

## 4. Voice and text

Full voice/barks optional; required dialogue is text with speaker IDs/subtitles. Existing AI voice access needs original voice design, provider terms and logging. No unauthorized real-person imitation; no invented human performer credits. Text plus silence/synthetic barks is the free fallback.

## 5. Production and acceptance

Default: AI-authored note/event/synthesis scripts, deterministic loop renders and edit scripts. Preserve source, parameters and hashes. Any used sample/library needs its actual licence record; a planned `audio/LICENSES.md` is not proof it exists or grants rights. No traditional performer is assumed.

Starting mix targets: −16 LUFS integrated on a representative complete mix; true peak ≤−1 dBTP. One-shots need headroom, not arbitrary normalization to −16 LUFS. Priority: stop > dialogue > pattern > hit > music > ambience. Duck music up to 6 dB smoothly under dialogue/stingers; test pumping/masking.

Music/SFX/Voice controls, mute, saved settings and separate audio-intensity control; reduced transients need not require Reduced Motion. Every essential sound has visible feedback. Web audio unlock follows a user gesture.

Verify seams/clicks/clipping/tails/missing clips/duplicate defensive procs/dialogue masking/tick overload. Retry/skip must not leave loops running. Measure imported memory/CPU and cold playback in the actual Web build. Tempo/loudness/performance targets are not measured results.
