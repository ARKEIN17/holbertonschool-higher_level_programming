#!/usr/bin/python3
""" def funtion for  awriting file """


def write_file(filename="", text=""):
    """ open file and write """
    with open(filename, "w", encoding="UTF-8") as f:
        """ terurn """
        return f.write(text)
