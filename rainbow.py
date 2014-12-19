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

def create_sprial(size=(1440, 900)):
    array = np.zeros(size) 
    for n in range(100):
        x = int(n*np.cos(n))
        y = int(n*np.sin(n))
        array[x, y] = 2**16
    return array

sprial = np.zeros((1440, 900), dtype='uint16') 
for n in range(100):
    x = int(n*np.cos(n))
    y = int(n*np.sin(n))
    x += 1440/2
    y += 900/2
    sprial[x, y] = 2**16-1


sprial = np.zeros((1440, 900), dtype='uint16') 
for x in np.linspa:
    for y in range(900):
        if int(np.sqrt(x**2 + y**2)) == 100:
            sprial[x, y] = 2**16-1

fb[:] = 

def color(r, g, b):
    return r << 11 | g << 5 | b