#!/usr/bin/python3

def search_replace(my_list, search, replace):
    if my_list is not None:
        return ([index if index != search else replace for index in my_list])
