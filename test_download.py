from app.settings import load_settings
from app.media.pexels import search_video
from app.media.downloader import download_file

settings = load_settings()

video = search_video(
    settings["pexels_api_key"],
    "artificial intelligence"
)

if video:
    video_url = video["video_files"][0]["link"]

    download_file(
        video_url,
        "temp/test_video.mp4"
    )