#!/usr/bin/python3
""" read file module """


def read_file(filename=""):
    """ read file module """
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            print(line, end="")
        print()
