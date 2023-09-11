#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    lenght = len(my_list)
    my_list_copy =[]
    if idx < 0 or idx >= lenght:
        return (my_list)
    if lenght > 0:
        for i in my_list:
            my_list_copy.append(i)
    my_list_copy[idx] = element
    return (my_list_copy)
