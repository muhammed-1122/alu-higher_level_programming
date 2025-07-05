#!/usr/bin/python3
"""Square with __str__ override."""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square with custom __str__."""

    def __init__(self, size):
        """Initialize square with size validation."""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """Return square description."""
        return f"[Square] {self.__size}/{self.__size}"
