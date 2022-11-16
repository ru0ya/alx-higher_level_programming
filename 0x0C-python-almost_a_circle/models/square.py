#!/usr/bin/python3
""" 
class square that inherits from class Rectangle
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """initializes a square"""
    def __init__(self, size, x=0, y=0, id=None):
        """calls the super class values and reassigns them"""
        self.size = size
        self.x = x
        self.y = y
        self.id = None
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """gets the value of size"""
        return self.__width
    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be greater than zero")

        self.__width = value
        self.__height = value
        

    def __str__(self):
        """a string representation of the square"""
        return ("[Square] {:d}/{:d} - {:d}".format(self.x, self.y, self.size))
    


    def update(self, *args, **kwargs):
        """   """
        if args is not None and len(args) != 0:
            if len(args) >= 1:
                if type(args[0]) != int and args[0] is not None:
                    raise TypeError("id must  be an integer")
                self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]

        else:
            for key, value in kwargs.items():
                if key == "id":
                    if type(value) != int and value is not None:
                        raise TypeError("id must be an integer")
                    self.id = value
                if key == "size":
                    self.size = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value
    def to_dictionary(self):
        my_dict = {'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y}
        return my_dict


