#!/usr/bin/python3
"""Program to create a pascal triangle"""


def pascal_triangle(n):
    """Function that returns a pascal triangle"""

    triangle = [[1]]
    while len(triangle) != n:
        tri = [1]
        tmp = triangle[-1]
        for i in range(len(tmp) - 1):
            tri.append(tmp[i] + tmp[i + 1])
        tri.append(1)
        triangle.append(tri)

    return triangle
