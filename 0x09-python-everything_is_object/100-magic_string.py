#!/usr/bin/python3
"""
My magic string module
"""


def magic_string():
    from counter import Counter
    Counter.i += 1
    return ", ".join(["Holberton" for i in range(0, Counter.i)])
