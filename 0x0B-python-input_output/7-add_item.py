#!/usr/bin/python3
"Method Module"
import json
from sys import argv


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"
# Create the object or calling from json
try:
    with open(filename, 'r') as f:
        obj = load_from_json_file(f)
except Exception:
    obj = []

for i in range(1, len(argv)):
    obj.append(argv[i])

# Create json file
with open(filename, 'w') as f:
    save_to_json_file(obj, f)
