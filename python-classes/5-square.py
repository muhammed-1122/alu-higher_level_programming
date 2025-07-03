#!/usr/bin/python3
"""Defines a Square class that prints itself using '#'."""


class Square:
    """Represents a square with print capability."""

    def __init__(self, size=0):
        """Initialize square with validated size."""
        self.size = size

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set size with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Compute and return area."""
        return self.__size ** 2

    def my_print(self):
        """Print the square with '#' or a blank line if size is 0."""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
