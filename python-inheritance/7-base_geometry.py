#!/usr/bin/python3
"""Module defines BaseGeometry class."""

class BaseGeometry:
    """BaseGeometry class with area method and integer validator."""

    def area(self):
        """Raise an exception for unimplemented area method."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that 'value' is a positive integer.

        Args:
            name (str): The name of the variable.
            value (int): The value to validate.

        Raises:
            TypeError: If value is not an int.
            ValueError: If value is <= 0.
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
