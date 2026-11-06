#!/usr/bin/env python3
"""Monte-Carlo check of reel-pattern odds for docs/TUNING.md (GDD §1.3 and §1.5).

Model: each hero stops their own Fate Wheel. A face's chance of landing is its width (wider = likelier).
`skill` is the chance a player lands the face they aim at (their own lucky digit); otherwise the stop is
random by width. Pattern priority follows GDD §1.5. Usage: python3 tools/sim_patterns.py [rounds]
"""
import random
import sys
from collections import Counter

ORDER = ["OVERWRITE", "REAPER", "JACKPOT", "CASCADE", "ZERO_SUM", "PAIR", "BUST"]


def evaluate(ds, lucky):
    a, b, c = ds
    if a == b == c:
        if a == lucky:
            return "OVERWRITE"
        if a == 4:
            return "REAPER"
        return "JACKPOT"
    if (b == a + 1 and c == b + 1) or (b == a - 1 and c == b - 1):
        return "CASCADE"
    if (a + b + c) % 10 == 0:
        return "ZERO_SUM"
    if a == b or b == c or a == c:
        return "PAIR"
    return "BUST"


def wheel(lucky, width):
    w = [1.0] * 10
    if lucky is not None:
        w[lucky] = width
    return w


def stop(weights, aim, skill, rng):
    if aim is not None and rng.random() < skill:
        return aim
    return rng.choices(range(10), weights=weights)[0]


def wheel_faces(lucky, width, faces):
    w = [1.0 if d in faces else 0.0 for d in range(10)]
    if lucky is not None and lucky in faces:
        w[lucky] = width
    return w


def closer_aim(ds, lucky):
    """The 3rd striker sees two digits on the reel and aims to finish the best pattern (GDD §1.1 'read the reel')."""
    a, b = ds
    if a == b:
        return a                      # Jackpot / Overwrite
    if abs(a - b) == 1:
        return max(a, b) + 1 if max(a, b) < 9 else min(a, b) - 1   # Cascade
    return a if lucky in (a, b) else (10 - (a + b) % 10) % 10       # Pair on your digit, else Zero-Sum


def run(party, nil_digit, skill, rounds, seed=7, faces=range(10), smart=False):
    rng = random.Random(seed)
    counts = Counter()
    faces = set(faces)
    for _ in range(rounds):
        ds = []
        for i, (d, w) in enumerate(party):
            aim = closer_aim(ds, nil_digit) if (smart and i == 2) else d
            if aim not in faces:
                aim = d
            ds.append(stop(wheel_faces(d, w, faces), aim, skill, rng))
        counts[evaluate(ds, nil_digit)] += 1
    return {k: counts[k] / rounds for k in ORDER}


if __name__ == "__main__" and "--favour" not in sys.argv:
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 200_000
    scenarios = [
        ("Prologue: NIL alone (3 strikes, digit 7, double-wide)", [(7, 2), (7, 2), (7, 2)], 7),
        ("Jam party: NIL 7 + Vesper 7 + Maeve 3", [(7, 2), (7, 2), (3, 2)], 7),
        ("Complements: NIL 3 + Vesper 7 + Maeve 3", [(3, 2), (7, 2), (3, 2)], 3),
        ("Mixed: NIL 1 + Hina 9 + Vesper 7", [(1, 2), (9, 2), (7, 2)], 1),
    ]
    print("NOTE: 'smart' = the 3rd striker aims to complete a pattern; 'faces' = wheel size.")
    print(f"{n:,} rounds per cell. Columns: " + " ".join(f"{k:>9}" for k in ORDER))
    for name, party, nil in scenarios:
        print("\n" + name)
        for skill in (0.0, 0.25, 0.5):
            for label, kw in (("10 faces", {}), ("10 faces, smart", {"smart": True}), ("8 faces, smart", {"smart": True, "faces": [0, 1, 2, 3, 5, 6, 7, 8] if nil != 4 else range(8)})):
                r = run(party, nil, skill, n, **kw)
                print(f"  skill {skill:.2f} {label:<17}" + " ".join(f"{r[k] * 100:8.1f}%" for k in ORDER))


def fight_streaks(party, nil_digit, skill, fights=20000, rounds=8, favour=True, seed=11):
    """Hap's Favour (SYSTEMS.md §2.4). Returns (share of fights with 3+ Busts in a row, overall Bust rate).
    Warm (after 1 Bust): +0.10 skill (wheels 20% slower); faces matching digits already on the reel this round x1.5.
    Hap's Hand (after 2 Busts in a row): the next round cannot Bust; a Bust becomes a Pair."""
    rng = random.Random(seed)
    faces = {0, 1, 2, 3, 5, 6, 7, 8}
    bad, busts, total = 0, 0, 0
    for _ in range(fights):
        streak, worst = 0, 0
        for _r in range(rounds):
            warm = favour and streak >= 1
            ds = []
            for i, (d, w) in enumerate(party):
                weights = wheel_faces(d, w, faces)
                if warm:
                    for x in ds:
                        weights[x] *= 1.5
                aim = closer_aim(ds, nil_digit) if i == 2 else d
                ds.append(stop(weights, aim, min(1.0, skill + 0.1 * warm), rng))
            res = evaluate(ds, nil_digit)
            if res == "BUST" and favour and streak >= 2:
                res = "PAIR"
            total += 1
            if res == "BUST":
                busts += 1
                streak += 1
                worst = max(worst, streak)
            else:
                streak = 0
        bad += worst >= 3
    return bad / fights, busts / total


if __name__ == "__main__" and "--favour" in sys.argv:
    party = [(7, 2), (7, 2), (3, 2)]
    for skill in (0.0, 0.25, 0.5):
        a, ab = fight_streaks(party, 7, skill, favour=False)
        b, bb = fight_streaks(party, 7, skill, favour=True)
        print(f"skill {skill:.2f}: 3+ Bust streaks {a * 100:5.1f}% -> {b * 100:4.1f}% of fights; Bust rate {ab * 100:4.1f}% -> {bb * 100:4.1f}%")
