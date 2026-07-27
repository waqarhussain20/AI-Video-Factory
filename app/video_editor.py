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