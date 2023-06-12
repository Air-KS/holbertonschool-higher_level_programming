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
        self.size = size

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Return the area of the square"""
        return (self.__size ** 2)

    def my_print(self):
        for index in range(self.__size):
            for length in range(self.__size):
                print("#", end="")
            print("")
        if self.__size == 0:
            print()
