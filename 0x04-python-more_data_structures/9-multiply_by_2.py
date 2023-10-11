#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dic = {}
    for key, value in a_dictionary.items():
        value = value * 2
        new_dic.update({key: value})
    return new_dic
