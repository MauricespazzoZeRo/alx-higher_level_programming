#!/usr/bin/python3


def print_sorted_dictionary(a_dictionary):
    sorted_a = sorted(a_dictionary.keys())

    for key in sorted_a:
        print(f"{key}: {a_dictionary[key]}")
