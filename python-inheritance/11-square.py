#!/usr/bin/python3
"""
Module for task 10
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Base Geametry """

    def __init__(self, size):
        """
        Initialize
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        calculate area / size
        """
        return ("{}".format(self.__size * self.__size))

    def __str__(self):
        """
        print area result
        """
        return ("[Square] {}/{}".format(self.__size, self.__size))
