#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    printed = 0

    for y in range(x):
        try:
            print("{}".format(my_list[y]), end="")
            printed += 1
        except (TypeError, IndexError):
            continue
    print()
    return printed
