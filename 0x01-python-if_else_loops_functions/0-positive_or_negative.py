#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number > 0:
    str = "{} is positive"
elif number == 0:
    str = "{} is zero"
elif number < 0:
    str = "{} is negative"
print(str.format(number))
