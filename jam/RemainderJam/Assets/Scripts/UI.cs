// Runtime UI construction helpers. The whole game is built from code so the jam
// project needs no hand-edited scenes or prefabs.
using System;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

namespace Remainder
{
    public static class UI
    {
        public static Font Body, Bold, Title;
        public static Sprite White, Round;
        static readonly Dictionary<string, Sprite> cache = new Dictionary<string, Sprite>();

        public static readonly Color Ink = new Color(0.06f, 0.07f, 0.10f, 1f);
        public static readonly Color Panel = new Color(0.07f, 0.08f, 0.12f, 0.88f);
        public static readonly Color Paper = new Color(0.96f, 0.92f, 0.86f, 1f);
        public static readonly Color Nixie = new Color(1f, 0.58f, 0.22f, 1f);
        public static readonly Color Brass = new Color(0.86f, 0.68f, 0.36f, 1f);
        public static readonly Color Gold = new Color(1f, 0.84f, 0.35f, 1f);
        public static readonly Color Teal = new Color(0.35f, 0.85f, 0.85f, 1f);
        public static readonly Color Red = new Color(0.92f, 0.32f, 0.28f, 1f);
        public static readonly Color Dim = new Color(1f, 1f, 1f, 0.55f);

        public static void Init()
        {
            Body = Resources.Load<Font>("Fonts/BarlowSemiCondensed-Regular");
            Bold = Resources.Load<Font>("Fonts/BarlowSemiCondensed-Bold");
            Title = Resources.Load<Font>("Fonts/BebasNeue-Regular");
            White = Sprite.Create(Texture2D.whiteTexture, new Rect(0, 0, 4, 4), new Vector2(0.5f, 0.5f), 100, 0, SpriteMeshType.FullRect, new Vector4(1, 1, 1, 1));
            const int n = 64;
            var tex = new Texture2D(n, n, TextureFormat.RGBA32, false);
            for (int y = 0; y < n; y++)
                for (int x = 0; x < n; x++)
                {
                    float dx = x - n / 2f + 0.5f, dy = y - n / 2f + 0.5f, d = Mathf.Sqrt(dx * dx + dy * dy);
                    tex.SetPixel(x, y, new Color(1, 1, 1, Mathf.Clamp01(n / 2f - d)));
                }
            tex.Apply();
            Round = Sprite.Create(tex, new Rect(0, 0, n, n), new Vector2(0.5f, 0.5f));
        }

        public static Sprite Load(string path)
        {
            if (cache.TryGetValue(path, out var s)) return s;
            var tex = Resources.Load<Texture2D>(path);
            if (tex == null) { Debug.LogWarning("Missing art: " + path); return White; }
            s = Sprite.Create(tex, new Rect(0, 0, tex.width, tex.height), new Vector2(0.5f, 0f));
            cache[path] = s;
            return s;
        }

        public static RectTransform Rect(string name, Transform parent)
        {
            var go = new GameObject(name, typeof(RectTransform));
            go.transform.SetParent(parent, false);
            return (RectTransform)go.transform;
        }

        public static RectTransform Stretch(RectTransform rt, float l = 0, float b = 0, float r = 0, float t = 0)
        {
            rt.anchorMin = Vector2.zero; rt.anchorMax = Vector2.one;
            rt.offsetMin = new Vector2(l, b); rt.offsetMax = new Vector2(-r, -t);
            return rt;
        }

        public static RectTransform Place(RectTransform rt, Vector2 anchor, Vector2 pivot, Vector2 pos, Vector2 size)
        {
            rt.anchorMin = rt.anchorMax = anchor; rt.pivot = pivot;
            rt.anchoredPosition = pos; rt.sizeDelta = size;
            return rt;
        }

        public static Image Img(Transform parent, string name, Color c, Sprite s = null)
        {
            var rt = Rect(name, parent);
            var img = rt.gameObject.AddComponent<Image>();
            img.sprite = s ?? White; img.color = c; img.raycastTarget = false;
            return img;
        }

        public static Text Txt(Transform parent, string name, string s, Font f, int size, Color c, TextAnchor a = TextAnchor.MiddleCenter)
        {
            var rt = Rect(name, parent);
            var t = rt.gameObject.AddComponent<Text>();
            t.font = f; t.fontSize = size; t.color = c; t.alignment = a; t.text = s; t.raycastTarget = false;
            t.horizontalOverflow = HorizontalWrapMode.Wrap; t.verticalOverflow = VerticalWrapMode.Overflow;
            t.supportRichText = true;
            return t;
        }

