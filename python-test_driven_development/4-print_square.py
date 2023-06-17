#!/usr/bin/python3

def print_square(size):
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for index in range(size):
        for length in range(size):
            print("#", end="")
        print()

# size is the size length of the square
# size must be an integer, otherwise raise a TypeError exception with the message size must be an integer
# if size is less than 0, raise a ValueError exception with the message size must be >= 0
# if size is a float and is less than 0, raise a TypeError exception with the message size must be an integer
# You are not allowed to import any module
