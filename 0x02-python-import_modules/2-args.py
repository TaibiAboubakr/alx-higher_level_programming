#!/usr/bin/python3
import sys
n_args = len(sys.argv) - 1
if n_args == 0:
    print("{} arguments.".format(n_args))
else:
    print("{} arguments.".format(n_args))
    for i in range(1, n_args + 1):
        print("{}: {}".format(i, sys.argv[i]))
