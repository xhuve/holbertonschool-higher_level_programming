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
    if type(div) not in [int, float]:
        raise TypeError("Div must be a number")
    if type(matrix) != list:
        raise TypeError("Matrix must be a matrix (list of lists) of integers/floats")
    if not isinstance(matrix[0], list):
        raise TypeError("Matrix must be a matrix (list of lists) of integers/floats")
    if not all(isinstance(value, int) or isinstance(value, float) for row in matrix for value in row):
        raise TypeError("Matrix must be a matrix (list of lists) of integers/floats")
    if all((len(row) != len(matrix[0]) for row in matrix[1:])):
        raise TypeError("Each row of the matrix must have the same size")

    div_matrix = [[round(value / div, 2) for value in row] for row in matrix]

    return div_matrix
