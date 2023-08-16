#!/usr/bin/python3


def common_element(set_1, set_2):
    set_of_common = set()

    for element in set_1:
        if element in set_2:
            set_of_common.add(element)

    return (set_of_common)
