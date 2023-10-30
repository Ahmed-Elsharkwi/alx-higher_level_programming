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
        self.width = width
        self.height = height

    @property
    def width(self):
        """ return the value of width """
        return self.__width

    @width.setter
    def width(self, value):
        """ set the value of width """
        if not isinstance(value, int):
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

    def area(self):
        """calculate the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """calculate the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        res = (self.__width * 2) + (self.__height * 2)
        return res

    def __str__(self):
        """ print the area of the rectangle with #"""
        shape = ""
        if self.__width == 0 or self.__height == 0:
            return shape
        for i in range(0, self.__height):
            for j in range(0, self.__width):
                shape += "#"
            if i + 1 != self.__height:
                shape += "\n"
        return shape

    def __repr__(self):
        """should return a string representation of the rectangle
        to be able to recreate a new instance
        """
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """delete the object or the instance"""
        del self
        print("Bye rectangle...")
