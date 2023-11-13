#!/usr/bin/python3
"""
create a base class
"""
import json


class Base:
    """ class base which has some useful methods """
    nb_objects = 0

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
            Base.nb_objects += 1
            self.id = Base.nb_objects
    @staticmethod
    def to_json_string(list_dictionaries):
        """ convert the list_dictionaries to json string """
        li = list_dictionaries
        if li is None or li == [] or li == [{}]:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
