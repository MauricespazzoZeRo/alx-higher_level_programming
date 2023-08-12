#!/usr/bin/python3


def element_at(my_list, idx):
    """
    Retrieves an element from a list.

    Args:
        my_list (list): List with elements.
        idx: Index for elements in list.
    """
    if idx < 0 or idx >= len(my_list):
        return (None)

    return (my_list[idx])
