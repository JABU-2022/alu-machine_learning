#!/usr/bin/env python3
def matrix_shape(matrix):
    """checks matrix and returs shape"""
    if not matrix:
        return []

    shape = []

    while isinstance(matrix, list):
        shape.append(len(matrix))
        matrix = matrix[0]

    return shape
