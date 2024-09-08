#!/usr/bin/python3

"""
This module contains the definition of a Square class with a size attribute
"""


class Square:
    """
    A Square class with a private size attribute
    """
    def __init__(self, size=0):
        """
        the __init__ method for the Square class

        Args:
            size (int): the size of the Square
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        A method of Square that returns the square area

        Return:
            the square area of the calling instance of Square
        """
        return self.__size * self.__size
