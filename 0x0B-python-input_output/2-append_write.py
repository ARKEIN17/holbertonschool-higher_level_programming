#!/usr/bin/python3
""" funtion tath write in a file """


def append_write(filename="", text=""):
    """ open file appends a string in the end of file """
    with open(filename, "a", encoding="UTF-8") as f:
        """ retur """
        return f.write(text)
