#!/usr/bin/python3
# Kevin R <6265@holbertonstudents.com>

"""Write a program that prints numbers from 00 to 99"""
for number in range(0, 100):
    if number == 99:
        print("{}".format(number))
    else:
        print("{:02}, ".format(number), end="")
