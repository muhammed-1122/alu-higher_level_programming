#!/usr/bin/python3
"""Square that inherits from Rectangle."""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square with validated size."""

    def __init__(self, size):
        """Initialize square using rectangle init."""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
