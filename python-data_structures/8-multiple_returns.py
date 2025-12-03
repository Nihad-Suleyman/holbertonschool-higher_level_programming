#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        return (0, None)
    mult = (len(sentence), sentence[0])
    return mult
