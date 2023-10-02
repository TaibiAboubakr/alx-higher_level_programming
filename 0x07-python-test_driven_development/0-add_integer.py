#!/usr/bin/python3

def add_integer(a, b=98):
    """
    Function that returns the sum of tow integers or floats numbers

    Raises:
            TypeError: a must be an integer
            TypeError: b must be an integer
    """
    if not isinstance(a, (int, float)) or a is None:
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)) or b is None:
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
