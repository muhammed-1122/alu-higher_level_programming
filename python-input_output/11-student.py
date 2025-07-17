#!/usr/bin/python3
"""Student module with JSON save and load."""


class Student:
    """Defines a student with serialization support."""

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

    def reload_from_json(self, json):
        """Replace all attributes from `json` dictionary."""
        for key, value in json.items():
            setattr(self, key, value)
