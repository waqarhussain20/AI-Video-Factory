from app.settings import load_settings
from app.media.pexels import search_video

settings = load_settings()

search_video(
    settings["pexels_api_key"],
    "artificial intelligence"
)