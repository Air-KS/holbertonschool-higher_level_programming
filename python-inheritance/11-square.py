#!/usr/bin/python3
"""
Module for task 11
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
