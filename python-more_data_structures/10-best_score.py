#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    elif len(a_dictionary) == 0:
        return None
    key, value = None, float('-inf')
    for i in a_dictionary:
        if a_dictionary[i] > value:
            value = a_dictionary[i]
            key = i
    return key
