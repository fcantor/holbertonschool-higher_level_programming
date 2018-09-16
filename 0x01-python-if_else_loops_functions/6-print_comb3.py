#!/usr/bin/python3
for n in range(0, 9):
    for i in range(n + 1, 10):
        if n < 8:
            print("{:d}{:d}, ".format(n, i), end="")
        else:
            print("{:d}{:d}".format(n, i))
