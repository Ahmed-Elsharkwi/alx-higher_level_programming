#!/usr/bin/python3
"""
 adds all arguments to a Python list,
 and then save them to a file
"""


import sys
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


try:
    list = load_from_json_file("add_item.json")
except FileNotFoundError:
    list = []
for arg in range(1, len(sys.argv)):
    list.append(sys.argv[arg])
save_to_json_file(list, "add_item.json")
