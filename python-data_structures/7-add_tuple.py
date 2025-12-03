#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    fst = 0
    snd = 0
    if len(tuple_a) == 1:
        fst += tuple_a[0]
    elif len(tuple_a) >= 2:
        fst += tuple_a[0]
        snd += tuple_a[1]
    if len(tuple_b) == 1:
        fst += tuple_b[0]
    elif len(tuple_b) >= 2:
        fst += tuple_b[0]
        snd += tuple_b[1]
    return (fst, snd)
