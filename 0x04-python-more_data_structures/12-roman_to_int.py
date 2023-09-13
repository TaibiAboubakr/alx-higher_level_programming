#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or not str:
        return 0
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    Number = 0
    ln = len(roman_string)
    r = roman_string
    for i in range(ln):
        if i < ln - 1 and r[i] == "I" and r[i + 1] in ["V", "X"]:
            continue
        if i > 0 and r[i - 1] == "I" and r[i] in ["V", "X"]:
            Number += roman.get(roman_string[i]) - 1
        else:
            Number += roman.get(roman_string[i])
    return (Number)
