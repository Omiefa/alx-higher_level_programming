#!/usr/bin/python3
"""
    A module that checks if an object is an instance of a class
"""


def is_kind_of_class(obj, a_class):
    """ A function that returns True if the object is an
        instance of the class"""
    return isinstance(obj, a_class)
