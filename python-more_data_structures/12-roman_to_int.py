#!/usr/bin/python3

def roman_to_int(roman_string):
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
    i = len(roman_string) -1 
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

# roman_number = "X"
# print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "VII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "IX"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "LXXXVII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "DCCVII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))
