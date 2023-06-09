#!/usr/bin/python3

def weight_average(my_list=[]):
    if not isinstance(my_list, list) or len(my_list) == 0:
        return (0)

    avg = 0
    size = 0
    for index in my_list:
        avg +=(index[0] * index[1])
        size += index[1]
    return (avg / size)
