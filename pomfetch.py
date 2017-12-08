#!/usr/bin/env python3
# Fetches a copy of each of the pomological watercolors, scaled.

import os, requests, json
from io import BytesIO
from PIL import Image
from bs4 import BeautifulSoup

for i in range(1,7584):
    imgname = "POM0000" + format(i,"04d") + ".jpg"
    res = requests.get("https://commons.wikimedia.org/wiki/File:Pomological_Watercolor_" + imgname)
    soup = BeautifulSoup(res.text, "lxml")
    thumbs = soup.select('.mw-thumbnail-link')

    print("got thumbnails for " + imgname)

    if len(thumbs) == 0:
        continue

    propersize = thumbs[len(thumbs)-2]
    jpeg = propersize.get('href')
    print("adding " + imgname)

    img = requests.get(jpeg)
    photo = Image.open(BytesIO(img.content))

    photo.save("sources/" + imgname)
