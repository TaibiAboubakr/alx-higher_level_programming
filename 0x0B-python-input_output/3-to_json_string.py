#!/usr/bin/python3
""" import json module """
import json
""" to_json_string module """


def to_json_string(my_obj):
    """ to_json_string function """
    data = json.dumps(my_obj)
    return (data)
