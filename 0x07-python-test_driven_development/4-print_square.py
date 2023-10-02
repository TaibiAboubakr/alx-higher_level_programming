#!/usr/bin/python3

def print_square(size):
    if not type(size) is int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    else:
        for _ in range(size):
            print("#" * size)
