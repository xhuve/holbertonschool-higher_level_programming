#!/usr/bin/python3
"""Programs to learn IO in python"""


class Student():
    def __init__(self, first_name, last_name, age):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__age = age

    def to_json(self):
        return {
            "first_name": self.__first_name,
            "last_name": self.__last_name,
            "age": self.__age
        }
