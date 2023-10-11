#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = [[] for _ in range(0, len(matrix))]
    count = 0
    for num in matrix:
        for i in num:
            i = i ** 2
            new_matrix[count].append(i)
        count = count + 1
    return new_matrix
