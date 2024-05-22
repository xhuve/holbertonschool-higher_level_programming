#!/usr/bin/python3
"""Program that creates a rectangle class"""


class Rectangle:
    """ A rectangle class """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        Rectangle.number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    def perimeter(self):
        if self.height == 0 or self.width == 0:
            return 0
        return (self.height + self.width) * 2

    def area(self):
        return self.height * self.width

    def __str__(self):
        image = ""
        if self.height == 0 or self.width == 0:
            return image
        for _ in range(self.height - 1):
            image += str(self.print_symbol) * self.width
            image += "\n"
        image += str(self.print_symbol) * self.width
        return image

    def __repr__(self):
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
