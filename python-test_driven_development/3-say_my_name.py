#!/usr/bin/python3
"""Python program to add 2 integers"""


def say_my_name(first_name, last_name=""):
    """ Function to divide values in a matrix

    Args:
        matrix (list): a list
        div (int): divider

    Returns:
        Divided list.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    my_name = "My name is"

    print(my_name, first_name, last_name)
