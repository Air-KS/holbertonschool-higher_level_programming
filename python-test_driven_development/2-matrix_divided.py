#!/usr/bin/python3
"""
Module 2-matrix_divided
Contains method that divides all elements of a matrix and returns new matrix
"""


def matrix_divided(matrix, div):
    """
    Returns new matrix with dividends
    """
    error = {
        "matrix": "matrix must be a matrix (list of lists) of integers/floats",
        "div": "div must be a number",
        "zero": "division by zero",
        "row": "Each row of the matrix must have the same size"
    }

    if not isinstance(div, (int, float)):
        raise TypeError(error["div"])

    if div == 0:
        raise ZeroDivisionError(error["zero"])

    # Boucle la matrice pour vérifié son contenu
    for content in matrix:
        if len(content) is not len(matrix[0]):
            raise TypeError(error["row"])

    for element in content:
        if not isinstance(element, (int, float)):
            raise TypeError(error["zero"])

    newList = map(lambda x: list(map(lambda y: round(y / div, 2), x)), matrix)
    return list(newList)
