#!/usr/bin/python3


def print_square(size):

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size == 0:
        return
    area = size ** 2
    for i in range(area):
        if i % size == 0 and i != 0:
            print()
        print("#", end="")
    print()
