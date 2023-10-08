#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return my_list
    my_list_2 = []
    for i in range(0, len(my_list)):
        if i == idx:
            my_list_2.append(element)
        else:
            my_list_2.append(my_list[i])
    return my_list_2
