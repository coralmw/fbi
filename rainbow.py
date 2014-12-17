import itertools
import base32

display = open('/dev/fb1', 'wb')

s = 32
while 1:
    for i in range(256):
        display.write(bytes(i))