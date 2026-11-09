// The Remainder: Meridian Prologue (Official Unity Game Jam 2026 slice).
// Shell: boot, canvas, stage, dialogue, settings, save, title, results.
using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;
using UnityEngine;
using UnityEngine.EventSystems;
using UnityEngine.UI;

namespace Remainder
{
    public partial class Game : MonoBehaviour
    {
        public static bool Assist, Reduced, InstantText, Auto, Skilled;
        float autoTimer;
        static string shotDir; static int shotIndex;
        void Shot(string tag)
        {
            if (shotDir == null || shotIndex > 400) return;
            string safe = new string(tag.Where(char.IsLetterOrDigit).Take(24).ToArray());
            ScreenCapture.CaptureScreenshot(System.IO.Path.Combine(shotDir, $"{shotIndex++:000}_{safe}.png"));
        }

        // run state
        int resonance = -1, checkpoint;
        string charm;
        bool vesperJoined;
#pragma warning disable 0414
        bool varroSpared, seal1;   // committed story flags (mercy, Seal 1), kept for the campaign save
#pragma warning restore 0414
        float runTime;
        long biggestRound;
        readonly HashSet<Pattern> found = new HashSet<Pattern>();
        readonly HashSet<string> shownCards = new HashSet<string>();

        // presentation
        Canvas canvas;
        RectTransform root, stage, fx, hud, reel, dialog, choice, banner, top, overlay;
        Image bg, tint, fade;
        RectTransform rainLayer;
        Text speakerText, lineText, bannerText, bannerSub, hintText;
        Image dialogBox;
        CanvasGroup stageGroup;
        Button skipButton, pauseButton;
        readonly Dictionary<string, Image> actors = new Dictionary<string, Image>();
        bool tap, skipScene, paused, inStory;
        Func<double> rng = Rules.CreateRng(1597);

        [RuntimeInitializeOnLoadMethod(RuntimeInitializeLoadType.AfterSceneLoad)]
        static void Boot()
        {
            if (FindAnyObjectByType<Game>() != null) return;
            var go = new GameObject("Game");
            DontDestroyOnLoad(go);
            go.AddComponent<Game>();
        }

        void Start()
        {
            Application.targetFrameRate = 60;
            UI.Init();
            Sfx.Init(gameObject);
            LoadSettings();
            BuildScene();
            if (DebugJump()) return;
            StartCoroutine(Title());
        }

        void Update()
        {
            if (!paused && inStory) runTime += Time.unscaledDeltaTime;
            if (Auto && !paused) { autoTimer += Time.unscaledDeltaTime; if (autoTimer > 0.2f) { autoTimer = 0; tap = true; } }
            if (Input.GetKeyDown(KeyCode.Space) || Input.GetKeyDown(KeyCode.Return) || Input.GetKeyDown(KeyCode.KeypadEnter) || Input.GetKeyDown(KeyCode.Z))
                if (!paused) tap = true;
            if (Input.GetKeyDown(KeyCode.P) || Input.GetKeyDown(KeyCode.Escape)) TogglePause();
            if (Input.GetKeyDown(KeyCode.Tab) && skipButton.gameObject.activeSelf && !paused) skipScene = true;
            UpdateRain();
        }

        // ------------------------------------------------------------------ scene graph

