#!/usr/bin/python3

index = 0
for alpha in range(ord("z"), ord("a") - 1, -1):
    if index % 2 == 0:
        print(chr(alpha).lower(), end="")
    else:
        print(chr(alpha).upper(), end="")
    index = 1 - index
