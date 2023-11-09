import os
import requests

def download_if_file_not_exists(filepath, url):
    # Check if the file already exists at the specified filepath
    if os.path.exists(filepath):
        print(f"File already exists at {filepath}. No need to download.")
        return

    # If the file doesn't exist, download it from the provided URL
    try:
        print(f"Attempting to download file from {url}")

        response = requests.get(url)
        response.raise_for_status()  # Check for any request errors

        with open(filepath, 'wb') as file:
            file.write(response.content)

        print(f"File downloaded and saved to {filepath}.")
    except Exception as e:
        print(f"An error occurred while downloading the file: {e}")

