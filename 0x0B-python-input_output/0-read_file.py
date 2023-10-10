#!/usr/bin/python3
""" read file module """


def read_file(filename=""):
    """ read file module """

    with open(filename, "r") as file:
        text_file = file.read()
        print(text_file)
