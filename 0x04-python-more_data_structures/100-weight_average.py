#!/usr/bin/python3
def weight_average(my_list=[]):
    sum = 0
    res = 0
    if my_list is None:
        return 0
    for l in my_list:
        sum += l[0] * l[1]
        res += l[1]
    return sum / res
