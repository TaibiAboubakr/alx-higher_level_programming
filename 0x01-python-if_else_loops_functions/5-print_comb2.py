#!/usr/bin/python3
for n in range(100):
    if n != 99:
        print(str(n).zfill(2), end=", ")
    if n == 99:
        print(f"{n}")
