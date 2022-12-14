#!/usr/bin/python3
"""adds two integers"""


def add_integer(a, b=98):
    """args:
    TypeError: a and b  must be an integer or a float
    returns sum of two integers
    """

    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    add = int(a) + int(b)

    return (add)
