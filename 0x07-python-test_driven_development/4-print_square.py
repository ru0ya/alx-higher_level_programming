#!/usr/bin/python3
"""defines a square #"""


def print_square(size):
    """prints a square with the character #.
    args:
    size int: prints sides of a square
    raise:
    TypeError if size is not an integer
    ValueError if size is less than 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        [print("#", end="") for b in range(size)]
        print("")
