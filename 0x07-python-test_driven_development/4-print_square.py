#!/usr/bin/python3
"""
print the are of a sqaure with # sympol
if number is negative or less than zero rasie an error
"""


def print_square(size):
    """print_sqare with #"""
    Error = "size must be an integer"
    if size is None:
        raise TypeError(Error)
    if (type(size) is not int and type(size) is not float):
        raise TypeError(Error)
    if (type(size) is float and size < 0):
        raise TypeError(Error)
    if int(size) < 0:
        raise ValueError("size must be >= 0")

    size = int(size)

    for i in range(0, size):
        for _ in range(0, size):
            print("#", end="")
        print()
    print()
