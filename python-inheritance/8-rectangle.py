#!/usr/bin/python3
"""
Module for task 8
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
