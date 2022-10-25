#!/usr/bin/python3
"""checks if object is instance of a 
class inherited directly/indirectly from 
specified class"""

def inherits_from(obj, a_class):
    """Returns: True - if object is an instance of class inherited
    False - otherwise
    """
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
