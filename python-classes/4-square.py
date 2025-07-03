#!/usr/bin/python3
"""Defines a Square class with property for size."""


class Square:
    """Represents a square with a private size and public getters/setters."""

    def __init__(self, size=0):
        """Initialize square with validated size."""
        self.size = size

    @property
    def size(self):
        """Get the current size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size with validation.

        Raises:
            TypeError: If size is not an int.
            ValueError: If size is < 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Compute and return the square's area."""
        return self.__size ** 2
