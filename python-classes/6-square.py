#!/usr/bin/python3
"""A square class that represents an actual square"""


class Square:
    """ An empty square class

        Args:
            size (int): The size of the square

    """

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square"""
        try:
            if not isinstance(value, int):
                raise TypeError("size must be an integer""")
            elif value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
        except TypeError:
            raise
        except ValueError:
            raise

    @property
    def position(self):
        """Get the position of the square"""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square"""
        string = "position must be a tuple of 2 positive integers"
        try:
            if not isinstance(value, tuple) or len(value) != 2:
                raise TypeError(string)
            if not isinstance(value[0], int) or not isinstance(value[1], int):
                raise TypeError(string)
            if value[0] < 0 or value[1] < 0:
                raise TypeError(string)
            else:
                self.__position = value
        except TypeError:
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
            A square made of # with the width and height of the size
            property along with spaces to fit the requested position
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
