#!/usr/bin/env python3
import pickle

class CustomObject:
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Is Student:", self.is_student)

    def serialize(self, filename):
        with open(filename, "wb") as f:
            pickle.dump(self.__dict__, f)
    
    @classmethod
    def deserialize(cls, filename):
        with open(filename, "rb") as f:
            result = pickle.load(f)
            return CustomObject(result['name'], result['age'], result['is_student'])
