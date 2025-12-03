#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        if len(matrix[i]) == 0:
            print()
        for k in range(len(matrix[i])):
            if k != len(matrix[i]) - 1:
                print("{:d}".format(matrix[i][k]), end=' ')
            else:
                print("{:d}".format(matrix[i][k]), end='\n')
