#!/usr/bin/python3

if __name__ == "__main__":

    import sys

    result = 0
    for j in range(len(sys.argv[1:])):
        result += int(sys.argv[j + 1])
    print("{}".format(result))
