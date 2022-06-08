#!/usr/bin/python3
""" conver a object a  string """
import json

from yaml import _Representer
""" import a lib json and def json """


def to_json_string(my_obj):
    """ my funtion """
    Represent = json.dumps(my_obj)
    return Represent
