#!/usr/bin/python3
""" system module  """
import sys

if __name__ == "__main__":
    n_args = len(sys.argv)
    if n_args != 2:
        print("Uage: nqueens N")
        sys.exit(1)
    N = sys.argv[1]
    if not N.isdigit():
        print("N must be a number")
        sys.exit(1)
    N = int(N)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)
