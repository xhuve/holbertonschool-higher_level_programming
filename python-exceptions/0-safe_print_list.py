#!/usr/bin/python3

def safe_print_list(my_list, x):
    try:
        i = 0
        while i < x:
            print(my_list[i], end="")
            i += 1
    except IndexError:
        pass
    print()
    return i
