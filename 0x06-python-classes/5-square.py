#!/usr/bin/python3
"""Defs a class Square"""


class Square:
    """showing a square"""
    def __init__(self, size=0):
        """square class is being initialized
        size - is an arguement that is being passed
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        else:
            if size < 0:
                raise ValueError("size must be >= 0")

            self.__size = size

    @property
    def size(self):
        """Retrieving the size of square"""

        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """
        Calculate area of the square
        Returns: The square of the size
        """
        return (self.__size ** 2)

    def my_print(self):
        """print the square in # """

        if self.__size == 0:
            print()

        for i in range(self.__size):
            print("#" * self.__size)
