// The Audit: three stopped digits per round, scored by Rules; enemy actions defended on a wheel.
// Numbers follow tuning/jam_tuning.csv; behaviour follows docs/JAM_SLICE.md and docs/JAM_SCRIPT.md.
using System;
using System.Collections;
using System.Linq;
using UnityEngine;
using UnityEngine.UI;

namespace Remainder
{
    public class FightDef
    {
        public string name, art;
        public long max, attack;
        public bool solo, tutorial, varro;
        public int level = 1, civic;
    }

    public partial class Game
    {
        class Bar { public Image fill; public Text value, omen; public long max; }

        // per-fight state
        long pBal, pMax, eBal, eMax, enemyBase, strikeBase;
        bool catUsed, ofudaUsed, cancelNext, phase2Pending, phase2, firstDefence;
        int streak;
        Jar jar;
        Bar partyBar, enemyBar;
        Text intentText, favourText, jarText, charmText, patternText;
        Text[] slotTexts = new Text[3];
        Image[] slotBoxes = new Image[3];
        Wheel wheel;
        FightDef cur;

        IEnumerator Fight(FightDef d)
        {
            while (true)
            {
                bool won = false;
                yield return FightOnce(d, w => won = w);
                Debug.Log($"JAM: fight {d.name} {(won ? "WON" : "LOST")} party={pBal}/{pMax} enemy={eBal}/{eMax}");
                if (won) yield break;
                yield return Card("YOUR STAKE IS SPENT", "Retry restores the stake and the fight from its checkpoint.", 0.1f, false, UI.Red);
                banner.gameObject.SetActive(true);
                int c = -1;
                yield return Choose(null, new[] { "RETRY FIGHT" }, x => c = x);
                banner.gameObject.SetActive(false);
            }
        }

