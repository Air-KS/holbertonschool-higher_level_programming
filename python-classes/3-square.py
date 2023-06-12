#!/usr/bin/python3
"""
based on 0-square.py
"""


class Square:
    """A Square classs"""

    def __init__(self, size=0):
        """
        Initialize the Square

        Args:
        size (int): The size of the square"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the area of the square"""
        return (self.__size ** 2)
