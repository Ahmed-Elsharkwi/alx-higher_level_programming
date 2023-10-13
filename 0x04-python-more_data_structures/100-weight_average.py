#!/usr/bin/python3
def weight_average(my_list=[]):
    sum = 0
    res = 0
    if my_list is None:
        return 0
    for i in my_list:
        sum += i[0] * i[1]
        res += i[1]
    return sum / res
