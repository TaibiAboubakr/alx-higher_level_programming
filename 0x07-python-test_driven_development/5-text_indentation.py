#!/usr/bin/python3
""" text_indentation module """


def text_indentation(text):
    """ text_indentation function """

    if not type(text) is str:
        raise TypeError("text must be a string")
    string = ""
    space = True
    for char in text:
        if char == '.' or char == '?' or char == ':':
            string += char + "\n\n"
            space = True
        else:
            if space and char != ' ':
                space = False
            if not space:
                string += char
    print(string, end="")
