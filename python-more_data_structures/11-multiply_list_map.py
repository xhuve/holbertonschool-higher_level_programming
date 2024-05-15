#!/usr/bin/python3

def multiply_list_map(my_list, number):
    new_list = list(map(lambda x: x * number, my_list))
    return new_list

my_list = [1, 2, 3, 4, 6]
new_list = multiply_list_map(my_list, 4)
print(new_list)
print(my_list)