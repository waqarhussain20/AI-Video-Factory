import requests


def search_video(api_key, query):
    url = "https://api.pexels.com/videos/search"

    headers = {
        "Authorization": api_key
    }

    params = {
        "query": query,
        "per_page": 1
    }

    response = requests.get(url, headers=headers, params=params)

    if response.status_code != 200:
        print("Pexels Error:", response.status_code)
        print(response.text)
        return None

    data = response.json()

    if not data["videos"]:
        print("No videos found.")
        return None

    video = data["videos"][0]

    print("\nPexels Video Found!")
    print("ID:", video["id"])
    print("URL:", video["url"])

    return video


def get_best_video_link(video):

    if not video:
        return None

    files = video.get("video_files", [])

    if not files:
        return None

    # Prefer 720p–1080p videos
    suitable = []

    for file in files:

        width = file.get("width", 0)

        if 700 <= width <= 1920:
            suitable.append(file)

    if suitable:

        suitable = sorted(
            suitable,
            key=lambda x: x["width"],
            reverse=True
        )

        return suitable[0]["link"]

    # Fallback
    files = sorted(
        files,
        key=lambda x: x["width"],
        reverse=True
    )

    return files[-1]["link"]