#!/usr/bin/python3
# 2-print_alphabet.py
# kevin R <6265@holbertonstudents.com>

"""Print the alphabet in lowercase, not followed by a new line."""
for alphabet in range(97, 123):
    print("{}".format(chr(alphabet)), end="")
