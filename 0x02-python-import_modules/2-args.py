#!/usr/bin/python3

if __name__ == "__main__":
    "print the number of and the list of its arguments"

    import sys

    arguments = sys.argv[1:]
    count = len(arguments)

    if count == 0:
        print("0 arguments.")
    elif count == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(count))
    for m in range(count):
        print("{}: {}".format(m + 1, sys.argv[m + 1]))
