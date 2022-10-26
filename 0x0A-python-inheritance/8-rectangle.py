#!/usr/bin/python3
"""contains class BaseGeometry and subclass Rectangle"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """a representation of a rectangle"""
    def __init__(self, width, height):
        """instatiation of a rectangle"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
