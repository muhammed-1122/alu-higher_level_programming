#!/usr/bin/python3
"""Module defining MyList class."""

class MyList(list):
    """List subclass with a method to print sorted elements."""

    def print_sorted(self):
        """Print elements of the list sorted in ascending order."""
        sorted_list = sorted(self)
        print(sorted_list)

