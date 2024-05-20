#!/usr/bin/python3
"""Python program to add 2 integers"""


def add_integer(a, b=98):
    """ Function to add 2 integers

    Args:
        a (int): an int
        a (int): another int, defaults to 98

    Returns:
        The sum of the two numbers.
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")

    return int(a + b)
