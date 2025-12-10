#!/usr/bin/python3
"let's create a class"""


class Mylist(list):
    """done"""
    def print_sorted(self):
        """another deocumentation"""
        sorted_list = sorted(self)
        print(sorted_list)
