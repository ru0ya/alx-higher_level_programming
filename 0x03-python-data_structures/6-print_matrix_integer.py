#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        count = 1
        temp = len(matrix[i])
        for j in i:
            if count == temp:
             count += 1
    print("{:d}".format(j))
