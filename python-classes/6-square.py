#!/usr/bin/python3
"""Defines a Square class with position-aware printing."""


class Square:
    """Represents a square with optional position offset when printed."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize the square with size and position."""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get current size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set and validate size."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Get current position."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set and validate position."""
        if (
            not isinstance(value, tuple) or
            len(value) != 2 or
            not all(isinstance(n, int) and n >= 0 for n in value)
            ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the square's area."""
        return self.__size ** 2

    def my_print(self):
        """Print the square using '#' with offset by position."""
        if self.__size == 0:
            print()
            return
        print("\n" * self.__position[1], end="")
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
