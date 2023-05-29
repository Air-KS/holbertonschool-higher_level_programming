#!/usr/bin/python3
# Kevin R <6265@holbertonstudents.com>

for number in range(0, 10):
    for digit in range(number + 1, 10):
        if number == 8 and digit == 9:
            print("{}{}".format(number, digit))
        else:
            print("{}{}".format(number, digit), end=", ")
