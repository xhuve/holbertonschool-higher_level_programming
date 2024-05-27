#!/usr/bin/python3
"""Programs to learn IO in python"""
import json


def save_to_json_file(my_obj, filename):
    f = open(filename, "w")
    return json.dump(my_obj, f)
