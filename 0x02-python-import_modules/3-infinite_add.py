#!/usr/bin/python3
import sys
if __name__ == "__main__":
    sum = 0
    n_args = len(sys.argv) - 1
    if n_args == 0:
        print("{}".format(n_args))
    else:
        for i in range(1, n_args + 1):
            sum += int(sys.argv[i])
        print("{}".format(sum))
