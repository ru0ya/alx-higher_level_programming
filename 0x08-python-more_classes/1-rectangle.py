#!/usr/bin/python3
class Rectangle:
    """defines a class rectangle"""
    def __init__(self, width=0, height=0):
        """initializes class rectangle
        Args:
            width: width of rectangle
            height: height of rectangle
            Raises:
                TypeError: if width and height is not integer
                ValueError: if width and height is not integer"""
        self.width = width
        self.height = height

    @property

    def width(self):
        """retrieves attribute width"""
        return self.__width
    @width.setter
    def width(self, value):
        """sets width attribute"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """retrieves  attribute height"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets height attribute"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
