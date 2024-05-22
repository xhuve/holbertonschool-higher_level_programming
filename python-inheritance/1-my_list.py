#!/usr/bin/python3
"""Programs that i am using to learn inheritance more in depth"""


class MyList(list):
    """A list object, in essence a list"""

    def print_sorted(self):
        """A function that prints an sorted list

            Return:
                List containing variables and attributes
        """

        sorted_list = sorted(self)
        print(sorted_list)
        return sorted_list
