#!/usr/bin/python3
"""A square class that represents an actual square"""


class Square:
    """ An empty square class

        Args:
            size (int): The size of the square

    """

    def __init__(self, size=0):
        try:
            if not isinstance(size, int):
                raise TypeError("size must be an integer""")
            elif size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
        except TypeError:
            raise
        except ValueError:
            raise
