#!/usr/bin/python3
"""Programs that i am using to learn inheritance more in depth"""


class BaseGeometry(object):
    """A geometry class containing simple geometrical operations"""

    def area(self):
        raise Exception("area() is not implemented")
