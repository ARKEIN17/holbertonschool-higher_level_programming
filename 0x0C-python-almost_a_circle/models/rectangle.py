#!/usr/bin/python3
"""
   Module for Rectangle class.
"""
from models.base import Base


class Rectangle(Base):
    """
        Constructor
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor Method"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Width of this rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method of width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value


    @property
    def height(self):
        """Getter method of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method of height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value
