#!/usr/bin/python3
"""defines a class Rectangle"""


class Rectangle:
    """represents a class rectangle"""
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
        """retrieves  attribute height"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets height attribute"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__width = value

    @property
    def height(self):
        """retrieves attribute width"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets width attribute"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__height = value

    def area(self):
        """returns area of rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """returns perimeter of rectangle"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width + self.__height) * 2)

    def __str__(self) -> str:
        """draws a diagram of rectangle defined in object"""
        if self.__width == 0 or self.__height == 0:
            return ("")
        rectangle = ""
        for i in range(self.__height):
            for j in range(self.__width):
                rectangle += "#"
            if i < self.__height - 1:
                rectangle += "\n"
        return (rectangle)

    def __repr__(self):
        """returns rectangle in string format"""
        return "Rectangle ({:d}, {:d}" .format(self.__width, self.__height)
