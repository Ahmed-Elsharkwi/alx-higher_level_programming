#!/usr/bin/python3
"""
returns the list of Available attributes
"""


def lookup(obj):
    """  returns the list of available attributes and methods of an object"""

    return list(obj.__dict__)
