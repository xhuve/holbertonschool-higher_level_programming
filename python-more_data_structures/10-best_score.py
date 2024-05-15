#!/usr/bin/python3

def best_score(a_dictionary):
    if not a_dictionary:
        return None
    value = list(a_dictionary.values()).index(max(a_dictionary.values()))
    return list(a_dictionary.keys())[value]
