#!/usr/bin/python3
"""input and output module"""
import json
from sys import argv


save_to_json_file = __import('5-save_to_json_file').save_to_json_file
load_from_json_file = __import('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

try:
    with open(filename, 'r') as f:
        obj = load_from_json_file(f)
except Exception:
    obj = []

for i in range(1, len(argv)):
    obj.append(argv[i])

with open(filename, 'w') as f:
    save_to_json_file(obj, f)
