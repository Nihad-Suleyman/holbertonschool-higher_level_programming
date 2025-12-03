#!/usr/bin/python3
def roman_to_int(roman_string):
    if (not type(roman_string) is str) or (roman_string is None):
        return 0
    r = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500}
    conv = []
    for n in roman_string:
        conv.append(r[n])
    for i in range(1, len(conv)):
        if conv[i] > conv[i-1]:
            conv[i-1] *= -1
    return sum(conv)