        void BuildScene()
        {
            var cam = new GameObject("Camera").AddComponent<Camera>();
            cam.clearFlags = CameraClearFlags.SolidColor; cam.backgroundColor = Color.black; cam.orthographic = true;
            DontDestroyOnLoad(cam.gameObject);

            var cgo = new GameObject("Canvas", typeof(Canvas), typeof(CanvasScaler), typeof(GraphicRaycaster));
            DontDestroyOnLoad(cgo);
            canvas = cgo.GetComponent<Canvas>(); canvas.renderMode = RenderMode.ScreenSpaceOverlay;
            var scaler = cgo.GetComponent<CanvasScaler>();
            scaler.uiScaleMode = CanvasScaler.ScaleMode.ScaleWithScreenSize; scaler.referenceResolution = new Vector2(1280, 720); scaler.matchWidthOrHeight = 0.5f;
            var es = new GameObject("EventSystem", typeof(EventSystem), typeof(StandaloneInputModule));
            DontDestroyOnLoad(es);

            // letterboxed 16:9 root so layout is identical at every window size
            var holder = UI.Rect("Holder", cgo.transform); UI.Stretch(holder);
            root = UI.Rect("Root", holder);
            var fit = root.gameObject.AddComponent<AspectRatioFitter>(); fit.aspectMode = AspectRatioFitter.AspectMode.FitInParent; fit.aspectRatio = 16f / 9f;
            root.gameObject.AddComponent<RectMask2D>();

            bg = UI.Img(root, "Background", Color.white);
            UI.Stretch(bg.rectTransform);
            bg.preserveAspect = false;
            tint = UI.Img(root, "Tint", new Color(0, 0, 0, 0)); UI.Stretch(tint.rectTransform);
            rainLayer = UI.Stretch(UI.Rect("Rain", root));
            stage = UI.Stretch(UI.Rect("Stage", root));
            stageGroup = stage.gameObject.AddComponent<CanvasGroup>();
            fx = UI.Stretch(UI.Rect("FX", root));

            var catcher = UI.Img(root, "TapCatcher", new Color(0, 0, 0, 0)); UI.Stretch(catcher.rectTransform);
            catcher.raycastTarget = true;
            catcher.gameObject.AddComponent<Button>().onClick.AddListener(() => { if (!paused) tap = true; });

            hud = UI.Stretch(UI.Rect("HUD", root));
            reel = UI.Stretch(UI.Rect("Reel", root));
            dialog = UI.Stretch(UI.Rect("Dialog", root));
            BuildDialog();
            banner = UI.Stretch(UI.Rect("Banner", root));
            BuildBanner();
            choice = UI.Stretch(UI.Rect("Choice", root));
            top = UI.Stretch(UI.Rect("Top", root));
            pauseButton = UI.Btn(top, "II", TogglePause, new Vector2(54, 44), 26);
            UI.Place((RectTransform)pauseButton.transform, new Vector2(1, 1), new Vector2(1, 1), new Vector2(-12, -10), new Vector2(54, 44));
            skipButton = UI.Btn(top, "SKIP  »", () => skipScene = true, new Vector2(120, 44), 24);
            UI.Place((RectTransform)skipButton.transform, new Vector2(1, 1), new Vector2(1, 1), new Vector2(-74, -10), new Vector2(120, 44));
            skipButton.gameObject.SetActive(false);
            hintText = UI.Txt(top, "Hint", "", UI.Bold, 26, UI.Paper, TextAnchor.MiddleCenter);
            UI.Place(hintText.rectTransform, new Vector2(0.5f, 0), new Vector2(0.5f, 0), new Vector2(0, 92), new Vector2(900, 34));
            UI.Outlined(hintText, Color.black, 2);
            overlay = UI.Stretch(UI.Rect("Overlay", root));
            fade = UI.Img(root, "Fade", Color.black); UI.Stretch(fade.rectTransform);
            BuildRain();
        }

        void BuildDialog()
        {
            dialogBox = UI.Img(dialog, "Box", UI.Panel);
            UI.Place(dialogBox.rectTransform, new Vector2(0.5f, 0), new Vector2(0.5f, 0), new Vector2(0, 18), new Vector2(1060, 150));
            var edge = UI.Img(dialogBox.transform, "Edge", UI.Brass); UI.Place(edge.rectTransform, new Vector2(0.5f, 1), new Vector2(0.5f, 1), Vector2.zero, new Vector2(1060, 3));
            speakerText = UI.Txt(dialogBox.transform, "Speaker", "", UI.Title, 30, UI.Nixie, TextAnchor.UpperLeft);
            UI.Place(speakerText.rectTransform, new Vector2(0, 1), new Vector2(0, 1), new Vector2(28, -12), new Vector2(600, 34));
            lineText = UI.Txt(dialogBox.transform, "Line", "", UI.Body, 30, UI.Paper, TextAnchor.UpperLeft);
            UI.Place(lineText.rectTransform, new Vector2(0, 1), new Vector2(0, 1), new Vector2(28, -50), new Vector2(1000, 96));
            var more = UI.Txt(dialogBox.transform, "More", "»", UI.Body, 26, UI.Brass, TextAnchor.LowerRight);
            UI.Place(more.rectTransform, new Vector2(1, 0), new Vector2(1, 0), new Vector2(-16, 6), new Vector2(40, 30));
            dialog.gameObject.SetActive(false);
        }

        void BuildBanner()
        {
            var strip = UI.Img(banner, "Strip", new Color(0, 0, 0, 0.62f));
            UI.Place(strip.rectTransform, new Vector2(0.5f, 0.5f), new Vector2(0.5f, 0.5f), new Vector2(0, 70), new Vector2(1400, 150));
            bannerText = UI.Txt(banner, "Title", "", UI.Title, 84, UI.Gold);
            UI.Place(bannerText.rectTransform, new Vector2(0.5f, 0.5f), new Vector2(0.5f, 0.5f), new Vector2(0, 92), new Vector2(1240, 96));
            UI.Outlined(bannerText, new Color(0, 0, 0, 0.8f), 3);
            bannerSub = UI.Txt(banner, "Sub", "", UI.Bold, 28, UI.Paper);
            UI.Place(bannerSub.rectTransform, new Vector2(0.5f, 0.5f), new Vector2(0.5f, 0.5f), new Vector2(0, 26), new Vector2(1180, 40));
            banner.gameObject.SetActive(false);
        }

        // ------------------------------------------------------------------ rain

