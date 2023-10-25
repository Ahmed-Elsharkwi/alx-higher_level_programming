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
    ''' function check_1 will check if the elements in the tuple
    are 2 positive integers'''
    def check_1(tup):
        if len(tup) != 2 or type(tup[0]) is not int or type(tup[1]) is not int:
            raise TypeError('position must be a tuple of 2 positive integers')
        if tup[0] < 0 or tup[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
    '''function which will check if size int or not
    and it will check if the size is less than 0
    assign the value of size to size of the square '''
    def __init__(self, size=0, position=(0, 0)):
        Square.check(size)
        Square.check_1(position)
        self.__position = position
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
    ''' position function will return the tuple position'''
    @property
    def position(self):
        return self.__position
    '''position setter will set the elements inside position tuple'''
    @position.setter
    def position(self, value):
        Square.check_1(value)
        index = 0

        for i in value:
            self.__position[index] = i
            index = index + 1
    '''my_print function will print the area of the square wiht #'''
    def my_print(self):
        if self.__size != 0:
            incat = 0
            area = self.area()
            size_1 = self.__size

            for i in range(self.__position[1]):
                print()
            while size_1 <= area:
                counter = 0
                print(" "*self.__position[0], end="")
                while counter < self.__size:
                    incat = 1
                    print("#", end="")
                    counter = counter + 1
                size_1 = size_1 + self.__size
                print()
        else:
            print()
    def __str__(self):
        self.my_print()
        return str()
