#!/usr/bin/python3
def print_last_digit(number):
    number = abs(number) % 10

    if number < 0:
        digit = -digit

    print("{}".format(number), end="")
    return (number)
