#!/usr/bin/python3

"""
This is my lookup function module
"""


def lookup(obj):
    """
    returns all objects in an objects dictionary
        -> as a list
    """
    return dir(obj)
