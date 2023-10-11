#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    new_dic = {}
    for key, value in a_dictionary.items():
        new_dic.update({key:value})
    for i in sorted(new_dic):
        print("{}:{}".format(i, new_dic[i]))
