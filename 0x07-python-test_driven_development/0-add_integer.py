#!/usr/bin/python3
"""
add_integer is a module which will add two integer
Both integers should be the type of int
and both var should not be None
if any varible is not integer our program will raise an error"""


def add_integer(a, b=98):
    """ add integer is the function
    which will add two integer to each other
    """
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    if a is None or type(a) is not int:
        raise TypeError("a must be an integer")
    if b is None or type(b) is not int:
        raise TypeError("b must be an integer")
    return a + b
