// Port of prototype/rules.js (the reference rules). Pure logic, no Unity dependencies.
using System;
using System.Collections.Generic;
using System.Linq;

namespace Remainder
{
    public enum Pattern { OVERWRITE, REAPER, JACKPOT, CASCADE, ZERO_SUM, PAIR, BUST }

    public struct Eval { public Pattern key; public int mult; }

    public class RepairEvent { public string type; public int[] before, after; }

    public class RoundResult
    {
        public int[] actualDigits, resolvedDigits, strikeValues;
        public long damage, enemyReaper, partyReaper, partyAfter, enemyAfter;
        public string terminal; // null, "WIN", "LOSS"
        public Eval pattern;
        public List<RepairEvent> events = new List<RepairEvent>();
        public bool blackCatUsed, extra, cancel;
        public int bustStreak;
    }

    public class DefendResult
    {
        public string kind; // HIT, PARRY, FORTUNE, PARRY_FORTUNE
        public long reflected, partyAfter, enemyAfter;
        public bool defended;
        public string terminal;
    }

    public enum JarState { Idle, Holding, Restoring, Spent }

    public struct Jar
    {
        public JarState state; public int digit; public int affectedRounds; public int defences;
        public static Jar New() => new Jar { state = JarState.Idle, digit = -1 };
    }

    public static class Rules
    {
        public const string Horseshoe = "charm_horseshoe", BlackCat = "charm_black_cat", Ofuda = "charm_ofuda";
        public const long MaxBalance = 1000000000000L;

        static void Digit(int d) { if (d < 0 || d > 9) throw new ArgumentOutOfRangeException(nameof(d), "digit must be 0..9"); }
        static void Amount(long n) { if (n < 0 || n > MaxBalance) throw new ArgumentOutOfRangeException(nameof(n), "invalid bounded amount"); }

        public static int Mult(Pattern p) => p switch
        {
            Pattern.OVERWRITE => 21, Pattern.REAPER => 4, Pattern.CASCADE => 3,
            Pattern.ZERO_SUM => 2, Pattern.PAIR => 2, Pattern.BUST => 1, _ => 2
        };

        public static int[] NilFaces(int lucky)
        {
            Digit(lucky);
            var omitted = new[] { (lucky + 4) % 10, (lucky + 5) % 10 }.Select(d => d == 0 ? (lucky + 6) % 10 : d).ToArray();
            return Enumerable.Range(0, 10).Where(d => !omitted.Contains(d)).ToArray();
        }

        public static int[] FacesFor(string hero, int lucky)
        {
            if (hero == "chr_nil") return NilFaces(lucky);
            if (hero == "chr_vesper") return new[] { 0, 1, 2, 3, 5, 6, 7, 8 };
            throw new ArgumentException("hero outside implemented reference scope");
        }

        public static Eval Evaluate(int[] ds, int lucky)
        {
            Digit(lucky);
            if (ds == null || ds.Length != 3) throw new ArgumentException("base reel requires exactly 3 digits");
            foreach (var d in ds) Digit(d);
            int a = ds[0], b = ds[1], c = ds[2];
            Pattern key;
            if (a == b && b == c) key = a == lucky ? Pattern.OVERWRITE : a == 4 ? Pattern.REAPER : Pattern.JACKPOT;
            else if ((b == a + 1 && c == b + 1) || (b == a - 1 && c == b - 1)) key = Pattern.CASCADE;
            else if (a + b + c == 10 || a + b + c == 20) key = Pattern.ZERO_SUM;
            else if (a == b || b == c || a == c) key = Pattern.PAIR;
            else key = Pattern.BUST;
            return new Eval { key = key, mult = key == Pattern.JACKPOT ? Math.Max(2, a) : Mult(key) };
        }

        public static int Omen(long balance, long max)
        {
            Amount(balance); Amount(max);
            if (max == 0 || balance > max) throw new ArgumentException("Balance requires 0 <= value <= positive max");
            return balance == 0 ? 0 : (int)Math.Min(99, Math.Max(1, (long)Math.Ceiling(balance * 99.0 / max)));
        }

        public static string Terminal(long party, long enemy) { Amount(party); Amount(enemy); return party == 0 ? "LOSS" : enemy == 0 ? "WIN" : null; }

        public class RoundInput
        {
            public int[] actualDigits, scoringDigits; public long[] bases; public int lucky;
            public long partyBalance, partyMax, enemyBalance, enemyMax;
            public IList<string> charms = new string[0]; public bool blackCatUsed; public int bustStreak;
            public IList<string> party = new string[0];
        }

