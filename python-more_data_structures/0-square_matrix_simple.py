#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = [[k for k in matrix[i]] for i in range(len(matrix))]
    for i in range(len(new_matrix)):
        new_matrix[i] = list(map(lambda x: x**2, new_matrix[i]))
    return new_matrix
