#!/usr/bin/python3
"""Programs to learn IO in python"""


def read_file(filename=""):
    """Read a file"""
    with open(filename) as f:
        print(f.read(), end="")
