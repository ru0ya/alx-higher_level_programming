#!/usr/bin/python3
"""checks if object is instance of a parent or child class"""


def is_kind_of_class(obj, a_class):
    """Returns: True - if object is an instance of parent
    or child class
    False - otherwise
    """
    return (isinstance(obj, a_class))
