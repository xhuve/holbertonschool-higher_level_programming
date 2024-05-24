#!/usr/bin/python3
from abc import ABCMeta, abstractmethod
import math
"""Code i will use to learn about ABC"""

class Shape(metaclass=ABCMeta):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):

    def __init__(self, radius):
        self.__radius = radius

    def area(self):
        return math.pi * (self.__radius ** 2) 
    
    def perimeter(self):
        return 2 * math.pi * abs(self.__radius) 

class Rectangle(Shape):

    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height
    
    def perimeter(self):
        return 2 * (self.__width + self.__height)

def shape_info(shape):
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
