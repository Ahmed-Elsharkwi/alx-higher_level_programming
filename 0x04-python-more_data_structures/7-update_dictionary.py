#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    indcat = 0
    for key_1 in a_dictionary:
        if key_1 == key:
            a_dictionary[key_1] = value
            indcat = 1
            break
        else:
            indcat = 0
    if indcat == 0:
        a_dictionary.update({key: value})
    return a_dictionary
