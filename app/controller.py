from app.scene_analyzer import analyze_script
from app.settings import load_settings
from app.keyword_generator import generate_keywords
from app.media.pexels import search_video, get_best_video_link
from app.media.downloader import download_file
from app.voice import generate_voice
from app.video_editor import trim_all_videos, merge_videos

print("Controller Loaded")


def generate(script):
    settings = load_settings()

    safe_settings = settings.copy()
    safe_settings["pexels_api_key"] = "***HIDDEN***"

    print("Current Settings:")
    print(safe_settings)

    scenes = analyze_script(script)

    print("\n====== SCENES ======")

    for i, scene in enumerate(scenes, start=1):
        keyword = generate_keywords(scene)

        print(f"\nScene {i}:")
        print(scene)

        print("Keyword:")
        print(keyword)

        video = search_video(
            settings["pexels_api_key"],
            keyword
        )

        if video:
            link = get_best_video_link(video)

            if link:
                download_file(
                    link,
                    f"temp/scene{i}.mp4"
                )

    print("\nGenerating Voice...")
    generate_voice(script)
    print("Voice Generated Successfully!")

    print("\nTrimming Videos...")
    trim_all_videos(len(scenes))
    print("Video Trimming Finished!")

    print("\nMerging Videos...")
    merge_videos(len(scenes))
    print("Video Merge Finished!")

    return scenes