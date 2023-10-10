#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for colu in row:
            if colu == row[-1]:
                print('{:d}'.format(colu), end='')
            else:
                print('{:d}'.format(colu), end=' ')
        print()
