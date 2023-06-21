#!/usr/bin/python3
"""
Module for task 5
"""

import json


def from_json_string(my_str):
    """ Return the Python object representation of a JSON string """
    jsonObj = json.loads(my_str)
    return jsonObj
