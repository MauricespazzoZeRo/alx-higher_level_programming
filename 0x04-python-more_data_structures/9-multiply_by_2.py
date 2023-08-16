#!/usr/bin/pthon3


def multiply_by_2(a_dictionary):
    """
    using dictionary comprehension for my first time
    in order to multiply the value of every key: value
    pair in a dictionary
    """
    return {key: value * 2 for (key, value) in a_dictionary.items()}

"""
---------------------OR-----------------------------
    new_dict = {}

    for key, val in a_dictionary.items():
        new_dict[key] = val * 2

    return new_dict
"""
