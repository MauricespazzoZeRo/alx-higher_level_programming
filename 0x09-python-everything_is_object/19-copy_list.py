#!/usr/bin/python3
"""
My copy list module
"""


def copy_list(l):
    """generates a copy of a list
    """
    if not isinstance(l, list):
        return None
    return l[:]
