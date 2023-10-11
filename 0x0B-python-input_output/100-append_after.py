#!/usr/bin/python3
"""append_after module"""


def append_after(filename="", search_string="", new_string=""):
    """append_after function """
    with open(filename, "r") as file:
        lines = file.readlines()
        idx = 0
        for line in lines:
            idx += 1
            if line.find(search_string) != -1:
                lines.insert(idx, new_string)

    with open(filename, "w") as filewrite:
        filewrite.writelines(lines)