        readonly List<RectTransform> drops = new List<RectTransform>();
        bool raining;
        void BuildRain()
        {
            for (int i = 0; i < 70; i++)
            {
                var d = UI.Img(rainLayer, "Drop", new Color(0.75f, 0.85f, 1f, 0.22f));
                UI.Place(d.rectTransform, Vector2.zero, new Vector2(0.5f, 0.5f), new Vector2(UnityEngine.Random.Range(0, 1280f), UnityEngine.Random.Range(0, 720f)), new Vector2(2, UnityEngine.Random.Range(18f, 34f)));
                d.rectTransform.localRotation = Quaternion.Euler(0, 0, 12);
                drops.Add(d.rectTransform);
            }
        }
        void UpdateRain()
        {
            rainLayer.gameObject.SetActive(raining && !Reduced);
            if (!raining || Reduced || paused) return;
            foreach (var d in drops)
            {
                var p = d.anchoredPosition + new Vector2(-220f, -1100f) * Time.deltaTime;
                if (p.y < -40) p = new Vector2(UnityEngine.Random.Range(0, 1500f), 760f);
                d.anchoredPosition = p;
            }
        }

        // ------------------------------------------------------------------ helpers

        IEnumerator WaitTap()
        {
            tap = false;
            while (!tap) yield return null;
            tap = false;
        }

        IEnumerator Wait(float s)
        {
            if (skipScene) yield break;
            float t = 0;
            while (t < s && !skipScene) { t += Time.deltaTime; yield return null; }
        }

        IEnumerator Fade(float to, float dur = 0.35f)
        {
            fade.raycastTarget = to > 0.5f;
            if (Reduced || skipScene) dur = Mathf.Min(dur, 0.12f);
            float from = fade.color.a, t = 0;
            while (t < dur) { t += Time.unscaledDeltaTime; fade.color = new Color(0, 0, 0, Mathf.Lerp(from, to, t / dur)); yield return null; }
            fade.color = new Color(0, 0, 0, to);
        }

        void SetBg(string plate, Color tintColor, bool rain)
        {
            bg.sprite = UI.Load("Art/plates/" + plate);
            var tex = bg.sprite.texture;
            var fitter = bg.GetComponent<AspectRatioFitter>() ?? bg.gameObject.AddComponent<AspectRatioFitter>();
            fitter.aspectMode = AspectRatioFitter.AspectMode.EnvelopeParent; fitter.aspectRatio = tex.width / (float)tex.height;
            tint.color = tintColor;
            raining = rain;
            Sfx.Ambience(rain, true);
        }

        static readonly Dictionary<string, float> Heights = new Dictionary<string, float>
        {
            {"nil", 470}, {"vesper", 462}, {"varro", 540}, {"hound", 270}, {"ama", 432}, {"tobi", 320},
            {"nought", 470}, {"gus", 450}, {"collector", 462}, {"livia", 432}
        };

        Image Actor(string key, string art, float x, bool flip = false, bool slideIn = true)
        {
            if (actors.TryGetValue(key, out var existing)) Destroy(existing.gameObject);
            var sprite = UI.Load("Art/chars/" + art);
            string id = art.Split('_')[0];
            float h = Heights.TryGetValue(id, out var v) ? v : 450;
            float w = h * sprite.texture.width / (float)sprite.texture.height;
            var img = UI.Img(stage, key, Color.white, sprite);
            UI.Place(img.rectTransform, new Vector2(x, 0), new Vector2(0.5f, 0), new Vector2(0, 26), new Vector2(w, h));
            if (flip) img.rectTransform.localScale = new Vector3(-1, 1, 1);
            actors[key] = img;
            img.gameObject.AddComponent<Breathe>();
            if (slideIn && !Reduced && !skipScene) StartCoroutine(SlideIn(img.rectTransform, x < 0.5f ? -1 : 1));
            return img;
        }

        IEnumerator SlideIn(RectTransform rt, int side)
        {
            var end = rt.anchoredPosition; var start = end + new Vector2(side * 240, 0);
            var g = rt.GetComponent<Image>(); float t = 0;
            while (t < 0.35f && rt != null)
            {
                t += Time.deltaTime; float k = 1 - Mathf.Pow(1 - t / 0.35f, 3);
                rt.anchoredPosition = Vector2.Lerp(start, end, k); g.color = new Color(1, 1, 1, k);
                yield return null;
            }
            if (rt != null) { rt.anchoredPosition = end; g.color = Color.white; }
        }

        IEnumerator Lunge(string key, float dx)
        {
            if (Reduced || !actors.TryGetValue(key, out var a) || a == null) yield break;
            var rt = a.rectTransform; var origin = rt.anchoredPosition; float t = 0;
            while (t < 0.1f && rt != null) { t += Time.deltaTime; rt.anchoredPosition = origin + new Vector2(dx * t / 0.1f, 0); yield return null; }
            t = 0;
            while (t < 0.18f && rt != null) { t += Time.deltaTime; rt.anchoredPosition = origin + new Vector2(dx * (1 - t / 0.18f), 0); yield return null; }
            if (rt != null) rt.anchoredPosition = origin;
        }

        void ClearActors() { foreach (var a in actors.Values) if (a) Destroy(a.gameObject); actors.Clear(); }

        void Remove(string key) { if (actors.TryGetValue(key, out var a)) { if (a) Destroy(a.gameObject); actors.Remove(key); } }

