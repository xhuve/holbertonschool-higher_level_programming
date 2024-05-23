#!/usr/bin/python3
"""Programs that i am using to learn inheritance more in depth"""


def inherits_from(obj, a_class):
    """Function exactly like isinstance

        Return:
            What isinstance would return
    """

    return issubclass(type(obj), a_class) and type(obj) is not a_class
