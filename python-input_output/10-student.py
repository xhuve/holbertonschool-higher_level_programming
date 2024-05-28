#!/usr/bin/python3
"""Programs to learn IO in python"""


class Student():
    def __init__(self, first_name, last_name, age):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__age = age

    def to_json(self, attrs=None):
        dictionary = {
            "first_name": self.__first_name,
            "last_name": self.__last_name,
            "age": self.__age
        }

        if attrs is None:
            return dictionary

        wanted_dict = {}
        for attr in attrs:
            if attr in dictionary:
                wanted_dict[attr] = dictionary[attr]
        return wanted_dict