        Text Label(Image actor, string s, Color c, int size = 34, float y = 18, Font font = null)
        {
            var t = UI.Txt(actor.transform, "Label", s, font ?? UI.Title, size, c);
            UI.Place(t.rectTransform, new Vector2(0.5f, 1), new Vector2(0.5f, 0), new Vector2(0, y), new Vector2(220, 44));
            if (actor.rectTransform.localScale.x < 0) t.rectTransform.localScale = new Vector3(-1, 1, 1);
            UI.Outlined(t, new Color(0, 0, 0, 0.8f));
            return t;
        }

        /// One spoken line. Tap completes the typewriter, then advances.
        IEnumerator Say(string speaker, string line)
        {
            if (skipScene) yield break;
            dialog.gameObject.SetActive(true);
            speakerText.text = speaker ?? "";
            lineText.text = "";
            tap = false;
            if (!InstantText)
            {
                for (int i = 1; i <= line.Length; i++)
                {
                    if (tap || skipScene) break;
                    lineText.text = line.Substring(0, i);
                    float t = 0; while (t < 0.022f) { t += Time.deltaTime; yield return null; }
                }
                tap = false;
            }
            lineText.text = line;
            if (shotDir != null) { tap = false; yield return null; Shot((speaker ?? "") + "_" + line); yield return null; yield return null; }
            while (!tap && !skipScene) yield return null;
            tap = false;
            dialog.gameObject.SetActive(false);
        }

        /// Large caption (rules teaching, pattern names). Optional wait for a tap.
        IEnumerator Card(string title, string sub, float hold = 1.1f, bool waitTap = false, Color? colour = null)
        {
            banner.gameObject.SetActive(true);
            float drop = wheel != null && wheel.gameObject.activeInHierarchy ? -340f : 0f;
            banner.offsetMin = new Vector2(0, drop); banner.offsetMax = new Vector2(0, drop);
            bannerText.text = title; bannerText.color = colour ?? UI.Gold; bannerSub.text = sub ?? "";
            if (!Reduced) StartCoroutine(Punch(bannerText.rectTransform));
            if (shotDir != null) { yield return null; Shot("card_" + title); yield return null; }
            if (waitTap) { hintText.text = "Tap or press Space"; yield return WaitTap(); hintText.text = ""; }
            else { float t = 0; tap = false; while (t < hold && !tap) { t += Time.deltaTime; yield return null; } tap = false; }
            banner.gameObject.SetActive(false);
        }

        IEnumerator Once(string id, string title, string sub, bool waitTap = true)
        {
            if (shownCards.Contains(id)) yield break;
            shownCards.Add(id);
            yield return Card(title, sub, 1.4f, waitTap, UI.Paper);
        }

        IEnumerator Punch(RectTransform rt)
        {
            float t = 0;
            while (t < 0.18f && rt != null) { t += Time.deltaTime; float s = 1.25f - 0.25f * (t / 0.18f); rt.localScale = new Vector3(s, s, 1); yield return null; }
            if (rt != null) rt.localScale = Vector3.one;
        }

        IEnumerator Flash(Color c, float dur = 0.25f)
        {
            if (Reduced) yield break;
            var f = UI.Img(fx, "Flash", c); UI.Stretch(f.rectTransform);
            float t = 0; while (t < dur) { t += Time.deltaTime; f.color = new Color(c.r, c.g, c.b, c.a * (1 - t / dur)); yield return null; }
            Destroy(f.gameObject);
        }

        IEnumerator Shake(RectTransform rt, float amount = 14f)
        {
            if (Reduced || rt == null) yield break;
            var origin = rt.anchoredPosition; float t = 0;
            while (t < 0.25f && rt != null) { t += Time.deltaTime; rt.anchoredPosition = origin + UnityEngine.Random.insideUnitCircle * amount * (1 - t / 0.25f); yield return null; }
            if (rt != null) rt.anchoredPosition = origin;
        }

        void FloatText(Vector2 pos, string s, Color c, int size = 54)
        {
            var t = UI.Txt(fx, "Float", s, UI.Title, size, c);
            UI.Place(t.rectTransform, new Vector2(0, 0), new Vector2(0.5f, 0.5f), pos, new Vector2(400, 70));
            UI.Outlined(t, new Color(0, 0, 0, 0.85f), 3);
            StartCoroutine(Rise(t));
        }

        IEnumerator Rise(Text t)
        {
            float d = 0; var p = t.rectTransform.anchoredPosition;
            while (d < 1.1f && t != null) { d += Time.deltaTime; t.rectTransform.anchoredPosition = p + new Vector2(0, (Reduced ? 0 : 60) * d); t.color = new Color(t.color.r, t.color.g, t.color.b, 1 - Mathf.Max(0, d - 0.6f) / 0.5f); yield return null; }
            if (t != null) Destroy(t.gameObject);
        }

        Vector2 ActorTop(string key)
        {
            if (!actors.TryGetValue(key, out var a) || a == null) return new Vector2(640, 420);
            return new Vector2(a.rectTransform.anchorMin.x * 1280, 26 + a.rectTransform.sizeDelta.y * 0.8f);
        }

