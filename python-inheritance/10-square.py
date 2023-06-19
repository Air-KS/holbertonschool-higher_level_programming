#!/usr/bin/python3
"""
Module for task 10
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Square(BaseGeometry):
    """ Base Geametry """

    def __init__(self, size):
        """
        Initialize
        """
        self.integer_validator("size", size)
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
        return ("[Rectangle] {}/{}".format(self.__size, self.__size))
