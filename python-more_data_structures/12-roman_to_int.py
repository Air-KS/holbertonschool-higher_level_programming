#!/usr/bin/python3

def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or not roman_string:
        return 0

    key_value = {
        "I": 1, "V": 5,
        "X": 10, "L": 50,
        "C": 100, "D": 500,
        "M": 1000
    }

    result = 0
    prevValue = 0

    for char in reversed(roman_string):
        value = key_value.get(char, 0)
        if value >= prevValue:
            result += value
            prevValue = value
        else:
            result -= value
            prevValue = value

    return result
