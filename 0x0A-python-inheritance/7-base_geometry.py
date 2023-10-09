#!/usr/bin/python3
""" class BaseGeometry """


class BaseGeometry:
    """ class BaseGeometry """
    def area(self):
        """
        area method
        raise :
        Exception : area() is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        integer_validator method that validates value
        raises
        TypeError  : <name> must be an integer
        ValueError : <name> must be greater than 0
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
