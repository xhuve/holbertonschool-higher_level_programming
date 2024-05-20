#!/usr/bin/python3
"""Python program to add 2 integers"""


def matrix_divided(matrix, div):
    """ Function to divide values in a matrix

    Args:
        matrix (list): a list
        div (int): divider

    Returns:
        Divided list.
    """
    string = "matrix must be a matrix (list of lists) of integers/floats"
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if matrix is list:
        raise TypeError(string)
    if not isinstance(matrix[0], list):
        raise TypeError(string)
    if not all(isinstance(val, int) or
               isinstance(val, float) for row in matrix for val in row):
        raise TypeError(string)
    if len(matrix) > 1:
        if all((len(row) != len(matrix[0]) for row in matrix[1:])):
            raise TypeError("Each row of the matrix must have the same size")

    div_matrix = [[round(value / div, 2) for value in row] for row in matrix]

    return div_matrix
