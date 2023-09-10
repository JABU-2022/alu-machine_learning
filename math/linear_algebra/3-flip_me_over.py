#!/usr/bin/env python3


"""Function that returns the transpose of a matrix"""



def matrix_transpose(matrix):
    """Get the number of rows and columns in the original matrix"""
    num_rows = len(matrix)
    num_columns = len(matrix[0])


    """Create a new matrix with swapped dimensions"""
    transpose = [[0 for _ in range(num_rows) for _ in range(num_columns)]]


    for i in range(num_rows):
        for j in range(num_columns):
            transpose[j][i] = matrix[i][j]


    return transpose
