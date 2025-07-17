#!/usr/bin/python3
"""Module that returns Pascal's Triangle up to `n`."""


def pascal_triangle(n):
    """Return Pascal’s triangle of n.
    Returns empty list if n <= 0.
    """
    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        prev = triangle[-1]
        row = [1] + [prev[j] + prev[j + 1] for j in range(len(prev) - 1)] + [1]
        triangle.append(row)

    return triangle
