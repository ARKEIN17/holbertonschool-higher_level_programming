#!/usr/bin/python3
"""Module for saving to json"""
import json
import os.path
import sys
"""libs"""
from sys import argv
"""coment"""
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
"""save"""
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
"""load"""

filename = "add_item.json"
json_list = []

"""str json"""
if os.path.exists(filename):
    json_list = load_from_json_file(filename)
    """def"""

for index in argv[1:]:
    """ argv """
    json_list.append(index)
    """append"""

save_to_json_file(json_list, filename)
