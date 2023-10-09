#!/usr/bin/python3
""" class BaseGeometry """


class BaseGeometry:
    """ class BaseGeometry """

    def area(self):
        """ Calculate and returns the rectangle area """

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
        Rectangle.integer_validator(self, "width", width)
        self.__width = width
        Rectangle.integer_validator(self, "height", height)
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        """ return a rectangle description: [Rectangle] <width>/<height> """
        return f"[Rectangle] {self.__width}/{self.__height}"

class Square(Rectangle):
    """
    This class allows you to create and manipulate Square objects.
    Each Square is defined by your size
    """
    def __init__(self, size):
        """Initialize a new Square.
            Args:
                size (int): The size of the new Square.
        """
        Square.integer_validator(self, "size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """ return a squre description: [Square] <width>/<height> """
        return f"[Square] {self.__size}/{self.__size}"