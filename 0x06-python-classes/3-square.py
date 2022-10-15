#!/usr/bin/python3
"""defines a class square"""

class Square:

    def __init__(self, size=0):
        """instantiates size"""
        if not isinstance(size, int):
            """checks if size is an integer value"""
            raise TypeError("size must be an integer")
        else:
            if size < 0:
                """checks if size is less than 0"""
                raise ValueError("size must be >= 0")

            self.__size = size

    def area(self):
        """calculates the area of a square"""

        return (self.__size ** 2)


