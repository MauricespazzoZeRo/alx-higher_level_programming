#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argv = sys.argv[1:]

    argc = len(argv)

    print(f"{argc} argument", end='')

    if argc == 0:
        print('.')
    elif argc == 1:
        print(':')
    else:
        print('s:')

    for i, arg in enumerate(argv, start=1):
        print(f"{i}: {arg}")
