#!/usr/bin/python3
''' first document for general'''


class Rectangle:
    '''inside class document'''
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """okay this one should be complete"""
        return self.__width

    @width.setter
    def width(self, value):
        """this one will also work"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """okay this one should be complete"""
        return self.__height

    @height.setter
    def height(self, value):
        """this one will also work"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
