from app.video_editor import get_duration, trim_video

duration = get_duration("temp/voice.wav")

print("Voice Duration:", duration)

trim_video(
    "temp/scene1.mp4",
    "temp/scene1_trim.mp4",
    5
)