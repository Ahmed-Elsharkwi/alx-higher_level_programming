#!/usr/bin/python3
def add_integer(a, b=98):

    if type(a) == float:
        a = int(a)
    if type(b) == float:
        b = int(b)
    if (a is None and b is None) or (type(a) != int and type(b) != int):
        raise TypeError("a must be an integer and b must be an integer")
    if a is None or type(a) != int:
        raise TypeError("a must be an integer")
    if b is None or type(b) != int:
        raise TypeError("b must be an integer")
    return a + b
