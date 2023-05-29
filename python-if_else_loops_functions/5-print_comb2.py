#!/usr/bin/python3
# Kevin R <6265@holbertonstudents.com>

for number in range(0, 100):
    if number == 99:
        print("{}".format(number))
    else:
        print("{:02}, ".format(number), end="")
