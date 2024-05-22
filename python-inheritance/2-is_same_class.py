#!/usr/bin/python3
"""Programs that i am using to learn inheritance more in depth"""


def is_same_class(obj, a_class):
    """Function exactly like is

        Return:
            What is would return
    """
    obj_type = type(obj)
    return obj_type == a_class
