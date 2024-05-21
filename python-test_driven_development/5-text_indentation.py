#!/usr/bin/python3
"""Python program to add 2 integers"""


def text_indentation(text):
    """Function to print a square

        Args:
            text (str): text that is to be printed

        Return:
            Returns a indented text
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    new_text = text.split()
    for word in new_text:
        print(word, end="")
        if word == new_text[-1]:
            break
        if '.' in word or ':' in word or '?' in word:
            print()
        else:
            print("", end=" ")
