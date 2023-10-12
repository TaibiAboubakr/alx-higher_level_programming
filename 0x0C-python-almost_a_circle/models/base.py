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
