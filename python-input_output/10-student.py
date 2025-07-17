#!/usr/bin/python3
"""Student module with attribute filtering."""


class Student:
    """Defines a student by first_name, last_name, and age."""

    def __init__(self, first_name, last_name, age):
        """Initialize student attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return dict representation of Student.
        If attrs is a list of strings, return only those attributes.
        """
        if isinstance(attrs, list) and all(isinstance(i, str) for i in attrs):
            return {key: getattr(self, key) for key in attrs if hasattr(self, key)}
        return self.__dict__
