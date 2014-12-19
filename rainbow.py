import numpy as np
from PIL import Image
import sys

#memory map the framebuffer as a numpy array
#1440, 900 as shape as that is the res of my display
#uint16 - 16 bit values for color
fb = np.memmap('/dev/fb1', mode='w+', dtype='uint16', shape=(900, 1440))

img = Image.open(sys.argv[1])

# blank the display
img = Image.open('tux-27.png')
fb[:] = np.zeros((1440, 900))
img = img.convert('RGB')
x, y = img.size
imgarray = np.array(img)[:,:,:3] # get the image as a numpy array as an array


#reasonably fast
fb[:] = 0


def color(r, g, b):
    #16 bit has 5 bit r, b and 6-bit g
    #5+6 == 11
    return r << 11 | g << 5 | b

r = np.floor(imgarray[:,:,0] / 256 * 32).astype('int') # conversion needs to happen sometime
g = np.floor(imgarray[:,:,1] / 256 * 64).astype('int')
b = np.floor(imgarray[:,:,2] / 256 * 32).astype('int')
flattenedarray = color(r, g, b)
xo, yo = 0, 0
while 1:
    fb[yo:y+yo, xo:x+xo] = flattenedarray
    fb[:] = 0
    xo += 1

