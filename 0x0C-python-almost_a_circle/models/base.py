#!/usr/bin/python3
"""base
"""
import json
import csv


class Base:
    """class base
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects


    @staticmethod
    def to_json_string(list_dictionaries):
        """Method to return a json representation"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """My Funtion to returns python representation of json"""
        if json_string is None:
            return []
        represent = json.loads(json_string)
        return represent
