#!/usr/bin/python3
''' class Square has one attrupite which is the size of '''


class Square:
    '''function which will check if size int or not
    and it will check if the size is less than 0
    assign the value of size to size of the square '''
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
