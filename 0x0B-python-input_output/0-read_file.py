#!/usr/bin/python3
""" def funtion for read a file """


def read_file(filename=""):
    """ funtion that read the text a file"""

    with open(filename) as f:
        text = f.read()
        print(text, end="")
