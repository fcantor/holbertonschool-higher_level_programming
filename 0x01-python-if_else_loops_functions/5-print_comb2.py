#!/usr/bin/python3
for n in range(0, 100):
    if n == 99:
        print("{:d}\n".format(n))
    else:
        print("{:d}, ".format(n), end="")
