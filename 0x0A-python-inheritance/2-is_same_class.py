#!/usr/bin/python3
"""checks is object is an instance of specified class"""

def is_same_class(obj, a_class):
    """Returns:True - if is an instance of object 
    False - otherwise
    """
    
    return (type(obj) == a_class)
