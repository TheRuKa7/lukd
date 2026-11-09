// Generate parity fixtures from prototype/rules.js for the Unity port (Remainder.Rules).
const fs = require('fs');
const path = require('path');
const R = require('../prototype/rules.js');

const rng = R.createRng(20261109);
const pick = arr => arr[Math.floor(rng() * arr.length)];
const int = (a, b) => a + Math.floor(rng() * (b - a + 1));

const evaluate = [];
for (let lucky = 0; lucky < 10; lucky++)
  for (let n = 0; n < 1000; n++) {
    const ds = [Math.floor(n / 100), Math.floor(n / 10) % 10, n % 10];
    const e = R.evaluate(ds, lucky);
    evaluate.push({ lucky, digits: ds, key: e.key, mult: e.mult });
  }

const rounds = [];
while (rounds.length < 4000) {
  const lucky = int(0, 9);
  const actual = [int(0, 9), int(0, 9), int(0, 9)];
  const useScoring = rng() < 0.3;
  const scoring = useScoring ? [actual[0], actual[1], int(0, 9)] : actual.slice();
  const partyMax = pick([300, 340]), enemyMax = pick([300, 1200]);
  const input = {
    actualDigits: actual, scoringDigits: scoring, bases: [pick([10, 20]), pick([10, 20]), pick([10, 20])], lucky,
    partyBalance: int(1, partyMax), partyMax, enemyBalance: int(1, enemyMax), enemyMax,
    charms: rng() < 0.5 ? [pick(R.CHARM_IDS)] : [], blackCatUsed: rng() < 0.3, bustStreak: int(0, 3),
    party: rng() < 0.5 ? ['chr_nil', 'chr_vesper'] : ['chr_nil']
  };
  const r = R.resolveRound(input);
  rounds.push({
    actual, scoring, bases: input.bases, lucky, pb: input.partyBalance, pm: partyMax, eb: input.enemyBalance, em: enemyMax,
    charms: input.charms, cat: input.blackCatUsed, streak: input.bustStreak, party: input.party,
    resolved: r.resolvedDigits, damage: r.damage, enemyAfter: r.enemyAfter, partyAfter: r.partyAfter, key: r.pattern.key,
    catUsed: r.blackCatUsed, streakAfter: r.bustStreak, extra: r.extra, cancel: r.cancel, events: r.events.length
  });
}

const defends = [];
while (defends.length < 2000) {
  const lucky = int(0, 9), pm = 340, em = 1200;
  const a = { stoppedDigit: int(0, 9), lucky, strikeBase: pick([20, 40, 80]), partyBalance: int(1, pm), partyMax: pm,
    enemyBalance: int(1, em), enemyMax: em, ofuda: rng() < 0.15 };
  const d = R.defend(a);
  defends.push({ stopped: a.stoppedDigit, lucky, base: a.strikeBase, pb: a.partyBalance, pm, eb: a.enemyBalance, em,
    ofuda: a.ofuda, kind: d.kind, reflected: d.reflected, partyAfter: d.partyAfter, enemyAfter: d.enemyAfter, defended: d.defended });
}

const r2 = R.createRng(7);
const rngValues = Array.from({ length: 50 }, () => r2());
const faces = Array.from({ length: 10 }, (_, l) => ({ lucky: l, faces: R.nilFaces(l) }));

const out = path.join(__dirname, '../jam/RemainderJam/Assets/Editor/Fixtures/rules_fixtures.json');
fs.mkdirSync(path.dirname(out), { recursive: true });
fs.writeFileSync(out, JSON.stringify({ evaluate, rounds, defends, rngSeed: 7, rngValues, faces }));
console.log(JSON.stringify({ evaluate: evaluate.length, rounds: rounds.length, defends: defends.length }));
