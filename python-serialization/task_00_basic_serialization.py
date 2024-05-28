#!/usr/bin/python3
import json

def serialize_and_save_to_file(data, filename):
    try:
        with open(filename, "w") as f:
            return json.dump(data, f)
    except Exception:
        return None

def load_and_deserialize(filename):
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except Exception:
        return None
