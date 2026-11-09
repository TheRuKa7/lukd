// Story chapters for the Meridian Prologue. Line text follows docs/JAM_SCRIPT.md (IDs in comments).
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

namespace Remainder
{
    public partial class Game
    {
        static readonly Color NightTint = new Color(0.03f, 0.05f, 0.12f, 0.35f);
        static readonly Color ShrineTint = new Color(0.25f, 0.13f, 0.02f, 0.62f);
        static readonly Color BazaarTint = new Color(0.20f, 0.10f, 0.02f, 0.30f);
        static readonly Color DrainTint = new Color(0.02f, 0.10f, 0.08f, 0.55f);

        void BeginScene(string plate, Color tintColour, bool rain)
        {
            UI.Clear(hud); UI.Clear(reel); UI.Clear(fx); UI.Clear(choice);
            ClearActors();
            SetBg(plate, tintColour, rain);
            skipButton.gameObject.SetActive(true);
        }

        Image Nil(float x = 0.26f, bool slide = true)
        {
            var nil = Actor("nil", "nil_side", x, false, slide);
            var halo = Label(nil, "NaN", UI.Nixie, 32, 4, UI.Bold);
            halo.gameObject.AddComponent<Flicker>();
            return nil;
        }

        // 1. Rain Alley and the rescue -------------------------------------------------
        IEnumerator Alley()
        {
            BeginScene("meridian_street", NightTint, true);
            yield return Fade(0, 0.6f);
            yield return Card("MERIDIAN", "EVERY SOUL WEARS A NUMBER.", 1.6f);            // jam_alley_010
            var ama = Actor("ama", "ama_front", 0.62f);
            var amaNum = Label(ama, "CIVIC 03", UI.Paper, 32);
            Actor("tobi", "tobi_front", 0.52f);
            yield return Wait(0.5f);
            amaNum.text = "CIVIC 02"; yield return Wait(0.45f);
            amaNum.text = "CIVIC 01"; amaNum.color = UI.Red;
            yield return Say("TOBI", "Mum?");                                              // jam_alley_020
            Actor("collector", "collector_front", 0.84f);
            var jar = JarOrbs(new Vector2(930, 300), 6);
            yield return Say("COLLECTOR", "Ama Okoro. Your account's closed.");            // jam_alley_030
            Nil(0.33f);
            yield return Say("COLLECTOR", "Move.");                                         // jam_alley_040

            // jam_rescue_010/020: authored 07 stop, six units return to Ama
            skipScene = false;
            var w = Wheel.Create(reel, new Vector2(0, -20));
            wheel = w;
            stageGroup.alpha = 0.45f;
            w.Build(new[] { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 }, d => 1f, -1);
            w.speed = 470f * 0.6f * (Assist ? 0.7f : 1f);
            w.SetCaption("AMA'S NUMBER", UI.Paper);
            w.Spin();
            hintText.text = "STOP THE NUMBER  ·  Tap or press Space";
            w.SetCaption("STOP THE NUMBER", UI.Paper);
            yield return WaitTap();
            hintText.text = "";
            yield return w.StopOn(7, Reduced);
            stageGroup.alpha = 1f;
            yield return Wait(0.3f);
            // the jar empties into Ama's account, one unit at a time
            for (int i = 0; i < jar.Count; i++)
            {
                var orb = jar[i];
                StartCoroutine(Fly(orb.rectTransform, ActorTop("ama") + new Vector2(0, 40), 0.45f));
                Sfx.Play("coin", 1f + i * 0.06f);
                amaNum.text = "CIVIC " + (2 + i).ToString("00"); amaNum.color = i == 5 ? UI.Gold : UI.Paper;
                yield return new WaitForSeconds(Reduced ? 0.05f : 0.22f);
            }
            Destroy(w.gameObject); wheel = null;
            yield return Card("01  »  07", "Six confiscated units returned. Nothing was created.", 1.8f);
            skipScene = false;
            yield return Say("COLLECTOR", "That one has no number.");                       // jam_rescue_030
            yield return Say("NIL", "Go. Both of you.");                                    // jam_rescue_040
            Remove("ama"); Remove("tobi");
            yield return Fade(1);
        }

