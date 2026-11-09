# Canonical decisions

Updated **7 November 2026 (IST)** under the request to audit and fix all documentation. These decisions are adopted design specifications, not proof of implementation. They supersede contradictory older prose and the proposals in the 6 November refinement reports. Domain documents carry the detailed contracts; [PROJECT_STATUS.md](PROJECT_STATUS.md) records implementation evidence.

## Authority and scope

**8 November story-first update:** [Resolved series bible](novel/RESOLVED_SERIES_BIBLE.md) governs the newly adopted novel/manga naming, cosmology clarification, character accountability, political transition and length targets. It supersedes conflicting older fictional prose for this edition. The seven-volume plan remains49 chapters ×22 story pages; the old jam timetable is historical under the user's story-first priority. Gameplay formulas remain governed by SYSTEMS and the rules below. Prior artbook PDFs and Mangaka projects are dated snapshots, not automatically updated by this decision.

1. This decision register resolves cross-document conflicts. `JAM_SLICE.md` controls jam content; `SYSTEMS.md` controls gameplay semantics; `WORLD_BIBLE.md` and `LORE_LEXICON.md` control fictional facts; `TECH_DESIGN.md` controls architecture and budgets. Conflicts must be corrected in both documents rather than silently choosing one at runtime.
2. Tuning CSV stores typed numerical inputs, not executable formula strings. A simulator is a model, not a gameplay implementation or proof of fun. Historical reports must name their baseline and link current resolutions.
3. State labels are **specified**, **implemented**, **verified**, or **not in scope**. A written document alone establishes only specified. Never use a completion checkmark to imply a build, test, consultation or asset acceptance that has not occurred.

## D01 — Jam scope

Ship **The Remainder: a 10–15 minute Meridian Prologue**. Required: interactive Rain Alley rescue, Naming/lucky-digit choice, one solo tutorial Audit, Vesper recruitment, one two-hero Audit, one choice from three defined charms, Varro's Debt Jar boss, mercy/rooftop map ending, results/retry, settings/credits/disclosure. NIL and Vesper are the only required playable heroes. One Meridian stage may serve multiple lighting/staging variants. Seven base pattern classifiers, Pattern Sight, Favour, defence and Balance/Audit Omen are required.

Maeve, Hyakki/Hina/Tamamo, extended reels, crafting, full bonds/Link Arts, and economy systems are expansion content. No extension enters the jam unless the entire required Prologue is already hosted, technically verified, final-presented and understood by fresh players by **9 November IST**; the default remains Prologue-only. Feature freeze 10 November, content lock end of 11 November, verification 12 November, submit 13 November; hard deadline 14 November 17:30 IST. Targets are not achievements.

