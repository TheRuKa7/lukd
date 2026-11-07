/* ZERO-SUM: OMEN reference rules. Browser + Node, no presentation dependencies. */
(function (root, factory) {
  const rules = factory();
  if (typeof module === 'object' && module.exports) module.exports = rules;
  else root.OmenRules = rules;
})(typeof globalThis !== 'undefined' ? globalThis : this, function () {
  'use strict';
  const ORDER = ['OVERWRITE', 'REAPER', 'JACKPOT', 'CASCADE', 'ZERO_SUM', 'PAIR', 'BUST'];
  const MULT = { OVERWRITE: 21, REAPER: 4, CASCADE: 3, ZERO_SUM: 2, PAIR: 2, BUST: 1 };
  const CHARM_IDS = ['charm_horseshoe', 'charm_black_cat', 'charm_ofuda'];
  const MAX_BALANCE = 1000000000000;
  function digit(d) { if (!Number.isInteger(d) || d < 0 || d > 9) throw new RangeError('digit must be 0..9'); }
  function amount(n) { if (!Number.isSafeInteger(n) || n < 0 || n > MAX_BALANCE) throw new RangeError('invalid bounded integer amount'); }
  function nilFaces(lucky) {
    digit(lucky);
    const omitted = [(lucky + 4) % 10, (lucky + 5) % 10].map(d => d === 0 ? (lucky + 6) % 10 : d);
    return Array.from({ length: 10 }, (_, d) => d).filter(d => !omitted.includes(d));
  }
  function facesFor(hero, lucky) {
    if (hero === 'chr_nil') return nilFaces(lucky);
    if (hero === 'chr_vesper') return [0, 1, 2, 3, 5, 6, 7, 8];
    throw new RangeError('hero outside implemented reference scope');
  }
  function evaluate(ds, lucky) {
    digit(lucky);
    if (!Array.isArray(ds) || ds.length !== 3) throw new RangeError('base reel requires exactly 3 digits');
    ds.forEach(digit);
    const [a, b, c] = ds;
    let key;
    if (a === b && b === c) key = a === lucky ? 'OVERWRITE' : a === 4 ? 'REAPER' : 'JACKPOT';
    else if ((b === a + 1 && c === b + 1) || (b === a - 1 && c === b - 1)) key = 'CASCADE';
    else if (a + b + c === 10 || a + b + c === 20) key = 'ZERO_SUM';
    else if (a === b || b === c || a === c) key = 'PAIR';
    else key = 'BUST';
    return { key, mult: key === 'JACKPOT' ? Math.max(2, a) : MULT[key] };
  }
  function omen(balance, max) {
    amount(balance); amount(max);
    if (!max || balance > max) throw new RangeError('Balance requires 0 <= value <= positive max');
    return balance === 0 ? 0 : Math.min(99, Math.max(1, Math.ceil(balance * 99 / max)));
  }
  function terminalOutcome(partyBalance, enemyBalance) {
    amount(partyBalance); amount(enemyBalance);
    return partyBalance === 0 ? 'LOSS' : enemyBalance === 0 ? 'WIN' : null;
  }
  function resolveRound(input) {
    const { actualDigits, bases, lucky, partyBalance, partyMax, enemyBalance, enemyMax } = input;
    evaluate(actualDigits, lucky);
    if (!Array.isArray(bases) || bases.length !== 3) throw new RangeError('three strike bases required');
    bases.forEach(amount);
    const partyOmen = omen(partyBalance, partyMax), enemyOmen = omen(enemyBalance, enemyMax);
    if (terminalOutcome(partyBalance, enemyBalance)) throw new RangeError('cannot act after terminal state');
    const charms = input.charms || [], events = [];
    let resolvedDigits = (input.scoringDigits || actualDigits).slice();
    let pattern = evaluate(resolvedDigits, lucky);
    let blackCatUsed = !!input.blackCatUsed;
    const streak = input.bustStreak || 0;
    if (pattern.key === 'BUST' && ((charms.includes('charm_black_cat') && !blackCatUsed) || streak >= 2)) {
      const source = charms.includes('charm_black_cat') && !blackCatUsed ? 'black_cat' : 'haps_hand';
      if (source === 'black_cat') blackCatUsed = true;
      const before = resolvedDigits.slice();
      resolvedDigits[2] = resolvedDigits[0];
      events.push({ type: source, before, after: resolvedDigits.slice() });
      pattern = evaluate(resolvedDigits, lucky);
    }
    const vesperBonus = (input.party || []).includes('chr_vesper') ? actualDigits.filter(d => d === 7).length * 7 : 0;
    const strikeValues = actualDigits.map((d, i) => bases[i] + d + vesperBonus);
    const damage = strikeValues.reduce((sum, n) => sum + n, 0) * pattern.mult;
    amount(damage);
    const containsFour = n => String(n).padStart(2, '0').includes('4');
    const enemyReaper = pattern.key === 'REAPER' && containsFour(enemyOmen) ? Math.floor(enemyBalance * 44 / 100) : 0;
    const partyReaper = pattern.key === 'REAPER' && containsFour(partyOmen) ? Math.floor(partyBalance * 44 / 100) : 0;
    const enemyAfter = Math.max(0, enemyBalance - damage - enemyReaper);
    const partyAfter = Math.max(0, partyBalance - partyReaper);
    const terminal = terminalOutcome(partyAfter, enemyAfter);
    return {
      actualDigits: actualDigits.slice(), resolvedDigits, strikeValues, damage, enemyReaper, partyReaper,
      partyAfter, enemyAfter, terminal, pattern, events, blackCatUsed,
      bustStreak: pattern.key === 'BUST' ? streak + 1 : 0,
      extra: !terminal && pattern.key === 'CASCADE', cancel: !terminal && pattern.key === 'ZERO_SUM'
    };
  }
  function defend({ stoppedDigit, lucky, strikeBase, partyBalance, partyMax, enemyBalance, enemyMax, ofuda }) {
    digit(lucky); amount(strikeBase); omen(partyBalance, partyMax); omen(enemyBalance, enemyMax);
    if (terminalOutcome(partyBalance, enemyBalance)) throw new RangeError('cannot act after terminal state');
    if (ofuda) return { kind: 'PARRY', reflected: 0, partyAfter: partyBalance, enemyAfter: enemyBalance, defended: true, terminal: null };
    digit(stoppedDigit);
    const parry = stoppedDigit === 0, fortune = stoppedDigit === lucky;
    const reflected = fortune ? strikeBase + stoppedDigit : 0;
    const partyAfter = parry || fortune ? partyBalance : Math.max(0, partyBalance - strikeBase - stoppedDigit);
    const enemyAfter = Math.max(0, enemyBalance - reflected);
    return { kind: parry && fortune ? 'PARRY_FORTUNE' : fortune ? 'FORTUNE' : parry ? 'PARRY' : 'HIT', reflected,
      partyAfter, enemyAfter, defended: parry || fortune, terminal: terminalOutcome(partyAfter, enemyAfter) };
  }
  function createRng(seed) {
    let value = seed >>> 0;
    return () => { value += 0x6D2B79F5; let t = value; t = Math.imul(t ^ t >>> 15, t | 1); t ^= t + Math.imul(t ^ t >>> 7, t | 61); return ((t ^ t >>> 14) >>> 0) / 4294967296; };
  }
  function newJar() { return { state: 'idle', digit: null, affectedRounds: 0, defences: 0 }; }
  function jarBeforeRound(actualDigits, current) {
    const scoringDigits = actualDigits.slice(), jar = { ...current };
    if (jar.state === 'holding') { scoringDigits[2] = 0; jar.affectedRounds++; }
    else if (jar.state === 'restoring') { scoringDigits[2] = jar.digit; jar.state = 'spent'; }
    return { scoringDigits, jar };
  }
  function jarAfterRound(current, resolvedDigits, isVarro, terminal) {
    const jar = { ...current };
    if (!isVarro || terminal) return jar;
    if (jar.state === 'idle') return { state: 'holding', digit: resolvedDigits[2], affectedRounds: 0, defences: 0 };
    if (jar.state === 'holding' && jar.affectedRounds >= 3) jar.state = 'restoring';
    return jar;
  }
  function jarDefence(current, defended, terminal) {
    const jar = { ...current };
    if (!terminal && defended && jar.state === 'holding' && ++jar.defences >= 3) jar.state = 'restoring';
    return jar;
  }
  return { ORDER, MULT, CHARM_IDS, MAX_BALANCE, nilFaces, facesFor, evaluate, omen, terminalOutcome, resolveRound, defend, createRng,
    newJar, jarBeforeRound, jarAfterRound, jarDefence };
});
