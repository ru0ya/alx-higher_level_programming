#!/usr/bin/python3
"""class that inerits from another   """

Rectangle = __import__('9-rectangle.py').Rectangle

def __init__(self, size):
    """initializes size"""
    self.integer_validator("size", size)
    self.__size = size

    def area(self):
        """calculates area of a square"""
        return self.__size ** 2
    def __str__(self):
        """informal means of printing square"""
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)


