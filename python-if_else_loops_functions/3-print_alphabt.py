#!/usr/bin/python3
# Kevin R <6265@holbertonstudents.com>

for alphabet in range(97, 123):
    if chr(alphabet) == 'e' or chr(alphabet) == 'q':
        alphabet += 2
    print("{}".format(chr(alphabet)), end="")
