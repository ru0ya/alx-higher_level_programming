#!/usr/bin/python3
"""  """

class BaseGeometry:
    def area(self):
        """defines an area of an object"""
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        """validates whether the value is an integer or less than 
        or equal to zero
        name is always a string
        Raises:
        TypeError; if value is not an integer
        ValueError: if value is less than or equal to zero
        """
        if not isinstance(value, int):
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")