        // ------------------------------------------------------------------ choice buttons

        IEnumerator Choose(string prompt, IList<string> options, Action<int> result, IList<KeyCode> keys = null)
        {
            UI.Clear(choice);
            int picked = -1;
            if (!string.IsNullOrEmpty(prompt))
            {
                var p = UI.Txt(choice, "Prompt", prompt, UI.Title, 40, UI.Paper);
                UI.Place(p.rectTransform, new Vector2(0.5f, 0.5f), new Vector2(0.5f, 0.5f), new Vector2(0, 150), new Vector2(1100, 50));
                UI.Outlined(p, Color.black);
            }
            float w = Mathf.Min(300, 1100f / options.Count - 16);
            for (int i = 0; i < options.Count; i++)
            {
                int k = i;
                var b = UI.Btn(choice, options[i], () => picked = k, new Vector2(w, 64), 30);
                UI.Place((RectTransform)b.transform, new Vector2(0.5f, 0.5f), new Vector2(0.5f, 0.5f), new Vector2((i - (options.Count - 1) / 2f) * (w + 16), 70), new Vector2(w, 64));
                if (i == 0) EventSystem.current.SetSelectedGameObject(b.gameObject);
            }
            if (Auto) picked = 0;
            while (picked < 0)
            {
                if (keys != null) for (int i = 0; i < keys.Count; i++) if (Input.GetKeyDown(keys[i])) picked = i;
                yield return null;
            }
            UI.Clear(choice);
            tap = false;
            result(picked);
        }

        // ------------------------------------------------------------------ settings, pause, save

        void LoadSettings()
        {
            try
            {
                Assist = PlayerPrefs.GetInt("assist", 0) == 1; Reduced = PlayerPrefs.GetInt("reduced", 0) == 1;
                InstantText = PlayerPrefs.GetInt("instant", 0) == 1; Sfx.Volume = PlayerPrefs.GetFloat("volume", 0.8f);
            }
            catch (Exception e) { Debug.LogWarning("Settings unavailable: " + e.Message); }
        }

        void SaveSettings()
        {
            try
            {
                PlayerPrefs.SetInt("assist", Assist ? 1 : 0); PlayerPrefs.SetInt("reduced", Reduced ? 1 : 0);
                PlayerPrefs.SetInt("instant", InstantText ? 1 : 0); PlayerPrefs.SetFloat("volume", Sfx.Volume); PlayerPrefs.Save();
            }
            catch (Exception e) { Debug.LogWarning("Settings not saved: " + e.Message); }
            Sfx.Refresh();
        }

        void SaveCheckpoint(int cp)
        {
            checkpoint = cp;
            try
            {
                PlayerPrefs.SetInt("cp", cp); PlayerPrefs.SetInt("res", resonance); PlayerPrefs.SetString("charm", charm ?? "");
                PlayerPrefs.SetInt("vesper", vesperJoined ? 1 : 0); PlayerPrefs.SetFloat("time", runTime);
                PlayerPrefs.SetString("biggest", biggestRound.ToString()); PlayerPrefs.SetInt("found", found.Aggregate(0, (m, p) => m | (1 << (int)p)));
                PlayerPrefs.Save();
            }
            catch (Exception e) { Debug.LogWarning("Checkpoint not saved: " + e.Message); }
        }

        bool HasSave() { try { return PlayerPrefs.GetInt("cp", -1) >= 1; } catch { return false; } }

        void LoadCheckpoint()
        {
            checkpoint = PlayerPrefs.GetInt("cp", 0); resonance = PlayerPrefs.GetInt("res", -1);
            var c = PlayerPrefs.GetString("charm", ""); charm = c == "" ? null : c;
            vesperJoined = PlayerPrefs.GetInt("vesper", 0) == 1; runTime = PlayerPrefs.GetFloat("time", 0);
            long.TryParse(PlayerPrefs.GetString("biggest", "0"), out biggestRound);
            int mask = PlayerPrefs.GetInt("found", 0); found.Clear();
            foreach (Pattern p in Enum.GetValues(typeof(Pattern))) if ((mask & (1 << (int)p)) != 0) found.Add(p);
        }

        void ClearSave() { try { PlayerPrefs.DeleteKey("cp"); PlayerPrefs.Save(); } catch { } }

        void TogglePause()
        {
            if (overlay.childCount > 0 && !paused) return;
            paused = !paused;
            Time.timeScale = paused ? 0 : 1;
            UI.Clear(overlay);
            if (paused) ShowPanel("PAUSED", PauseBody);
        }

