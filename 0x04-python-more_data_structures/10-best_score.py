#!/usr/bin/python3
def best_score(a_dictionary):
    bestScore = None
    bestStudent = None
    if a_dictionary is None:
        return None
    else:
        for student, score in a_dictionary.items():
            if bestScore is None or score > bestScore:
                bestScore = score
                bestStudent = student
        return (bestStudent)
