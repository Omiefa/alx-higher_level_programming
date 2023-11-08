#!/usr/bin/python3
""" A module that read a text and print to stdout"""


def read_file(filename=""):
    """A function that reads and prints a text
       file to the stdout"""
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")
