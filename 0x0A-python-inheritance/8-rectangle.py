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


""" A class representing a Rectangle  that inherits from BaseGeometry """


class Rectangle(BaseGeometry):
    """
    This class allows you to create and manipulate Rectangle objects.
    Each Rectangle is defined by its width and height
    """
    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.
            Args:
                width (int): The width of the new Rectangle.
                height (int): The height of the new Rectangle.
        """

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
        
        
        
