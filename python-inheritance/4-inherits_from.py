#!/usr/bin/python3
"""Defines a function to check only inherited class relationships."""


def inherits_from(obj, a_class):
    """Return True if obj is instance of a subclass of a_class, else False."""
    return isinstance(obj, a_class) and type(obj) is not a_class
