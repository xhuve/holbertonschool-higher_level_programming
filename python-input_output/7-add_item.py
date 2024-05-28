#!/usr/bin/python3
"""Programs to learn IO in python"""
from sys import argv
from os.path import exists
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

if __name__ == '__main__':
    my_list = []
    if exists("add_item.json"):
        my_list = load_from_json_file("add_item.json")
    for arg in argv[1:]:
        my_list.append(arg)
    save_to_json_file(my_list, "add_item.json")
