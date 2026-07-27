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