#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        k = 1
        for j in i:
            if k == len(i):
                print("{:d}".format(j), end="")
            else:
                print("{:d} ".format(j), end="")
            k = k + 1
        print()
