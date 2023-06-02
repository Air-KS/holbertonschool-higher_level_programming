#!/usr/bin/python

def remove_char_at(str, n):
    if n < 0 or n >= len(str):
        return (str)

    result = ""
    for index in range(len(str)):
        if index != n:
            result += str[index]

    return (result)