        public static Outline Outlined(Graphic g, Color c, float d = 2f)
        {
            var o = g.gameObject.AddComponent<Outline>();
            o.effectColor = c; o.effectDistance = new Vector2(d, -d);
            return o;
        }

        public static Button Btn(Transform parent, string label, Action onClick, Vector2 size, int fontSize = 28, Color? fill = null)
        {
            var img = Img(parent, "Button " + label, fill ?? new Color(0.14f, 0.15f, 0.2f, 0.95f));
            img.raycastTarget = true;
            img.rectTransform.sizeDelta = size;
            var edge = Img(img.transform, "Edge", Brass);
            Stretch(edge.rectTransform, 0, 0, 0, size.y - 3);
            var t = Txt(img.transform, "Label", label, Title, fontSize, Paper);
            Stretch(t.rectTransform, 8, 4, 8, 4);
            var b = img.gameObject.AddComponent<Button>();
            var colors = b.colors;
            colors.highlightedColor = new Color(1.35f, 1.25f, 1.05f, 1f);
            colors.selectedColor = new Color(1.35f, 1.25f, 1.05f, 1f);
            colors.pressedColor = new Color(0.8f, 0.8f, 0.8f, 1f);
            b.colors = colors;
            b.onClick.AddListener(() => { Sfx.Play("click"); onClick?.Invoke(); });
            return b;
        }

        public static void SetLabel(Button b, string s) => b.GetComponentInChildren<Text>().text = s;

        public static T Clear<T>(T rt) where T : Transform
        {
            for (int i = rt.childCount - 1; i >= 0; i--) UnityEngine.Object.Destroy(rt.GetChild(i).gameObject);
            return rt;
        }
    }

    /// A vertical Nixie reel. Faces have individual heights (resonance faces are wider),
    /// scroll continuously and report the face under the centre line when stopped.
    public class Wheel : MonoBehaviour
    {
        class Face { public int digit; public float start, height; public bool lucky, shimmer; public List<Image> panels = new List<Image>(); public List<Text> texts = new List<Text>(); }

        public float speed = 470f;
        public bool Running { get; private set; }
        public int Result { get; private set; } = -1;
        readonly List<Face> faces = new List<Face>();
        RectTransform strip, window;
        float offset, total;
        Face lastFace;
        Text caption;
        public const float Cell = 128f;

        public static Wheel Create(Transform parent, Vector2 pos)
        {
            var frame = UI.Img(parent, "Wheel", new Color(0.03f, 0.03f, 0.05f, 0.96f));
            UI.Place(frame.rectTransform, new Vector2(0.5f, 0.5f), new Vector2(0.5f, 0.5f), pos, new Vector2(176, 330));
            var border = UI.Img(frame.transform, "Border", UI.Brass);
            UI.Stretch(border.rectTransform, -4, -4, -4, -4);
            border.transform.SetAsFirstSibling();
            var w = frame.gameObject.AddComponent<Wheel>();
            w.window = UI.Rect("Window", frame.transform);
            UI.Stretch(w.window, 6, 6, 6, 6);
            w.window.gameObject.AddComponent<RectMask2D>();
            w.strip = UI.Rect("Strip", w.window);
            w.strip.anchorMin = w.strip.anchorMax = new Vector2(0.5f, 0.5f);
            w.strip.pivot = new Vector2(0.5f, 1f);
            w.strip.sizeDelta = new Vector2(164, 10);
            foreach (var y in new[] { 1f, -1f })
            {
                var mark = UI.Img(frame.transform, "Mark", UI.Nixie);
                UI.Place(mark.rectTransform, new Vector2(0.5f, 0.5f), new Vector2(0.5f, 0.5f), new Vector2(0, y * 64), new Vector2(190, 3));
            }
            var shade = UI.Img(frame.transform, "Shade", new Color(0, 0, 0, 0.45f));
            UI.Place(shade.rectTransform, new Vector2(0.5f, 1f), new Vector2(0.5f, 1f), new Vector2(0, -6), new Vector2(164, 92));
            var shade2 = UI.Img(frame.transform, "Shade", new Color(0, 0, 0, 0.45f));
            UI.Place(shade2.rectTransform, new Vector2(0.5f, 0f), new Vector2(0.5f, 0f), new Vector2(0, 6), new Vector2(164, 92));
            w.caption = UI.Txt(frame.transform, "Caption", "", UI.Title, 26, UI.Paper);
            UI.Place(w.caption.rectTransform, new Vector2(0.5f, 1f), new Vector2(0.5f, 0f), new Vector2(0, 10), new Vector2(320, 34));
            return w;
        }

