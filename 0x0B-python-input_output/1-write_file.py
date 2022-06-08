#!/usr/bin/python3
""" def funtion for  awriting file """


def write_file(filename="", text=""):
    with open(filename, "w", encoding="UTF8") as f:
        return f.write(text)
