// Scoring regression test for the browser prototype (GDD §1.2–1.5).
// Extracts evaluate() and PATTERN_MULT from prototype/index.html and checks pattern priority and round totals.
// Usage: node tools/test_scoring.js
const fs = require('fs');
const path = require('path');
const assert = require('assert');

const src = fs.readFileSync(path.join(__dirname, '..', 'prototype', 'index.html'), 'utf8');
const grab = (re) => { const m = src.match(re); if (!m) throw new Error('not found: ' + re); return m[0]; };
const code = [
  grab(/const FIBSETS = [^\n]+/),
  grab(/function evaluate\(ds\) \{[\s\S]*?\n\}/),
  grab(/const PATTERN_MULT = [^\n]+/),
].join('\n');
const G = { lucky: 7, charms: [] };
const api = new Function('G', code + '\nreturn { evaluate, PATTERN_MULT };')(G);

// Round total = strikes (dealt on impact) + reel bonus (mult - 1) x roundDamage  ==  roundDamage x mult
function roundTotal(ds, roundDamage) {
  const p = api.evaluate(ds);
  const mult = p.key === 'JACKPOT' ? Math.max(2, p.d) : api.PATTERN_MULT[p.key];
  return { key: p.key, total: roundDamage + roundDamage * (mult - 1) };
}

const cases = [
  // digits, lucky, expected pattern, expected multiplier
  [[7, 7, 7], 7, 'LUCKY', 21],
  [[0, 0, 0], 0, 'LUCKY', 21],          // Overwrite pays the same for every digit
  [[4, 4, 4], 4, 'LUCKY', 21],          // your own 4s are an Overwrite, not a Reaper's Toll
  [[4, 4, 4], 7, 'REAPER', 4],
  [[5, 5, 5], 7, 'JACKPOT', 5],
  [[1, 1, 1], 7, 'JACKPOT', 2],         // Jackpot minimum x2
  [[3, 4, 5], 7, 'CASCADE', 3],
  [[9, 8, 7], 7, 'CASCADE', 3],
  [[3, 3, 4], 7, 'ZERO', 2],            // sums to 10: Zero-Sum beats Pair
  [[7, 1, 7], 7, 'PAIR', 2],
  [[2, 9, 5], 7, 'BUST', 1],
];
for (const [ds, lucky, key, mult] of cases) {
  G.lucky = lucky;
  const r = roundTotal(ds, 100);
  assert.strictEqual(r.key, key, `${ds} (lucky ${lucky}) should be ${key}, got ${r.key}`);
  assert.strictEqual(r.total, 100 * mult, `${ds} (lucky ${lucky}) should total x${mult}, got ${r.total / 100}`);
}
console.log(`scoring OK: ${cases.length} cases (priority and multipliers match GDD §1.3/§1.5)`);
