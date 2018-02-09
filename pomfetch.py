#!/usr/bin/env python3
# Fetches a copy of each of the pomological watercolors, scaled.

import os, requests, json, os.path
from io import BytesIO
from PIL import Image
from bs4 import BeautifulSoup

data = []
loaded = set()

if os.path.exists("sources/thumbs.json"):
    with open("sources/thumbs.json", "r") as thumbsJSON:
        data = json.load(thumbsJSON)
        for each in data:
            loaded.add(each["id"])

try:
    for i in range(1,7584):
        if i in loaded:
            print("skipping: %d" % i)
            continue

        imgname = "POM0000" + format(i,"04d") + ".jpg"
        imgurl = "https://commons.wikimedia.org/wiki/File:Pomological_Watercolor_" + imgname
        res = requests.get(imgurl)
        soup = BeautifulSoup(res.text, "lxml")
        thumbs = soup.select('.mw-thumbnail-link')

        if len(thumbs) == 0:
            print("no thumbnails at " + imgurl)
            continue

        print("got thumbnails for " + imgname)
        propersize = thumbs[len(thumbs)-2]
        jpeg = propersize.get('href')
        print("adding " + imgname)

        img = requests.get(jpeg)
        photo = Image.open(BytesIO(img.content))

        photo.save("sources/" + imgname)
        data.append({
            'id':       i,
            'filename': imgname,
            'url':      jpeg,
        })
finally:
    with open("sources/thumbs.json", "w") as thumbsJSON:
        json.dump(data, thumbsJSON, indent=4)
        thumbsJSON.write('\n')
