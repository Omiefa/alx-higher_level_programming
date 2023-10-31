#!/usr/bin/python3
"""
A function that adds 2 integer

"""
def add_integer(a, b=98):
    """ Return the sum of two integers or floats as integer
        
        Args:
            a: first argument
            b: second argument

        Returns: sum of the two arguments

        Raises:
            TypeError: if the arguments are not integer or float
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
