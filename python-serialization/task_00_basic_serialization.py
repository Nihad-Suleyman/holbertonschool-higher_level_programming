#!/usr/bin/python3
"""now let's start to python serialization"""


import json
def serialize_and_save_to_file(data, filename):
    filename = json.dumps(data).encode("utf-8")

def load_and_deserialize(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return json.loads(f.read())