        void PauseBody(RectTransform body)
        {
            float y = 120;
            void Row(string label, Action a) { var b = UI.Btn(body, label, a, new Vector2(360, 56), 30); UI.Place((RectTransform)b.transform, new Vector2(0.5f, 1), new Vector2(0.5f, 1), new Vector2(0, -y), new Vector2(360, 56)); y += 70; }
            Row("RESUME", TogglePause);
            Row("SETTINGS", () => { UI.Clear(overlay); ShowPanel("SETTINGS", SettingsBody, () => { UI.Clear(overlay); ShowPanel("PAUSED", PauseBody); }); });
            Row("RULES", () => { UI.Clear(overlay); ShowPanel("HOW TO PLAY", RulesBody, () => { UI.Clear(overlay); ShowPanel("PAUSED", PauseBody); }); });
            Row("QUIT TO TITLE", () => { paused = false; Time.timeScale = 1; UI.Clear(overlay); StopAllCoroutines(); StartCoroutine(Title()); });
        }

        void ShowPanel(string title, Action<RectTransform> fill, Action back = null)
        {
            var dim = UI.Img(overlay, "Dim", new Color(0, 0, 0, 0.78f)); UI.Stretch(dim.rectTransform); dim.raycastTarget = true;
            var box = UI.Img(overlay, "Panel", new Color(0.08f, 0.09f, 0.13f, 0.98f));
            UI.Place(box.rectTransform, new Vector2(0.5f, 0.5f), new Vector2(0.5f, 0.5f), Vector2.zero, new Vector2(860, 620));
            var t = UI.Txt(box.transform, "Title", title, UI.Title, 56, UI.Nixie);
            UI.Place(t.rectTransform, new Vector2(0.5f, 1), new Vector2(0.5f, 1), new Vector2(0, -16), new Vector2(800, 64));
            fill(box.rectTransform);
            var close = UI.Btn(box.transform, back == null ? "CLOSE" : "BACK", back ?? (() => { if (paused) TogglePause(); else UI.Clear(overlay); }), new Vector2(220, 52), 28);
            UI.Place((RectTransform)close.transform, new Vector2(0.5f, 0), new Vector2(0.5f, 0), new Vector2(0, 20), new Vector2(220, 52));
        }

        void SettingsBody(RectTransform body)
        {
            float y = 110;
            void Toggle(string name, Func<bool> get, Action<bool> set)
            {
                Button b = null;
                b = UI.Btn(body, "", () => { set(!get()); SaveSettings(); UI.SetLabel(b, name + ":  " + (get() ? "ON" : "OFF")); }, new Vector2(560, 56), 28);
                UI.SetLabel(b, name + ":  " + (get() ? "ON" : "OFF"));
                UI.Place((RectTransform)b.transform, new Vector2(0.5f, 1), new Vector2(0.5f, 1), new Vector2(0, -y), new Vector2(560, 56)); y += 68;
            }
            Toggle("ASSIST (SLOWER WHEELS)", () => Assist, v => Assist = v);
            Toggle("REDUCED MOTION", () => Reduced, v => Reduced = v);
            Toggle("INSTANT TEXT", () => InstantText, v => InstantText = v);
            Button vol = null;
            vol = UI.Btn(body, "", () => { Sfx.Volume = Sfx.Volume >= 0.99f ? 0f : Mathf.Round((Sfx.Volume + 0.2f) * 10) / 10; SaveSettings(); UI.SetLabel(vol, "VOLUME:  " + Mathf.RoundToInt(Sfx.Volume * 100) + "%"); }, new Vector2(560, 56), 28);
            UI.SetLabel(vol, "VOLUME:  " + Mathf.RoundToInt(Sfx.Volume * 100) + "%");
            UI.Place((RectTransform)vol.transform, new Vector2(0.5f, 1), new Vector2(0.5f, 1), new Vector2(0, -y), new Vector2(560, 56)); y += 68;
            var fs = UI.Btn(body, "TOGGLE FULLSCREEN", () => Screen.fullScreen = !Screen.fullScreen, new Vector2(560, 56), 28);
            UI.Place((RectTransform)fs.transform, new Vector2(0.5f, 1), new Vector2(0.5f, 1), new Vector2(0, -y), new Vector2(560, 56));
            var note = UI.Txt(body, "Note", "Every cue is shown on screen; sound is never required. Keys: Space/Enter/Z to stop and advance · 1/2 choose striker · P pause · Tab skip scene.", UI.Body, 20, UI.Dim);
            UI.Place(note.rectTransform, new Vector2(0.5f, 0), new Vector2(0.5f, 0), new Vector2(0, 86), new Vector2(760, 60));
        }

        void RulesBody(RectTransform body)
        {
            var t = UI.Txt(body, "Rules",
                "Each round you stop three numbers. The three digits score a pattern:\n" +
                "<color=#ffd75a>OVERWRITE</color>  three of your chosen number  ×21\n" +
                "<color=#ffd75a>JACKPOT</color>  three alike  ×digit (min 2)       <color=#ffd75a>REAPER</color>  three 4s  ×4\n" +
                "<color=#ffd75a>CASCADE</color>  run up or down (3-4-5)  ×3 and go again\n" +
                "<color=#ffd75a>ZERO-SUM</color>  digits add to 10 or 20  ×2, cancels their next action\n" +
                "<color=#ffd75a>PAIR</color>  two alike  ×2        <color=#ffd75a>BUST</color>  nothing  ×1, your strikes still count\n\n" +
                "Defend by stopping 0 to Parry. Stopping your own number reflects the blow.\n" +
                "After a Bust, luck turns: wheels slow and repeated faces widen. After two Busts, Hap's hand repairs the next one.\n" +
                "Shimmering faces on the last wheel finish a pattern.", UI.Body, 24, UI.Paper, TextAnchor.UpperLeft);
            UI.Place(t.rectTransform, new Vector2(0.5f, 1), new Vector2(0.5f, 1), new Vector2(0, -96), new Vector2(780, 420));
        }

