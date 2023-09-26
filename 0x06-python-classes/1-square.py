#!/usr/bin/python3
""" A class representing a square. """


class Square:
    """
    This class allows you to create and manipulate square objects.
    Each square is defined by its side length.
    """
    def __init__(self, size):
        """Initialize a new Square.
        Args:
            size (int): The size of the new square.
        """
        self.__size = size
