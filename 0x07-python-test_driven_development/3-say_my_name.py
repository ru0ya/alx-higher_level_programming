#!/usr/bin/python3
"""defines a name function"""


def say_my_name(first_name, last_name=""):
    """prints name

    first argument: string that prints first name
    second argument: string that prints last name
    raise a TypeError(both must be a string)
    """
    if not isinstance(last_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
