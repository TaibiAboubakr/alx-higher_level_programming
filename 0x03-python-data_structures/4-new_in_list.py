#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    lenght = len(my_list)
    my_list_copy = my_list.copy()
    if idx < 0 or idx >= lenght:
        return (my_list_copy)
    my_list[idx] = element
    return (my_list_copy)
