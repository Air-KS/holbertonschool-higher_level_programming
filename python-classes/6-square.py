#!/usr/bin/python3
"""
based on 0-square.py
"""


class Square:
    """A Square classs"""

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize the Square

        Args:
        size (int): The size of the square"""
        self.size = size
        self.position = position

    @property
    def size(self):
        return (self.__size)

    @property
    def position(self):
        return (self.__position)

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @position.setter
    def position(self, value):
        if not type(value) or len(value) != 2 \
                or not type(value[0]) is int or not type(value[1]) is int \
                or value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 position integers")
        else:
            self.__position = value

    def area(self):
        """Return the area of the square"""
        return (self.__size ** 2)

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            print("\n"*self.__position[1], end="")
            for index in range(0, self.__size):
                print(" "*self.__position[0], end="")
                print("#"*self.__size)
