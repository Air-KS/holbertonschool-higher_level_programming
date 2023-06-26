#!/usr/bin/python3
"""Defines a base model class."""
from models.rectangle import Rectangle

class Square(Rectangle):
    """Represent a Square

        Args:
            size (int): The size of the new Square.
            x (int): The x coordinate of the new Square.
            y (int): The y coordinate of the new Square.
            id (int): The identity of the new Square.
        """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
