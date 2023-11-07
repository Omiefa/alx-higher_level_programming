#!/usr/bin/python3
"""
    A module that checks if the object is an instance of the specified class
"""


def is_same_class(obj, a_class):
    """ A function that retyrns true if the object is an
        instance of the class, otherwise false"""
    return type(obj) == a_class
