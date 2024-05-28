#!/usr/bin/python3
"""Programs to learn IO in python"""


class Student():
    def __init__(self, first_name, last_name, age):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__

        wanted_dict = {}
        for attr in attrs:
            if attr in self.__dict__:
                wanted_dict[attr] = self.__dict__[attr]
        return wanted_dict
