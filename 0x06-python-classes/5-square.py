#!/usr/bin/python3
""" A class representing a square. """


class Square:
    """
    This class allows you to create and manipulate square objects.
    Each square is defined by its side length.
    """

    def __init__(self, size=0):
        """Initialize a new Square.
        Args:
            size (int): The size of the new square.
        """
        self.__size = size

    def area(self):
        square_area = self.__size * self.__size
        return (square_area)

    @property
    def size(self):
        """
        Retrieve the size (side length) of the square.

        Returns:
            int: The size of the square.
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """
        Set the size (side length) of the square.

        Args:
            value (int): The new size for the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        if self.size == 0:
            print("")
            return
        else:
            for i in range(self.size):
                print("#" * self.size)
