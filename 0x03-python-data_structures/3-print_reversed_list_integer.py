#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list is None:
        exit(0)
    lenght = len(my_list) - 1
    if len(my_list) == 0:
        exit(0)
    elif len(my_list) == 1:
        print("{:d}".format(my_list[0]))
    else:
        for i in range(lenght, -1, -1):
            print("{:d}".format(my_list[i]))
