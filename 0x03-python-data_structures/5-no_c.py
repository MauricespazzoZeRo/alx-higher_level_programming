#!/usr/bin/python3


def no_c(my_string):
    remove = "c"
    new_string = ""

    for char in my_string:
        if char != remove:
            new_string += char

    return (new_string)