        IEnumerator FightOnce(FightDef d, Action<bool> done)
        {
            cur = d;
            pMax = 300 + 40 * (d.level - 1); pBal = pMax;
            eMax = eBal = d.max; enemyBase = d.attack; strikeBase = 10 * d.level;
            catUsed = ofudaUsed = cancelNext = phase2Pending = phase2 = false; firstDefence = true;
            streak = 0; jar = Jar.New();
            UI.Clear(hud); UI.Clear(reel);
            if (!actors.ContainsKey("nil")) Nil(0.26f);
            if (!d.solo && !actors.ContainsKey("vesper")) Actor("vesper", "vesper_side", 0.12f);
            if (!actors.ContainsKey("enemy")) Actor("enemy", d.art, d.art.StartsWith("hound") ? 0.81f : 0.78f);
            actors["enemy"].color = Color.white;
            BuildHud(d);
            wheel = Wheel.Create(reel, new Vector2(0, -40));
            wheel.gameObject.SetActive(false);
            int round = 0;

            while (true)
            {
                // ---------------- player rounds (a Cascade grants another before the enemy acts)
                bool again = true;
                while (again)
                {
                    again = false; round++;
                    var party = d.solo ? new[] { "chr_nil" } : new[] { "chr_nil", "chr_vesper" };
                    int[] actual = new int[3]; string[] who = new string[3];
                    ResetSlots();
                    bool authored = d.tutorial && round == 1;
                    int j = TutorialDigit();
                    for (int i = 0; i < 3; i++)
                    {
                        string hero = "chr_nil";
                        if (!d.solo)
                        {
                            yield return Once("duo_010", "CHOOSE WHO STRIKES.", "Both heroes act. One acts twice.");
                            string chosen = null;
                            yield return ChooseStriker(i, who, h => chosen = h);
                            hero = chosen;
                        }
                        who[i] = hero;
                        ConfigureWheel(hero, actual, i, authored, false);
                        if (i == 2)
                        {
                            int a0 = actual[0], a1 = actual[1];
                            wheel.SetShimmer(x => Preview(a0, a1, x));
                        }
                        else wheel.SetShimmer(null);
                        if (d.tutorial && round == 1 && i == 0) yield return Once("solo_010", "STOP THE NUMBER.", "Tutorial round: these three stops are scripted.");
                        if (i == 2 && !d.solo) yield return Once("duo_030", "SHIMMERING FACES FINISH A PATTERN.", "Pattern Sight shows which last digits score.");
                        wheel.Spin();
                        hintText.text = "Tap or press Space to stop";
                        yield return WaitTap();
                        hintText.text = "";
                        if (authored) yield return wheel.StopOn(j, Reduced);
                        else if (Auto && Skilled) yield return wheel.StopOn(BotPick(hero, actual, i, party), Reduced);
                        else yield return wheel.Stop(Reduced);
                        actual[i] = wheel.Result;
                        SetSlot(i, actual[i].ToString(), hero == "chr_vesper" ? new Color(0.95f, 0.45f, 0.45f) : UI.Nixie);
                        if (d.tutorial && round == 1 && i == 0) yield return Once("solo_020", "THREE STOPS MAKE A PATTERN.", "", false);
                    }
                    wheel.gameObject.SetActive(false);

                    // jar substitution happens after the actual stops, before repair and evaluation
                    int[] scoring = actual;
                    if (d.varro)
                    {
                        var before = jar.state;
                        var jb = Rules.JarBeforeRound(actual, jar);
                        scoring = jb.scoring; jar = jb.jar;
                        if (before == JarState.Holding) { SetSlot(2, actual[2] + ">0", UI.Red); yield return Wait(0.5f); }
                        if (before == JarState.Restoring) { SetSlot(2, actual[2] + ">" + scoring[2], UI.Gold); Sfx.Play("coin"); yield return Card("DIGIT RETURNED", "Your saved digit scores in the last slot.", 1.2f); }
                    }
                    var r = Rules.ResolveRound(new Rules.RoundInput
                    {
                        actualDigits = actual, scoringDigits = scoring, bases = new[] { strikeBase, strikeBase, strikeBase }, lucky = resonance,
                        partyBalance = pBal, partyMax = pMax, enemyBalance = eBal, enemyMax = eMax,
                        charms = charm == null ? new string[0] : new[] { charm }, blackCatUsed = catUsed, bustStreak = streak, party = party
                    });
                    foreach (var ev in r.events)
                    {
                        SetSlot(2, ev.before[2] + ">" + ev.after[2], UI.Teal);
                        Sfx.Play("coin");
                        if (ev.type == "black_cat") yield return Card("BLACK CAT", "The third digit copies the first.", 1.2f, false, UI.Teal);
                        else
                        {
                            yield return Card("HAP'S HAND", "After two Busts, luck repairs the third digit.", 1.2f, false, UI.Teal);
                            if (!d.solo && !shownCards.Contains("favour_020")) { shownCards.Add("favour_020"); yield return Say("VESPER", "Hap's watching."); }
                        }
                    }
                    found.Add(r.pattern.key);
                    biggestRound = Math.Max(biggestRound, r.damage);
                    Sfx.Play(Sfx.ForPattern(r.pattern.key));
                    patternText.text = Rules.Label(r.pattern.key) + "  ×" + r.pattern.mult;
                    string maths = string.Join(" + ", r.strikeValues) + "  ×" + r.pattern.mult + "  =  " + r.damage;
                    var colour = r.pattern.key == Pattern.BUST ? UI.Paper : r.pattern.key == Pattern.OVERWRITE ? UI.Gold : UI.Nixie;
                    if (r.pattern.key == Pattern.OVERWRITE || r.pattern.key == Pattern.JACKPOT) yield return Flash(new Color(1, 0.85f, 0.4f, 0.5f));
                    yield return Card(Rules.Label(r.pattern.key) + (r.pattern.mult > 1 ? "  ×" + r.pattern.mult : ""), maths, 1.0f, false, colour);
                    FloatText(ActorTop("enemy"), "-" + r.damage, UI.Gold, 60);
                    StartCoroutine(Shake(actors["enemy"].rectTransform));
                    if (r.enemyReaper > 0) FloatText(ActorTop("enemy") + new Vector2(0, -60), "REAPER -" + r.enemyReaper, UI.Red, 40);
                    eBal = r.enemyAfter; pBal = r.partyAfter;
                    yield return AnimateBars();
                    yield return PatternLesson(r.pattern.key, d);
                    catUsed = r.blackCatUsed;
                    int prevStreak = streak; streak = r.bustStreak;
                    if (streak >= 1 && prevStreak == 0) yield return Once("favour_010", "LUCK IS TURNING.", "After a Bust: slower wheels, and faces you already stopped grow wider.");
                    UpdateStatus();
                    if (d.varro)
                    {
                        var prev = jar.state;
                        jar = Rules.JarAfterRound(jar, r.resolvedDigits, true, r.terminal);
                        if (prev == JarState.Idle && jar.state == JarState.Holding)
                        {
                            Sfx.Play("alarm");
                            yield return Card("HE HOLDS YOUR LAST DIGIT.", "IT SCORES AS 0 WHILE HELD.", 1.8f, false, UI.Red);   // jam_jar_warn
                            yield return Say("VESPER", "Three defences—or three rounds. Then you get it back.");                       // jam_jar_help
                        }
                        if (prev == JarState.Holding && jar.state == JarState.Restoring) yield return Card("THE JAR OPENS", "Your digit returns next round.", 1.2f, false, UI.Gold);
                        UpdateStatus();
                    }
                    if (r.terminal == "WIN") { yield return Victory(d); done(true); yield break; }
                    if (r.terminal == "LOSS") { done(false); yield break; }
                    if (r.extra) again = true;
                    if (r.cancel) cancelNext = true;
                    if (d.varro && !phase2Pending && eBal * 2 <= eMax)
                    {
                        phase2Pending = true;
                        yield return Say("VARRO", "Final notice.");                                                     // jam_varro_phase2
                        intentText.text = "NEXT STRIKE 40  ·  THEN 80";
                    }
                }

                // ---------------- enemy action
                if (cancelNext)
                {
                    cancelNext = false;
                    yield return Card("ACTION CANCELLED", "Zero-Sum: their next action never happens.", 1.2f, false, UI.Teal);
                    continue;
                }
                long atk = enemyBase;
                string target = d.solo ? "chr_nil" : (rng() < 0.5 ? "chr_nil" : "chr_vesper");
                string targetName = target == "chr_nil" ? "NIL" : "VESPER";
                yield return Card(d.name + " STRIKES " + targetName, atk + " + the digit you stop.  Stop 0 to Parry.", 1.1f, false, UI.Red);
                DefendResult dr;
                if (charm == Rules.Ofuda && !ofudaUsed)
                {
                    ofudaUsed = true;
                    dr = Rules.Defend(0, resonance, atk, pBal, pMax, eBal, eMax, true);
                    Sfx.Play("parry");
                    yield return Card("OFUDA WARD", "The first strike is parried automatically.", 1.3f, false, UI.Teal);
                }
                else
                {
                    ConfigureWheel(target, null, 0, false, true);
                    wheel.SetShimmer(x => x == 0 || x == resonance);
                    wheel.SetCaption("DEFEND · " + targetName, UI.Red);
                    yield return Once("solo_050", "STOP ON 0 TO PARRY.",
                        resonance == 0 ? "0 PARRIES AND REFLECTS ONCE." : "Stopping your lucky number reflects the blow.");
                    wheel.Spin();
                    hintText.text = "Tap or press Space to defend";
                    yield return WaitTap();
                    hintText.text = "";
                    if (Auto && Skilled) yield return wheel.StopOn(0, Reduced); else yield return wheel.Stop(Reduced);
                    int digit = wheel.Result;
                    wheel.gameObject.SetActive(false);
                    dr = Rules.Defend(digit, resonance, atk, pBal, pMax, eBal, eMax, false);
                }
                firstDefence = false;
                var hurt = target == "chr_nil" ? "nil" : "vesper";
                if (dr.kind == "HIT")
                {
                    Sfx.Play("hit");
                    StartCoroutine(Flash(new Color(0.9f, 0.1f, 0.1f, 0.35f)));
                    StartCoroutine(Shake(actors[hurt].rectTransform));
                    FloatText(ActorTop(hurt), "-" + (pBal - dr.partyAfter), UI.Red);
                    if (target == "chr_nil" && !shownCards.Contains("solo_090")) { shownCards.Add("solo_090"); pBal = dr.partyAfter; yield return AnimateBars(); yield return Say("NIL", "Noted."); }
                }
                else
                {
                    Sfx.Play("parry");
                    FloatText(ActorTop(hurt), dr.kind == "PARRY" ? "PARRY" : dr.kind == "FORTUNE" ? "FORTUNE" : "PARRY + FORTUNE", UI.Teal, 46);
                    if (dr.reflected > 0) FloatText(ActorTop("enemy"), "REFLECT -" + dr.reflected, UI.Gold, 46);
                }
                pBal = dr.partyAfter; eBal = dr.enemyAfter;
                yield return AnimateBars();
                if (d.varro)
                {
                    var prev = jar.state;
                    jar = Rules.JarDefence(jar, dr.defended, dr.terminal);
                    if (prev == JarState.Holding && jar.state == JarState.Restoring) yield return Card("THE JAR OPENS", "Three defences. Your digit returns next round.", 1.3f, false, UI.Gold);
                    UpdateStatus();
                }
                if (phase2Pending && !phase2) { phase2 = true; enemyBase = 80; intentText.text = "STRIKES NOW 80"; }
                if (dr.terminal == "WIN") { yield return Victory(d); done(true); yield break; }
                if (dr.terminal == "LOSS") { done(false); yield break; }
            }
        }

