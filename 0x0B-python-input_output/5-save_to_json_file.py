#!/usr/bin/python3
""" funtion that save"""
import json


def save_to_json_file(my_obj, filename):
    """ funtion adn definition """
    with open(filename, "w", encoding="UTF-8") as f:
        json.dump(my_obj, f)
