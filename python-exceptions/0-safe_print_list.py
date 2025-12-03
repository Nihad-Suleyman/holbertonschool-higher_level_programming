#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    ln = 0
    for _ in my_list:
        ln += 1
    try:
        if x > ln:
            print(my_list[x])
        for i in range(x):
            print(my_list[i], end='')
        print()
        return x
    except IndexError:
        for i in my_list:
            print(i, end='')
        print()
        return ln