The free reward offers exactly `charm_horseshoe` (chosen resonance faces ×1.5 width on allied wheels where present), `charm_black_cat` (first would-be Bust per fight uses D05's visible repair once), and `charm_ofuda` (first enemy strike auto-Parry, no reflection because no accepted stop; counts once toward the jar). No fen/shop/crafting, narrative-bond menu, ultimate gauge, extended reel or Link Art is required in the jam. A scripted Vesper finishing shot is presentation, not an unimplemented charge system.

## D02 — AI-only and free-first production

AI authors code, writing, assets and processing/animation scripts; the user directs choices. No required human artist/overpaint/animator/composer/programmer finishing stage. Use installed/local/free tooling first, with scripted Blender/SVG and Unity presentation as reproducible fallbacks. Higgsfield, Meshy and other paid generation are optional and require actual account/quota checks before use. No purchase or paid job is authorized by this document. Preserve provenance; do not claim manual work or external cultural review that did not occur. Player feedback is validation evidence, not outsourced production.

## D03 — Identity, Civic Omen and Audit Omen

Store four separate concepts: **resonance digit** (0–9; NIL chosen, Fibi round-dependent), **Civic Omen** (00–99; personal luck/status outside an Audit), **Balance** (integer luck staked in an Audit), **Audit Omen** (normalized 99–00 readout of that stake). Combat rules reading an Omen read Audit Omen unless explicitly marked civic. Render different frames; NIL's `NaN` identity remains visible beside the shared party Audit readout. A positive Balance displays `ceil(99 × Balance / MaxBalance)`, clamped 01–99; zero displays 00. Validate MaxBalance > 0 and Balance within bounds.

Settling an Audit exhausts the stake and ends combat; it does not automatically kill/disintegrate a person or set their Civic Omen to 00. Civic settlement is a distinct story event. The hopeful ending gives NIL a stable resonance equal to the player's choice and a **positive** Civic Omen; resonance zero is never depicted as healthy Civic 00. Luck transfer, not the normalized combat display, obeys the pre-finale conservation law. Ama's rescue visibly transfers six units from confiscated luck rather than creating them.

## D04 — Round resolution and defence

Seven base patterns use priority **Overwrite → Reaper → Jackpot → Cascade → Zero-Sum → Pair → Bust**. Overwrite is ×21 for every chosen digit; Jackpot is `max(2, digit)`; other base multipliers are 4/3/2/2/1 respectively. Cascade requires ordered ±1 steps without wrap; Zero-Sum is sum 10 or 20. Do not double-pay base strikes. Presentation may show provisional strike values, but settle the round's total exactly once after all three digits. Specify any boss digit debt as a stored slot token with an explicit replacement/restoration rule in SYSTEMS/BESTIARY.

Reaper's percentage uses **current Balance**, snapshotted with Audit Omens before that round's damage; apply integer floor(44% × current Balance) to each qualifying side once, in addition to ordinary pattern damage. Commit both sides' results atomically. If both reach zero, the party loses/retries; do not grant rewards or another enemy action. All secondary events stop after terminal state.

On enemy stop: 0 is Parry (no damage); a nonzero chosen digit is Fortune (no damage and reflect the strike); other digits deal the stated strike. If the player's chosen digit is 0, stopping 0 combines Parry and Fortune with one reflection and one defensive proc, not two triggers. This is explicit overlap; equal Overwrite strength does **not** prove equal win rates. Validate every digit and ensure required counters remain possible.

Party: NIL plus up to two companions; three strikes per round. Solo NIL acts three times; two-person party uses both heroes with one acting twice; three-person party each acts once. Legal build examples must include NIL.

Varro captures scoring slot three once per fight after the first completed nonterminal player round, storing its resolved digit in a visible debt token. The next three player rounds replace scoring slot three with zero before pattern/Favour resolution; actual stopped digits still drive landing effects. The jar opens after three successful defended enemy actions (Parry/Fortune/Ofuda count once each) or immediately after the third affected player round. Its saved digit restores scoring slot three on the next player round after its stop, then clears; no stacking or recursive capture. Announce capture in advance. At≤50% Balance, phase-two base80 replaces base40 only after one further base40 enemy action, with the80 telegraph visible before the affected player round.

## D05 — Wheels, Favour and extended mechanics

Starter wheels use explicit legal face lists. NIL omits `(chosen+4) mod 10` and `(chosen+5) mod 10`, preserving the chosen digit and zero; if either omission is zero, omit `(chosen+6) mod 10` instead. SYSTEMS must publish the ten resulting lists. Most companions have eight faces; Prima deliberately has five. Aimed outcomes must be on the active wheel. Widths describe exposure under defined motion; they are not measured human stopping probabilities.

After one Bust, warm Favour applies next round: speed ×0.8 and already-matching faces ×1.5 width. After two consecutive Busts, a would-be Bust is visibly repaired **before scoring/passives** into a Pair by changing the third digit to the first, with a provenance event `haps_hand`; do not merely relabel an unchanged reel. Re-evaluate higher-priority patterns after repair. Pattern results cool the streak. Authored tutorial results are explicit exceptions, disclosed in tutorial data.

Shunya's base zero-wild applies to pattern matching only; bond-wild is an Awakening. Wild assignments maximize pattern priority, then base multiplier, then lexicographically smallest assignment; actual stopped digits still drive charge/land/face effects unless a rule says resolved digits. Favour/Black Cat use the same visible repair and a single conversion. Each source may trigger once per declared event; generated effects do not recursively re-trigger their parent. Full-game extended reels and advanced kits need explicit domain contracts and content-gate status; none is required by the jam.

## D06 — Bonds, progression and content

Eight core companions + three secret companions + NIL = **12 authored playable characters** across the full game/postgame. Resonance bonds: Complement is nonzero digits summing to ten; Twins is equal digits (including zero); Neighbours differ by one without wrap. Zero has no ordinary Complement. Shunya's bond-wild is an explicit later exception. Never promise equivalent early partner availability for every digit; Varro is a guest late and a full recruit after the ending/NG+.

63 party charms: nine per set across seven sets. Slots 3→6. Replace the impossible seven-item equipped set requirement with five-piece Hyakki bonus; combined deities share one charm and must not be counted as extra equipped items. Narrative bonds and mathematical bonds are separate state. Any core companion required by an ending has a guaranteed catch-up route; secret recruits never silently gate the central resolution. Four narrative stages per companion may include story-integrated scenes; pre-ending conditions cannot depend on post-ending rewards.

Campaign target: **315 minutes critical path + 45–105 minutes optional bonds/quests/navigation = 6–7 hours hypothesis**, not measured. Use STORY's segment budget (35/45/50/50/45/50/40 minutes), distinct from the shortened jam. Do not lengthen the game by multiplying regions before the pipeline is proven.

Act carryover: keep face modifications, gem levels, unlocked heroes/verbs/bonds and permanent progression; keep three selected **party charms active**, stash other owned charms for later camp re-equipping. Slots can still grow to six within an act. Fen halves with integer floor; Karma becomes floor(0.75 × Karma). Personal gear does not count toward party-charm sets; state that separately. Defeat restores the complete act-start gameplay snapshot; permanent narrative/unlock journal evidence is idempotent and reconciled, not a duplicated reward source. Jam uses encounter retry/checkpoint and does not implement act resets.

## D07 — Narrative continuity

The Basilica/cage predates Thale. Thale inherits it, discovers Hap in TR999 and develops Fixed Fate; his institutional authorship claims are propaganda or revised. Distinguish objective history, public doctrine and personal belief. Default denotes absolute stillness from extinguished chance; public doctrine may incorrectly describe collapse/Noise, clearly labelled as such.

Hina remains 99 until the true-ending epilogue; Awakening changes self-acceptance/kit, not literal age. Bai Si has four physical lanterns. Maeve's grandmother experienced a recent tightening of an old Rounding system, not its creation 300 years ago. Six acquired Seals plus NIL's chosen resonance open the ritual gate; guard recall, Seal lock and interior service passage are separate obstacles. Named defeated people survive where their aftermath requires it; only appropriate constructs/Noise disintegrate. Finale companion recalls are scripted from recruited/required roster and do not require an absent wheel face.

Balance ending caps Civic Omens at99 and transfers gains from an identified reserve; Positive-Sum changes how distinct regional ledgers can share possibilities, seeded by earlier evidence. No ordinary pre-finale attack creates luck. Rahu/Ketu are revered celestial figures; combat targets are invented Basilica eclipse constructs taking their names, explicitly distinguished in text and visuals. Keepers test rather than die. Native expertise and cultural approval are not claimed by AI source checks.

## D08 — Runtime and evidence

Use the installed **Unity 6000.4.11f1 + Web module** for the first viability build, not an unverified LTS directory. This is an implementation target; no Unity project or verified game build exists at this decision date. Pin Editor/package versions in project files when created. Pure rules Core, content import, one sequencing owner, replaceable presentation, versioned saves. Named gameplay RNG streams and accepted face IDs/ticks are replay data; visual RNG cannot change gameplay.

Use checked bounded integer/fixed-point calculations with specified rounding; do not promise cross-runtime determinism from unbounded double arithmetic. Test exact rule fixtures; statistical simulation is secondary. Use one selected deployment compression format with verified host headers or its JS decompression fallback; no fictional automatic Brotli→Gzip fallback.

Jam planning budgets: ≤50MB compressed total, ≤25MB initial package, ≤512MiB measured peak memory on a named reference laptop, desktop60fps target. These are starting budgets, not measured values. Define cold download/startup separately from **Start-to-first-action ≤20s** and **lucky choice ≤60s**. The first scene starts interactively; no mandatory myth film before input. Required gameplay feedback is in engine; video is optional, URL-backed, bundled on itch, subtitled/skippable and has a still fallback. No runtime generation API, mutable remote gameplay content or telemetry in jam.

## D09 — Open work versus documentation defects

Unimplemented scenes/tests/assets, unmeasured fun/performance, incomplete future content data and external licensing/cultural checks remain **production work**, not completed by editing this register. Each needs an owner, artifact and gate. Documentation must specify its interfaces, dependencies and acceptance test now; no “all done” claim without actual evidence. Historical PDFs and review inventories must carry snapshot dates, and current books must be regenerated or clearly marked stale.
