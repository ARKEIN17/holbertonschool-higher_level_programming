#!/usr/bin/python3
""" function that creates an 
    Object from a “JSON file” """

import json
""" funtion that read and return file json"""

def load_from_json_file(filename):
    with open(filename, "r", encoding="UTF-8") as f:
        return json.load(f)
