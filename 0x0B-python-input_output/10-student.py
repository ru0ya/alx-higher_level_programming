#!/usr/bin/python3
"""class student that defines a student"""


class Student:
    """represents a student"""
    def __init__(self, first_name, last_name, age):
        """initializes a public instance attribute
        Args:
        first_name (str): The first name of the student.
        last_name (str): The last name of the student.
         age (int): The age of the student.
         """
        self.__first_name = first_name
        self.__last_name = last_name
        self.__age = age

    def to_json(self, attrs=None):
        """Get a dictionary representation of the Student.
        If attrs is a list of strings, represents only those attributes
        included in the list.
        Args:
            attrs (list): (Optional) The attributes to represent"""
        
        if (type(attrs) is list and
                    all(type(ele) == str for ele in attrs)):
                        return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

