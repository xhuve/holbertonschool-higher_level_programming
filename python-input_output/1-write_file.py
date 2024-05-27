#!/usr/bin/python3
"""Programs to learn IO in python"""


def write_file(filename="", text=""):
    """Write to a file"""
    with open(filename, "w") as f:
        return f.write(text)
