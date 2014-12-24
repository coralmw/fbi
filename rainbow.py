import numpy as np
from PIL import Image
import time
import sys

def color(r, g, b):
    #16 bit has 5 bit r, b and 6-bit g
    #5+6 == 11
    return r << 11 | g << 5 | b

def loop(charqueue, imgbytes, framebuffer):
    xo, yo = 0, 0
    xs, ys = imgbytes.shape
    framebuffer[xo:xo+xs, yo:yo+ys] = imgbytes
    while 1:
        if not charqueue.empty():
            while not charqueue.empty():
                print('procesing move')
                char = charqueue.get()
                if char == 'w':
                    yo -= 1
                elif char == 's':
                    yo += 1
                elif char == 'a':
                    xo -= 1
                elif char == 'd':
                    xo += 1
                elif char == 'q':
                    exit()
            #print('paint to {}, {}'.format(xo, yo))
            framebuffer[:] = 0 # blank for update
            framebuffer[xo:xo+xs, yo:yo+ys] = imgbytes
        else:
            time.sleep(0.001) # lets not kill a cpu.


def exit():
    print('recieved kill')
    sys.exit()


def main(args, charqueue):
    #memory map the framebuffer as a numpy array
    #1440, 900 as shape as that is the res of my display
    #uint16 - 16 bit values for color
    fb = np.memmap('/dev/fb1', mode='w+', dtype='uint16', shape=(1080, 1920))
    fb[:] = 0 # blank the display

    img = Image.open(args[1])

    img = img.convert('RGB')
    x, y = img.size
    imgarray = np.array(img)[:,:,:3] # get the image as a numpy array as an array


    #reasonably fast
    fb[:] = 0

    r = np.floor(imgarray[:,:,0] / 256 * 32).astype('int') # conversion needs to happen sometime
    g = np.floor(imgarray[:,:,1] / 256 * 64).astype('int')
    b = np.floor(imgarray[:,:,2] / 256 * 32).astype('int')
    flattenedarray = color(r, g, b)

    loop(charqueue, flattenedarray, fb)

