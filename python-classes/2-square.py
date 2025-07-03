#!/usr/bin/python3
"""Defines a Square class with size validation."""


class Square:
    """Represents a square with validated size.

    Attributes:
        __size (int): Size of the square's side.
    """

    def __init__(self, size=0):
        """Initialize the square and validate size.

        Args:
            size (int): The size of the square (must be >= 0).

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
