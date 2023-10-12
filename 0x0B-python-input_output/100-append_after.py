#!/usr/bin/python3
"""append_after module"""


def append_after(filename="", search_string="", new_string=""):
    """append_after function """
    with open(filename, "r") as file:
        lines = file.readlines()
        skip_next_line = False
        for idx, line in enumerate(lines):
            if skip_next_line:
                skip_next_line = False
                continue
            if line.find(search_string) != -1:
                lines.insert(idx + 1, new_string)
                skip_next_line = True

    with open(filename, "w") as filewrite:
        filewrite.writelines(lines)
