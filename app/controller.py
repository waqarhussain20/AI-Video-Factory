from app.scene_analyzer import analyze_script
from app.settings import load_settings
from app.keyword_generator import generate_keywords

print("Controller Loaded")


def generate(script):
    settings = load_settings()

    print("Current Settings:")
    print(settings)

    scenes = analyze_script(script)

    print("\n====== SCENES ======")

    for i, scene in enumerate(scenes, start=1):
        keyword = generate_keywords(scene)

        print(f"\nScene {i}:")
        print(scene)

        print("Keyword:")
        print(keyword)

    return scenes