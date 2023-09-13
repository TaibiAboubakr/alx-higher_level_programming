#!/usr/bin/python3

def roman_to_int(roman_string):
    if roman_string is None or not isinstance(roman_string, str):
        return 0

    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    Number = 0
    prev_value = 0

    for char in reversed(roman_string):

        value = roman.get(char)
        if value < prev_value:
            Number -= value
        else:
            Number += value
        prev_value = value

    return Number
