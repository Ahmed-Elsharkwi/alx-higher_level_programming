#!/usr/bin/python3
"""
divide each element in the matrix by div number
our function will round each number and add it to new_matrix
"""


def matrix_divided(matrix, div):
    """ matrix_divided: divide each element in the matrix """
    Error = "matrix must be a matrix (list of lists) of integers/floats"

    if matrix is None or type(matrix) is not list:
        raise TypeError(Error)
    if type(matrix[0]) is not list:
        raise TypeError(Error)
    length = len(matrix[0])
    for small_list in matrix:
        if len(small_list) != length:
            raise TypeError("Each row of the matrix must have the same size")
        for element in small_list:
            if type(element) is not int and type(element) is not float:
                raise TypeError(Error)
    if type(div) is not int:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[] for _ in range(0, len(matrix))]
    count = 0

    for small_list in matrix:
        for element in small_list:
            new_matrix[count].append(round(element / div, 2))
        count = count + 1
    return new_matrix
