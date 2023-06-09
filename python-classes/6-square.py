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
        if not (
            isinstance(value, tuple) and
            len(value) == 2 and
            all(isinstance(num, int) and num >= 0 for num in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the area of the square"""
        return (self.__size ** 2)

    def my_print(self):
        if self.__size == 0:
            print()
            return

        # Afficher la marge supperieur
        for _ in range(self.__position[1]):
            print("")

        # Affiche les ligne de motif
        for _ in range(self.__size):
            for _ in range(self.__position[0]):
                print(" ", end="")

            for _ in range(self.__size):
                print("#", end="")
            print("")
