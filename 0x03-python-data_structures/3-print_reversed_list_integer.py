#!/usr/bin/python3i

def print_reversed_list_integer(my_list=[]):
    for i in range(len(my_list) - 1, -1, -1):
        print(my_list[i])
