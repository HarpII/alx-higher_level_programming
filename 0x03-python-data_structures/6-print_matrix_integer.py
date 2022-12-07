#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    
    lengthOfMatrix = len(matrix)
    
    if lengthOfMatrix == 0:
        print()
    else:
        for i in range(lengthOfMatrix):
            for j in range(lengthOfMatrix):
                print("{:d}".format(matrix[i][j]), end=" ")
            print()
