#!/usr/bin/python3
"""
create a base class
"""


class Base:
    """ class base which has some useful methods """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        In case that id is None
        assign to id to the attribute id
        otherwise, increment __nb_objects and
        assign the new value to the public instance attribute id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
