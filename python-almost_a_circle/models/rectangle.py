#!/usr/bin/python3
"""Defines a base model class."""
from models.base import Base


class Rectangle(Base):
    """Represent a rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initialize a new Rectangle

        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
            x (int): The x coordinate of the new Rectangle.
            y (int): The y coordinate of the new Rectangle.
            id (int): The identity of the new Rectangle.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Get/Set - the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Get/Set - the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Get/Set - The x coordinate of the Rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Get/Set - The y coordinate of the Rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ Return the area of the Rectangle """
        return self.__width * self.__height

    def display(self):
        """ Print the Rectangle using the `#` character """
        if self.__width == 0 or self.__height == 0:
            print("")
            return

        for _ in range(self.__y):
            print("")

        for _ in range(self.__height):
            for _ in range(self.__x):
                print(" ", end="")
            for _ in range(self.__width):
                print("#", end="")
            print("")

    def __str__(self):
        """ Return the print() and str() representation of the Rectangle """
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                        self.x,
                                                        self.y,
                                                        self.width,
                                                        self.height))

    def update(self, *args, **kwargs):
        """Update the Rectangle.

        Args:
            - 1st argument should be the id attribute
            - 2nd argument should be the width attribute
            - 3rd argument should be the height attribute
            - 4th argument should be the x attribute
            - 5th argument should be the y attribute
        **kwargs (Dictionary): New key/value of attributes.
        """
        if args:
            for key, value in enumerate(args):
                if key == 0:
                    self.id = value
                elif key == 1:
                    self.width = value
                elif key == 2:
                    self.height = value
                elif key == 3:
                    self.x = value
                else:
                    self.y = value
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "width" in kwargs:
                self.width = kwargs["width"]
            if "height" in kwargs:
                self.height = kwargs["height"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """ Return dictionary representation """
        dictionary = {}
        dictionary["id"] = self.id
        dictionary["width"] = self.width
        dictionary["height"] = self.height
        dictionary["x"] = self.x
        dictionary["y"] = self.y
        return (dictionary)
