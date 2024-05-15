#!/usr/bin/python3

def roman_to_int(roman_string):
    if not roman_string or not isinstance(roman_string, str):
        return 0

    roman_symbols = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    total = 0
    i = len(roman_string) - 1
    while i >= 0:
        char = roman_string[i]
        prev = roman_string[i - 1]
        if char in roman_symbols.keys():
            total += roman_symbols[char]
        if roman_symbols[char] > roman_symbols[prev] and i - 1 != -1:
            total = total - roman_symbols[prev]
            i -= 1
        i -= 1

    return total
