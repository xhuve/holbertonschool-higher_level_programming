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
