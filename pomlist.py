#!/usr/bin/env python3
# Prepares the "sources.json" file for pomtiler.py and pomrender.py

import os, json

imgdict = {}
index = 1

for i in os.listdir("sources"):
    imgdict[index] = i
    index += 1

with open("sources.json","w") as outfile:
    json.dump(imgdict,outfile)
