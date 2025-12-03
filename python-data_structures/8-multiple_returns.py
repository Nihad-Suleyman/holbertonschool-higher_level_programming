#!/usr/bin/python3
def multiple_returns(sentence):
    mult = (len(sentence), sentence[0])
    if mult[0] == 0:
        return None
    return mult
