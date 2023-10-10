#!/usr/bin/python3
""" import json module """
import json
""" save_to_json_file module """


def save_to_json_file(my_obj, filename):
    """ save_to_json_file function """
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
