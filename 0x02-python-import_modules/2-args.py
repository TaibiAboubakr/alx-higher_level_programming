#!/usr/bin/python3
import sys
if __name__ == "__main__":
    n_args = len(sys.argv) - 1
    if n_args == 0:
        print("{} arguments.".format(n_args))
    elif n_args == 1:
        print("1 argument:".format(n_args))
        print("1: {}".format(sys.argv[1]))

    else:
        print("{} arguments:".format(n_args))
        for i in range(1, n_args + 1):
            print("{}: {}".format(i, sys.argv[i]))
