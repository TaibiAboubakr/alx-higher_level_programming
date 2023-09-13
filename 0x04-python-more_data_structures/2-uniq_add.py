#!/usr/bin/python3
def uniq_add(my_list=[]):
    my_set  = set(my_list)
    sum_fn = lambda x: x
    return sum(map(sum_fn, my_set))


