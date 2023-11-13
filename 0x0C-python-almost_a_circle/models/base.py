#!/usr/bin/python3
""" This module house a class to serve as base for other classes"""


class Base:
    """ Private Class Attribute """
    __nb_ojects = 0

    """ Class Constructor """
    def __init__(self, id=None):
        """ Assign the public instance attribute id with
        the argument vale"""
        if id is not None:
            self.id = id
        else:
            """ Increment the class attribute and assign the
            new value to the public instance attribute id"""
            Base.__nb_ojects += 1
            self.id = Base.__nb_ojects
