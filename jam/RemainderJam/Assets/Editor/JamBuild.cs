// Batch build: Unity -batchmode -quit -projectPath . -buildTarget WebGL -executeMethod JamBuild.Build
using System.IO;
using UnityEditor;
using UnityEditor.Build;
using UnityEditor.Build.Reporting;
using UnityEditor.SceneManagement;
using UnityEngine;

public static class JamBuild
{
    const string ScenePath = "Assets/Scenes/Main.unity";

    static void Configure()
    {
        if (!File.Exists(ScenePath))
        {
            Directory.CreateDirectory("Assets/Scenes");
            var scene = EditorSceneManager.NewScene(NewSceneSetup.EmptyScene, NewSceneMode.Single);
            EditorSceneManager.SaveScene(scene, ScenePath);
        }
        EditorBuildSettings.scenes = new[] { new EditorBuildSettingsScene(ScenePath, true) };
        PlayerSettings.productName = "The Remainder";
        PlayerSettings.companyName = "ZERO-SUM OMEN";
        PlayerSettings.bundleVersion = "0.9.0-jam";
        PlayerSettings.defaultWebScreenWidth = 1280;
        PlayerSettings.defaultWebScreenHeight = 720;
        PlayerSettings.runInBackground = true;
        PlayerSettings.WebGL.compressionFormat = WebGLCompressionFormat.Gzip;
        PlayerSettings.WebGL.decompressionFallback = true;   // itch.io serves .gz without Content-Encoding
        PlayerSettings.WebGL.dataCaching = true;
        PlayerSettings.SetManagedStrippingLevel(NamedBuildTarget.WebGL, ManagedStrippingLevel.Medium);
    }

    public static void Build()
    {
        Configure();
        string output = Path.GetFullPath("../build/web");
        var report = BuildPipeline.BuildPlayer(new BuildPlayerOptions
        {
            scenes = new[] { ScenePath },
            locationPathName = output,
            target = BuildTarget.WebGL,
            options = BuildOptions.None
        });
        var s = report.summary;
        Debug.Log($"BUILD RESULT: {s.result} errors={s.totalErrors} size={s.totalSize} time={s.totalTime} output={output}");
        if (Application.isBatchMode) EditorApplication.Exit(s.result == BuildResult.Succeeded ? 0 : 1);
    }

    public static void Windows()
    {
        Configure();
        string output = Path.GetFullPath("../build/win/TheRemainder.exe");
        var report = BuildPipeline.BuildPlayer(new BuildPlayerOptions { scenes = new[] { ScenePath }, locationPathName = output, target = BuildTarget.StandaloneWindows64 });
        Debug.Log($"BUILD RESULT: {report.summary.result} output={output}");
        if (Application.isBatchMode) EditorApplication.Exit(report.summary.result == BuildResult.Succeeded ? 0 : 1);
    }
}
