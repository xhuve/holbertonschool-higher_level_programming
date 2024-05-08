#!/usr/bin/python3

def pow(a, b):
    res = 1
    if b > 0:
        for _ in range(b):
            res = res * a
        return res
    else:
        for _ in range(b * -1):
            res = res / a
        return res

print(pow(10, -2))