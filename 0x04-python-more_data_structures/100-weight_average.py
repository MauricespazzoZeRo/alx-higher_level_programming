#!/usr/bin/python3


def weight_average(my_list=[]):
    if not my_list:
        return (0)

    sum_p = 0
    sum_w = 0

    for score, weigth in my_list:
        mult = score * weight
        sum_p += mult
        sum_w += weight
        weight_avg = sum_p / sum_w

    return (weight_avg)
