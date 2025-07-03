#!/usr/bin/python3
"""Defines a Square class that computes area."""


class Square:
    """Represents a square with size and area computation.

    Attributes:
        __size (int): Size of the square's side.
    """

    def __init__(self, size=0):
        """Initialize square and validate size."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Compute and return the area of the square."""
        return self.__size ** 2
