#!/usr/bin/python3
"""now let's start to python serialization"""


import json
def serialize_and_save_to_file(data, filename):
    filename = json.dumps(data).encode("utf-8")
    pass

def load_and_deserialize(filename):
    filename = json.loads(filename.decode("utf-8")
    pass
