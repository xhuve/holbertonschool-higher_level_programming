#!/usr/bin/python3
"""A square class that represents an actual square"""


class Square:
    """ An empty square class

        Args:
            size (int): The size of the square

    """

    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        """Get the size of the square"""
        return self.__size

    @size.setter
    def size(self, size):
        """Set the size of the square"""
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

    def area(self):
        """ Method to return the area of the square

        Return:
            Pow 2 of the object's size
        """
        return self.__size ** 2

    def my_print(self):
        """ Method to print a square consisting of #

        Return:
            A square made of # with the width and height of the size property
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
