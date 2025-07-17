#!/usr/bin/python3
"""Module that converts Python object to JSON string."""

import json


def to_json_string(my_obj):
    """Returns the JSON representation of `my_obj`."""
    return json.dumps(my_obj)