        List<Image> JarOrbs(Vector2 at, int n)
        {
            var list = new List<Image>();
            var glass = UI.Img(fx, "Jar", new Color(0.7f, 0.85f, 1f, 0.25f));
            UI.Place(glass.rectTransform, Vector2.zero, new Vector2(0.5f, 0.5f), at, new Vector2(90, 110));
            for (int i = 0; i < n; i++)
            {
                var o = UI.Img(fx, "Unit", UI.Nixie, UI.Round);
                UI.Place(o.rectTransform, Vector2.zero, new Vector2(0.5f, 0.5f), at + new Vector2((i % 3 - 1) * 24, (i / 3 - 0.5f) * 30), new Vector2(20, 20));
                list.Add(o);
            }
            return list;
        }

        IEnumerator Fly(RectTransform rt, Vector2 to, float dur)
        {
            var from = rt.anchoredPosition; float t = 0;
            if (Reduced) dur *= 0.3f;
            while (t < dur && rt != null) { t += Time.deltaTime; float k = Mathf.SmoothStep(0, 1, t / dur); rt.anchoredPosition = Vector2.Lerp(from, to, k) + new Vector2(0, Mathf.Sin(k * Mathf.PI) * 80); yield return null; }
            if (rt != null) Destroy(rt.gameObject);
        }

        // 2. Shrine and the Naming ----------------------------------------------------
        IEnumerator Shrine()
        {
            BeginScene("meridian_street", ShrineTint, false);
            Nil(0.3f);
            Actor("nought", "nought_front", 0.7f);
            yield return Fade(0);
            yield return Say("BROTHER NOUGHT", "In here. Quick.");                         // jam_shrine_010
            yield return Say("BROTHER NOUGHT", "Every soul needs a number, child.");        // jam_shrine_020
            yield return Say("NIL", "I don't have one.");                                   // jam_shrine_030
            yield return Say("BROTHER NOUGHT", "Then pick. The machine is listening.");     // jam_shrine_040
            skipScene = false;
            yield return NamingChoice();
            yield return Flash(new Color(1f, 0.6f, 0.2f, 0.8f), 0.5f);
            Sfx.Play("alarm");
            yield return Card("REMAINDER DETECTED", "The terminal cannot find your account.", 1.6f, false, UI.Red);   // jam_naming_020
            yield return Say("BROTHER NOUGHT", "Hap's watching. Run.");                    // jam_naming_030
            yield return Fade(1);
        }

        IEnumerator NamingChoice()
        {
            UI.Clear(choice);
            int selected = resonance >= 0 ? resonance : -1;
            bool confirmed = false;
            var prompt = UI.Txt(choice, "Prompt", "STATE YOUR LUCKY NUMBER", UI.Title, 52, UI.Paper);   // jam_naming_010
            UI.Place(prompt.rectTransform, new Vector2(0.5f, 0.5f), new Vector2(0.5f, 0.5f), new Vector2(0, 230), new Vector2(1100, 60));
            UI.Outlined(prompt, Color.black, 3);
            var help = UI.Txt(choice, "Help", "A personal resonance, not your health. Any digit is valid, including 0.", UI.Body, 26, UI.Paper);
            UI.Place(help.rectTransform, new Vector2(0.5f, 0.5f), new Vector2(0.5f, 0.5f), new Vector2(0, 185), new Vector2(1100, 34));
            UI.Outlined(help, Color.black);
            var buttons = new List<Button>();
            for (int d = 0; d <= 9; d++)
            {
                int k = d;
                var b = UI.Btn(choice, d.ToString(), () => { selected = k; }, new Vector2(84, 96), 70);
                UI.Place((RectTransform)b.transform, new Vector2(0.5f, 0.5f), new Vector2(0.5f, 0.5f), new Vector2((d - 4.5f) * 96, 90), new Vector2(84, 96));
                buttons.Add(b);
            }
            var confirm = UI.Btn(choice, "CONFIRM", () => { if (selected >= 0) confirmed = true; }, new Vector2(260, 60), 32);
            UI.Place((RectTransform)confirm.transform, new Vector2(0.5f, 0.5f), new Vector2(0.5f, 0.5f), new Vector2(0, -10), new Vector2(260, 60));
            UnityEngine.EventSystems.EventSystem.current.SetSelectedGameObject(buttons[selected >= 0 ? selected : 7].gameObject);
            if (Auto) { selected = resonance >= 0 ? resonance : 7; confirmed = true; }
            while (!confirmed)
            {
                for (int d = 0; d <= 9; d++) if (Input.GetKeyDown(KeyCode.Alpha0 + d) || Input.GetKeyDown(KeyCode.Keypad0 + d)) selected = d;
                if (selected >= 0 && (Input.GetKeyDown(KeyCode.Return) || Input.GetKeyDown(KeyCode.KeypadEnter))) confirmed = true;
                for (int d = 0; d <= 9; d++) buttons[d].GetComponent<Image>().color = d == selected ? new Color(0.55f, 0.32f, 0.08f, 1f) : new Color(0.14f, 0.15f, 0.2f, 0.95f);
                UI.SetLabel(confirm, selected >= 0 ? "CONFIRM  " + selected : "CHOOSE A DIGIT");
                yield return null;
            }
            resonance = selected;
            UI.Clear(choice);
            tap = false;
        }

