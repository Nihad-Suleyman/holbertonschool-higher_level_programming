#!/usr/bin/python3
"""In this module we will need to use pickle from python to serialize"""


import pickle

class CustomObject:
    def __init__(self, name="", age=0, is_student=False):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print(f"Name:{self.name}\nAge: {self.age}\nIs Student: {self.is_student}")

    def serialize(self, filename):
        try:
            with open(filename, "wb") as file:
                pickle.dump(self, file)
        except:
            return None

    @classmethod
    def deserialize(cls, filename):
        try:
            with open(filename, "rb") as file:
                data = pickle.load(file)
        except:
            return None

        return data
