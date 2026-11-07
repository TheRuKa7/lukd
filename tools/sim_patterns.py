#!/usr/bin/env python3
"""Pattern-exposure model, not a fight simulator or measured player behaviour.

Run: python tools/sim_patterns.py 60000 [--favour] [--json]
Uses actual NIL/Vesper face lists and legal solo/two-hero orders. Aim skill is an
independent Bernoulli assumption; speed has no fitted conversion to accuracy.
"""
import argparse
import csv
import json
import math
from pathlib import Path
import random
from collections import Counter

ORDER = ['OVERWRITE', 'REAPER', 'JACKPOT', 'CASCADE', 'ZERO_SUM', 'PAIR', 'BUST']
ROOT = Path(__file__).resolve().parents[1]


def tuning():
    with (ROOT / 'tuning/jam_tuning.csv').open(encoding='utf-8-sig') as source:
        rows = list(csv.DictReader(source))
    values = {}
    for row in rows:
        key = (row['section'], row['key'])
        if key in values:
            raise ValueError(f'Duplicate tuning key: {key}')
        value = float(row['value'])
        if not (-float('inf') < value < float('inf')):
            raise ValueError(f'Non-finite tuning: {key}')
        values[key] = value
    return values


def evaluate(ds, lucky):
    if len(ds) != 3 or any(type(d) is not int or not 0 <= d <= 9 for d in [*ds, lucky]):
        raise ValueError('Three reel digits and lucky digit must be integers 0..9')
    a, b, c = ds
    if a == b == c:
        return 'OVERWRITE' if a == lucky else 'REAPER' if a == 4 else 'JACKPOT'
    if (b == a + 1 and c == b + 1) or (b == a - 1 and c == b - 1):
        return 'CASCADE'
    if a + b + c in (10, 20):
        return 'ZERO_SUM'
    return 'PAIR' if a == b or b == c or a == c else 'BUST'


def multiplier(pattern, ds):
    return max(2, ds[0]) if pattern == 'JACKPOT' else {
        'OVERWRITE': 21, 'REAPER': 4, 'CASCADE': 3, 'ZERO_SUM': 2, 'PAIR': 2, 'BUST': 1,
    }[pattern]


def nil_faces(lucky):
    if type(lucky) is not int or not 0 <= lucky <= 9:
        raise ValueError('Lucky digit must be 0..9')
    omitted = {(lucky + offset) % 10 for offset in (4, 5)}
    if 0 in omitted:
        omitted.remove(0)
        omitted.add((lucky + 6) % 10)
    return [d for d in range(10) if d not in omitted]


def faces_for(hero, lucky):
    if hero == 'chr_nil':
        return nil_faces(lucky)
    if hero == 'chr_vesper':
        return [0, 1, 2, 3, 5, 6, 7, 8]
    raise ValueError('Hero outside implemented jam model')


def wheel_faces(lucky, width, faces):
    if not faces or any(type(d) is not int or not 0 <= d <= 9 for d in faces):
        raise ValueError('Wheel needs legal faces')
    if not math.isfinite(width) or width <= 0:
        raise ValueError('Width must be positive')
    return [width if d == lucky and d in faces else 1.0 if d in faces else 0.0 for d in range(10)]


def stop(weights, aim, skill, rng):
    if len(weights) != 10 or any(not math.isfinite(w) or w < 0 for w in weights) or sum(weights) <= 0 or not 0 <= skill <= 1:
        raise ValueError('Invalid weights/skill')
    if aim is not None and (type(aim) is not int or not 0 <= aim <= 9 or weights[aim] <= 0):
        raise ValueError('Aimed face is absent')
    if aim is not None and rng.random() < skill:
        return aim
    return rng.choices(range(10), weights=weights)[0]


def closer_aim(ds, lucky, faces=range(10)):
    """Highest-priority legal completion, then multiplier, then smallest digit."""
    if len(ds) != 2 or not faces:
        raise ValueError('Two digits and available faces required')
    return min(faces, key=lambda d: (ORDER.index(evaluate([*ds, d], lucky)), -multiplier(evaluate([*ds, d], lucky), [*ds, d]), d))


def repair(ds, lucky, streak, black_cat=False, black_cat_used=False):
    out, source = list(ds), None
    if evaluate(out, lucky) == 'BUST':
        if black_cat and not black_cat_used:
            source, black_cat_used = 'black_cat', True
        elif streak >= 2:
            source = 'haps_hand'
        if source:
            out[2] = out[0]
    return out, evaluate(out, lucky), source, black_cat_used


def run(lucky, party_size, skill, rounds, favour=False, seed=7):
    if party_size not in (1, 2) or rounds <= 0:
        raise ValueError('Positive rounds and jam party size required')
    config, rng, counts, streak, repairs = tuning(), random.Random(seed), Counter(), 0, 0
    order = ['chr_nil'] * 3 if party_size == 1 else ['chr_nil', 'chr_vesper', 'chr_nil']
    for r in range(rounds):
        if r % 8 == 0:
            streak = 0
        warm, ds = favour and streak >= 1, []
        for i, hero in enumerate(order):
            faces = faces_for(hero, lucky)
            resonance = lucky if hero == 'chr_nil' else 7
            weights = wheel_faces(resonance, config[('hero', 'lucky_width')], faces)
            if warm:
                for d in set(ds):
                    weights[d] *= config[('favour', 'warm_match_width')]
            aim = closer_aim(ds, lucky, faces) if i == 2 else resonance
            ds.append(stop(weights, aim, skill, rng))
        resolved, pattern, source, _ = repair(ds, lucky, streak if favour else 0)
        repairs += bool(source)
        counts[pattern] += 1
        streak = streak + 1 if pattern == 'BUST' else 0
    return {
        'lucky': lucky, 'party_size': party_size, 'skill_assumption': skill,
        'rounds': rounds, 'seed': seed, 'favour': favour, 'favour_repairs': repairs,
        'rates': {key: counts[key] / rounds for key in ORDER},
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('rounds', nargs='?', type=int, default=20000)
    parser.add_argument('--favour', action='store_true')
    parser.add_argument('--json', action='store_true')
    args = parser.parse_args()
    results = [run(lucky, size, skill, args.rounds, args.favour) for size in (1, 2) for lucky in range(10) for skill in (0.0, 0.25, 0.5)]
    if args.json:
        print(json.dumps({'model': 'jam-pattern-v2', 'limitations': 'No damage/defence/boss/economy/timing-skill fit; fixed legal strike order; eight-round fight resets; speed has no modeled aim bonus', 'results': results}, indent=2))
    else:
        print('Model jam-pattern-v2; seed7; fixed legal strike order; independent aim assumptions; no measured human accuracy.')
        print('Columns: party lucky aim ' + ' '.join(ORDER) + ' repairs')
        for r in results:
            print(f"{r['party_size']} {r['lucky']} {r['skill_assumption']:.2f} " + ' '.join(f"{r['rates'][k]*100:.2f}%" for k in ORDER) + f" {r['favour_repairs']}")


if __name__ == '__main__':
    main()
