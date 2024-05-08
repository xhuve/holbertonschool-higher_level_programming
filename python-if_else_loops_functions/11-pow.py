#!/usr/bin/python3

def pow(a, b):
    res = 1
    for _ in range(b):
        res = res * a
    return res
