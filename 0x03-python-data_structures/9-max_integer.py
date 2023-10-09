#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == "" or my_list == None:
        return None
    count = 1
    for i in range(0, len(my_list)):
        j = 0
        j = i + 1
        temp = my_list[i]
        while j < len(my_list):
            if temp < my_list[j]:
                count = 0
                break
            else:
                count = 1
            j = j + 1
        if count == 1:
            break
    return temp