        // 3. Solo Audit ---------------------------------------------------------------
        IEnumerator SoloAudit()
        {
            BeginScene("meridian_street", NightTint, true);
            Nil(0.26f);
            yield return Fade(0);
            yield return Card("DEBT HOUND", "A collection construct has your trail.", 1.2f, false, UI.Red);
            skipScene = false; skipButton.gameObject.SetActive(false);
            yield return Fight(new FightDef { name = "DEBT HOUND", art = "hound_side", max = 300, attack = 20, solo = true, tutorial = true, level = 1 });
        }

        // 4. Vesper ---------------------------------------------------------------------
        IEnumerator VesperJoins()
        {
            BeginScene("meridian_street", NightTint, true);
            Nil(0.3f);
            yield return Fade(0);
            Actor("enemy", "hound_side", 0.81f);
            Sfx.Play("hit");
            yield return Card("ANOTHER HOUND", "", 0.9f, false, UI.Red);
            Sfx.Play("shot");
            yield return Flash(new Color(1, 0.95f, 0.8f, 0.9f), 0.2f);
            Actor("vesper", "vesper_side", 0.12f);
            yield return Say("VESPER", "Need a hand? Seven fen.");                          // jam_vesper_010
            yield return Say("NIL", "I don't have seven fen.");                             // jam_vesper_020
            yield return Say("VESPER", "Then owe me a good story, kid.");                   // jam_vesper_030
            vesperJoined = true;                                                            // recruit commits before combat
            skipScene = false; skipButton.gameObject.SetActive(false);
            yield return Fight(new FightDef { name = "DEBT HOUND", art = "hound_side", max = 300, attack = 20, solo = false, level = 1 });
        }

