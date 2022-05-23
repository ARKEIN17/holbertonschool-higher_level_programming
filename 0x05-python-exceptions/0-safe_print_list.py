#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):

    i = 0
    prt = 0
    for i in range(0, x):
        try:
            print("{}".format(my_list[i]), end="")
            prt += 1
        except TypeError:
            continue
    print()
    return prt
