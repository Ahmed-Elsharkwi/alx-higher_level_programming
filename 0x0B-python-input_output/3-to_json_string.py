#!/usr/bin/python3
"""
deal with serializion of json files
"""


import json


def to_json_string(my_obj):
    """ return the json representation of an object """
    return json.dumps(my_obj)
