#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    i = 0
    print_count = 0
    while i < x:
        try:
            print("{:d}".format(my_list[i]), end="")
            print_count += 1
        except (TypeError, ValueError):
            pass
        except IndexError:
            raise
        i += 1

    print()
    return print_count
