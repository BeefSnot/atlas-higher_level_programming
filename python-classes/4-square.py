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
        self.__size = size

    @property
    def size(self):
        """
        Getter for size attribute.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter for size attribute.

        Args:
            value: the value to set as size
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        A method of the class that finds area.
        """
        return self.__size ** 2
