#!/usr/bin/python3
"""Module that writes an object to a text file using JSON."""

import json


def save_to_json_file(my_obj, filename):
    """Writes `my_obj` to a file in JSON format."""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
