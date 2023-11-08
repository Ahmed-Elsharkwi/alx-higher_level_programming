#!/usr/bin/python3
"""
check is the object is the same type
of the class
"""


def is_same_class(obj, a_class):
    """ check if the obj is instance from the class """
    if obj is None or a_class is None:
        return False
    return isinstance(obj, a_class)
