#!/usr/bin/python3
"""Programs that i am using to learn inheritance more in depth"""


class BaseGeometry(object):
    """A geometry class containing simple geometrical operations"""

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
        return value


class Rectangle(BaseGeometry):
    """A rectangle class inheriting from BaseGeometry"""

    def __init__(self, width, height):
        self.__width = super().integer_validator("width", width)
        self.__height = super().integer_validator("height", height)

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return f"[{self.__class__.__name__}] {self.__width}/{self.__height}"
