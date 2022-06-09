#!/usr/bin/python3
"""class pascal`s triangle"""


def pascal_triangle(n):
    fila = [1]
    cero = [0]

    for i in range(n):
        """print"""
        n = [i + d for i, d in zip(fila + cero, cero + fila)]
        
