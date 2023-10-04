#!/usr/bin/python3
""" print square module """


def print_square(size):
    """ print_square function that prints a square using # character"""

    if not type(size) is int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    else:
        for _ in range(size):
            print("#" * size)
