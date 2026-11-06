# ZERO-SUM: OMEN — Technical Design (Gate A11)

The decisions that are expensive to change on Day 5: architecture, data, determinism, WebGL limits, build and save. Engine: **Unity 6 LTS, URP 2D, WebGL 2** (WebGPU optional later).

---

## 1. Architecture

```
Core/          pure C#, no UnityEngine: wheels, faces, reel, patterns (+priority), Balance/Omen, scoring,
               bonds, charms pipeline, Land Laws, Hap's Favour, seeded RNG. EditMode tests.
Sequencing/    async beat scripts (UniTask): HeroStrike, EnemyStrike, PatternPayoff, LinkArt, Ultimate,
               StoryBeat. Reads Core results; drives Presentation; owns timing from GAME_FEEL.
Data/          ScriptableObjects: HeroDef, WheelDef, FaceDef, CharmDef(+SetTag), EnemyDef, BossRuleDef,
               LandLawDef, ActMapDef, StoryDef. Tuning CSV importer.
Presentation/  actors (2D Animation rigs), wheels, reel object, VFX, camera (Cinemachine 3), UI (UGUI/TMP).
Audio/         beat clock, stem controller, SFX bank.
Meta/          save, settings, codex, results, telemetry (opt-in, post-jam).
```

**Rules:** Core never references Unity; Presentation never decides outcomes; Sequencing is the only place time passes. Every random draw goes through `Core.Rng` with a seed.

## 2. Core model (C# sketch)
```csharp
public sealed record Face(int Digit, float Width, FaceEnh Enh);
public sealed class Wheel { public IReadOnlyList<Face> Faces; public float Speed; }
public enum Pattern { Bust, Pair, ZeroSum, Cascade, Jackpot, ReapersToll, Overwrite }   // priority reversed
public static class Patterns {
  public static Pattern Evaluate(int a, int b, int c, int lucky) { /* GDD §1.5 order; mirrors prototype evaluate() */ }
}
public sealed class Combatant { public long Balance, MaxBalance; public int Omen => Balance <= 0 ? 0 : Math.Clamp((int)Math.Ceiling(Balance * 99.0 / MaxBalance), 1, 99); }
public sealed class Favour { public int BustStreak; public bool Warm => BustStreak >= 1; public bool HapsHand => BustStreak >= 2; }
```
Damage uses `long` (Balances reach 99,999,999 and damage can exceed `int` with stacked Mult). Mult is `double`, rounded at the end of the round.

## 3. Data and tuning
- `tuning/jam_tuning.csv` → imported by an editor tool into a `TuningTable` asset on change; runtime reads only the asset.
- Content ids match [`ASSET_LIST.md`](ASSET_LIST.md) (`chr_nil`, `enm_debthound`…).
- Strings live in a string table (Unity Localization) from day one, even in English only (LOCALISATION.md).

## 4. Determinism and testing
- Seeded RNG per run; per-fight sub-seeds. A **replay log** (seed + inputs with timestamps) is written for every fight and attached to bug reports.
- **EditMode tests:** every pattern, the priority order, Omen readout, Favour/Hap's Hand, each Land Law, each charm's rule. Run in CI on every push.
- **PlayMode smoke test:** boot → Naming → Fight 1 auto-played with a fixed seed → Results.
- The pattern simulation (`tools/sim_patterns.py`) is the spec's reference; a C# port of its numbers must match within 0.5%.

## 5. WebGL budgets
| Budget | Target |
|---|---|
| Download size | < 250 MB total; first scene < 40 MB (Addressables for later acts and video) |
| Load to first fight | ≤ 20 s on a mid laptop (cold cache) |
| Frame rate | 60 fps on a 2020 laptop; 30 fps floor on mid phones |
| Memory | < 1.5 GB WebGL heap |
| Textures | Character atlases ≤ 2048², Crunch; stages streamed per scene |
| Audio | Vorbis, music streamed; SFX in a bank |
| Video | 720p H.264 ~2.5 Mbps from StreamingAssets via URL; audio unlocked by the title tap |
| Compression | Brotli with Gzip fallback; decompression fallback on |

**Browser matrix:** Chrome, Firefox, Safari (macOS), Edge; Chrome on Android; Safari on iOS (best effort).

## 6. Build and release
- **Daily build** to a private itch page from Day 1 (GitHub Actions + GameCI, or a local script); the build number shows on the title screen.
- Versioning `jam-0.DAY.BUILD`. Tag the submitted build.
- Branches: `main` always builds; feature branches merge daily.
- Large files: Git LFS for PSB/PSD/PNG/WAV/MP4.

## 7. Save data
- PlayerPrefs (IndexedDB on WebGL): lucky number, act progress, settings, codex unlocks, best scores.
- If storage is cleared or blocked, the game still runs from the title (no crash); "Continue" is hidden.
- Save at node boundaries only (never mid-fight in the jam).

## 8. Performance and safety
- Pool every VFX and damage number; no allocations per frame in combat.
- Cap particles; Reduced Motion disables camera shake and full-screen flashes at the shader level.
- No network calls in the jam build (telemetry is post-jam and opt-in).

**Done when:** an empty WebGL build is live on the private itch page and the Core tests pass for all seven patterns and the priority order.
