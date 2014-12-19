import numpy as np

#memory map the framebuffer as a numpy array
#1440, 900 as shape as that is the res of my display
#uint16 - 16 bit values for color
fb = np.memmap('/dev/fb1', mode='w+', dtype='uint16', shape=(1440, 900))

#array with the same shape - will be cast on assignment to uint16! no worries
black = np.zeros((1440, 900))

#reasonably fast
fb[:] = black

def color(r, g, b):
    #16 bit has 5 bit r, b and 6-bit g
    #5+6 == 11
    assert(r < 32)
    assert(b < 32)
    assert(g < 64)
    return r << 11 | g << 5 | b

#go all flashy. on the rpi this is slow enough to appreciate.
for r in range(32):
    for g in range(64):
        for b in range(32):
            fb[:] = color(r, g, b)

