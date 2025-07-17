#!/usr/bin/python3
"""Module that appends a string to a text file."""


def append_write(filename="", text=""):
    """Appends `text` to `filename`. Creates file if it doesn't exist.
    Returns number of characters added.
    """
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
