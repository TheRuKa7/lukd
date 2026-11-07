# ZERO-SUM: OMEN — Localisation contract

Updated 7 November 2026 IST. English jam only. Additional language order is a planning hypothesis after the core pipeline: Japanese, Simplified/Traditional Chinese, Hindi, then French/German/Spanish (Lat Am)/Brazilian Portuguese/Korean. No translation or language QA is claimed by this document.

## 1. String and asset boundaries

Unity content gate L-IMPORT requires stable string IDs, locale/namespace, source text, speaker, context/screenshot, variables, plural/gender rules and fallback. Unity Localization string/asset tables are the intended implementation; none exists in this repository yet. The browser sandbox hardcodes English and is not localisation-ready evidence. A validated importer must reject duplicate IDs/missing placeholders and produce a dependency report before non-English content is enabled.

No critical text/numerals baked into generated art; signs requiring translation use replaceable text layers. Mechanical reel/resonance digits remain 0–9 consistently across languages; decorative regional numerals cannot resemble an interactive face. Locale-aware formatting handles large Balance values separately from the actual stopped digit.

## 2. Fonts and shaping

Candidate Latin fonts: Big Shoulders Display, Barlow Semi Condensed, Jet Brains Mono. Candidate fallback families: Noto Sans JP/SC/TC/Devanagari/Greek. Verify licence and bundle the exact font files; no required Google Fonts network call in the Unity jam. Fontgate L-FONT requires glyph coverage, valid fallback stack, atlas/memorybudget, CJK wrapping and Devanagariconjunct tests on the chosen TextMeshPro/Editor version. Do not claim TMP conjunct support merely because a font contains glyphs. Use screenshots of real strings for acceptance.

## 3. Layout and terminology

Allow at least 40%text expansion as a planning baseline, test actual strings and 150%text scale, and support line-break rules without assuming spaces. Smart Strings or equivalent handles plural/gender without concatenation. NIL uses they/them in English; translators choose an appropriate grammatical equivalent with consistent identity.

Lock distinct terms: resonance, Civic Omen, Audit Omen, Balance, Audit, Settled, Remainder, Basilica, Fate Wheel, reel, Pair, Jackpot, Bust, Cascade, Zero-Sum, Overwrite, Reaper, Hap, Open Hand/Favour, fen. NaN remains exact case. Combatstake settlement must not translate as literal death by default. Chosen resonance 0 is never healthy Civic 00. Proper names and mythic figure depictions use the same reviewed glossary/context as the narrative docs.

## 4. Workflow and gate

Freeze source per scene/act → export with context → AI draft translation → glossary/consistency checks → build imported language → actual-device visual/readability review → record unresolved native-language/cultural validation. AI translation/source checks are not claimed to be native expertise or external approval. Any community/native review, if obtained, records exact scope and findings.

Gate L-ENABLE is per locale: source/translation placeholders equal, no missing string ID, no overflow, correctglyph/shaping/focus, subtitles/skip intact, mechanics/civic distinctions preserved, and performance within budget. Incomplete locales stay disabled; no empty language selector in jam. Language choices/settings saves must migrate by stable locale ID.
