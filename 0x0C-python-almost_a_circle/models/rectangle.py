#!/usr/bin/python3
""" This module contains the rectangle class """

from models.base import Base


class Rectangle(Base):
    """Initialize instance attributes"""
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("Width must be an integer")
        elif value <= 0:
            raise ValueError("Width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("Height must be an integer")
        elif value <= 0:
            raise ValueError("Height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x coordinate must be an integer")
        elif value < 0:
            raise ValueError("x coordinate must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y coordinate must be an integer")
        elif value < 0:
            raise ValueError("y coordinate must be >= 0")
        else:
            self.__y = value

    def area(self):
        """ Calcuates the area of the rectangle """
        return (self.__width * self.__height)

    def display(self):
        """Displays the rectangle using # """
        for y in range(self.y):
            print("")
        for row in range(self.__height):
            for x in range(self.x):
                print(" ", end="")
            for column in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """Defines a format for the string representation of the class"""
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - \
{self.__width}/{self.__height}"

    def update(self, *args, **kwargs):
        """Assigns arguments to attributes: id, width, height, x, y."""
        if args:
            """If *args exists and is not empty
            update attributes using *args"""
            for m, arg in enumerate(args):
                if m == 0 and arg is not None:
                    self.id = arg
                elif m == 1:
                    self.width = arg
                elif m == 2:
                    self.height = arg
                elif m == 3:
                    self.x = arg
                elif m == 4:
                    self.y = arg
        elif kwargs:
            """If *args is empty, update attributes using **kwargs"""
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        return {
            'id': self.id,
            'width': self.__width,
            'height': self.__height,
            'x': self.__x,
            'y': self.__y
        }
