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

    @classmethod
    def save_to_file(cls, list_objs):
        """ save some content to a file """
        list = []
        name = cls.__name__ + ".json"

        with open(name, 'w', encoding="utf-8") as file:
            if list_objs is None:
                file.write("[]")
            else:
                for obj in list_objs:
                    obj = obj.to_dictionary()
                    list.append(obj)
                list = Base.to_json_string(list)
                file.write(list)

    @staticmethod
    def from_json_string(json_string):
        """
        returns the list of the JSON string
        representation json_string
        """
        json_1 = json_string
        if json_1 is None or json_1 == "[]" or json_1 == "[{}]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ returns an instance with all attributes already set:"""
        if dictionary is not None or dictonary != {}:
            if cls.__name__ == "Square":
                dummy = cls(2, 4, 5, 6)
            else:
                dummy = cls(2, 4, 5, 8, 9)
            dummy.update(**dictionary)
            return dummy
