#!/usr/bin/python3
# 0-rectangle.py my Melvin
"""Defines a rectangle"""


class Rectangle:
    """Represnts a rectangle"""

    def __init__(self, width=0, height=0):
        """Initializing this rectangle clas
        Args: width - represents the width of the defined rectangle
              height - represents the height of the defined rectangle
        Raises:
               TypeError: if width/height is not integer
               ValueError: if width/height is less than zero
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """retrieve width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """set the width attribute"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """retrieve the height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """set the height attribute"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """calculates and returns the area of a rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """calculates and returns the perimeter of a rectangle"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))
