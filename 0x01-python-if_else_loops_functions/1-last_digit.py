#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
str = "Last digit of {:d} is {:d} {:s}"
mod = 10
if number < 0:
    mod *= -1
last_digit = number % mod
if last_digit > 5:
    msg = "and is greater than 5"
elif last_digit == 0:
    msg = "and is 0"
else:
    msg = "and is less than 6 and not 0"
print(str.format(number, last_digit, msg))
