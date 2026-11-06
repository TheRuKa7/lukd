# ZERO-SUM: OMEN — Localisation Guide (Gate B8)

English at the jam; Japanese, Simplified and Traditional Chinese and Hindi next (World Bible §10); then French, German, Spanish (LatAm), Brazilian Portuguese, Korean.

---

## 1. Engineering rules (from day one)
- All text in Unity Localization string tables; ids from the dialogue database ([`BOND_ARCS.md`](BOND_ARCS.md) §3).
- No text baked into images (signs in art use digits or are layered for replacement).
- **Digits are universal**: Omens and reels always use Western Arabic numerals (0–9) in every language, because the mechanics are about those glyphs. Each language's own numerals (kanji, hanzi, Devanagari) appear only as decoration.
- Plural and gender support via Smart Strings; NIL is always they/them in English; translators choose the natural equivalent (e.g. no pronoun) per language.
- Text expansion: UI boxes fit +40% (German) and line breaks work for CJK (no spaces).

## 2. Fonts
| Script | Font | Notes |
|---|---|---|
| Latin | Big Shoulders Display, Barlow Semi Condensed, JetBrains Mono | |
| Japanese | Noto Sans JP | Vertical text only for decorative signs |
| Chinese (SC/TC) | Noto Sans SC / TC | |
| Devanagari | Noto Sans Devanagari | Check conjuncts render in TMP |
| Greek | Noto Sans (Greek) | |
Fallback chains per language in TextMeshPro; subset fonts per build to save WebGL size.

## 3. Glossary for translators
Keep untranslated: **NaN**, **Omen** (or the agreed local term, decided once), the names of heroes and bosses.
Translate consistently (lock once): Balance, Remainder, the Basilica, the Tally, Settled, Audit, Fate Wheel, the reel, Jackpot, Pair, Bust, Cascade, Zero-Sum, Omen Overwrite, Reaper's Toll, Hap, the Open Hand, Hap's Favour, fen.
Puns to adapt, not translate: Vesper's "Seven bucks", Maeve's "third time lucky", the catechism "Every soul a number".

## 4. Culture-specific care
- Where a land's own language appears (Hyakki in Japanese, the River Empire in Chinese, Śūnyapura in Hindi), the native-language version should feel *more* authentic, not less: localisers may restore terms the English simplifies.
- Lucky and unlucky numbers are part of the mechanics; translators must not "localise" them away (4 stays unlucky in Hyakki in every language).

## 5. Process
Freeze English per act → export → translation (with the glossary, screenshots and character sheets) → in-game LQA pass → cultural reviewer pass for that land ([`CULTURAL_CONSULTATION.md`](CULTURAL_CONSULTATION.md)) → fix → ship.
