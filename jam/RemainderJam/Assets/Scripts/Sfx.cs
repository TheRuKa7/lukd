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
        static AudioSource rain, drone;
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
            if (droneOn && !drone.isPlaying) drone.Play(); else if (!droneOn) drone.Stop();
        }

        public static void Refresh() { if (rain != null) { rain.volume = Volume * 0.5f; drone.volume = Volume * 0.6f; } }

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
