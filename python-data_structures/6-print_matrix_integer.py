#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):

    for row in matrix:
        for index in row:
            if index is not row[len(row) - 1]:
                print("{:d}".format(index), end=" ")
            else:
                print("{:d}".format(index), end="")
        print()
