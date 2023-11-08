#!/usr/bin/python3
"""
check if the object is an instance of, or if the object is
an instance of a class that inherited from, the specified class
"""


def inherits_from(obj, a_class):
    """ check if the obj is instance from the class """
    if type(obj) != a_class:
        return isinstance(obj, a_class)
    return False
