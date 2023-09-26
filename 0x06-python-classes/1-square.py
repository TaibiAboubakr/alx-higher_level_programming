#!/usr/bin/python3
class Square:
    """
    A class representing a square.
    This class allows you to create and manipulate square objects.
    Each square is defined by its side length.
    """
    def __init__(self, size):
        """Initialize a new Square.
        Args:
            size (int): The size of the new square.
        """
        self.__size = size
