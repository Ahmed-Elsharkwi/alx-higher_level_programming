#!/usr/bin/python3
""" get the peak number """


def find_peak(list_of_integers):
    """ find the peak element """
    if list_of_integers is None or len(list_of_integers) == 0:
        return None
    num = 0
    for i in range(len(list_of_integers)):
        if (list_of_integers[i - 1] is None or list_of_integers[
            i] > list_of_integers[i - 1]) and (list_of_integers[
                i] > list_of_integers[i + 1]):
                num = list_of_integers[i]
                break
    if num == 0:
        num = list_of_integers[i]
    return num
