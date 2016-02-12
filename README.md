# pomtiles

A tiling program for making visuals with the pomological watercolor collection

Here's how it works: run `pomfetch.py` to fetch a bunch of pomological watercolors from Wikimedia's servers. It'll download 7500 of them into a folder called `sources/`. That's about 700 MB, so it might take a few minutes.

Then run `pomlist.py` to create a file, `sources.json`, that matches each source image up with an ID number. I don't package it here because you might want to add or remove images from your sources folder.

Tweak the number of frames you want in `pomtiler.py`, then run it to generate `slide_deck.json`.

Finally, run `pomrender.py` to render the actual tiled images that will live in `imgs/`. They're named in the form `img###.png`.

With that output, I run something like:

`ffmpeg -framerate 1/12 -i img%03d.png -c:v mpeg4 -q 1 -pix_fmt yuv420p out.mp4`

to generate a [video with 12 seconds for each slide](https://www.youtube.com/watch?v=GnhwNxZ9hRs).
