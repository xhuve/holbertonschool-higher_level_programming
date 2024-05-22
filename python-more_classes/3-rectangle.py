#!/usr/bin/python3
"""Program that creates a rectangle class"""


class Rectangle:
    """ A rectangle class """

    def __init__(self, width=0, height=0):
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
        for _ in range(self.height):
            image += "#" * self.width
            image += "\n"
        return image

my_rectangle = Rectangle(2, 4)
print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))

print(str(my_rectangle))
print(repr(my_rectangle))

print("--")

my_rectangle.width = 10
my_rectangle.height = 3
print(my_rectangle)
print(repr(my_rectangle))
