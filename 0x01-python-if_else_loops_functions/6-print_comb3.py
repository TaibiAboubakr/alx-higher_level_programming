#!/usr/bin/python3
for n in range(10):
    for x in range(1, 10):
        if n == 8 and x == 9:
            print(89)
            break
        if x == n or n > x:
            continue
        print("{}{}".format(n, x), end=", ")
