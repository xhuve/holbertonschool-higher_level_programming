#!/usr/bin/python3

for first in range(9):
    for second in range(first + 1, 10):
        if (first + second != 17):
            print("{}{}".format(first, second), end=", ")
        else:
            print("{}{}".format(first, second))
