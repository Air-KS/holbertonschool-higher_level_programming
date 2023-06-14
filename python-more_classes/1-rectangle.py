#!/usr/bin/python3
"""
Module 1-Rectangle
Define a Rectangle class
"""


class Rectangle:
    """A Rectangle classs"""

    def __init__(self, width=0, height=0):
        """
        Initialize the Rectangle

        Args:
        width, height (int): The size of the Rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter method for the width property"""
        return (self.__width)

    @property
    def height(self):
        """Getter method for the height property"""
        return (self.__height)

    @width.setter
    def width(self, value):
        """
        Setter method for the width property

        Args:
        value (int): The new value for the width
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width mus be >= 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        """
        Setter method for the height property

        Args:
        value (int): The new value for the height
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
