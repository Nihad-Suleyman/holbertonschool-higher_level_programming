#!/usr/bin/python3
"""
Defines a Square class (Square #2)
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square class that inherits from Rectangle
    """

    def __init__(self, size):
        """
        Initialize Square with size
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        Returns the area of the square
        """
        return self.__size * self.__size

    def __str__(self):
        """
        Returns the square description
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
