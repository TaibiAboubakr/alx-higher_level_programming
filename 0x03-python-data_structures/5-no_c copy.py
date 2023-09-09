#!/usr/bin/python3
def no_c(my_string):
    str_copy = ""
    for i in range(0, len(my_string)):
        if my_string[i] != 'c' or i != 'C':
            str_copy +=  my_string[i]
    return (str_copy)
            
           
