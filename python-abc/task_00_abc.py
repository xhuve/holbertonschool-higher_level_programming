#!/usr/bin/python3
from abc import ABCMeta, abstractmethod
"""Code i will use to learn about ABC"""

class Animal(metaclass=ABCMeta):
    """An abstract class"""

    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    """A class that inherits from the ABC 'Animal'"""
    
    def sound(self):
        return "Bark"

class Cat(Animal):
    """A class that inherits from the ABC 'Animal'"""
    
    def sound(self):
        return "Meow"