        public void SetCaption(string s, Color c) { caption.text = s; caption.color = c; }

        /// widthFor returns a multiplier on the 128 px face (1 = normal).
        public void Build(int[] digits, Func<int, float> widthFor, int lucky)
        {
            UI.Clear(strip);
            faces.Clear();
            total = 0;
            foreach (var d in digits)
            {
                var f = new Face { digit = d, start = total, height = Cell * Mathf.Max(0.25f, widthFor(d)), lucky = d == lucky };
                total += f.height;
                faces.Add(f);
            }
            for (int copy = 0; copy < 3; copy++)
                foreach (var f in faces)
                {
                    var p = UI.Img(strip, "Face " + f.digit, f.lucky ? new Color(0.22f, 0.15f, 0.06f, 1f) : new Color(0.1f, 0.1f, 0.13f, 1f));
                    p.rectTransform.anchorMin = p.rectTransform.anchorMax = new Vector2(0.5f, 1f);
                    p.rectTransform.pivot = new Vector2(0.5f, 1f);
                    p.rectTransform.anchoredPosition = new Vector2(0, -(copy * total + f.start) - 2);
                    p.rectTransform.sizeDelta = new Vector2(156, f.height - 4);
                    var t = UI.Txt(p.transform, "Digit", f.digit.ToString(), UI.Title, 104, f.lucky ? UI.Gold : UI.Nixie);
                    UI.Stretch(t.rectTransform);
                    f.panels.Add(p); f.texts.Add(t);
                }
            strip.sizeDelta = new Vector2(164, total * 3);
            offset = UnityEngine.Random.value * total;
            Layout();
        }

        public void SetShimmer(Func<int, bool> shimmer)
        {
            foreach (var f in faces) f.shimmer = shimmer != null && shimmer(f.digit);
        }

        public void Spin() { Result = -1; Running = true; gameObject.SetActive(true); }

        void Update()
        {
            if (Running) offset += speed * Time.deltaTime;
            Layout();
            if (Running && total > 0)
            {
                var f = At(offset);
                if (f != lastFace) { lastFace = f; Sfx.Play("tick", 0.9f + 0.03f * f.digit); }
            }
            float pulse = 0.55f + 0.45f * Mathf.Sin(Time.time * 9f);
            foreach (var f in faces)
                foreach (var t in f.texts)
                    t.color = f.shimmer ? Color.Lerp(UI.Teal, Color.white, pulse) : f.lucky ? UI.Gold : UI.Nixie;
        }

        void Layout()
        {
            if (total <= 0) return;
            float q = Mathf.Repeat(offset, total);
            strip.anchoredPosition = new Vector2(0, q + total);
        }

        Face At(float o)
        {
            float q = Mathf.Repeat(o, total);
            foreach (var f in faces) if (q >= f.start && q < f.start + f.height) return f;
            return faces[faces.Count - 1];
        }

        /// Stop where the player pressed. Returns the actual landed digit after a short settle.
        public System.Collections.IEnumerator Stop(bool reducedMotion)
        {
            Running = false;
            var f = At(offset);
            float baseLoop = Mathf.Floor(offset / total) * total;
            float target = baseLoop + f.start + f.height / 2f;
            if (target < offset - f.height) target += total;
            yield return Settle(target, reducedMotion ? 0f : 0.09f);
            Result = f.digit;
            Sfx.Play("stop");
        }

        /// Authored tutorial stop: visibly travels forward to the named digit.
        public System.Collections.IEnumerator StopOn(int digit, bool reducedMotion)
        {
            Running = false;
            Face f = faces.Find(x => x.digit == digit) ?? faces[0];
            float baseLoop = Mathf.Floor(offset / total) * total;
            float target = baseLoop + f.start + f.height / 2f;
            while (target < offset) target += total;
            yield return Settle(target, reducedMotion ? 0f : Mathf.Clamp((target - offset) / 900f, 0.2f, 0.7f));
            Result = f.digit;
            Sfx.Play("stop");
        }

        System.Collections.IEnumerator Settle(float target, float duration)
        {
            float from = offset, t = 0;
            while (t < duration)
            {
                t += Time.deltaTime;
                float k = 1f - Mathf.Pow(1f - Mathf.Clamp01(t / duration), 3f);
                offset = Mathf.Lerp(from, target, k);
                yield return null;
            }
            offset = target;
        }
    }
}
