#!/usr/bin/python3
"""Programs that i am using to learn inheritance more in depth"""

class MyList(list):
    """A list object, in essence a list"""
    my_list = []

    def __init__(self):
        MyList.my_list.append(self)


    def print_sorted(self):
        """A function that prints an sorted list

            Return:
                List containing variables and attributes
        """
        print(sorted(my_list))
