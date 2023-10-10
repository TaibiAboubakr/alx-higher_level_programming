#!/usr/bin/python3
""" class_to_json module """


def class_to_json(obj):
    """ class_to_json function """

    attributes = obj.__dict__
    serialized_data = {}
    for attr, value in attributes.items():
        if isinstance(value, (list, dict, str, int, bool)):
            serialized_data[attr] = value

    return serialized_data
