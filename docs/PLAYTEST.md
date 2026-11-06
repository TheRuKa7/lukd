# ZERO-SUM: OMEN — Playtest Plan and Fun Metrics (Gate A9)

Playtests find the fun; documents only point at it. We test **every day from Day 2**, starting with the browser prototype.

---

## 1. Schedule (jam)
| Day | Build | Testers | Focus |
|---|---|---|---|
| Fri 6 (tonight) | Browser prototype | 3 friends | Does stopping a wheel feel good? Do they want another round? |
| Sat 7 | Prototype + tuning CSV | 3 new | Pattern Sight, Hap's Favour, Bust feel |
| Sun 8 | Unity greybox: Prologue | 3–5 new | First 10 minutes (FIRST_10_MINUTES rules) |
| Mon 9 | Prologue + Act I start | 3–5 new | Charms, party of 3, bonds |
| Tue 10 | Full slice (freeze) | 5 new + 2 returning | Difficulty curve, Tamamo, pacing |
| Wed 11 | Content lock | 5 new | Balance; bugs; one cultural reviewer for Hyakki |
| Thu 12 | Release candidate | 3 new on itch (WebGL, 3 browsers) | Load time, performance, last confusions |

New testers each day (fresh eyes beat returning ones). At least one tester per round who doesn't play games much.

## 2. Protocol
1. Give them the link and **say nothing**. No explanation, no help.
2. Observe (screen + face if they agree); the observer only takes notes.
3. Stop at 15 minutes or when they stop on their own.
4. Five questions afterwards (no leading).

## 3. What we watch (log per tester)
| Metric | How | Target |
|---|---|---|
| Time to first tap | Timestamp | ≤ 20 s |
| First smile / "oh!" | Observer notes the moment | Before 2:00 |
| Confusion moments | Any pause > 6 s or a question | ≤ 2 before Varro |
| Busts that look frustrating | Sighs, "ugh" | Rare; never 3 in a row (Hap's Hand) |
| Pattern that got the biggest reaction | Observer | Jackpot/Overwrite, then Link Art |
| Quits | Where and why | No quits before Varro |
| "One more" | Did they replay or say so? | ≥ 60% |
| Can explain Pair, Jackpot, Parry | Ask after | ≥ 3 of 5 |

## 4. The five questions
1. What was the best moment?
2. When were you confused?
3. When were you bored?
4. Which character do you want to know more about?
5. Would you play again? (Yes / maybe / no, and why.)

## 5. Thresholds that change the plan
- If fewer than half want "one more": **stop adding content** and fix the core loop (feel, tuning, pacing) the next day.
- If anyone can't find the tap or the third-striker choice: fix the prompt, not the tutorial text.
- If a fight takes more than 2× its target rounds for most testers: lower enemy Balance first (TUNING §6).
- If a cultural reviewer flags something: fix it before release, no exceptions.

## 6. Log
Keep findings in `playtests/YYYY-MM-DD.md`: tester id (no names), metrics table, quotes, top 3 issues, what we changed.

**Done when:** the first session on the browser prototype has happened and its findings are logged.
