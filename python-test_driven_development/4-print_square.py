#!/usr/bin/python3
"""
Module that prints a square.
"""

def print_square(size):
    """Prints a square with # based on size"""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
