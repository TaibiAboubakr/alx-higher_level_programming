#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    list_ret = []
    for x in my_list:
        if x % 2 == 0:
            list_ret.append(True)
        else:
            list_ret.append(False)
    return (list_ret)
