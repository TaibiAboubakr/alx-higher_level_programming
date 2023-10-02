#!/usr/bin/python3
def text_indentation(text):
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
    print(string)
