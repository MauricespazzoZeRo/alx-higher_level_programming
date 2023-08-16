#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    new_matrix = []
    for row in matrix:
        new_row = []
        for idx in row:
            new_row.append(idx ** 2)

        new_matrix.append(new_row)

    return (result_matrix)
