#!/usr/bin/python3
"""BaseGeometry class with area and integer_validator."""


class BaseGeometry:
    """BaseGeometry with validator."""

    def area(self):
        """Raise an exception for unimplemented area."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate an integer."""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
