#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    dict1 = {}
    for key in a_dictionary:
        value = a_dictionary.get(key) * 2
        dict1.update({key: value})
    return (dict1)
