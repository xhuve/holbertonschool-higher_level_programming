#!/usr/bin/python3

def max_integer(my_list):
    maximum = my_list[0]
    if not my_list:
        maximum = None
    for num in my_list:
        if num > maximum:
            maximum = num

    return (maximum)
