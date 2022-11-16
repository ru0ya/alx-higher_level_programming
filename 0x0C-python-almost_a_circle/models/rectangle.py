#!/usr/bin/python3
"""contains the class 'Rectangle'"""



from models.base import Base



class Rectangle(Base):
    """representation of a rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """initializes the rectangle"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """getter of width"""
        return self.__width

    @property
    def height(self):
        """getter of height"""
        return self.__height

    @property
    def x(self):
        """getter of x"""
        return self.__x

    @property
    def y(self):
        """getter of y"""
        return self.__y



    @width.setter
    def width(self, value):
        """setter of width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be greater than zero")
        self.__width = value

    @height.setter
    def height(self, value):
        """setter of height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be an integer")
        self.__height = value

    @x.setter
    def x(self, value):
        """setter of x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be greater than zero")
        self.__x = value

    @y.setter
    def y(self, value):
        """setter of y"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be greater than zero")
        self.__y = value

    def area(self):
        """calculates area of rectangle"""
        return self.__width * self.__height

    def display(self):
        """displaying a rectangle in str format using #"""
        for y in range(self.y):
            print("")
        for row in range(self.__height):
            for x in range(self.x):
                print(" ", end="")
            for column in range(self.__width):
                print("#", end="")
            print()
    def __str__(self):
        """string representation of rectangle"""
        return ("[Rectangle] ({:d}) {:d}/{:d} -  {:d}/{:d}".format(self.id, self.__x, self.__y, self.__width, self.__height))

    def update(self, *args, **kwargs):
        """updating the class 'Rectangle'"""
        if len(args):
            for i, a in enumerate(args):
                if i == 0:
                    self.id = a
                elif i == 1:
                    self.width = a
                elif i == 2:
                    self.height = a
                elif i == 3:
                    self.x = a
                elif i == 4:
                    self.x = a
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "width" in kwargs:
                self.width = kwargs["width"]
            if "height" in kwargs:
                self.height = kwargs["height"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]
    def to_dictionary(self):
        my_dict = {'x':self.__x, 'y': self.__y, 'id': self.id, 'height': self.__height, 'width': self.__width}
        return my_dict
