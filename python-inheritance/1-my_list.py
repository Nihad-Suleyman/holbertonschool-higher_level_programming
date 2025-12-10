#!/usr/bin/python3
"""let's create a class called Mylist"""


class MyList(list):
    """done"""
    def print_sorted(self):
        """another deocumentation"""
        sorted_list = sorted(self)
        print(sorted_list)
