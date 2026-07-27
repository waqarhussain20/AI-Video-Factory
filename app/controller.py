from app.scene_analyzer import analyze_script
from app.settings import load_settings

print("Controller Loaded")


def generate(script):
    settings = load_settings()

    print("Current Settings:")
    print(settings)

    scenes = analyze_script(script)

    print("\n====== SCENES ======")

    for i, scene in enumerate(scenes, start=1):
        print(f"Scene {i}: {scene}")

    return scenes