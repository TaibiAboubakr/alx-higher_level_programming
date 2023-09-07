#!/usr/bin/python3
import sys
n_args = len(sys.argv) - 1
if n_args == 0:
    print(n_args, "arguments.")
else:
    print(n_args, "arguments:")
    for i in range(1, n_args + 1):
        print(f"{i}: {sys.argv[i]}")
