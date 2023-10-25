#!/usr/bin/python3
# 0-square.py by Melvin
"""Defines a square"""


class Square:
    """Represnts a square"""

    def __init__(self, size=0):
        """Initializing this square clas
        Args:
               size - represents the size of the defined square
        Raises:
               TypeError: if size is not integer
               ValueError: if size is less than zero
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def size(self):
        """method that retrieves the size"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Returns the current square area"""
        return self.__size * self.__size
