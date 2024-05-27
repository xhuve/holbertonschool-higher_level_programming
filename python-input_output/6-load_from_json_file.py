#!/usr/bin/python3
"""Programs to learn IO in python"""
import json


def load_from_json_file(filename):
    """Get json from file"""
    with open(filename) as f:
        return json.loads(f)
