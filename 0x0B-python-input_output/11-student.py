#!/usr/bin/python3
"""
class student
"""


class Student:
    """ class for each student"""

    def __init__(self, first_name, last_name, age):
        """Instantiation with first_name, last_name, age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        that retrieves a dictionary
        representation of a Student instance
        """
        is_okay = True
        dic = {}
        dict_1 = self.__dict__
        if type(attrs) is list:
            for word in attrs:
                if type(word) is not str:
                    is_okay = False
        if type(attrs) is not list:
            is_okay = False
        if is_okay is True:
            for word in attrs:
                if word in dict_1:
                    dic.update({word: dict_1[word]})
            return dic
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """replace the attribute value with the json value"""
        dict_1 = self.__dict__
        for key, item in json.items():
            if key in dict_1:
                dict_1[key] = item
