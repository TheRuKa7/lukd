// Procedurally synthesised sound: no audio files to license or download.
using System.Collections.Generic;
using UnityEngine;

namespace Remainder
{
    public static class Sfx
    {
        const int Rate = 44100;
        static readonly Dictionary<string, AudioClip> clips = new Dictionary<string, AudioClip>();
        static AudioSource[] pool;
        static AudioSource rain, drone, music;
        static string currentSong;
        static int next;
        public static float Volume = 0.8f;

        public static void Init(GameObject host)
        {
            pool = new AudioSource[10];
            for (int i = 0; i < pool.Length; i++) { pool[i] = host.AddComponent<AudioSource>(); pool[i].playOnAwake = false; }
            clips["click"] = Tone(1200, 0.03f, 0.25f, decay: 60);
            clips["tick"] = Tone(2400, 0.015f, 0.08f, decay: 200);
            clips["stop"] = Mix(Tone(180, 0.12f, 0.6f, decay: 28), Noise(0.05f, 0.35f, 60));
            clips["hit"] = Mix(Tone(90, 0.25f, 0.7f, decay: 14), Noise(0.18f, 0.5f, 20));
            clips["parry"] = Mix(Tone(1560, 0.35f, 0.4f, decay: 9), Tone(2340, 0.35f, 0.25f, decay: 11));
            clips["shot"] = Mix(Noise(0.3f, 0.9f, 16), Tone(70, 0.3f, 0.6f, decay: 12));
            clips["coin"] = Arp(new[] { 988f, 1319f }, 0.07f, 0.3f);
            clips["bust"] = Arp(new[] { 330f, 262f }, 0.12f, 0.3f);
            clips["pair"] = Arp(new[] { 523f, 659f }, 0.09f, 0.35f);
            clips["zero"] = Arp(new[] { 440f, 554f, 440f }, 0.08f, 0.35f);
            clips["cascade"] = Arp(new[] { 523f, 659f, 784f, 1047f }, 0.07f, 0.35f);
            clips["jackpot"] = Arp(new[] { 523f, 784f, 1047f, 1568f }, 0.09f, 0.4f);
            clips["overwrite"] = Arp(new[] { 392f, 523f, 659f, 784f, 1047f, 1319f, 1568f }, 0.08f, 0.45f);
            clips["alarm"] = Arp(new[] { 880f, 660f, 880f, 660f }, 0.14f, 0.3f);
            clips["rain"] = Noise(4f, 0.12f, 0, loopFriendly: true);
            clips["drone"] = Pad(new[] { 55f, 82.5f, 110f, 165f }, 8f, 0.12f);
            // A minor loops: Am F C G (street), Am F G E (battle), Am Dm (shrine)
            clips["m_street"] = Song(80, new[] { 57, 53, 48, 55 }, battle: false, density: 0.35f, seed: 3);
            clips["m_battle"] = Song(112, new[] { 57, 53, 55, 52 }, battle: true, density: 0.5f, seed: 11);
            clips["m_shrine"] = Song(64, new[] { 57, 50, 57, 52 }, battle: false, density: 0.2f, seed: 5);
            music = host.AddComponent<AudioSource>(); music.loop = true;
            rain = host.AddComponent<AudioSource>(); rain.clip = clips["rain"]; rain.loop = true;
            drone = host.AddComponent<AudioSource>(); drone.clip = clips["drone"]; drone.loop = true;
        }

        public static void Play(string id, float pitch = 1f)
        {
            if (pool == null || !clips.TryGetValue(id, out var c)) return;
            var s = pool[next++ % pool.Length];
            s.pitch = pitch; s.volume = Volume; s.PlayOneShot(c);
        }

        public static void Ambience(bool rainOn, bool droneOn)
        {
            if (rain == null) return;
            rain.volume = Volume * 0.5f; drone.volume = Volume * 0.6f;
            if (rainOn && !rain.isPlaying) rain.Play(); else if (!rainOn) rain.Stop();
            if (droneOn && currentSong == null && !drone.isPlaying) drone.Play(); else if (!droneOn) drone.Stop();
        }

