#!/usr/bin/python3

def no_c(my_string):
    s = ""

    if my_string.count("c") == 0 and my_string.count("C") == 0:
        return new_string
    new_string = [char for char in my_string if char != "c" and char != "C"]
    return s.join(new_string)
