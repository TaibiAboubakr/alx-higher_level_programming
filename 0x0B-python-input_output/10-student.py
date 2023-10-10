#!/usr/bin/python3
""" class Student """


class Student:
    """ class Student """

    def __init__(self, first_name, last_name, age):
        """ initialize attributes """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ to_json function """

        attributes = self.__dict__
        serialized_data = {}
        for attr, value in attributes.items():
            if isinstance(value, (list, dict, str, int, bool)):
                serialized_data[attr] = value

        return serialized_data