        // 5. One charm ----------------------------------------------------------------
        IEnumerator CharmChoice()
        {
            BeginScene("meridian_street", BazaarTint, false);
            Actor("nil", "nil_front", 0.2f);
            Actor("vesper", "vesper_front", 0.09f);
            Actor("gus", "gus_front", 0.84f);
            yield return Fade(0);
            yield return Say("GUS", "One for the road. Pick what you trust.");            // jam_charm_010
            yield return Say("VESPER", "Generous today?");                                  // jam_charm_020
            yield return Say("GUS", "Alive customers come back.");                          // jam_charm_030
            skipScene = false;
            if (charm == null)
            {
                string[] ids = { Rules.Horseshoe, Rules.BlackCat, Rules.Ofuda };
                string[] names = { "HORSESHOE", "BLACK CAT", "OFUDA WARD" };
                string[] text =
                {
                    "Your resonance face is 50% wider where it appears.",              // jam_charm_horseshoe
                    "First Bust each fight: the third digit copies the first.",      // jam_charm_cat
                    "Automatically parry the first enemy action each fight."           // jam_charm_ofuda
                };
                string[] glyph = { "Ω", "=^.^=", "§" };
                int pick = -1, focus = 0;
                var cards = new List<Image>();
                for (int i = 0; i < 3; i++)
                {
                    int k = i;
                    var card = UI.Img(choice, "Charm", new Color(0.1f, 0.1f, 0.14f, 0.95f));
                    card.raycastTarget = true;
                    UI.Place(card.rectTransform, new Vector2(0.5f, 0.5f), new Vector2(0.5f, 0.5f), new Vector2((i - 1) * 300, 60), new Vector2(270, 330));
                    var g = UI.Txt(card.transform, "Glyph", glyph[i], UI.Bold, 84, UI.Brass); UI.Place(g.rectTransform, new Vector2(0.5f, 1), new Vector2(0.5f, 1), new Vector2(0, -20), new Vector2(250, 110));
                    var n = UI.Txt(card.transform, "Name", names[i], UI.Title, 40, UI.Nixie); UI.Place(n.rectTransform, new Vector2(0.5f, 1), new Vector2(0.5f, 1), new Vector2(0, -140), new Vector2(250, 44));
                    var d = UI.Txt(card.transform, "Text", text[i], UI.Body, 23, UI.Paper); UI.Place(d.rectTransform, new Vector2(0.5f, 1), new Vector2(0.5f, 1), new Vector2(0, -190), new Vector2(236, 110));
                    var b = card.gameObject.AddComponent<Button>(); b.onClick.AddListener(() => { Sfx.Play("click"); pick = k; });
                    cards.Add(card);
                }
                var hint = UI.Txt(choice, "Hint", "Choose with the mouse, or the arrow keys and Enter", UI.Body, 22, UI.Paper);
                UI.Place(hint.rectTransform, new Vector2(0.5f, 0.5f), new Vector2(0.5f, 0.5f), new Vector2(0, -130), new Vector2(800, 30));
                if (Auto) pick = Mathf.Abs(resonance) % 3;
                while (pick < 0)
                {
                    if (Input.GetKeyDown(KeyCode.LeftArrow)) focus = (focus + 2) % 3;
                    if (Input.GetKeyDown(KeyCode.RightArrow)) focus = (focus + 1) % 3;
                    for (int k = 0; k < 3; k++) if (Input.GetKeyDown(KeyCode.Alpha1 + k)) focus = k;
                    if (Input.GetKeyDown(KeyCode.Return) || Input.GetKeyDown(KeyCode.Space)) pick = focus;
                    for (int k = 0; k < 3; k++) cards[k].color = k == focus ? new Color(0.24f, 0.17f, 0.08f, 0.98f) : new Color(0.1f, 0.1f, 0.14f, 0.95f);
                    yield return null;
                }
                charm = ids[pick];                                                          // awarded once; checkpoint stores it
                UI.Clear(choice);
                tap = false;
                Sfx.Play("coin");
                yield return Card(names[pick], "Charm equipped.", 1.4f);                   // jam_charm_confirm
            }
            yield return Fade(1);
        }

        // 6. Varro --------------------------------------------------------------------
        IEnumerator VarroFight()
        {
            BeginScene("meridian_street", DrainTint, true);
            Nil(0.3f);
            Actor("vesper", "vesper_side", 0.12f);
            var varro = Actor("enemy", "varro_side", 0.78f);
            yield return Fade(0);
            yield return Say("VARRO", "NaN. Worth more than my whole street.");             // jam_varro_010
            yield return Say("VESPER", "They promised your sister an exemption?");          // jam_varro_020
            yield return Say("VARRO", "Don't talk about her.");                             // jam_varro_030
            yield return Card("VARRO KADE", "THE LEDGERHOUND  ·  CIVIC 61", 1.8f, false, UI.Nixie);   // jam_varro_card
            skipScene = false; skipButton.gameObject.SetActive(false);
            yield return Fight(new FightDef { name = "VARRO KADE", art = "varro_side", max = 1200, attack = 40, varro = true, level = 2, civic = 61 });
        }

