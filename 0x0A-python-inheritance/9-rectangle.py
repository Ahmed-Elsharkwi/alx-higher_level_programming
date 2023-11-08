#!/usr/bin/python3
"""
class BaseGeometry
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ class which is inhirted from BaseGeometry"""
    def __init__(self, width, height):
        """ instantion width height """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ calculate the area """
        return self.__width * self.__height

    def __str__(self):
        """ return a string """
        return f"[Rectangle] {self.__width}/{self.__height}"