        // Test bot for headless balance sweeps (-jam auto=1 skill=1): aims like a careful player.
        int BotPick(string hero, int[] actual, int slot, string[] party)
        {
            var faces = Rules.FacesFor(hero, resonance);
            if (slot == 0) return faces.Contains(resonance) ? resonance : faces.Max();
            if (slot == 1) return faces.Contains(actual[0]) ? actual[0] : faces.Max();
            int best = faces[0]; long bestScore = -1;
            foreach (var f in faces)
            {
                var a = new[] { actual[0], actual[1], f };
                var s = (int[])a.Clone();
                if (cur.varro && jar.state == JarState.Holding) s[2] = 0;
                if (cur.varro && jar.state == JarState.Restoring) s[2] = jar.digit;
                var r = Rules.ResolveRound(new Rules.RoundInput
                {
                    actualDigits = a, scoringDigits = s, bases = new[] { strikeBase, strikeBase, strikeBase }, lucky = resonance,
                    partyBalance = pBal, partyMax = pMax, enemyBalance = eBal, enemyMax = eMax,
                    charms = charm == null ? new string[0] : new[] { charm }, blackCatUsed = catUsed, bustStreak = streak, party = party
                });
                long score = r.damage + (r.cancel ? 60 : 0) + (r.extra ? 80 : 0);
                if (score > bestScore) { bestScore = score; best = f; }
            }
            return best;
        }

