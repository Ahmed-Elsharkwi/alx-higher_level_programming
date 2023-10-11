#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    for key_1 in a_dictionary:
        if key_1 == key:
            del a_dictionary[key]
            break
    return a_dictionary
