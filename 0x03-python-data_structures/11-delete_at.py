#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    list_ret = []
    lenght = len(my_list)
    if 0 > idx >= lenght:
        return (my_list)
    for i in range(lenght):
        if i == idx:
            continue
        else:
            list_ret.append(my_list[i])
    my_list[:] = []
    for x in list_ret:
        my_list.append(x)
    return (list_ret)
