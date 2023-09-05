#!/usr/bin/python3
def uppercase(str):
    res_str = ""
    for ch in str:
        if 'a' <= ch <= 'z':
            res_str += chr(ord(ch) - 32)
        else:
            res_str += ch
    print(res_str)
