#!/usr/bin/python3
"""
Rectangle is an inherited class from Base class
"""
from models.base import Base


class Rectangle(Base):
    """ Rectangle is an inherited class from Base class """
    def check_width(width):
        """ check the width """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")

    def check_height(height):
        """ check the height """
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")

    def check_x(x):
        """ check x """
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")

    def check_y(y):
        """ check x """
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        assign all of those argrument to thier private attributes
        except id is a puplic attribute
        """
        Rectangle.check_width(width)
        Rectangle.check_height(height)
        Rectangle.check_x(x)
        Rectangle.check_y(y)

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """get the width """
        return self.__width

    @width.setter
    def width(self, width):
        """ set width """
        Rectangle.check_width(width)
        self.__width = width

    @property
    def height(self):
        """ get the height """
        return self.__height

    @height.setter
    def height(self, height):
        """ set the height """
        Rectangle.check_height(height)
        self.__height = height

    @property
    def x(self):
        """ get the x """
        return self.__x

    @x.setter
    def x(self, x):
        """ set the x """
        Rectangle.check_x(x)
        self.__x = x

    @property
    def y(self):
        """ get the y """
        return self.__y

    @y.setter
    def y(self, y):
        """ set the y """
        Rectangle.check_y(y)
        self.__y = y

    def area(self):
        """ calculate the area of the rectangle"""
        return self.__width * self.__height

    def display(self):
        """ display the area of the rectangle with #"""
        for line in range(0, self.__height):
            for symbol in range(0, self.__width):
                print("#", end="")
            print()

    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
                self.id, self.__x, self.__y, self.__width, self.__height)
