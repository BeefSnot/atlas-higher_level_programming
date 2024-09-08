#!/usr/bin/python3

"""
This module defines a class Square with an attribute size.
"""


class Square:
    """
    The Square class with a size attribute.
    """
    def __init__(self, size=0):
        """
        The constructor for the Square class.

        Parameters:
        size (int): The size of the square.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
