#!/usr/bin/python3
"""now let's start to python serialization"""


import json
def serialize_and_save_to_file(data, filename):
    with open(filename, "w", encoding="utf-8") as f:
        json.dumps(f, data)

def load_and_deserialize(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return json.loads(f.read())
