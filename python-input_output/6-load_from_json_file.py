#!/usr/bin/python3
"""Module that loads an object from a JSON file."""

import json


def load_from_json_file(filename):
    """Reads a JSON string from file and returns the object."""
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
