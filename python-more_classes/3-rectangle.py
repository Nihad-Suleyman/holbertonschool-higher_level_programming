#!/usr/bin/python3
''' first document for general'''


class Rectangle:
    '''inside class document'''
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

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

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            return 0
        return (self.__height + self.__width) * 2

    def my_print(self):
        if self.__height == 0 or self.__width == 0:
            print('')
            return
        for _ in range(self.__width):
            print("#" * self.__height)

    def __str__(self):
        """
        Returns a string representation of the rectangle using '#' characters,
        or an empty string if width or height is 0.
        """
        if self.__width == 0 or self.__height == 0:
            return ""

        rectangle_lines = []
        for i in range(self.__height):
            # Each line has a length equal to the width
            # The character used is '#'
            rectangle_lines.append("#" * self.__width)

        return "\n".join(rectangle_lines)
