#!/usr/bin/python3
"""Code i will use to learn about ABC"""

class CountedIterator():

    def __init__(self, iterable):
        self.iterator = iter(iterable)
        self.count = 0
        self.start = 0
    
    def __next__(self):
        next(self.iterator)
        self.start += 1
        self.count += 1
        return self.start

    def get_count(self):
        return self.count