        public static RoundResult ResolveRound(RoundInput i)
        {
            Evaluate(i.actualDigits, i.lucky);
            if (i.bases == null || i.bases.Length != 3) throw new ArgumentException("three strike bases required");
            foreach (var b in i.bases) Amount(b);
            int partyOmen = Omen(i.partyBalance, i.partyMax), enemyOmen = Omen(i.enemyBalance, i.enemyMax);
            if (Terminal(i.partyBalance, i.enemyBalance) != null) throw new InvalidOperationException("cannot act after terminal state");
            var r = new RoundResult { actualDigits = (int[])i.actualDigits.Clone() };
            var resolved = (int[])(i.scoringDigits ?? i.actualDigits).Clone();
            var pattern = Evaluate(resolved, i.lucky);
            bool blackCatUsed = i.blackCatUsed;
            int streak = i.bustStreak;
            bool hasCat = i.charms.Contains(BlackCat);
            if (pattern.key == Pattern.BUST && ((hasCat && !blackCatUsed) || streak >= 2))
            {
                string source = hasCat && !blackCatUsed ? "black_cat" : "haps_hand";
                if (source == "black_cat") blackCatUsed = true;
                var before = (int[])resolved.Clone();
                resolved[2] = resolved[0];
                r.events.Add(new RepairEvent { type = source, before = before, after = (int[])resolved.Clone() });
                pattern = Evaluate(resolved, i.lucky);
            }
            int vesperBonus = i.party.Contains("chr_vesper") ? i.actualDigits.Count(d => d == 7) * 7 : 0;
            r.strikeValues = i.actualDigits.Select((d, k) => (int)(i.bases[k] + d + vesperBonus)).ToArray();
            long damage = r.strikeValues.Sum(v => (long)v) * pattern.mult;
            Amount(damage);
            bool ContainsFour(int n) => n.ToString("00").Contains('4');
            r.enemyReaper = pattern.key == Pattern.REAPER && ContainsFour(enemyOmen) ? i.enemyBalance * 44 / 100 : 0;
            r.partyReaper = pattern.key == Pattern.REAPER && ContainsFour(partyOmen) ? i.partyBalance * 44 / 100 : 0;
            r.enemyAfter = Math.Max(0, i.enemyBalance - damage - r.enemyReaper);
            r.partyAfter = Math.Max(0, i.partyBalance - r.partyReaper);
            r.terminal = Terminal(r.partyAfter, r.enemyAfter);
            r.damage = damage; r.resolvedDigits = resolved; r.pattern = pattern; r.blackCatUsed = blackCatUsed;
            r.bustStreak = pattern.key == Pattern.BUST ? streak + 1 : 0;
            r.extra = r.terminal == null && pattern.key == Pattern.CASCADE;
            r.cancel = r.terminal == null && pattern.key == Pattern.ZERO_SUM;
            return r;
        }

        public static DefendResult Defend(int stoppedDigit, int lucky, long strikeBase, long partyBalance, long partyMax, long enemyBalance, long enemyMax, bool ofuda)
        {
            Digit(lucky); Amount(strikeBase); Omen(partyBalance, partyMax); Omen(enemyBalance, enemyMax);
            if (Terminal(partyBalance, enemyBalance) != null) throw new InvalidOperationException("cannot act after terminal state");
            if (ofuda) return new DefendResult { kind = "PARRY", reflected = 0, partyAfter = partyBalance, enemyAfter = enemyBalance, defended = true };
            Digit(stoppedDigit);
            bool parry = stoppedDigit == 0, fortune = stoppedDigit == lucky;
            long reflected = fortune ? strikeBase + stoppedDigit : 0;
            long partyAfter = parry || fortune ? partyBalance : Math.Max(0, partyBalance - strikeBase - stoppedDigit);
            long enemyAfter = Math.Max(0, enemyBalance - reflected);
            return new DefendResult
            {
                kind = parry && fortune ? "PARRY_FORTUNE" : fortune ? "FORTUNE" : parry ? "PARRY" : "HIT",
                reflected = reflected, partyAfter = partyAfter, enemyAfter = enemyAfter, defended = parry || fortune,
                terminal = Terminal(partyAfter, enemyAfter)
            };
        }

        // mulberry32, identical to the prototype
        public static Func<double> CreateRng(uint seed)
        {
            uint value = seed;
            return () =>
            {
                unchecked
                {
                    value += 0x6D2B79F5;
                    uint t = value;
                    t = (uint)((int)(t ^ (t >> 15)) * (int)(t | 1));
                    t ^= t + (uint)((int)(t ^ (t >> 7)) * (int)(t | 61));
                    return (t ^ (t >> 14)) / 4294967296.0;
                }
            };
        }

        public static (int[] scoring, Jar jar) JarBeforeRound(int[] actual, Jar jar)
        {
            var scoring = (int[])actual.Clone();
            if (jar.state == JarState.Holding) { scoring[2] = 0; jar.affectedRounds++; }
            else if (jar.state == JarState.Restoring) { scoring[2] = jar.digit; jar.state = JarState.Spent; }
            return (scoring, jar);
        }

        public static Jar JarAfterRound(Jar jar, int[] resolved, bool isVarro, string terminal)
        {
            if (!isVarro || terminal != null) return jar;
            if (jar.state == JarState.Idle) return new Jar { state = JarState.Holding, digit = resolved[2] };
            if (jar.state == JarState.Holding && jar.affectedRounds >= 3) jar.state = JarState.Restoring;
            return jar;
        }

        public static Jar JarDefence(Jar jar, bool defended, string terminal)
        {
            if (terminal == null && defended && jar.state == JarState.Holding && ++jar.defences >= 3) jar.state = JarState.Restoring;
            return jar;
        }

        public static string Label(Pattern p) => p == Pattern.ZERO_SUM ? "ZERO-SUM" : p.ToString();
    }
}
