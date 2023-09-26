#!/usr/bin/python3
""" A class representing a square. """


class Square:
    """
    This class allows you to create and manipulate square objects.
    Each square is defined by its side length.
    """

    def __init__(self, size=0, position=(0, 0)):

        """Initialize a new Square.
            Args:
                size (int): The size of the new square.
                position (tuple): The position of the new square.
        """
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """
        Retrieve the position of the square.

        Returns:
            tuple: The position of the square.
        """
        return (self.__position)

    @position.setter
    def position(self, value):
        """
        Set the position of the square.

        Args:
            value (tuple): The position of the square.

        Raises:
            TypeError: position must be a tuple of 2 positive integers.
            ValueError: position must be a tuple of 2 positive integers.
        """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise ValueError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """Print the square with the #"""
        if self.__size == 0:
            print("")
            return
        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
