import numpy as np

#memory map the framebuffer as a numpy array
#1440, 900 as shape as that is the res of my display
#uint16 - 16 bit values for color
fb = np.memmap('/dev/fb1', mode='w+', dtype='uint16', shape=(1440, 900))

#array with the same shape - will be cast on assignment to uint16! no worries
black = np.zeros((1440, 900))

#reasonably fast
fb[:] = black