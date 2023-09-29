#!/usr/bin/python3
def add_integer(a, b=98):
    """
    Function that returns the sum of tow integers or floats numbers

    Raises:
            TypeError: a must be an integer
            TypeError: b must be an integer
    """
    if (not isinstance(a, int) and not isinstance(a, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return (a + b)
