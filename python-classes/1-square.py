#!/usr/bin/python3
"""Defines a Square class with private size attribute."""

class Square:
    """Represents a square with a private size attribute.
    Attributes:
        __size (int): Size of the square's side.
    """

    def __init__(self, size):
        """Initialize the square with a given size.

        Args:
            size (int): The size of the square's side.
        """
        self.__size = size

