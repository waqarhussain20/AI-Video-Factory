import subprocess
import os

FFMPEG = r"C:\ffmpeg\bin\ffmpeg.exe"
FFPROBE = r"C:\ffmpeg\bin\ffprobe.exe"


def get_duration(file_path):
    command = [
        FFPROBE,
        "-v", "error",
        "-show_entries", "format=duration",
        "-of", "default=noprint_wrappers=1:nokey=1",
        file_path
    ]

    result = subprocess.run(
        command,
        capture_output=True,
        text=True
    )

    return float(result.stdout.strip())


def trim_video(input_file, output_file, duration):
    command = [
        FFMPEG,
        "-y",
        "-i", input_file,
        "-t", str(duration),
        "-c", "copy",
        output_file
    ]

    subprocess.run(command, check=True)

    print(f"Trimmed: {output_file}")


def trim_all_videos(scene_count):
    voice_duration = get_duration("temp/voice.wav")

    duration_per_scene = voice_duration / scene_count

    print(f"\nVoice Duration: {voice_duration:.2f} sec")
    print(f"Each Scene: {duration_per_scene:.2f} sec")

    for i in range(1, scene_count + 1):
        trim_video(
            f"temp/scene{i}.mp4",
            f"temp/scene{i}_trim.mp4",
            duration_per_scene
        )


def normalize_video(input_file, output_file):
    command = [
        FFMPEG,
        "-y",
        "-i", input_file,
        "-vf",
        "scale=1920:1080:force_original_aspect_ratio=decrease,"
        "pad=1920:1080:(ow-iw)/2:(oh-ih)/2:black,"
        "setsar=1",
        "-r", "30",
        "-c:v", "libx264",
        "-preset", "fast",
        "-crf", "23",
        "-an",
        output_file
    ]

    subprocess.run(command, check=True)

    print(f"Normalized: {output_file}")


def normalize_all_videos(scene_count):
    print("\nNormalizing Videos...")

    for i in range(1, scene_count + 1):
        normalize_video(
            f"temp/scene{i}_trim.mp4",
            f"temp/scene{i}_ready.mp4"
        )

    print("All Videos Normalized!")


def merge_videos(scene_count):
    os.makedirs("temp", exist_ok=True)

    list_file = os.path.join("temp", "video_list.txt")

    with open(list_file, "w", encoding="utf-8") as f:
        for i in range(1, scene_count + 1):
            f.write(f"file 'scene{i}_ready.mp4'\n")

    command = [
        FFMPEG,
        "-y",
        "-f", "concat",
        "-safe", "0",
        "-i", "video_list.txt",
        "-c", "copy",
        "merged.mp4"
    ]

    subprocess.run(
        command,
        cwd="temp",
        check=True
    )

    print("Merged Video Created!")


def add_voice():
    os.makedirs("output", exist_ok=True)

    command = [
        FFMPEG,
        "-y",

        "-i", "temp/merged.mp4",
        "-i", "temp/voice.mp3",

        "-map", "0:v:0",
        "-map", "1:a:0",

        "-c:v", "copy",
        "-c:a", "copy",

        "-shortest",

        "output/final_video.mp4"
    ]

    subprocess.run(command, check=True)

    print("\n==============================")
    print("Final Video Created!")
    print("Location: output/final_video.mp4")
    print("==============================")