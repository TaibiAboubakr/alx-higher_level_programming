#!/usr/bin/python3
""" A class representing a Rectangle. """


class Rectangle:
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
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Retrieve the width of the rectangle.

        Returns:
            int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width (side length) of the rectangle.

        Args:
            value (int): The new width for the rectangle.

        Raises:
            TypeError: width must be an integer
            ValueError: width must be >= 0.
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Retrieve the height of the rectangle.

        Returns:
            int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height (side length) of the rectangle.

        Args:
            value (int): The new height for the rectangle.

        Raises:
            TypeError: height must be an integer
            ValueError: height must be >= 0.
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Calculate and returns the rectangle area """
        rectangle_area = self.__width * self.__height
        return (rectangle_area)

    def perimeter(self):
        """ Calculate and returns the rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        rectangle_perimeter = (self.__width + self.__height) * 2
        return (rectangle_perimeter)

    def __str__(self):
        """ print a rectangle using the "#" character
            based on its width and height """
        rect = ""
        for _ in range(self.__height):
            rect += "#" * self.__width + "\n"
        return (rect.rstrip())

    def __repr__(self):
        """ Recreate a rectangle """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """print the message 'Bye rectangle...' when an object is destroyed."""
        print("Bye rectangle...")
