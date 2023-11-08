#!/usr/bin/python3
"""
check is the object is the same type
of the class
"""


def is_same_class(obj, a_class):
    """ check if the obj is instance from the class """
    if type(obj) is a_class:
        return True
    return False
