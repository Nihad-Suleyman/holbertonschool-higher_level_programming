#!/usr/bin/python3
"""done"""


class BaseGeometry:
    """class"""

    def area(self):
        """raises exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validate"""
        if type(value) is not int:
            raise TypeError(f"{name} mus be an integer")
        if value <= 0:
            raise ValueError(f"{name} mus be greater than 0")
