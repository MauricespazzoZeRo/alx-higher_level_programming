#!/usr/bin/python3


def print_list_integer(my_list=[]):
    """
    prints a list of given integers
    """
    new_list = my_list.copy
    new_list.reverse()
    for i in len(new_list):
        print("{:d}".format(i))
