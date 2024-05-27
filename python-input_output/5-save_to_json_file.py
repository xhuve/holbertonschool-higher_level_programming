#!/usr/bin/python3
"""Programs to learn IO in python"""
import json


def save_to_json_file(my_obj, filename):
    """Save json to file"""
    with open(filename, "w") as f:
        return json.dump(my_obj, f)
