#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):
    """
    prints the reverse of a given list
    """
    if type(my_list) is list:
        new_list = my_list[0:]
        new_list.reverse()
        for i in range(len(new_l)):
            print("{:d}".format(new_list[i]))
