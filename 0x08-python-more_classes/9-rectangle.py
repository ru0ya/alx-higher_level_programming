#!/usr/bin/python3
"""defines a class Rectangle"""


class Rectangle:
    """represents a class rectangle"""
    number_of_instances = 0
    print_symbol = "#"

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
        Rectangle.number_of_instances += 1

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
                try:
                    rectangle += str(self.print_symbol)
                except Exception:
                    rectangle += type(self).print_symbol
            if i < self.__height - 1:
                rectangle += "\n"
        return (rectangle)

    def __repr__(self):
        """returns rectangle in string format"""
        return "Rectangle ({:d}, {:d}" .format(self.__width, self.__height)

    def __del__(self):
        """deletes an instance of the class rectangle"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

        @classmethod
        def square(cls, size=0):
            return Rectangle(size, size)