        int TutorialDigit()
        {
            var faces = Rules.NilFaces(Mathf.Max(0, resonance));
            for (int d = 1; d <= 9; d++) if (d != resonance && d != 4 && faces.Contains(d)) return d;
            return 1;
        }

        bool Preview(int a0, int a1, int x)
        {
            var s = new[] { a0, a1, x };
            if (cur.varro && jar.state == JarState.Holding) s[2] = 0;
            if (cur.varro && jar.state == JarState.Restoring) s[2] = jar.digit;
            var e = Rules.Evaluate(s, resonance);
            if (e.key == Pattern.BUST && ((charm == Rules.BlackCat && !catUsed) || streak >= 2)) { s[2] = s[0]; e = Rules.Evaluate(s, resonance); }
            return e.key != Pattern.BUST;
        }

        void ConfigureWheel(string hero, int[] stopped, int count, bool firstDemo, bool defence)
        {
            var faces = Rules.FacesFor(hero, resonance);
            bool tutorialZero = defence && cur.tutorial && firstDefence;
            wheel.Build(faces, digit =>
            {
                float w = 1f;
                if (hero == "chr_nil" && digit == resonance) w *= 2f;
                if (charm == Rules.Horseshoe && digit == resonance) w *= 1.5f;
                if (!defence && streak >= 1 && stopped != null && stopped.Take(count).Contains(digit)) w *= 1.5f;
                if (tutorialZero && digit == 0) w *= 2f;   // explicit, labelled tutorial width
                return w;
            }, hero == "chr_nil" ? resonance : -1);
            float speed = hero == "chr_nil" ? 470f : 620f;
            if (Assist) speed *= 0.7f;
            if (streak >= 1 && !defence) speed *= 0.8f;
            if (firstDemo) speed *= 0.6f;
            wheel.speed = speed;
            wheel.SetCaption((hero == "chr_nil" ? "NIL" : "VESPER") + (tutorialZero ? " · TUTORIAL: WIDE 0" : ""), hero == "chr_nil" ? UI.Nixie : new Color(0.95f, 0.45f, 0.45f));
        }

