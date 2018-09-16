#!/usr/bin/python3
for alpha in range(122, 96, -1):
    odd = 0
    if alpha % 2:
        odd = 32
    print("{:s}".format(chr(alpha - odd)), end="")
