#!/usr/bin/python3
"""
based on 0-square.py
"""


class Rectangle:
    """A Rectangle classs"""

    def __init__(self, width=0, height=0):
        """
        Initialize the Rectangle

        Args:
            width, (int): The width of the new Rectangle
            height (int): The height of the new Rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter method for the width property"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width mus be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter method for the height property"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
