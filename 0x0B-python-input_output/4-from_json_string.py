#!/usr/bin/python3
""" function that returns an object """

import json

""" funtion return a str"""
def from_json_string(my_str):
    return json.loads(my_str)