#!/usr/bin/python3
"""
check if the object is an instance of, or if the object is
an instance of a class that inherited from, the specified class
"""


def is_kind_of_class(obj, a_class):
    """ check if the obj is instance from the class """
    return isinstance(obj, a_class)
