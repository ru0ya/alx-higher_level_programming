#!/usr/bin/python3
"""function to write string to text file"""



def write_file(filename="", text=""):
    """writes a string to a text file"""
    with open(filename, "w", encoding="utf-8") as f:
        print(f.write(text))
