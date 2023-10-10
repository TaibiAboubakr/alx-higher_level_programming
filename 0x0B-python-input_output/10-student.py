#!/usr/bin/python3
""" class Student """


class Student:
    """ class Student """

    def __init__(self, first_name, last_name, age):
        """ initialize attributes """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ to_json function """
        if (type(attrs) is list and
                all(isinstance(ele, str) for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
