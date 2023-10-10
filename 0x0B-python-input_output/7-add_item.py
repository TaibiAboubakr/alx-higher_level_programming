#!/usr/bin/python3
""" import json module """
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

""" load_from_json_file module """


try:
    current_data = load_from_json_file("add_item.json")
except Exception as e:
    current_data = []

for arg in range(1, len(sys.argv)):
    current_data.append(sys.argv[arg])
save_to_json_file(current_data, "add_item.json")
