#!/usr/bin/python3
from abc import ABCMeta, abstractmethod
"""Code i will use to learn about ABC"""

class VerboseList(list):

    def append(self, value):
        super().append(value)
        print(f"Added {value} to the list.")

    def extend(self, list):
        super().extend(list)
        print(f"Extended the list with {len(list)} items.")

    def remove(self, value):
        super().remove(value)
        print(f"Removed {value} from the list.")    
    
    def pop(self, value):
        super().pop(value)
        print(f"Popped {value} from the list.")
