#!/usr/bin/python3
"""
create an Object from JSON function
"""
import json


def load_from_json_file(filename):
    """
    create an Object from JSON function
    """
    with open(filename, 'r', encoding="utf-8") as file:
        data = json.load(file)
    return data
