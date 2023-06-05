#!/usr/bin/python3

def no_c(my_string):
    zap = ''
    for letter in my_string:
        if letter == 'C' or letter == 'c':
            continue
        zap = zap + letter
    return zap
