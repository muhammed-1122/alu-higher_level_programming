#!/usr/bin/python3
"""Defines a function to check class inheritance (direct or indirect)."""


def is_kind_of_class(obj, a_class):
    """Return True if obj is instance or inherits from a_class, else False."""
    return isinstance(obj, a_class)
