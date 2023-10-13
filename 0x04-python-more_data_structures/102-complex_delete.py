#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    new_list = []
    for key in a_dictionary:
        new_list.append(key)
    for key in new_list:
        if a_dictionary[key] == value:
            del a_dictionary[key]
    return a_dictionary
