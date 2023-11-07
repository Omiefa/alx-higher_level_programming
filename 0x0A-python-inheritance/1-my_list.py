#!/usr/bin/python3
"""
    This module creates a clas that inherits from a list
"""


class MyList(list):
    """ This class inherits from a list"""
    def print_sorted(self):
        sorted_list = sorted(self)
        print(sorted_list)
