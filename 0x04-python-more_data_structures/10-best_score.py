#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    else:
        bestScore = 0
        for key in a_dictionary:
            score = a_dictionary.get(key)
            if score > bestScore:
                bestScore = score
                key_bestScore = key
        return (key_bestScore)
            