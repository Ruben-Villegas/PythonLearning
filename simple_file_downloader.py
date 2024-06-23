# simple_file_downloader.py
import requests

def download_file(url, destination):
    response = requests.get(url)
    if response.status_code == 200:
        with open(destination, 'wb') as file:
            file.write(response.content)
        print(f"File downloaded to {destination}")
    else:
        print(f"Failed to download file. Status code: {response.status_code}")

if __name__ == "__main__":
    file_url = 'https://example.com/somefile.zip'
    destination_path = 'downloaded_file.zip'
    download_file(file_url, destination_path)
