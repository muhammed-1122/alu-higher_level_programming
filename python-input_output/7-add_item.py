#!/usr/bin/python3
"""Script that adds arguments to a list and saves them in a file."""

import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

try:
    items = load_from_json_file(filename)
except Exception:
    items = []

items.extend(sys.argv[1:])
save_to_json_file(items, filename)
