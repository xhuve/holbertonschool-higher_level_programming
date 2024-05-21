#!/usr/bin/python3
"""Python program to add 2 integers"""


def print_square(size):
    """Function to print a square

        Args:
            size (int): size of the square

        Return:
            Returns a square based on the input size
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    # if isinstance(size, float) and size < 0:

    for _ in range(size):
        for _ in range(size):
            print("#", end="")
        print()
