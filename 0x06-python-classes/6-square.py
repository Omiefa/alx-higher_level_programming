#!/usr/bin/python3
# 0-square.py by Melvin
"""Defines a square"""


class Square:
    """Represnts a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initializing this square clas
        Args:
               size - represents the size of the defined square
               position - represents the coordinates of the square
        Raises:
               TypeError: if size is not integer
               ValueError: if size is less than zero
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple):
            raise TypeError('position must be a tuple of 2 positive integers')
        if len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        if sum(1 for i in value if isinstance(i, int) and i >= 0) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def area(self):
        """Returns the current square area"""
        return self.__size * self.__size

    def my_print(self):
        """method that prints in stdout the square with the #"""
        if self.__size == 0:
            print()
        else:
            if self.__position[1] > 0:
                print("\n" * self.__position[1], end="")
            for _ in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)
