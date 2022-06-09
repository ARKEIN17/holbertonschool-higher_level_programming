#!/usr/bin/python3
"""class pascal`s triangle"""


def PascalTriangle(n):
   trow = 1
   y = 0
   """Inside the for loop we will print the list initialized by trow variable"""
   for x in range(n):
      print(trow)
      trow = [left + right for left, right in zip(trow + y, y + trow)]
   return n >= 0
