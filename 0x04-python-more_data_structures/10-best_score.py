#!/usr/bin/python3


def best_score(a_dictionary):
    if a_dictionary is None:
        return None

    sorted_dict = dict(sorted(a_dictionary.items(), key=lambda item: item[1]))
    best_key = list(sorted_dict.keys())[-1]
    return best_key
