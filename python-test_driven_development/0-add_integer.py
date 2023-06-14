#!/usr/bin/python3

def add_integer(a, b=98):
    """ Return the integer addition a of b """

    typeA, typeB = type(a), type(b)
    if typeA != int and typeA != float:
        raise TypeError("a must be an integer")
    if typeB != int and typeB != float:
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
