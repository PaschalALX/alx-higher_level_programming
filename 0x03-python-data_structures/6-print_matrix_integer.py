#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return None

    for x in matrix:
        for y in range(len(x)):
            if y >= len(x) - 1:
                print("{:d}".format(x[y]))
            else:
                print("{:d}".format(x[y]), end=" ")
