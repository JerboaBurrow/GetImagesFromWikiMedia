import urllib.request
from bs4 import BeautifulSoup
import json
from pathlib import Path
import shutil

import argparse

def attribution(url):
    img = url.split("/")[-1]
    url = f"https://commons.wikimedia.org/w/api.php?action=query&iiprop=extmetadata&prop=imageinfo&titles=Image%3A{img}&format=json"
    response = urllib.request.urlopen(url)
    if response.status == 200:
        body = response.read()
        encoding = response.info().get_content_charset('utf-8')
        data = json.loads(body.decode(encoding))
        try:
            pages = data["query"]["pages"]
            k = [k for k in pages][0]
            info = pages[k]["imageinfo"][0]["extmetadata"]
            vals = {}
            for val in ["Attribution", "LicenseShortName", "LicenseUrl", "Artist"]:
                v = info[val]["value"] if val in info else ""
                vals[val] = v
            return vals
        except:
            pass
    print(f"Incomplete attribution for image: {img}")
    return []

def full_image(url, file_name, attrib):
    response = urllib.request.urlopen(url)
    if response.status == 200:
        doc = BeautifulSoup(response.read(), "html.parser")
        div = doc.find_all("div", {"class": "fullImageLink"})[0]
        img = div.find_all("a")[0].get("href")
        try:
            urllib.request.urlretrieve(img, file_name)
        except:
            print(f"Full image url: {url}, retrieval failed")
            return False
        attrib[len(attrib)+1] = attribution(img)
        return True
    else:
        print(f"Full image url: {url}, returned {response.status}")
    return False

def search(query: str, *, take=3, save_path="images"):
    q = query.replace(" ", "+")
    url = f"https://commons.wikimedia.org/w/index.php?search={q}&title=Special:MediaSearch&go=Go&type=image"
    response = urllib.request.urlopen(url)
    if response.status == 200:
        doc = BeautifulSoup(response.read(), "html.parser")
        taken = 0
        name = query.replace(" ", "_")
        success = False

        if not Path(save_path).is_dir():
            Path(save_path).mkdir()

        dir = Path(f"{save_path}/{name}")
        if not dir.is_dir():
            dir.mkdir()

        attrib = {}
        for img in doc.find_all("a", {"class": "sdms-image-result"}):
            src = img.get("href")
            extension = src.split(".")[-1]
            if extension in ["jpg", "jpeg", "png"]:
                taken += 1
                result = full_image(src, dir/f"{taken}.{extension}", attrib)
                success = success or result
                if taken == take:
                    break

        if success:
            with open(dir/"attributions.json", "w") as f:
                json.dump(attrib, f, indent=4)
        else:
            print(f"No successful scraping for query {query}")
            if not any(Path(save_path).iterdir()):
                shutil.rmtree(save_path)
    else:
        print(f"Query: {query}, returned {response.status}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("query", type=str, help="Query to extract images for")
    parser.add_argument("-take", type=int, default=1, help="Number of images to extract", dest="take")
    parser.add_argument("-path", type=str, default="images", help="Path to save images", dest="path")
    args = parser.parse_args()

    search(args.query, take=args.take, save_path=args.path)