        void CreditsBody(RectTransform body)
        {
            var t = UI.Txt(body, "Credits",
                "<b>THE REMAINDER</b>, a ZERO-SUM: OMEN prologue.\nMade for the Official Unity Game Jam 2026, theme <i>Lucky Number</i>. Built in Unity 6.\n\n" +
                "<b>AI disclosure.</b> Character art and the street: concept boards generated with Higgsfield image models from the team's written designs, cut out by script. Shrine, bazaar, drain and rooftop backgrounds and charm icons: generated with Meshy. " +
                "Game code, rules port and procedural audio written with an AI coding assistant (Claude) under the creator's direction; the scoring rules match the team's reference implementation. " +
                "Story, world and characters: original to ZERO-SUM: OMEN.\n\n" +
                "Fonts: Bebas Neue and Barlow Semi Condensed (SIL Open Font License).\nAll sound is synthesised in code.", UI.Body, 23, UI.Paper, TextAnchor.UpperLeft);
            UI.Place(t.rectTransform, new Vector2(0.5f, 1), new Vector2(0.5f, 1), new Vector2(0, -96), new Vector2(780, 440));
        }

        bool DebugJump()
        {
            var args = new Dictionary<string, string>();
            string url = Application.absoluteURL ?? "";
            int q = url.IndexOf('?');
            if (q >= 0) foreach (var kv in url.Substring(q + 1).Split('&')) { var p = kv.Split('='); if (p.Length == 2) args[p[0]] = p[1]; }
            var cli = Environment.GetCommandLineArgs();   // standalone: -jam cp=0 auto=1 res=7 charm=...
            for (int i = 0; i < cli.Length; i++) if (cli[i] == "-jam") for (int k = i + 1; k < cli.Length && cli[k].Contains("="); k++) { var p = cli[k].Split('='); args[p[0]] = p[1]; }
            if (!args.ContainsKey("cp")) return false;
            NewRun(false);
            Auto = args.TryGetValue("auto", out var a) && a == "1";
            Skilled = args.TryGetValue("skill", out var sk) && sk == "1";
            if (args.TryGetValue("shots", out var sd)) { shotDir = sd; System.IO.Directory.CreateDirectory(sd); }
            if (Auto) { Time.timeScale = args.TryGetValue("speed", out var sp) ? float.Parse(sp) : 3f; InstantText = true; Reduced = true; }
            int cp = int.Parse(args["cp"]);
            resonance = args.TryGetValue("res", out var r) ? int.Parse(r) : 7;
            charm = args.TryGetValue("charm", out var c) ? c : (cp > 4 ? Rules.Horseshoe : null);
            vesperJoined = cp >= 4;
            fade.color = Color.black;
            StartCoroutine(Run(cp));
            return true;
        }

        // ------------------------------------------------------------------ title and run

        IEnumerator Title()
        {
            inStory = false; skipScene = false;
            Time.timeScale = 1; paused = false;
            UI.Clear(hud); UI.Clear(reel); UI.Clear(choice); UI.Clear(fx); UI.Clear(overlay);
            dialog.gameObject.SetActive(false); banner.gameObject.SetActive(false);
            skipButton.gameObject.SetActive(false);
            ClearActors();
            SetBg("meridian_street", new Color(0.02f, 0.03f, 0.08f, 0.55f), true);
            Sfx.Music("m_street");
            var hero = Actor("title_nil", "nil_front", 0.13f, false, false);
            hero.color = new Color(0.85f, 0.85f, 0.95f, 1f);
            var logo = UI.Rect("Logo", choice);
            UI.Place(logo, new Vector2(0.5f, 0.5f), new Vector2(0.5f, 0.5f), new Vector2(0, 120), new Vector2(1000, 300));
            var nan = UI.Txt(logo, "NaN", "NaN", UI.Bold, 50, UI.Nixie); UI.Place(nan.rectTransform, new Vector2(0.5f, 1), new Vector2(0.5f, 1), new Vector2(0, 0), new Vector2(300, 60));
            var title = UI.Txt(logo, "Title", "THE REMAINDER", UI.Title, 140, UI.Paper); UI.Place(title.rectTransform, new Vector2(0.5f, 0.5f), new Vector2(0.5f, 0.5f), new Vector2(0, 10), new Vector2(1000, 150));
            UI.Outlined(title, new Color(0, 0, 0, 0.8f), 4);
            var sub = UI.Txt(logo, "Sub", "ZERO-SUM: OMEN  ·  A MERIDIAN PROLOGUE", UI.Bold, 26, UI.Brass); UI.Place(sub.rectTransform, new Vector2(0.5f, 0), new Vector2(0.5f, 0), new Vector2(0, 0), new Vector2(1000, 40));
            yield return Fade(0, 0.6f);
            int pick = -1;
            var opts = new List<string> { "START" };
            bool canContinue = HasSave();
            if (canContinue) opts.Add("CONTINUE");
            opts.Add("SETTINGS"); opts.Add("CREDITS");
            float bx = -(opts.Count - 1) * 120;
            for (int i = 0; i < opts.Count; i++)
            {
                int k = i;
                var b = UI.Btn(choice, opts[i], () => pick = k, new Vector2(220, 60), 32);
                UI.Place((RectTransform)b.transform, new Vector2(0.5f, 0.5f), new Vector2(0.5f, 0.5f), new Vector2(bx + i * 240, -120), new Vector2(220, 60));
                if (i == 0) EventSystem.current.SetSelectedGameObject(b.gameObject);
            }
            while (true)
            {
                pick = -1;
                while (pick < 0) { if (Input.GetKeyDown(KeyCode.Space) || Input.GetKeyDown(KeyCode.Return)) { if (overlay.childCount == 0) pick = 0; } yield return null; }
                string o = opts[pick];
                if (o == "SETTINGS") { ShowPanel("SETTINGS", SettingsBody); while (overlay.childCount > 0) yield return null; continue; }
                if (o == "CREDITS") { ShowPanel("CREDITS", CreditsBody); while (overlay.childCount > 0) yield return null; continue; }
                UI.Clear(choice);
                tap = false;
                if (o == "CONTINUE") { LoadCheckpoint(); yield return Run(checkpoint); }
                else { NewRun(keepResonance: false); yield return Run(0); }
                yield break;
            }
        }

