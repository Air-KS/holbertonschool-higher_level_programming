#!/usr/bin/python3
"""
Module for task 6
"""

import json


def load_from_json_file(filename):
    """ Create a Python object from a JSON file. """
    with open(filename) as file:
        jsonObj = json.load(file)
    return jsonObj
