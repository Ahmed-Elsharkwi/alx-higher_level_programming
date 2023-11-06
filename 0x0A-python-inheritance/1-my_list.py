#!/usr/bin/python3
"""
inhert a class from the list class
"""

class MyList(list):
    """
    My list in a inherted class from list class
    """
    def print_sorted(self):
        print(sorted(self))
