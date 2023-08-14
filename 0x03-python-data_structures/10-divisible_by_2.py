#!/usr/bin/python3


def divisible_by_2(my_list=[]):
    new_list = []

    for element in my_list:
        div_by_2 = element % 2
        if div_by_2 == 0:
            new_list.append(True)
        else:
            new_list.append(False)

    return (new_list)
