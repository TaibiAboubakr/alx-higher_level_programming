#!/usr/bin/python3
def remove_char_at(str, n):
    res_str = ""
    lenght = len(str)
    for i in range(lenght):
        if i == n:
            continue
        res_str += str[i]
    return (res_str)
