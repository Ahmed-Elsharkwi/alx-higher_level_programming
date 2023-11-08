#!/usr/bin/python3
"""
class square which is inherits from Rectangle
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ class square """
    def __init__(self, size):
        """ instantiation size """
        super().integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """ return string """
        return f"[Square] {self.__size}/{self.__size}"

    def area(self):
        """ calculate the area of the square """
        return self.__size * self.__size
