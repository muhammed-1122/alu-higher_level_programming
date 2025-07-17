#!/usr/bin/python3
"""Module that returns dictionary description for JSON serialization."""


def class_to_json(obj):
    """Returns dict of attributes that are JSON serializable."""
    return obj.__dict__
