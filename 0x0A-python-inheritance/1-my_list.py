#!/usr/bin/python3

"""
This is my MyList module
"""


class MyList(list):
    """extended version of list
    """
    def print_sorted(self):
        """prints the list in ascending order
        """
        copy = self[:]
        copy.sort()
        print(copy)
