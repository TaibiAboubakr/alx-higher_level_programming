#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    Key_Removes = []
    for key, val in a_dictionary.items():
        if val == value:
            Key_Removes.append(key)
    for key in Key_Removes:
        a_dictionary.pop(key)
    return (a_dictionary)
