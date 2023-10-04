#!/usr/bin/python3
""" say_my_name module contain say_my_name function """


def say_my_name(first_name, last_name=""):
    """ function thats prints : My name is 'first name' 'last name' """
    if not type(first_name) is str:
        raise TypeError("first_name must be a string")
    if not type(last_name) is str:
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
