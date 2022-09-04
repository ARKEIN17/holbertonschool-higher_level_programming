#!/usr/bin/python3
""" make pascal triangle """


def pascal_triangle(n):
    """definition a pascal triangle"""
    pasc_list = []

    for i in range(n):
        pasc_list.append([])
        pasc_list[i].append(1)
        for j in range(1, i):
            pasc_list[i].append(pasc_list[i - 1][j - 1] + pasc_list[i - 1][j])
        if (i != 0):
            pasc_list[i].append(1)
    return pasc_list
