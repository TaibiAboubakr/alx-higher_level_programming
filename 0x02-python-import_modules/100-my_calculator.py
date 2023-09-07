#!/usr/bin/python3
import sys
from calculator import *
if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <a> <operator> <b>".format(sys.argv[0]))
        exit(1)
    n1 = (sys.argv[1])
    n2 = (sys.argv[3])
    if not n1.isdigit() or not n2.isdigit():
        print("Error: <a> and <b> must be a number")
        exit(1)
    n1 = int(n1)
    n2 = int(n2)
    if sys.argv[2] == "+":
        print("{:d} + {:d} = {:d} ".format(n1, n2, add(n1, n2)))
    elif sys.argv[2] == "-":
        print("{:d} - {:d} = {:d} ".format(n1, n2, sub(n1, n2)))
    elif sys.argv[2] == "*":
        print("{:d} * {:d} = {:d} ".format(n1, n2, mul(n1, n2)))
    elif sys.argv[2] == "/":
        print("{:d} / {:d} = {:d} ".format(n1, n2, div(n1, n2)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
