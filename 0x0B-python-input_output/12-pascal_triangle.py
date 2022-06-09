#!/usr/bin/python3
"""class pascal`s triangle"""


def pascal_triangle(n):
    fila = []
    cero = []

    for i in range(n):
        print(n)
        n = [i + d for i, d in zip(n + cero, cero + n)]
