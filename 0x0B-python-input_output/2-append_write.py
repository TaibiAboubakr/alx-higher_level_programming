#!/usr/bin/python3
""" write_file module """


def append_write(filename="", text=""):
    """ write_file function """
    with open(filename, "a", encoding="utf-8") as file:
        text_file = file.write(text)
        return (text_file)
