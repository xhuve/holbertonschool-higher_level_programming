#!/usr/bin/python3
"""Programs to learn IO in python"""


def append_write(filename="", text=""):
    with open(filename, "a") as f:
        return f.write(text)
