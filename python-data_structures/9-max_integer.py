#!/usr/bin/python3

def max_integer(my_list):
    if not my_list:
        maximum = None
    maximum = 0
    for num in my_list:
        if num > maximum:
            maximum = num
    
    return (maximum)
