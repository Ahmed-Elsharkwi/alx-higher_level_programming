#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    new_list = []
    for key, value_1 in a_dictionary.items():
        new_list.append(value)
    for value_1 in new_list:
        for key in a_dictionary:
            if a_dictionary[key] == value:
                del a_dictionary[key]
                break
    return a_dictionary
