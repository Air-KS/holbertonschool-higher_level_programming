#!/usr/bin/python3
""" Modul 1 """


def matrix_divided(matrix, div):
    # Create new list

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
