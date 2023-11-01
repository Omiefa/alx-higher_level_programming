#!/usr/bin/python3
""" Function that prints the full name """


def say_my_name(first_name, last_name=""):
    """ Return the full name of the user

        Args:
            first_name = user's first name
            last_name = user's last name
i
        Returns: The user's full name if the last name is given

        TypeError: if names are not strings
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    full_name = (f"My name is {first_name} {last_name}")
    print(full_name)
