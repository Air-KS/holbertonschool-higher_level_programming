#!/usr/bin/python3
"""
based on 6-square.py
"""


class Rectangle:
    """A Rectangle classs"""

    """
        number_of_instances (int): The number of Rectangle instances.
        print_symbol (any): The symbol used for string
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initialize the Rectangle

        Args:
            width, (int): The width of the new Rectangle
            height (int): The height of the new Rectangle
        """
        self.__width = width
        self.__height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """Getter method for the width property"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter method for the height property"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Return the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """
        Affiche le rectangle avec le symbol spécifié
        """
        width, height = self.__width, self.__height
        symbol = self.print_symbol

        if width == 0 or height == 0:
            return ""

        line = str(symbol) * width
        rectangle = line
        for _ in range(height - 1):
            rectangle += "\n" + line
        return (rectangle)

    def __repr__(self):
        """
            Return un string represente if the Rectangle
        """
        width, height = self.__width, self.__height
        return ("Rectangle({}, {})".format(width, height))

    def __del__(self):
        """ Print a message for delete the Rectangle. """
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
