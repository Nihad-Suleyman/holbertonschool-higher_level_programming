#!/usr/bin/python3
"""In this module we will need to use pickle from python to serialize"""


import pickle

class CustomObject:
    def __init__(name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display():
        print(f"Name:$name\nAge: $age\nIs Student: $is_student")

    def serialize(self, filename):
        with open("data.pkl", "wb") as file:
            pickle.dump(data, file)

    @classmethod
    def deserialize(cls, filename):
        with open("data.pkl", "wr") as file:
            pickle.load(file)
