#!/usr/bin/python3


def uniq_add(my_list=[]):
    first_occ = {}
    total = 0

    for element in my_list:
        if element not in first_occ:
            first_occ[element] = True
            total += element

    return (total)
