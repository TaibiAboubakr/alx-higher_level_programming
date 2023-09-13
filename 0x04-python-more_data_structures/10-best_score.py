#!/usr/bin/python3
def best_score(a_dictionary):
    bestScore = None
    bestStudent = None
    if a_dictionary is None:
        return None
    else:
        for key in a_dictionary:
            score = a_dictionary.get(key)
            if bestScore is None or score > bestScore:
                bestScore = score
                key_bestScore = key
        return (key_bestScore)
