#!/usr/bin/python3


def multiple_returns(sentence):
    if sentence == "":
        sentence[0] = None
    else:
        str_len = len(sentence)
        first_char = sentence[0]
        tup = (str_len, first_char)
        return (tup)
