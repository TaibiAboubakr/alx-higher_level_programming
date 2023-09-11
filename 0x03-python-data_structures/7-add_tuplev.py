#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    list_a = [0, 0]
    list_b = [0, 0]
    i = 0
    for a in tuple_a:
        list_a[i] = a
        i += 1
    i = 0
    for b in tuple_b:
        list_b[i] = b
        i += 1
    new_tuple = ((list_a[0] + list_b[0]), (list_a[1] + list_b[1]))
    return (new_tuple)
