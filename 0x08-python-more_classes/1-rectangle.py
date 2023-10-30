#!/usr/bin/python3
"""
module of class Rectangle
"""


class Rectangle:
    """
    class Rectangle wich will calculate the area of that shape
    first thing set the width and the height of that rectangle
    """
    def __init__(self, width=0, height=0):
        """ set the width and height of the Rectangele"""
        self.__width = width
        self.__heigth = height

    @property
    def width(self):
        """ return the value of width """
        return self.__width

    @width.setter
    def width(self, value):
        """ set the value of width """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ return the value of height """
        return self.__height

    @height.setter
    def height(self, value):
        """ set the value of height """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
