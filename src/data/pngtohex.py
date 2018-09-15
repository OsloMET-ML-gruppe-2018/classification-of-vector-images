#!/usr/bin/python
from PIL import Image

def rgb2hex(r, g, b):
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)

img = Image.open('Pictures/download.png')


if img.mode in ('RGB', 'LA') or (img.mode == 'P' and 'transparency' in img.info):
    pixels = list(img.convert('RGB').getdata())

    for r, g, b in pixels: # just ignore the alpha channel
       print (rgb2hex(r, g, b))