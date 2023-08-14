#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for idx, element in eneumerate(row):
            print("{:d}".format(element))
            if idx < len(row) - 1:
                print(" ")

        print()
