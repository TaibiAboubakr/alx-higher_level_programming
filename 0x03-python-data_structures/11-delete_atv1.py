#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    lenght = len(my_list)
    if 0 > idx >= lenght:
        return (my_list)
    list_ret = my_list[:idx] + my_list[idx + 1:]
    my_list[:] = []
    for x in list_ret:
        my_list.append(x)
    return (list_ret)
