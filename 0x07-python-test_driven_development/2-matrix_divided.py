#!/usr/bin/python3
"""
    standard math module
"""
import math


def matrix_divided(matrix, div):
    """
    Function that returns the sum of tow integers or floats numbers

    Raises:
        TypeError: Matrix must be a matrix (list of lists) of integers/floats
        TypeError: Each row of the matrix must have the same size
        TypeError: div must be a number
        ZeroDivisionError: division by zero
    """
    err = "Matrix must be a matrix (list of lists) of integers/floats"
    if not all(isinstance(row, list) and all(isinstance(val, (int, float))
       for val in row) for row in matrix):
        raise TypeError(err)
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError('div must be a number')

    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = [[]]
    for row in matrix:
        i = 0
        for x in row:
            new_matrix[0].append(round((x / div), 2))
        i += 1
    return (new_matrix)
