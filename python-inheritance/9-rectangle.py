#!/usr/bin/python3
"""
Module for task 9
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Base Geametry """

    def __init__(self, width, height):
        """
        Initialize
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

    def area(self):
        """
        calculate area
        """
        return("{}".format(self.__width * self.__height))

    def __str__(self):
        """
        print area result
        """
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
