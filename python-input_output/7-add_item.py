#!/usr/bin/python3
"""
This script adds all command-line arguments to a Python list,
and saves them to a file as a JSON representation.
"""
import sys
from os.path import exists

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

# Check if the file exists, if it does, load the existing data
if exists(filename):
    my_list = load_from_json_file(filename)
else:
    my_list = []

# Add all arguments from the command line (excluding the script name)
my_list.extend(sys.argv[1:])

# Save the updated list back to the file
save_to_json_file(my_list, filename)
