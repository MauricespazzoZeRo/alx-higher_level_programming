#!/usr/bin/python3


def best_score(a_dictionary):
    sorted_dict = dict(sorted(a_dictionary.item(), key=lambda item: item[1]))
    sorted_vals = sorted_dict.values()
    best_score = sorted_vals[-1]

    return (best_score)
