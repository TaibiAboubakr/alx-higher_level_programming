#!/usr/bin/python3
""" Base calss """


class Base:
    """ Base class """
    __nb_objects = 0
    
    def __init__(self, id=None):
        """Initialize a new instance.
            Args:
                id (int): id of the new instance
        """
        if id is not None:
            self.id = id
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ static method def to_json_string(list_dictionaries): 
        that returns the JSON string representation of list_dictionaries
        """
        json_dict = "["
        if list_dictionaries is None or len(list_dictionaries) == 0:
            json_dict += "]"
            return json_dict
        else:
            json_dict += "{"
            for dict in list_dictionaries:
                for key, value in dict.items():
                    json_dict += f"'{key}'" + ": " + str(value) + ", "
            json_dict += "}]"
            return json_dict