        public static void Refresh() { if (rain != null) { rain.volume = Volume * 0.5f; drone.volume = Volume * 0.6f; music.volume = Volume * 0.55f; } }

        /// Switch the music loop (m_street, m_battle, m_shrine) or stop it with null.
        public static void Music(string id)
        {
            if (music == null || id == currentSong) return;
            currentSong = id;
            music.volume = Volume * 0.55f;
            if (id == null || !clips.TryGetValue(id, out var c)) { music.Stop(); return; }
            music.clip = c; music.Play();
            drone.Stop();
        }

        static float Midi(int m) => 440f * Mathf.Pow(2f, (m - 69) / 12f);

        // Small deterministic sequencer: keys or arpeggio, bass, pentatonic melody, light drums.
        static AudioClip Song(float bpm, int[] roots, bool battle, float density, int seed)
        {
            const int sr = 22050;
            float beat = 60f / bpm; int steps = roots.Length * 8;            // 8th notes, 4 beats per chord
            float step = beat / 2f; int n = Mathf.RoundToInt(steps * step * sr);
            var d = new float[n]; var rnd = new System.Random(seed);
            int[] penta = { 0, 3, 5, 7, 10, 12, 15 };
            void Note(float start, float freq, float dur, float amp, float decay, float bright)
            {
                int s0 = (int)(start * sr), len = (int)(dur * sr);
                for (int i = 0; i < len; i++)
                {
                    int k = (s0 + i) % n; float t = i / (float)sr;
                    float env = Mathf.Exp(-decay * t) * Mathf.Clamp01(t * 200f);
                    d[k] += amp * env * (Mathf.Sin(2 * Mathf.PI * freq * t) + bright * Mathf.Sin(4 * Mathf.PI * freq * t) + bright * 0.4f * Mathf.Sin(6 * Mathf.PI * freq * t));
                }
            }
            void Hit(float start, float amp, float decay, float lowFreq)
            {
                int s0 = (int)(start * sr), len = (int)(0.25f * sr); float lp = 0;
                for (int i = 0; i < len; i++)
                {
                    int k = (s0 + i) % n; float t = i / (float)sr;
                    if (lowFreq > 0) d[k] += amp * Mathf.Sin(2 * Mathf.PI * lowFreq * (1 + 2 * Mathf.Exp(-30 * t)) * t) * Mathf.Exp(-decay * t);
                    else { float w = (float)(rnd.NextDouble() * 2 - 1); lp += (w - lp) * 0.6f; d[k] += amp * (w - lp) * Mathf.Exp(-decay * t); }
                }
            }
            for (int c = 0; c < roots.Length; c++)
            {
                int r = roots[c]; bool minor = c == 0 || (battle ? false : r == 50);
                int[] chord = { r, r + (minor || r == 57 ? 3 : 4), r + 7 };
                float bar = c * 8 * step;
                if (battle)
                    for (int s = 0; s < 8; s++) Note(bar + s * step, Midi(chord[s % 3] + 12), step * 1.2f, 0.05f, 9f, 0.2f);
                else
                    foreach (var off in new[] { 0, 4 }) foreach (var m in chord) Note(bar + off * step, Midi(m + 12), step * 4f, 0.045f, 2.2f, 0.35f);
                for (int s = 0; s < 8; s += battle ? 1 : 4) Note(bar + s * step, Midi(r - 12), step * (battle ? 0.9f : 3.5f), 0.11f, battle ? 6f : 1.5f, 0.1f);
                for (int s = 0; s < 8; s++)
                    if (rnd.NextDouble() < density) Note(bar + s * step, Midi(57 + 12 + penta[rnd.Next(penta.Length)]), step * 2f, 0.035f, 5f, 0.15f);
                for (int s = 0; s < 8; s++)
                {
                    if (battle) { if (s % 2 == 0) Hit(bar + s * step, 0.22f, 18f, 55f); if (s == 2 || s == 6) Hit(bar + s * step, 0.08f, 22f, 0); Hit(bar + s * step + step / 2, 0.025f, 60f, 0); }
                    else { if (s == 0 || s == 5) Hit(bar + s * step, 0.12f, 14f, 50f); if (s % 2 == 1) Hit(bar + s * step, 0.018f, 70f, 0); }
                }
            }
            float peak = 0.001f; foreach (var v in d) peak = Mathf.Max(peak, Mathf.Abs(v));
            for (int i = 0; i < n; i++) d[i] = d[i] / peak * 0.7f;
            var clip = AudioClip.Create("song", n, 1, sr, false); clip.SetData(d, 0); return clip;
        }

