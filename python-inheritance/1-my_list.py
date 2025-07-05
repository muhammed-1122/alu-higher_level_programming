#!/usr/bin/python3
"""Class MyList that inherits from list."""


class MyList(list):
    """Custom list class that can print sorted list."""

    def print_sorted(self):
        """Print the list in ascending sorted order."""
        print(sorted(self))

