#!/usr/bin/python3
"""
draw the pasical triginal
"""


def pascal_triangle(n):
    """ make the pasical triginal """
    lists = []
    arr = []
    if n <= 0:
        return lists
    res = 0
    for i in range(1, n+1):
        list = []
        list.append(1)
        if i != 1:
            for j in range(0, len(arr)):
                res = j + 1
                if res is not len(arr):
                    list.append(arr[j] + arr[res])
            list.append(1)
        arr = list.copy()
        lists.append(list)
    return lists
