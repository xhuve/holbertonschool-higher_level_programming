#!/usr/bin/python3

def max_integer(my_list):
    if not my_list:
        maximum = None
    else:
        maximum = my_list[0]
    for num in my_list:
        if num > maximum:
            maximum = num

    return (maximum)
