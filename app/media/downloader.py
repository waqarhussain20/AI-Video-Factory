import os
import requests


def download_file(url, output_path):

    os.makedirs(
        os.path.dirname(output_path),
        exist_ok=True
    )

    try:

        response = requests.get(
            url,
            stream=True,
            timeout=30
        )

        response.raise_for_status()

        total = 0

        with open(output_path, "wb") as file:

            for chunk in response.iter_content(chunk_size=1024 * 1024):

                if chunk:

                    file.write(chunk)
                    total += len(chunk)

                    print(
                        f"\rDownloading... {total / 1024 / 1024:.1f} MB",
                        end=""
                    )

        print(f"\nDownloaded: {output_path}")

        return True

    except requests.exceptions.RequestException as e:

        print("\nDownload Error:")
        print(e)

        return False