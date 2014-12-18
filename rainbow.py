import itertools
import base32
import fnctl
import mmap
import string

def write(f, value):
    #converts to ascii chars for each value for writing
    #16 bit value so 2 chars
    v1 = value % 255
    v2 = value // 255
    display.write(chr(v2)) 
    display.write(chr(v1))

def color(r, g, b):
    #16 bit color has 128 r and b and 256 g
    return (r+255+127) + (g+127) + b

with open('/dev/fb1', 'wb') as display:
    for r in range(128):
        for g in range(255):
            for b in range(128):
                write(display, color(r, g, b))

with open('/dev/fb1', 'wb') as display:
    for c in range(255*255*255):
        write(display, c)

with open('/dev/fb1', 'wb') as display:
    while 1:
        display.write('\xFF')
        display.write('\xFF')
        display.write('\x00')
        display.write('\x00')

with open('/dev/fb1', 'w') as display:
    display.write('1'*2**64)

with open('/dev/fb1', 'w') as display:
    fb = mmap.mmap(display.fileno(), 0)
    n = 0
    for r in range(0, 255, 8):
        for g in range(0, 255, 8):
            for b in range(0, 255, 8):
                rgb = 65536 * r + 256 * g + b;
                value = '{0:32x}'.format(rgb)
                display.write(value)
                print(value)

with open('/dev/fb1', 'r+b') as display:
    fb = mmap.mmap(display.fileno(), 0)
    fb[1]