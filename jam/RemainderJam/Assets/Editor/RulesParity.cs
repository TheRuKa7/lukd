// Batch-mode parity check: Remainder.Rules against fixtures generated from prototype/rules.js.
// Run: Unity -batchmode -quit -projectPath . -executeMethod RulesParity.Run
using System;
using System.IO;
using System.Linq;
using Remainder;
using UnityEngine;

public static class RulesParity
{
    [Serializable] class ECase { public int lucky; public int[] digits; public string key; public int mult; }
    [Serializable] class RCase
    {
        public int[] actual, scoring; public long[] bases; public int lucky; public long pb, pm, eb, em;
        public string[] charms; public bool cat; public int streak; public string[] party;
        public int[] resolved; public long damage, enemyAfter, partyAfter; public string key; public bool catUsed; public int streakAfter;
        public bool extra, cancel; public int events;
    }
    [Serializable] class DCase { public int stopped, lucky; public long @base, pb, pm, eb, em; public bool ofuda; public string kind; public long reflected, partyAfter, enemyAfter; public bool defended; }
    [Serializable] class FCase { public int lucky; public int[] faces; }
    [Serializable] class All { public ECase[] evaluate; public RCase[] rounds; public DCase[] defends; public uint rngSeed; public double[] rngValues; public FCase[] faces; }

    public static void Run()
    {
        int failures = 0, checks = 0;
        void Check(bool ok, string what) { checks++; if (!ok && failures++ < 20) Debug.LogError("PARITY FAIL " + what); }
        var all = JsonUtility.FromJson<All>(File.ReadAllText("Assets/Editor/Fixtures/rules_fixtures.json"));

        foreach (var e in all.evaluate)
        {
            var r = Rules.Evaluate(e.digits, e.lucky);
            Check(r.key.ToString() == e.key && r.mult == e.mult, $"evaluate {string.Join("", e.digits)} lucky {e.lucky}: {r.key}x{r.mult} vs {e.key}x{e.mult}");
        }
        foreach (var c in all.rounds)
        {
            var r = Rules.ResolveRound(new Rules.RoundInput
            {
                actualDigits = c.actual, scoringDigits = c.scoring, bases = c.bases, lucky = c.lucky,
                partyBalance = c.pb, partyMax = c.pm, enemyBalance = c.eb, enemyMax = c.em,
                charms = c.charms, blackCatUsed = c.cat, bustStreak = c.streak, party = c.party
            });
            Check(r.resolvedDigits.SequenceEqual(c.resolved) && r.damage == c.damage && r.enemyAfter == c.enemyAfter &&
                  r.partyAfter == c.partyAfter && r.pattern.key.ToString() == c.key && r.blackCatUsed == c.catUsed &&
                  r.bustStreak == c.streakAfter && r.extra == c.extra && r.cancel == c.cancel && r.events.Count == c.events,
                  $"round {string.Join("", c.actual)} lucky {c.lucky}: dmg {r.damage} vs {c.damage}, {r.pattern.key} vs {c.key}");
        }
        foreach (var d in all.defends)
        {
            var r = Rules.Defend(d.stopped, d.lucky, d.@base, d.pb, d.pm, d.eb, d.em, d.ofuda);
            Check(r.kind == d.kind && r.reflected == d.reflected && r.partyAfter == d.partyAfter && r.enemyAfter == d.enemyAfter && r.defended == d.defended,
                  $"defend {d.stopped} lucky {d.lucky}: {r.kind} vs {d.kind}");
        }
        var rng = Rules.CreateRng(all.rngSeed);
        foreach (var v in all.rngValues) { var x = rng(); Check(Math.Abs(x - v) < 1e-12, $"rng {x} vs {v}"); }
        foreach (var f in all.faces) Check(Rules.NilFaces(f.lucky).SequenceEqual(f.faces), $"faces lucky {f.lucky}");

        var msg = $"RULES PARITY: {checks - failures}/{checks} passed";
        if (failures > 0) { Debug.LogError(msg); EditorExit(1); }
        else { Debug.Log(msg); EditorExit(0); }
    }

    static void EditorExit(int code) { if (Application.isBatchMode) UnityEditor.EditorApplication.Exit(code); }
}
