#!/usr/bin/python3
"""
appending to a module
"""


def append_write(filename="", text=""):
    """
    append text into file and create a file
    if it is not exist
    """
    with open(filename, 'a', encoding="utf-8") as file:
        number_letter = file.write(text)
    return number_letter
