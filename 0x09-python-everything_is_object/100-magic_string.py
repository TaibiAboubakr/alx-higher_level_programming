#!/usr/bin/python3
""" magic_string module """


def magic_string(n):
    """ magic_string function """
    s = ""
    for i in range(1, n + 1):
        s += "BestSchool" * i
    return s
