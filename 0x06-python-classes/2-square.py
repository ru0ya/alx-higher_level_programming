#!/usr/bin/python3
"""defines a class square"""


class Square:
    """defines a square"""
    def __init__(self, size=0):
        """defines size instance"""
        if not isinstance(size, int):
            """checks for errors"""
            raise TypeError("size must be an integer")
        else:
            if size < 0:
                """checks if value is less than zero"""
                raise ValueError("size must be >=0")

            self.__size = size
