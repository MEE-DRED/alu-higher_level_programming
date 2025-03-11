#!/usr/bin/python3
"""Yes"""


import json


def load_from_json_file(filename):
    """yes"""
    with open(filename) as f:
        return json.load(f)
