#!/usr/bin/python3


def multiple_returns(sentence):
    if sentence == "":
        length = 0
        first_char = None
    else:
        length = len(sentence)
        first_char = sentence[0]

    tup = (length, first_char)
    return (tup)
