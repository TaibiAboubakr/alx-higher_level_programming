#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or not isinstance(roman_string, str):
        return 0
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    Number = 0
    ln = len(roman_string)
    r = roman_string
    for i in range(ln):
        if i < ln - 1 and r[i] == "I" and r[i + 1] in ["V", "X"]:
            continue
        elif i < ln - 1 and r[i] == "X" and r[i + 1] == "C":
            continue
        elif i > 0 and r[i - 1] == "I" and r[i] in ["V", "X"]:
            Number += roman.get(roman_string[i]) - 1
        elif i > 0 and r[i - 1] == "X" and r[i] == "C":
            Number += roman.get(roman_string[i]) - 10
        else:
            Number += roman.get(roman_string[i])
    return (Number)