        IEnumerator ChooseStriker(int slot, string[] who, Action<string> result)
        {
            string forced = null;
            if (slot == 2)
            {
                if (who[0] == who[1]) forced = who[0] == "chr_nil" ? "chr_vesper" : "chr_nil";
            }
            if (forced != null) { result(forced); yield break; }
            string suggestion = slot == 1 ? (who[0] == "chr_nil" ? "chr_vesper" : "chr_nil") : "chr_nil";
            string picked = null;
            var nilB = UI.Btn(reel, "[1] NIL", () => picked = "chr_nil", new Vector2(190, 56), 28, new Color(0.3f, 0.17f, 0.06f, 0.95f));
            UI.Place((RectTransform)nilB.transform, new Vector2(0.5f, 0.5f), new Vector2(0.5f, 0.5f), new Vector2(-110, -40), new Vector2(190, 56));
            var vesB = UI.Btn(reel, "[2] VESPER", () => picked = "chr_vesper", new Vector2(190, 56), 28, new Color(0.32f, 0.06f, 0.08f, 0.95f));
            UI.Place((RectTransform)vesB.transform, new Vector2(0.5f, 0.5f), new Vector2(0.5f, 0.5f), new Vector2(110, -40), new Vector2(190, 56));
            var note = UI.Txt(reel, "Note", "WHO STRIKES " + (slot + 1) + "?   Space picks " + (suggestion == "chr_nil" ? "NIL" : "VESPER"), UI.Bold, 24, UI.Paper);
            UI.Place(note.rectTransform, new Vector2(0.5f, 0.5f), new Vector2(0.5f, 0.5f), new Vector2(0, 20), new Vector2(600, 30));
            UI.Outlined(note, Color.black);
            tap = false;
            while (picked == null)
            {
                if (Input.GetKeyDown(KeyCode.Alpha1) || Input.GetKeyDown(KeyCode.Keypad1)) picked = "chr_nil";
                if (Input.GetKeyDown(KeyCode.Alpha2) || Input.GetKeyDown(KeyCode.Keypad2)) picked = "chr_vesper";
                if (tap) picked = suggestion;
                yield return null;
            }
            tap = false;
            Destroy(nilB.gameObject); Destroy(vesB.gameObject); Destroy(note.gameObject);
            result(picked);
        }

        IEnumerator PatternLesson(Pattern p, FightDef d)
        {
            switch (p)
            {
                case Pattern.JACKPOT:
                    if (d.tutorial && !shownCards.Contains("solo_030")) { yield return Once("solo_030", "JACKPOT", "THREE MATCH."); yield return Say("NIL", "…Huh."); }
                    break;
                case Pattern.PAIR: yield return Once("solo_070", "PAIR", "TWO MATCH."); break;
                case Pattern.BUST: yield return Once("solo_080", "BUST", "YOUR STRIKES STILL COUNT."); break;
                case Pattern.CASCADE: yield return Once("duo_040", "CASCADE", "GO AGAIN."); break;
                case Pattern.ZERO_SUM: yield return Once("duo_050", "ZERO-SUM", "THEIR NEXT ACTION IS CANCELLED."); break;
                case Pattern.OVERWRITE: yield return Once("overwrite", "OVERWRITE", "Three of the number you chose. ×21."); break;
                case Pattern.REAPER: yield return Once("reaper", "REAPER", "Three fours. Unlucky for anyone whose Audit shows a 4."); break;
            }
        }

