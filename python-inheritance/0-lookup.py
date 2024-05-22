#!/usr/bin/python3
"""A program that returns a list of an objects attributes, variables etc"""


def lookup(obj):
    """A function that looks up variables and stuff about an object

        Return:
            List containing variables and attributes
    """
    return dir(obj)
