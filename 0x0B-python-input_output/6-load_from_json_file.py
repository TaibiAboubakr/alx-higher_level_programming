#!/usr/bin/python3
""" import json module """
import json
""" load_from_json_file module """


def load_from_json_file(filename):
    """ load_from_json_file function """
    with open(filename, 'r') as file:
        data = json.load(file)
        return (data)
