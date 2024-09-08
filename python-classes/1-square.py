#!/usr/bin/python3

"""
This module that defines a class square with an attribute size.
"""


class Square:
    """
    The Square class with a size attribute.
    """
    def __init__(self, size):
        """
        The constructor for the Square class.

        Parameters:
        size (int): The size of the square.
        """
        self.__size = size
