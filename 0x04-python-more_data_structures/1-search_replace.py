#!/usr/bin/python3

def search_replace(my_list, search, replace):
    def replace_func(item):
        if item == search:
            return replace
        else:
            return item
    return list(map(replace_func, my_list))
