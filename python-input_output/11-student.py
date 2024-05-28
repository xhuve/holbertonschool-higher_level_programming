#!/usr/bin/python3
"""Programs to learn IO in python"""


class Student():
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        dictionary = {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "age": self.age
        }

        if attrs is None:
            return dictionary

        wanted_dict = {}
        for attr in attrs:
            if attr in dictionary:
                wanted_dict[attr] = dictionary[attr]
        return wanted_dict

    def reload_from_json(self, json):
        if 'first_name' in json:
            self.first_name = json['first_name']
        if 'last_name' in json:
            self.last_name = json['last_name']
        if 'age' in json:
            self.age = json['age']
