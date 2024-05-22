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


my_list = MyList()
my_list.append(1)
my_list.append(4)
my_list.append(2)
my_list.append(3)
my_list.append(5)
print(my_list)
my_list.print_sorted()
print(my_list)
