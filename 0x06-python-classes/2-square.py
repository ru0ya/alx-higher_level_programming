#!/usr/bin/python3
"""defines a class square"""


class Square:
    """defines a square"""
    def __init__(self, size=0):
        """
        defines size instance
        size - an argument that is being passed
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        else:
            if size < 0:
                raise ValueError("size must be >= 0")

            self.__size = size
