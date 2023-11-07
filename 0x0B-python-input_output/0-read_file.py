#!/usr/bin/python3
"""
read a file and print its content
"""


def read_file(filename=""):
    """ read a file and print its content"""
    with open(filename, 'r', encoding="utf-8") as file:
        print(file.read(), end="")