        // 7. Mercy, rooftop -----------------------------------------------------------
        IEnumerator Ending()
        {
            BeginScene("meridian_street", DrainTint, true);
            Nil(0.3f);
            Actor("vesper", "vesper_side", 0.14f);
            var v = Actor("varro", "varro_front", 0.76f);
            v.color = new Color(0.8f, 0.8f, 0.85f, 1);
            v.rectTransform.sizeDelta *= 0.92f;
            yield return Fade(0);
            yield return Say("VARRO", "Go on. Settle the rest.");                          // jam_mercy_010
            yield return Say("NIL", "No.");                                                 // jam_mercy_020
            yield return Say("VARRO", "…You'll regret that.");                              // jam_mercy_030
            yield return Say("VESPER", "Livia. She still waiting?");                        // jam_mercy_035
            yield return Say("VARRO", "Every morning.");                                    // jam_mercy_037
            varroSpared = true; seal1 = true;
            Remove("varro");
            Sfx.Play("jackpot");
            yield return Card("SEAL 1 RELEASED", "Varro limps away alive.", 1.8f);         // jam_mercy_040
            yield return Fade(1);

            BeginScene("meridian_aerial", new Color(0.05f, 0.03f, 0.10f, 0.25f), false);
            Actor("nil", "nil_side", 0.2f);
            Actor("vesper", "vesper_side", 0.08f);
            var map = SealMap();
            yield return Fade(0);
            yield return Say("VESPER", "Six Auditors. Six Seal Digits. Then the Upper Gate.");   // jam_roof_010
            yield return Say("NIL", "Seven locks.");                                        // jam_roof_020
            yield return Say("VESPER", "The last one's yours. You told the whole city.");   // jam_roof_030
            yield return Say("NIL", "They got away?");                                      // jam_roof_040
            yield return Say("VESPER", "Both of them. Come on.");                           // jam_roof_050
            skipScene = false; skipButton.gameObject.SetActive(false);
            Destroy(map.gameObject);
            yield return Card("THE REMAINDER", "A beginning in the Tally.", 2.4f, false, UI.Paper);   // jam_end_010
            yield return Fade(1);
        }

        RectTransform SealMap()
        {
            var map = UI.Rect("SealMap", fx);
            UI.Place(map, new Vector2(0.62f, 0.62f), new Vector2(0.5f, 0.5f), Vector2.zero, new Vector2(620, 140));
            var bgp = UI.Img(map, "Back", new Color(0, 0, 0, 0.55f)); UI.Stretch(bgp.rectTransform);
            var cap = UI.Txt(map, "Cap", "THE UPPER GATE", UI.Title, 28, UI.Brass); UI.Place(cap.rectTransform, new Vector2(0.5f, 1), new Vector2(0.5f, 1), new Vector2(0, -4), new Vector2(600, 32));
            for (int i = 0; i < 7; i++)
            {
                var sock = UI.Img(map, "Socket", i == 0 ? UI.Gold : i == 6 ? UI.Nixie : new Color(0.3f, 0.3f, 0.35f, 1), UI.Round);
                UI.Place(sock.rectTransform, new Vector2(0.5f, 0.5f), new Vector2(0.5f, 0.5f), new Vector2((i - 3) * 82, -14), new Vector2(64, 64));
                var lab = UI.Txt(sock.transform, "D", i == 0 ? "1" : i == 6 ? resonance.ToString() : "?", UI.Title, 40, UI.Ink);
                UI.Stretch(lab.rectTransform);
            }
            return map;
        }
    }

    /// The NaN halo never settles.
    public class Flicker : MonoBehaviour
    {
        Text t; float next;
        static readonly string[] Glitch = { "NaN", "NaN", "NaN", "N_N", "NaN", "N/A", "NaN", "?aN" };
        void Awake() { t = GetComponent<Text>(); }
        void Update()
        {
            if (Game.Reduced) { t.text = "NaN"; return; }
            if (Time.time < next) return;
            next = Time.time + Random.Range(0.08f, 0.5f);
            t.text = Glitch[Random.Range(0, Glitch.Length)];
        }
    }
}
