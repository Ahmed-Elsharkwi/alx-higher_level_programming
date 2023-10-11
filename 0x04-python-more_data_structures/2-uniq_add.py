#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = []
    sum = 0
    indcat = 0
    for i in my_list:
        for n in new_list:
            if n == i:
                indcat = 1
                break
            else:
                indcat = 0
        if indcat == 0:
            new_list.append(i)
            sum += i
    return sum
