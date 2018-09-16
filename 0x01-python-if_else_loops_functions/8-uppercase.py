#!/usr/bin/python3
def uppercase(str):
    for alpha in str:
        odd = 0
        if ord(alpha) > 96 and ord(alpha) < 123: # if letter is lowercase
            odd = -32
        print("{:s}".format(chr(ord(alpha) + odd)), end='') # print upper
    else:
        print()
