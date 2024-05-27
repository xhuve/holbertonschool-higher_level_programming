#!/usr/bin/python3
import json

def save_to_json_file(my_obj, filename):
    f = open(filename, "w")
    return json.dump(my_obj, f)
