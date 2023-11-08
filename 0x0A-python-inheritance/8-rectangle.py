#!/usr/bin/python3
"""
class BaseGeometry
"""


class BaseGeometry:
    """ class BaseGeometry"""
    def area(self):
        """ raise an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validate the value """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """ class which is inhirted from BaseGeometry"""
    def __init__(self, width, height):
        """ instantion width height """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
