#!/usr/bin/python3
import json
"""
deal with serializion of json files
"""


def to_json_string(my_obj):
    """ return the json representation of an object """
    return json.dumps(my_obj)
