'use strict';
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const R = require('../prototype/rules.js');
const cases = require('./pattern_cases.json');
for (const c of cases) assert.deepEqual(R.evaluate(c.digits, c.lucky), { key: c.pattern, mult: c.mult });
const expectedFaces = ['01236789','01234789','01234589','01234569','01234567','02345678','03456789','03456789','01456789','01256789'];
for (let d = 0; d < 10; d++) {
  assert.equal(R.nilFaces(d).join(''), expectedFaces[d]);
  assert.ok(R.nilFaces(d).includes(0) && R.nilFaces(d).includes(d));
  assert.equal(R.evaluate([d,d,d],d).mult,21);
}
const base = { actualDigits:[7,7,7], bases:[10,10,10], lucky:7, partyBalance:300, partyMax:300, enemyBalance:10000, enemyMax:10000 };
for (const [digits, damage] of [[[7,7,7],1071], [[3,3,3],117], [[1,2,3],108], [[3,3,4],80], [[7,1,7],90], [[2,9,5],46]]) {
  const r = R.resolveRound({ ...base, actualDigits:digits });
  assert.equal(r.damage,damage,'single-settlement damage');
  assert.equal(r.enemyAfter,10000-damage);
}
const reap = R.resolveRound({ ...base, actualDigits:[4,4,4], bases:[0,0,0], partyBalance:44, partyMax:99, enemyBalance:44, enemyMax:99 });
assert.equal(reap.enemyReaper,19); assert.equal(reap.partyReaper,19);
assert.equal(reap.damage,48); assert.equal(reap.partyAfter,25); assert.equal(reap.enemyAfter,0); assert.equal(reap.terminal,'WIN');
assert.equal(R.terminalOutcome(0,0),'LOSS');
assert.equal(R.terminalOutcome(1,0),'WIN');
assert.throws(()=>R.resolveRound({ ...base, partyBalance:0 }),/terminal/);
assert.throws(()=>R.defend({lucky:7,stoppedDigit:0,strikeBase:20,partyBalance:0,partyMax:300,enemyBalance:100,enemyMax:100}),/terminal/);
assert.equal(R.omen(1,300),1); assert.equal(R.omen(300,300),99); assert.equal(R.omen(0,300),0);
assert.throws(()=>R.omen(1,0)); assert.throws(()=>R.omen(301,300));
const favour = R.resolveRound({ ...base, actualDigits:[1,8,4], bustStreak:2 });
assert.deepEqual(favour.actualDigits,[1,8,4]); assert.deepEqual(favour.resolvedDigits,[1,8,1]);
assert.equal(favour.pattern.key,'ZERO_SUM'); assert.equal(favour.damage,86); assert.equal(favour.bustStreak,0); assert.equal(favour.events[0].type,'haps_hand');
const cat = R.resolveRound({ ...base, actualDigits:[2,9,5], bustStreak:2, charms:['charm_black_cat'] });
assert.equal(cat.events.length,1); assert.equal(cat.events[0].type,'black_cat'); assert.equal(cat.blackCatUsed,true);
const usedCat = R.resolveRound({ ...base, actualDigits:[2,9,5], charms:['charm_black_cat'], blackCatUsed:true });
assert.equal(usedCat.pattern.key,'BUST');
const vesper = R.resolveRound({ ...base, actualDigits:[7,1,2], party:['chr_nil','chr_vesper'] });
assert.deepEqual(vesper.strikeValues,[24,18,19]); assert.equal(vesper.damage,122);
const defence = { lucky:0,stoppedDigit:0,strikeBase:20,partyBalance:100,partyMax:100,enemyBalance:100,enemyMax:100 };
const zero = R.defend(defence); assert.equal(zero.kind,'PARRY_FORTUNE'); assert.equal(zero.reflected,20); assert.equal(zero.enemyAfter,80); assert.equal(zero.partyAfter,100);
const ofuda = R.defend({...defence, stoppedDigit:null, ofuda:true}); assert.equal(ofuda.kind,'PARRY'); assert.equal(ofuda.reflected,0); assert.equal(ofuda.enemyAfter,100);
assert.equal(R.defend({...defence,lucky:7}).reflected,0);
assert.equal(R.defend({...defence,lucky:7,stoppedDigit:7}).reflected,27);
let jar = R.jarAfterRound(R.newJar(),[1,2,3],true,null);
assert.equal(jar.digit,3);
for (let i=0;i<3;i++) {
  const round=R.jarBeforeRound([7,7,7],jar); assert.deepEqual(round.scoringDigits,[7,7,0]);
  jar=R.jarAfterRound(round.jar,round.scoringDigits,true,null);
}
assert.equal(jar.state,'restoring','expiry counts player rounds without enemy actions');
const restored=R.jarBeforeRound([7,7,7],jar); assert.deepEqual(restored.scoringDigits,[7,7,3]); assert.equal(restored.jar.state,'spent');
assert.deepEqual(R.jarBeforeRound([7,7,7],restored.jar).scoringDigits,[7,7,7]);
jar=R.jarAfterRound(R.newJar(),[1,2,3],true,null);
jar=R.jarDefence(jar,true,null); assert.equal(jar.defences,1,'Ofuda is one defended action');
jar=R.jarDefence(jar,true,null); jar=R.jarDefence(jar,true,null); assert.equal(jar.state,'restoring');
assert.equal(R.jarAfterRound(R.newJar(),[1,2,3],true,'WIN').state,'idle');
const rng1=R.createRng(713),rng2=R.createRng(713);for(let i=0;i<100;i++) assert.equal(rng1(),rng2());
const prototype=fs.readFileSync(path.join(__dirname,'../prototype/index.html'),'utf8');
new Function(prototype.match(/<script>\s*([\s\S]*?)<\/script>/)[1]);
console.log('Reference rules: exact pattern, settlement, Reaper snapshot, terminal, zero defence, repair, face, passive and jar regressions passed; prototype syntax parsed.');
