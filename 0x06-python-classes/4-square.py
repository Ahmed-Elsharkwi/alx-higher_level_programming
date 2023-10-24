#!/usr/bin/python3
''' class Square has one attrupite which is the size of '''


class Square:
    '''function check will check if the value is int
    and it also check if the value is less than zero'''
    def check(value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
    '''function which will check if size int or not
    and it will check if the size is less than 0
    assign the value of size to size of the square '''
    def __init__(self, size=0):
        Square.check(size)
        self.__size = size
    '''function which will return the value of area of the square'''
    def area(self):
        return self.__size * self.__size
    '''property size which will return the value of the size of the square'''
    @property
    def size(self):
        return self.__size
    '''size setter which will set the size of the square'''
    @size.setter
    def size(self, value):
        Square.check(value)
        self.__size = value
