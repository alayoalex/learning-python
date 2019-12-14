from __future__ import print_function
from PIL import Image

im = Image.open("image_processing/_MG_5192.jpg")
print(im.format, im.size, im.mode)
#im.show()

#box = (100, 100, 400, 400)
#region = im.crop(box)
# region.show()

#r, g, b = im.split()
#mm = Image.merge("RGB", (b, g, r))
#mm.show()

