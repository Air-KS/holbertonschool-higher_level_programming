#!/usr/bin/python3

def search_replace(my_list, search, replace):
    newList = my_list[:]
    for index in range(len(newList)):
        if newList[index] == search:
            newList[index] = replace
            return newList
