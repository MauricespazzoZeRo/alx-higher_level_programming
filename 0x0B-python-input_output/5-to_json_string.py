#!/usr/bin/python3
"""
my module
"""
import json


def to_json_string(my_obj):
    """returs json string containing object's representation
        -> handles no exceptions in serialization proccess
    """
    return json.dumps(my_obj)
