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
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except Exception:
            return None
    
    @classmethod
    def deserialize(cls, filename):
        try:
            with open(filename, "rb") as f:
                result = pickle.load(f)
                return result
        except Exception:
            return None
