#!/usr/bin/python3
class MyList(list):
    """Custom list class that can print sorted version of itself."""

    def print_sorted(self):
        """Prints the list in ascending sorted order."""
        print(sorted(self))
