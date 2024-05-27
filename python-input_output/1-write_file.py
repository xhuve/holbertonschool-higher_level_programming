#!/usr/bin/python3
"""Programs to learn IO in python"""


def write_file(filename="", text=""):
    with open(filename, "w") as f:
        f.write(text)
