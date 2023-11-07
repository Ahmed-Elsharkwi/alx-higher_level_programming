#!/usr/bin/python3
"""
writing a module
"""


def write_file(filename="", text=""):
    """
    write text into file and create a file
    if it is not exist or overwite the file
    if it already exist
    """
    with open(filename, 'w', encoding="utf-8") as file:
        number_letter = file.write(text)
    return number_letter
