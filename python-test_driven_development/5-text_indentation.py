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

    i = 0
    while i < len(text):
        print(text[i], end="")
        if text[i] in ['.', ':', '?']:
            if i != len(text) - 1 and text[i + 1] == " ":
                i += 1
            print("\n")

        i += 1
