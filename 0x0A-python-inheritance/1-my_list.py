#!/usr/bin/python3
"""Class definition"""


class MyList(list):
    """A class that inherits from list."""

    def print_sorted(self):
        """A method that prints a sorted list"""
        print(sorted(self))
