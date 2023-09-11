#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    len1 = len(matrix)
    len2 = len(matrix[0])
    for i in range(len1):
        for x in range(len2):
            if x < len2 - 1:
                print("{:d}".matrix[i][x], end=" ")
            else:
                print("{:d}".matrix[i][x], end="")
        print("")
