#!/usr/bin/python3
"""
Module for task 1
"""


class MyList(list):
    """Class for a list """

    def print_sorted(self):
        """'''Print a list in sorted"""
        print(sorted(self))
