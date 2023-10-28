#!/usr/bin/python3
"""
print the name of the user and that name is composed of
(first name), (last name)
example: My name is Ahmed Elsharkway
"""


def say_my_name(first_name, last_name=""):
    """ print the first name and last name of the user"""

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
