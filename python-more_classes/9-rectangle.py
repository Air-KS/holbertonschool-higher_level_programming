#!/usr/bin/python3
"""
based on 8-square.py
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

    def __del__(self):
        """ Print a message for delete the Rectangle. """
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ Return the Rectangle with the greater area.

        args:
            rect_1 (Rectangle): The first Rectangle.
            rect_2 (Rectangle): The second Rectangle.
        raises:
            If rect_1 or rect_2 is not a Rectangle.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        else:
            return (rect_2)

    @classmethod
    def square(cls, size=0):
        """ Create a Square """
        return (cls(size, size))

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
        return ("Rectangle({:d}, {:d})".format(width, height))
