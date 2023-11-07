#!/usr/bin/python3
"""
deal with deserializion of json files
"""


import json


def from_json_string(my_str):
    """ return the python representation of an object """
    return json.loads(my_str)
