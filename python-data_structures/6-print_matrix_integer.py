#!/usr/bin/python3

def print_matrix_integer(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i]) - 1):
            print("{:d}".format(matrix[i][j]), end=" ")
        if(len(matrix[i]) == 1):
            j = -1
        print("{:d}".format(matrix[i][j + 1]))

matrix = [
    [1]
]
print_matrix_integer(matrix)
