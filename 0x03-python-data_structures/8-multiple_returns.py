#!/usr/bin/python3
def multiple_return(sentence):
    lenght = len(sentence)
    if lenght == 0:
        tuple_ret = (0, None)
        return (tuple_ret)
    else:
        tuple_ret = (lenght, sentence[0])
        return (tuple_ret)
