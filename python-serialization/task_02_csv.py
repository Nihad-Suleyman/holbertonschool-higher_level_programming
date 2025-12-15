#!/usr/bin/python3
"""now let's change from csv to json"""


python import csv import json

def convert_csv_to_json(filename):
    try:
        data = []

        with open(filename, 'r', newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for i in reader:
                data.append(f)

        with open("data.json", "w", encoding='utf-8') as f:
            json.dump(data, f)

        return True
    except:
        return False
