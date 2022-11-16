#!/usr/bin/python3
"""Append to a file"""


def append_write(filename="", text=""):
    """appends a string to the end of a UTF8 text file.
    Args:
        filename(str): name of file to append
        text(str): string to append to file
        Returning number of characters appended
        """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
