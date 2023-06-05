#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    listA = list(tuple_a)
    listB = list(tuple_b)

    listA.extend((0, 0))
    listB.extend((0, 0))

    sum1 = listA[0] + listB[0]
    sum2 = listA[1] + listB[1]

    return (sum1, sum2)
