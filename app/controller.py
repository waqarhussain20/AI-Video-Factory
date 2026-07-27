from app.scene_analyzer import analyze_script
print("Controller Loaded")

def generate(script):
    scenes = analyze_script(script)

    print("\n====== SCENES ======")

    for i, scene in enumerate(scenes, start=1):
        print(f"Scene {i}: {scene}")

    return scenes