        void NewRun(bool keepResonance)
        {
            if (!keepResonance) resonance = -1;
            charm = null; vesperJoined = false; varroSpared = false; seal1 = false; runTime = 0; biggestRound = 0; found.Clear(); shownCards.Clear();
            rng = Rules.CreateRng(1597);
        }

        IEnumerator Run(int from)
        {
            inStory = true;
            Func<IEnumerator>[] chapters = { Alley, Shrine, SoloAudit, VesperJoins, CharmChoice, VarroFight, Ending };
            for (int cp = from; cp < chapters.Length; cp++)
            {
                SaveCheckpoint(cp);
                Debug.Log($"JAM: chapter {cp} start (resonance {resonance}, charm {charm ?? "none"}, t={runTime:0.0}s)");
                skipScene = false;
                yield return chapters[cp]();
                skipScene = false;
            }
            inStory = false;
            Debug.Log($"JAM: RUN COMPLETE biggest={biggestRound} patterns={found.Count} [{string.Join(",", found)}] time={runTime:0.0}s");
            if (Auto && !Application.isEditor && Application.platform != RuntimePlatform.WebGLPlayer) { Application.Quit(0); yield break; }
            ClearSave();
            yield return Results();
        }

        IEnumerator Results()
        {
            skipButton.gameObject.SetActive(false);
            UI.Clear(hud); UI.Clear(reel); ClearActors();
            SetBg("rooftop", new Color(0.02f, 0.03f, 0.08f, 0.6f), false);
            yield return Fade(0);
            var t = UI.Txt(choice, "Results", "", UI.Title, 44, UI.Paper);
            UI.Place(t.rectTransform, new Vector2(0.5f, 0.5f), new Vector2(0.5f, 0.5f), new Vector2(0, 140), new Vector2(1100, 300));
            var ts = TimeSpan.FromSeconds(runTime);
            string patterns = found.Count == 0 ? "none" : string.Join(" · ", found.OrderBy(p => (int)p).Select(Rules.Label));
            t.text = $"<color=#ff9438>RESULTS</color>\nBIGGEST ROUND  {biggestRound}\nPATTERNS FOUND  {found.Count}/7\n<size=28>{patterns}</size>\nTIME  {(int)ts.TotalMinutes}:{ts.Seconds:00}   ·   LUCKY NUMBER  {resonance}";
            int pick = -1;
            string[] opts = { "RETRY THIS NUMBER", "NEW NUMBER", "CREDITS", "TITLE" };
            for (int i = 0; i < opts.Length; i++)
            {
                int k = i;
                var b = UI.Btn(choice, opts[i], () => pick = k, new Vector2(270, 60), 28);
                UI.Place((RectTransform)b.transform, new Vector2(0.5f, 0.5f), new Vector2(0.5f, 0.5f), new Vector2(-435 + i * 290, -150), new Vector2(270, 60));
            }
            while (true)
            {
                pick = -1;
                while (pick < 0) yield return null;
                if (pick == 2) { ShowPanel("CREDITS", CreditsBody); while (overlay.childCount > 0) yield return null; continue; }
                UI.Clear(choice);
                if (pick == 0) { NewRun(keepResonance: true); yield return Run(0); }
                else if (pick == 1) { NewRun(keepResonance: false); yield return Run(0); }
                else yield return Title();
                yield break;
            }
        }
    }
}
