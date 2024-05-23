#!/usr/bin/python3
"""Programs that i am using to learn inheritance more in depth"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class inherited from the Rectangle class"""

    def __init__(self, size):
        super().integer_validator("size", size)
        super().__init__(size, size)
