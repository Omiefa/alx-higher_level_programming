#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        last_d = number % -(10)
        print(-(last_d), end='')
    else:
        last_d = number % 10
        print(last_d, end='')
    return abs(last_d)