        IEnumerator Victory(FightDef d)
        {
            Sfx.Play("jackpot");
            var e = actors["enemy"];
            float t = 0;
            while (t < 0.6f && e != null) { t += Time.deltaTime; e.color = new Color(1, 1, 1, 1 - t / 0.6f * 0.6f); yield return null; }
            yield return Card("AUDIT COMPLETE", d.varro ? "Varro's stake reaches zero. He is still breathing." : "The construct falls inert.", 1.8f);   // jam_solo_100 / jam_duo_060 / jam_varro_win
            UI.Clear(hud); UI.Clear(reel);
        }

        // ---------------- HUD

        void BuildHud(FightDef d)
        {
            partyBar = MakeBar(new Vector2(0, 1), d.solo ? "NIL" : "NIL & VESPER", pMax);
            enemyBar = MakeBar(new Vector2(1, 1), d.name + (d.civic > 0 ? "  ·  CIVIC " + d.civic : ""), eMax);
            intentText = UI.Txt(hud, "Intent", "STRIKES " + d.attack, UI.Bold, 22, UI.Red, TextAnchor.UpperRight);
            UI.Place(intentText.rectTransform, new Vector2(1, 1), new Vector2(1, 1), new Vector2(-92, -112), new Vector2(420, 28));
            UI.Outlined(intentText, Color.black);
            for (int i = 0; i < 3; i++)
            {
                slotBoxes[i] = UI.Img(hud, "Slot", new Color(0.05f, 0.05f, 0.08f, 0.92f));
                UI.Place(slotBoxes[i].rectTransform, new Vector2(0.5f, 0.5f), new Vector2(0.5f, 0.5f), new Vector2((i - 1) * 104, 220), new Vector2(94, 88));
                var e = UI.Img(slotBoxes[i].transform, "Edge", UI.Brass); UI.Place(e.rectTransform, new Vector2(0.5f, 0), new Vector2(0.5f, 0), Vector2.zero, new Vector2(94, 3));
                slotTexts[i] = UI.Txt(slotBoxes[i].transform, "Digit", "", UI.Title, 64, UI.Nixie);
                UI.Stretch(slotTexts[i].rectTransform);
            }
            patternText = UI.Txt(hud, "Pattern", "", UI.Title, 30, UI.Gold);
            UI.Place(patternText.rectTransform, new Vector2(0.5f, 0.5f), new Vector2(0.5f, 0.5f), new Vector2(0, 160), new Vector2(400, 34));
            UI.Outlined(patternText, Color.black);
            favourText = UI.Txt(hud, "Favour", "", UI.Bold, 22, UI.Teal, TextAnchor.UpperLeft);
            UI.Place(favourText.rectTransform, new Vector2(0, 1), new Vector2(0, 1), new Vector2(24, -112), new Vector2(460, 28));
            UI.Outlined(favourText, Color.black);
            charmText = UI.Txt(hud, "Charm", "", UI.Bold, 22, UI.Brass, TextAnchor.UpperLeft);
            UI.Place(charmText.rectTransform, new Vector2(0, 1), new Vector2(0, 1), new Vector2(24, -140), new Vector2(460, 28));
            UI.Outlined(charmText, Color.black);
            jarText = UI.Txt(hud, "Jar", "", UI.Bold, 22, UI.Paper, TextAnchor.UpperRight);
            UI.Place(jarText.rectTransform, new Vector2(1, 1), new Vector2(1, 1), new Vector2(-92, -140), new Vector2(520, 56));
            UI.Outlined(jarText, Color.black);
            UpdateStatus();
            SetBars();
        }

