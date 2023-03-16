#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = []
    for sublist in matrix:
        new_sublist = []
        for num in sublist:
            new_sublist.append((num*num))
        new_matrix.append(new_sublist)
    return new_matrix
