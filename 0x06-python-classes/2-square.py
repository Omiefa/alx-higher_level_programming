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
