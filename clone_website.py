import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin


def save_html(content, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)


def download_file(url, folder_path):
    local_filename = url.split('/')[-1]
    file_path = os.path.join(folder_path, local_filename)

    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(file_path, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)

    return file_path


def clone_website(url, folder_path):
    os.makedirs(folder_path, exist_ok=True)

    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.content, 'html.parser')

    # Save the main page
    save_html(soup.prettify(), os.path.join(folder_path, 'index.html'))

    # Download linked CSS and images
    for link in soup.find_all(['link', 'img']):
        src = link.get('href') or link.get('src')
        if src:
            full_url = urljoin(url, src)
            download_file(full_url, folder_path)


# Example usage:
url = 'https://frejlich.com'
folder_path = 'cloned_website'
clone_website(url, folder_path)
