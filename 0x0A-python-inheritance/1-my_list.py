#!/usr/binpython3
"""declaration of a class list"""


class MyList(list):
    """MyList inherits from parent list"""


    def print_sorted(self):
        """printing a sorted list"""
        print(sorted(self))


    