        Bar MakeBar(Vector2 corner, string title, long max)
        {
            bool right = corner.x > 0.5f;
            var box = UI.Img(hud, "Bar", UI.Panel);
            UI.Place(box.rectTransform, corner, corner, new Vector2(right ? -84 : 16, -12), new Vector2(440, 92));
            var name = UI.Txt(box.transform, "Name", title, UI.Title, 28, UI.Paper, right ? TextAnchor.UpperRight : TextAnchor.UpperLeft);
            UI.Place(name.rectTransform, new Vector2(0, 1), new Vector2(0, 1), new Vector2(12, -6), new Vector2(436, 30));
            var back = UI.Img(box.transform, "Back", new Color(0, 0, 0, 0.7f));
            UI.Place(back.rectTransform, new Vector2(0, 0), new Vector2(0, 0), new Vector2(12, 14), new Vector2(300, 22));
            var fill = UI.Img(back.transform, "Fill", right ? UI.Red : UI.Nixie);
            fill.type = Image.Type.Filled; fill.fillMethod = Image.FillMethod.Horizontal; UI.Stretch(fill.rectTransform);
            var value = UI.Txt(box.transform, "Value", "", UI.Bold, 22, UI.Paper, TextAnchor.LowerLeft);
            UI.Place(value.rectTransform, new Vector2(0, 0), new Vector2(0, 0), new Vector2(12, 36), new Vector2(300, 24));
            var omen = UI.Txt(box.transform, "Omen", "", UI.Title, 44, UI.Gold, TextAnchor.LowerRight);
            UI.Place(omen.rectTransform, new Vector2(1, 0), new Vector2(1, 0), new Vector2(-12, 6), new Vector2(140, 50));
            return new Bar { fill = fill, value = value, omen = omen, max = max };
        }

        void SetBars()
        {
            void Set(Bar b, long v, string label)
            {
                b.fill.fillAmount = b.max == 0 ? 0 : v / (float)b.max;
                b.value.text = label + " " + v + " / " + b.max;
                b.omen.text = "AUDIT " + Rules.Omen(v, b.max).ToString("00");
            }
            Set(partyBar, pBal, "STAKE"); Set(enemyBar, eBal, "STAKE");
        }

        IEnumerator AnimateBars()
        {
            float pf = partyBar.fill.fillAmount, ef = enemyBar.fill.fillAmount, t = 0;
            float pt = pBal / (float)pMax, et = eBal / (float)eMax;
            SetBars();
            float dur = Reduced ? 0.05f : 0.4f;
            while (t < dur) { t += Time.deltaTime; partyBar.fill.fillAmount = Mathf.Lerp(pf, pt, t / dur); enemyBar.fill.fillAmount = Mathf.Lerp(ef, et, t / dur); yield return null; }
            partyBar.fill.fillAmount = pt; enemyBar.fill.fillAmount = et;
        }

        void UpdateStatus()
        {
            favourText.text = streak >= 2 ? "FAVOUR: HAP'S HAND READY" : streak == 1 ? "FAVOUR: LUCK IS TURNING" : "";
            charmText.text = charm == null ? "" :
                charm == Rules.Horseshoe ? "CHARM: HORSESHOE (lucky face wider)" :
                charm == Rules.BlackCat ? "CHARM: BLACK CAT" + (catUsed ? " (spent)" : " (ready)") :
                "CHARM: OFUDA WARD" + (ofudaUsed ? " (spent)" : " (ready)");
            if (cur != null && cur.varro)
            {
                string Pips(int n) => new string('#', Mathf.Min(3, n)) + new string('-', Mathf.Max(0, 3 - n));
                jarText.text = jar.state switch
                {
                    JarState.Idle => "DEBT JAR: EMPTY",
                    JarState.Holding => $"DEBT JAR HOLDS {jar.digit}  ·  ROUNDS [{Pips(jar.affectedRounds)}]  DEFENCES [{Pips(jar.defences)}]",
                    JarState.Restoring => $"DEBT JAR OPEN  ·  {jar.digit} RETURNS NEXT ROUND",
                    _ => "DEBT JAR: SPENT"
                };
            }
        }

        void ResetSlots() { for (int i = 0; i < 3; i++) SetSlot(i, "", UI.Nixie); if (patternText) patternText.text = ""; }

        void SetSlot(int i, string s, Color c)
        {
            slotTexts[i].text = s; slotTexts[i].color = c;
            slotTexts[i].fontSize = s.Length > 2 ? 44 : 64;
            if (!string.IsNullOrEmpty(s) && !Reduced) StartCoroutine(Punch(slotBoxes[i].rectTransform));
        }
    }
}
