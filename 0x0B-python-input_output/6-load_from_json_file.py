#!/usr/bin/python3
"""function that creates an object"""
import json


def load_from_json_file(filename):
    """creates an object from a JSON file"""
    with open(filename) as f:
        json.load(f)
