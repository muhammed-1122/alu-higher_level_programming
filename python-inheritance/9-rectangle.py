#!/usr/bin/python3
"""Rectangle with area and __str__ method."""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class with validated width and height."""

    def __init__(self, width, height):
        """Initialize rectangle with validated dimensions."""
        self.integer_validator("width", width)
        self.__width = width

        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Return area of rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """String representation of rectangle."""
        return f"[Rectangle] {self.__width}/{self.__height}"
