#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    i = 0
    j = 0
    indcat = 0
    tuple_e = ()
    list_a = list(tuple_a)
    list_b = list(tuple_b)
    list_e = list(tuple_e)
    while indcat < 2:
        if i == len(list_a):
            c = 0
        else:
            c = list_a[i]
            i = i + 1
        if j == len(list_b):
            b = 0
        else:
            b = list_b[j]
            j = j + 1
        list_e.append(c + b)
        indcat = indcat + 1
    tuple_e = tuple(list_e)
    return (tuple_e)
