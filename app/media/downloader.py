import os
import requests


def download_file(url, output_path):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    response = requests.get(url, stream=True)

    if response.status_code != 200:
        print("Download failed.")
        return False

    with open(output_path, "wb") as file:
        for chunk in response.iter_content(chunk_size=8192):
            if chunk:
                file.write(chunk)

    print(f"Downloaded: {output_path}")
    return True