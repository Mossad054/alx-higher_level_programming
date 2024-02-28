#!/usr/bin/python3
"""Define a JSON file-writiing function."""
import json


def save_to_json_file(my_obj, filename):
    """Writes objects to a text file using JSON representation."""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