        public static string ForPattern(Pattern p) => p switch
        {
            Pattern.OVERWRITE => "overwrite", Pattern.JACKPOT => "jackpot", Pattern.REAPER => "jackpot",
            Pattern.CASCADE => "cascade", Pattern.ZERO_SUM => "zero", Pattern.PAIR => "pair", _ => "bust"
        };

        static AudioClip Make(float[] data, string name)
        {
            var c = AudioClip.Create(name, data.Length, 1, Rate, false);
            c.SetData(data, 0);
            return c;
        }

        static AudioClip Tone(float freq, float dur, float amp, float decay)
        {
            int n = (int)(Rate * dur); var d = new float[n];
            for (int i = 0; i < n; i++) { float t = i / (float)Rate; d[i] = amp * Mathf.Sin(2 * Mathf.PI * freq * t) * Mathf.Exp(-decay * t); }
            return Make(d, "tone");
        }

        static readonly System.Random noise = new System.Random(7);
        static AudioClip Noise(float dur, float amp, float decay, bool loopFriendly = false)
        {
            int n = (int)(Rate * dur); var d = new float[n]; float lp = 0;
            for (int i = 0; i < n; i++)
            {
                float t = i / (float)Rate;
                float w = (float)(noise.NextDouble() * 2 - 1);
                lp += (w - lp) * (loopFriendly ? 0.08f : 0.5f);
                float env = loopFriendly ? 1f : Mathf.Exp(-decay * t);
                if (loopFriendly) { float edge = Mathf.Min(i, n - i) / (Rate * 0.05f); env *= Mathf.Clamp01(edge); }
                d[i] = amp * lp * env;
            }
            return Make(d, "noise");
        }

        static AudioClip Arp(float[] notes, float step, float amp)
        {
            int per = (int)(Rate * step), tail = (int)(Rate * 0.25f), n = per * notes.Length + tail; var d = new float[n];
            for (int k = 0; k < notes.Length; k++)
                for (int i = 0; i < per + tail && k * per + i < n; i++)
                {
                    float t = i / (float)Rate;
                    d[k * per + i] += amp * 0.6f * (Mathf.Sin(2 * Mathf.PI * notes[k] * t) + 0.3f * Mathf.Sin(4 * Mathf.PI * notes[k] * t)) * Mathf.Exp(-9 * t);
                }
            return Make(d, "arp");
        }

        static AudioClip Pad(float[] notes, float dur, float amp)
        {
            int n = (int)(Rate * dur); var d = new float[n];
            for (int i = 0; i < n; i++)
            {
                float t = i / (float)Rate, s = 0;
                foreach (var f in notes) s += Mathf.Sin(2 * Mathf.PI * f * t + Mathf.Sin(2 * Mathf.PI * 0.125f * t) * 0.8f);
                d[i] = amp * s / notes.Length;
            }
            return Make(d, "pad");
        }

        static AudioClip Mix(AudioClip a, AudioClip b)
        {
            int n = Mathf.Max(a.samples, b.samples);
            var da = new float[a.samples]; var db = new float[b.samples]; a.GetData(da, 0); b.GetData(db, 0);
            var d = new float[n];
            for (int i = 0; i < n; i++) d[i] = (i < da.Length ? da[i] : 0) + (i < db.Length ? db[i] : 0);
            return Make(d, "mix");
        }
    }
}
