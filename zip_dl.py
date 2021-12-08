import requests
import re
import os
from bs4 import BeautifulSoup
from tqdm import tqdm

target_url = "Downloads Splash Page"  # example "https://domain.org/downloads/"

parent_dir = "absolute path"  # declare the main directory for this batch download
                            # "/Users/thomas/media/"
                            # "c:\user\music\"


headers = {  # Some sites prevent suspicious user-agent strings from sending requests, change as necessary

    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:94.0) Gecko/20100101 Firefox/94.0',
}


def crawl():
    target_links = []
    print("Crawling Main Page")
    response = requests.get(target_url, headers=headers)
    soup = BeautifulSoup(response.content, 'html5lib')

    # change regex below as appropriate
    indirect_links = soup.find_all('a', {'href': re.compile(r'/en.*-.*/')})

    authors = [link['href'] for link in indirect_links]
    print("Crawling Secondary Pages)
    for each in tqdm(authors):
        response = requests.get(each, headers=headers)
        soup = BeautifulSoup(response.content, 'html5lib')

        # regex below will find .zip files, change as appropriate
        download_links = soup.find_all('a', {'href': re.compile(r'.*.zip')})
        for link in download_links:
            target_links.append(link['href'])
    target_links = list(set(target_links))
    print(len(target_links), "Files available for download...")
    return target_links


def download(target_links):
          
    print("Begining Downloads...")
    for link in tqdm(target_links):

        # assuming files are in the format domain.org/downloads/author/file_name:
        author = link.split('/')[-2]
        file_name = link.split('/')[-1]

        dir_path = os.path.join(parent_dir, author)
        if not os.path.exists(dir_path):
            os.mkdir(dir_path)
        file_path = os.path.join(dir_path, file_name)
        if not os.path.isfile(file_path):
            print("Downloading file:%s from %s" % (file_name, author))
            response = requests.get(link, stream=True)
            with open(file_path, "wb+") as f:
                for chunk in response.iter_content(chunk_size=1024 * 1024):
                    if chunk:
                        f.write(chunk)
            print("%s downloaded!\n" % file_name)
    print("All files downloaded!")
    return


if __name__ == "__main__":
    links = crawl()
    download(links)



