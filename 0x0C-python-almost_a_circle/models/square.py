#!/usr/bin/python3
"""
class square
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Square inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """
        Call the super class with id, x, y, width and height -
        this super call will use the logic of
        the __init__ of the Rectangle class.
        The width and height must be assigned to the value of size
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ return the instance of the class square"""
        return "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """ get the size of the square"""
        return self.width

    @size.setter
    def size(self, size):
        """ set the size of the square """
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """ update the size """
        args_1 = []
        dictionary = {}
        for arg in range(0, len(args)):
            args_1.append(args[arg])
            if arg == 1:
                args_1.append(args[arg])

        for key, value in kwargs.items():
            if key == "size":
                dictionary.update(width=value, height=value)

            else:

                dictionary.update({key: value})
        Rectangle.update(self, *args_1, **dictionary)

    def to_dictionary(self):
        """  returns the dictionary representation of a Square"""
        return {'x': self.x, 'y': self.y, 'size': self.width, 'id': self.id}
