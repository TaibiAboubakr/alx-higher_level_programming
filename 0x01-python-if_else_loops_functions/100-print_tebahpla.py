#!/usr/bin/env python3
for ch in range(122, 96, -1):
    if ch % 2 == 1:
        ch = ch - 32
    print(chr(ch), end="")
